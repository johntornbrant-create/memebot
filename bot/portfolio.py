"""Paper broker. Fake money, realistic frictions."""
import json, os, uuid
from datetime import datetime, timezone
from . import config

ROOT      = os.path.join(os.path.dirname(__file__), "..")
PF_PATH   = os.path.join(ROOT, "state", "portfolio.json")
TRADES    = os.path.join(ROOT, "state", "trades.jsonl")
SIGNALS   = os.path.join(ROOT, "state", "signals.jsonl")


def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def hours_since(iso):
    t = datetime.fromisoformat(iso)
    return (datetime.now(timezone.utc) - t).total_seconds() / 3600.0


def fresh():
    return {
        "started": now_iso(), "updated": now_iso(),
        "cash": config.START_EQUITY, "equity": config.START_EQUITY,
        "positions": {}, "blacklist": {}, "halted": False, "halt_reason": "",
        "marks": {"day": "", "day_equity": config.START_EQUITY,
                  "week": "", "week_equity": config.START_EQUITY, "trades_today": 0},
        "stats": {"ticks": 0, "opened": 0, "closed": 0, "wins": 0, "losses": 0,
                  "fees_paid": 0.0, "realized_pnl": 0.0},
    }


def load():
    try:
        with open(PF_PATH) as fh:
            pf = json.load(fh)
        for k, v in fresh().items():          # forward-compat for new fields
            pf.setdefault(k, v)
        return pf
    except Exception:
        return fresh()


def save(pf):
    pf["updated"] = now_iso()
    os.makedirs(os.path.dirname(PF_PATH), exist_ok=True)
    with open(PF_PATH, "w") as fh:
        json.dump(pf, fh, indent=2)


def _append(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as fh:
        fh.write(json.dumps(obj) + "\n")


def log_signal(rec):
    _append(SIGNALS, rec)


def _friction(notional, liquidity):
    """Slippage grows with size-to-pool. Returns fractional cost of one side."""
    liq = max(liquidity, 1.0)
    slip = config.SLIPPAGE_K * (notional / liq) + config.EXTRA_SLIP_FLOOR
    return min(slip, 0.25) + config.DEX_FEE


def open_position(pf, cand, notional, feats, score):
    frac = _friction(notional, cand["liquidity"])
    fees = notional * frac + config.PRIORITY_FEE_USD
    tokens = (notional - fees) / cand["price"]
    key = f"{cand['chain']}:{cand['address']}"
    pf["positions"][key] = {
        "id": uuid.uuid4().hex[:10], "chain": cand["chain"], "address": cand["address"],
        "symbol": cand["symbol"], "opened": now_iso(),
        "entry_price": cand["price"], "tokens": tokens, "tokens_initial": tokens,
        "cost_usd": notional, "fees_usd": round(fees, 4),
        "realized_usd": 0.0, "peak_gain": 0.0, "tp_hit": [],
        "entry_liq": cand["liquidity"], "score": score, "features": feats,
        "last_price": cand["price"],
    }
    pf["cash"] -= notional
    pf["stats"]["opened"] += 1
    pf["stats"]["fees_paid"] += fees
    pf["marks"]["trades_today"] = pf["marks"].get("trades_today", 0) + 1
    return pf["positions"][key]


def sell(pf, key, price, liquidity, fraction, reason):
    p = pf["positions"][key]
    tokens = p["tokens"] * fraction
    gross = tokens * price
    fees = gross * _friction(gross, liquidity) + config.PRIORITY_FEE_USD
    net = max(gross - fees, 0.0)
    p["tokens"] -= tokens
    p["realized_usd"] += net
    p["fees_usd"] += fees
    p["last_price"] = price
    pf["cash"] += net
    pf["stats"]["fees_paid"] += fees

    closed = p["tokens"] <= p["tokens_initial"] * 1e-6
    if closed:
        pnl = p["realized_usd"] - p["cost_usd"]
        pf["stats"]["closed"] += 1
        pf["stats"]["realized_pnl"] += pnl
        pf["stats"]["wins" if pnl > 0 else "losses"] += 1
        _append(TRADES, {
            "id": p["id"], "symbol": p["symbol"], "chain": p["chain"], "address": p["address"],
            "opened": p["opened"], "closed": now_iso(), "hold_h": round(hours_since(p["opened"]), 2),
            "entry_price": p["entry_price"], "exit_price": price,
            "cost_usd": round(p["cost_usd"], 2), "proceeds_usd": round(p["realized_usd"], 2),
            "pnl_usd": round(pnl, 2), "pnl_pct": round(pnl / p["cost_usd"], 4),
            "fees_usd": round(p["fees_usd"], 2), "peak_gain": round(p["peak_gain"], 4),
            "reason": reason, "score": p["score"], "features": p["features"],
        })
        if pnl / p["cost_usd"] < -0.25:
            pf["blacklist"][key] = now_iso()
        del pf["positions"][key]
    return net, closed


def mark_to_market(pf, quotes):
    """quotes: {key: candidate-dict or None}. Unpriceable positions are marked to zero -
    that is the honest assumption for a memecoin that has stopped trading."""
    val = 0.0
    for key, p in pf["positions"].items():
        q = quotes.get(key)
        if q and q["price"] > 0:
            p["last_price"] = q["price"]
        else:
            p["last_price"] = 0.0
        val += p["tokens"] * p["last_price"]
        gain = (p["last_price"] / p["entry_price"] - 1) if p["entry_price"] else -1
        p["peak_gain"] = max(p.get("peak_gain", 0.0), gain)
    pf["equity"] = round(pf["cash"] + val, 4)
    return pf["equity"]


def exit_rules(p, price, liq):
    """-> list of (fraction, reason). Evaluated top-down, first match wins."""
    if price <= 0:
        return [(1.0, "untradeable / rugged")]
    gain = price / p["entry_price"] - 1
    held = hours_since(p["opened"])

    if gain <= config.STOP_LOSS:
        return [(1.0, f"stop loss {gain:+.0%}")]
    if liq < config.MIN_LIQUIDITY_USD * 0.5:
        return [(1.0, "liquidity drained")]
    if p["peak_gain"] >= config.TRAIL_AFTER and gain <= p["peak_gain"] * (1 - config.TRAIL_PCT):
        return [(1.0, f"trailing stop from {p['peak_gain']:+.0%}")]
    for i, (trigger, frac) in enumerate(config.TP_LADDER):
        if gain >= trigger and i not in p["tp_hit"]:
            p["tp_hit"].append(i)
            return [(frac, f"take profit {trigger:+.0%} (sold {frac:.0%})")]
    if held >= config.TIME_STOP_H and gain < config.TIME_STOP_MIN_GAIN:
        return [(1.0, f"time stop {held:.0f}h, only {gain:+.0%}")]
    if held >= config.MAX_HOLD_H:
        return [(1.0, f"max hold {held:.0f}h")]
    return []
