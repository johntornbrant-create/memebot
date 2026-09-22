"""The shadow book - how the bot learns from what it did NOT buy.

Every candidate that clears the safety gates gets tracked for 24h, bought or not.
Without this the bot only ever sees outcomes for its own picks, so it can never
discover that the thing it rejected went 40x. It would keep making the same miss forever.
"""
import json, os, random
from . import config, portfolio as pf_mod
from .sources import onchain

ROOT     = os.path.join(os.path.dirname(__file__), "..")
BOOK     = os.path.join(ROOT, "state", "shadow.json")
OUTCOMES = os.path.join(ROOT, "state", "shadow_outcomes.jsonl")


def load():
    try:
        with open(BOOK) as fh:
            return json.load(fh)
    except Exception:
        return {}


def save(book):
    os.makedirs(os.path.dirname(BOOK), exist_ok=True)
    with open(BOOK, "w") as fh:
        json.dump(book, fh, indent=1)


def track(book, cand, feats, score, taken):
    key = f"{cand['chain']}:{cand['address']}"
    if key in book:
        book[key]["taken"] = book[key]["taken"] or taken
        return
    if len(book) >= config.SHADOW_MAX_OPEN:
        return
    book[key] = {
        "t0": pf_mod.now_iso(), "symbol": cand["symbol"], "chain": cand["chain"],
        "address": cand["address"], "price0": cand["price"], "liq0": cand["liquidity"],
        "features": feats, "score": score, "taken": bool(taken),
        "peak": 0.0, "trough": 0.0, "last": cand["price"],
    }


def update(book):
    """Re-price the book, close out anything past the window. Returns (closed, wins)."""
    if not book:
        return 0, 0
    keys = list(book.keys())
    random.shuffle(keys)
    live = keys[:120]                      # cap API work per tick
    quotes = onchain.quote_many(live)

    closed = wins = 0
    for key in keys:
        rec = book[key]
        q = quotes.get(key) if key in live else None
        if q and q["price"] > 0 and rec["price0"] > 0:
            g = q["price"] / rec["price0"] - 1
            rec["last"] = q["price"]
            rec["peak"] = max(rec["peak"], g)
            rec["trough"] = min(rec["trough"], g)
        elif key in live:
            rec["last"] = 0.0
            rec["trough"] = -1.0

        age_h = pf_mod.hours_since(rec["t0"])
        if age_h >= config.SHADOW_TRACK_H:
            final = (rec["last"] / rec["price0"] - 1) if rec["price0"] else -1.0
            win = rec["peak"] >= config.SHADOW_WIN_MOVE
            _append({
                "t0": rec["t0"], "closed": pf_mod.now_iso(), "symbol": rec["symbol"],
                "chain": rec["chain"], "address": rec["address"],
                "score": rec["score"], "features": rec["features"], "taken": rec["taken"],
                "peak_gain": round(rec["peak"], 4), "trough": round(rec["trough"], 4),
                "final_gain": round(final, 4), "win": bool(win),
            })
            closed += 1
            wins += int(win)
            del book[key]
    return closed, wins


def _append(obj):
    os.makedirs(os.path.dirname(OUTCOMES), exist_ok=True)
    with open(OUTCOMES, "a") as fh:
        fh.write(json.dumps(obj) + "\n")


def read_outcomes():
    rows = []
    try:
        with open(OUTCOMES) as fh:
            for line in fh:
                if line.strip():
                    rows.append(json.loads(line))
    except FileNotFoundError:
        pass
    return rows


def missed_report(n=8):
    """The ones it skipped that ran. This is the bot's own mistake list."""
    rows = [r for r in read_outcomes() if not r["taken"]]
    rows.sort(key=lambda r: -r["peak_gain"])
    return rows[:n]
