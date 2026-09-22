"""The part that decides whether we survive. Every gate here is a veto."""
from datetime import datetime, timezone, timedelta
from . import config


def _now():
    return datetime.now(timezone.utc)


def equity_curve_checks(pf):
    """Returns (can_enter, reasons[]). Breakers never block exits, only new entries."""
    reasons, ok = [], True
    eq = pf["equity"]

    if eq < config.START_EQUITY * config.KILL_SWITCH_EQ:
        pf["halted"] = True
        pf["halt_reason"] = (f"KILL SWITCH: equity ${eq:.2f} below "
                             f"${config.START_EQUITY * config.KILL_SWITCH_EQ:.2f}. Manual reset required.")
    if pf.get("halted"):
        return False, [pf.get("halt_reason", "halted")]

    day_ref = pf["marks"].get("day_equity", config.START_EQUITY)
    if day_ref and (eq / day_ref - 1) <= config.DAILY_LOSS_HALT:
        ok = False; reasons.append(f"daily loss {eq/day_ref-1:+.1%} <= {config.DAILY_LOSS_HALT:.0%}")

    wk_ref = pf["marks"].get("week_equity", config.START_EQUITY)
    if wk_ref and (eq / wk_ref - 1) <= config.WEEKLY_LOSS_HALT:
        ok = False; reasons.append(f"weekly loss {eq/wk_ref-1:+.1%} <= {config.WEEKLY_LOSS_HALT:.0%}")

    if pf["marks"].get("trades_today", 0) >= config.MAX_TRADES_DAY:
        ok = False; reasons.append("daily trade cap reached")

    if len(pf["positions"]) >= config.MAX_CONCURRENT:
        ok = False; reasons.append("max concurrent positions")

    deployed = sum(p["cost_usd"] for p in pf["positions"].values())
    if deployed >= eq * config.MAX_DEPLOYED_PCT:
        ok = False; reasons.append(f"deployed {deployed/eq:.0%} >= {config.MAX_DEPLOYED_PCT:.0%} cap")

    return ok, reasons


def can_open(pf, cand):
    """Per-candidate vetoes."""
    key = f"{cand['chain']}:{cand['address']}"
    if key in pf["positions"]:
        return False, "already held"
    if key in pf.get("blacklist", {}):
        return False, "blacklisted (previously stopped out)"
    per_chain = sum(1 for p in pf["positions"].values() if p["chain"] == cand["chain"])
    if per_chain >= config.MAX_PER_CHAIN:
        return False, f"{cand['chain']} concentration cap"
    return True, ""


def size_position(pf, cand):
    """Fixed fractional. Assumes -100% is possible on every single trade, because it is.
    Also capped by pool liquidity so we never become the price."""
    eq = pf["equity"]
    cash = pf["cash"]
    notional = eq * config.MAX_POS_PCT
    notional = min(notional, cand["liquidity"] * 0.004)   # <=0.4% of pool = tolerable impact
    room = eq * config.MAX_DEPLOYED_PCT - sum(p["cost_usd"] for p in pf["positions"].values())
    notional = min(notional, room, cash * 0.9)
    return round(notional, 2) if notional >= config.MIN_POS_USD else 0.0


def roll_marks(pf):
    """Reset the daily/weekly reference equity when the calendar rolls."""
    now = _now()
    m = pf["marks"]
    d = now.strftime("%Y-%m-%d")
    if m.get("day") != d:
        m["day"] = d
        m["day_equity"] = pf["equity"]
        m["trades_today"] = 0
    wk = now.strftime("%G-W%V")
    if m.get("week") != wk:
        m["week"] = wk
        m["week_equity"] = pf["equity"]
