"""Self-diagnosis. The bot grades its own work and changes tactics from what it finds.

Every refit this runs, measures four things it can actually act on, and writes the
adjustments into state/diagnosis.json where config and run pick them up.

The failures it is built to catch are the real ones from the first month:
  - traded for 18 days with the breaker silently blocking every entry
  - set stops at -35% that actually filled at -54% because of 15-min gaps
  - sold winners early while the tail was paying for everything
"""
import json, os, statistics as st
from . import config, portfolio as pf_mod

ROOT = os.path.join(os.path.dirname(__file__), "..")
DIAG = os.path.join(ROOT, "state", "diagnosis.json")


def _load(name):
    rows = []
    try:
        with open(os.path.join(ROOT, "state", name)) as fh:
            rows = [json.loads(l) for l in fh if l.strip()]
    except FileNotFoundError:
        pass
    return rows


def run():
    trades = _load("trades.jsonl")
    shadow = _load("shadow_outcomes.jsonl")
    d = {"at": pf_mod.now_iso(), "n_trades": len(trades), "n_shadow": len(shadow),
         "actions": []}

    # 1. SELECTION EDGE - is the picking actually better than the reject pile?
    tk = [r for r in shadow if r["taken"]]
    sk = [r for r in shadow if not r["taken"]]
    hit = lambda a: (sum(1 for r in a if r["peak_gain"] >= 0.5) / len(a)) if a else 0.0
    if len(tk) >= 20 and len(sk) >= 20:
        d["edge_pp"] = round((hit(tk) - hit(sk)) * 100, 1)
        if d["edge_pp"] < 3:
            d["actions"].append("edge near zero - selection is not working, do not raise size")

    # 2. FILL QUALITY - what the stop was SET to vs what it actually got.
    # This is the single most important self-measurement: a stop that gaps turns a
    # +22%/trade strategy into a -2% one, and nothing else in the log reveals it.
    stopped = [r for r in trades if r["pnl_pct"] < -0.20 and r["peak_gain"] < 0.40]
    if len(stopped) >= 10:
        actual = st.median([r["pnl_pct"] for r in stopped])
        d["stop_intended"] = config.STOP_LOSS
        d["stop_actual"] = round(actual, 3)
        d["stop_slippage_pp"] = round((actual - config.STOP_LOSS) * 100, 1)
        if actual < config.STOP_LOSS - 0.12:
            # The stop is not being honoured. Tightening it would only fire more often at
            # the same bad price; what helps is giving winners room and sizing smaller.
            d["actions"].append(
                f"stop set {config.STOP_LOSS:+.0%} but filling {actual:+.0%} "
                f"- gapping, not a stop. Reduce size rather than tighten.")
            d["suggest_size_mult"] = 0.75

    # 3. CAPTURE - how much of each peak we actually banked.
    runners = [r for r in trades if r["peak_gain"] >= 0.5]
    if len(runners) >= 8:
        cap = st.median([r["pnl_pct"] / r["peak_gain"] for r in runners])
        d["capture_of_peak"] = round(cap, 3)
        if cap < 0.15:
            d["actions"].append(
                f"banking only {cap:.0%} of peak on runners - take profit earlier")
            d["suggest_first_rung"] = 0.30

    # 4. IDLE - running but not trading is the failure that looks like success.
    try:
        with open(os.path.join(ROOT, "state", "portfolio.json")) as fh:
            pf = json.load(fh)
        le = pf.get("last_entry")
        d["idle_hours"] = round(pf_mod.hours_since(le), 1) if le else None
        d["halted"] = bool(pf.get("halted"))
        if d["idle_hours"] and d["idle_hours"] > 24 and not d["halted"]:
            d["actions"].append(f"no entry in {d['idle_hours']:.0f}h while not halted "
                                f"- selection is too tight, loosening")
            d["suggest_loosen"] = True
    except Exception:
        pass

    os.makedirs(os.path.dirname(DIAG), exist_ok=True)
    with open(DIAG, "w") as fh:
        json.dump(d, fh, indent=2)
    return d


def load():
    try:
        with open(DIAG) as fh:
            return json.load(fh)
    except Exception:
        return {}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
