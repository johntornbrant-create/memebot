"""Self-development: the bot refits its own weights on its OWN closed trades.

No external strategies, no copied alpha - the only teacher is our realised PnL.
Pure stdlib logistic regression so the workflow has zero dependencies.
"""
import json, math, os
from . import config
from .features import FEATURES, PRIOR_WEIGHTS
from .scoring import load_weights, save_weights

TRADES = os.path.join(os.path.dirname(__file__), "..", "state", "trades.jsonl")
WIN_THRESHOLD = 0.15          # a "win" is +15% net, not +0.01%


def _read_trades():
    rows = []
    try:
        with open(TRADES) as fh:
            for line in fh:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
    except FileNotFoundError:
        pass
    return [r for r in rows if isinstance(r.get("features"), dict)]


def _fit(X, y, l2=2.0, lr=0.35, epochs=1200):
    n, d = len(X), len(FEATURES)
    w = [0.0] * d
    b = 0.0
    for _ in range(epochs):
        gw = [0.0] * d
        gb = 0.0
        for xi, yi in zip(X, y):
            z = b + sum(w[j] * xi[j] for j in range(d))
            p = 1 / (1 + math.exp(-max(-30, min(30, z))))
            e = p - yi
            for j in range(d):
                gw[j] += e * xi[j]
            gb += e
        for j in range(d):
            w[j] -= lr * (gw[j] / n + l2 * w[j] / n)
        b -= lr * gb / n
    return w, b


def refit(force=False):
    """Returns a human-readable report string."""
    rows = _read_trades()
    n = len(rows)
    if n < config.LEARN_MIN_TRADES and not force:
        return f"learn: {n}/{config.LEARN_MIN_TRADES} closed trades - not enough. Weights unchanged."

    X = [[float(r["features"].get(k, 0.0)) for k in FEATURES] for r in rows]
    y = [1.0 if r.get("pnl_pct", -1) >= WIN_THRESHOLD else 0.0 for r in rows]
    wins = int(sum(y))
    if wins < 5 or wins == n:
        return f"learn: {wins}/{n} wins - degenerate labels, weights unchanged."

    w, _ = _fit(X, y)
    fitted = dict(zip(FEATURES, w))

    # scale fitted weights to the prior's magnitude, then blend. Small samples lie.
    fs = sum(abs(v) for v in fitted.values()) or 1.0
    ps = sum(abs(v) for v in PRIOR_WEIGHTS.values())
    fitted = {k: v * ps / fs for k, v in fitted.items()}
    a = config.LEARN_BLEND
    new = {k: round(a * fitted[k] + (1 - a) * PRIOR_WEIGHTS[k], 4) for k in FEATURES}

    old, meta = load_weights()
    wr = wins / n
    # raise the bar when we are losing, relax it (never below prior) when we are winning
    thr = config.ENTRY_THRESHOLD
    if wr < 0.25:
        thr = min(0.80, config.ENTRY_THRESHOLD + 0.08)
    elif wr > 0.45:
        thr = max(0.55, config.ENTRY_THRESHOLD - 0.03)

    meta = {
        "version": meta.get("version", 0) + 1,
        "fitted_on": n, "win_rate": round(wr, 3), "threshold": round(thr, 3),
        "note": f"refit on {n} closed trades, {wins} wins (>= +{WIN_THRESHOLD:.0%})",
        "prev_weights": old,
    }
    save_weights(new, meta)

    moves = sorted(((k, new[k] - old.get(k, 0)) for k in FEATURES),
                   key=lambda t: -abs(t[1]))[:4]
    delta = ", ".join(f"{k} {d:+.3f}" for k, d in moves)
    return (f"learn: refit v{meta['version']} on {n} trades (WR {wr:.0%}), "
            f"threshold -> {thr:.2f}. Biggest moves: {delta}")


if __name__ == "__main__":
    print(refit(force=os.environ.get("FORCE_REFIT") == "1"))
