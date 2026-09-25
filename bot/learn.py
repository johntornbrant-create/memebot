"""Self-development. The bot's only teachers are its own wins, its own losses,
and its own misses. Nothing is imported from research or from anyone else.

Two training sets:
  1. SHADOW outcomes - every gate-passing candidate it ever saw, bought or not,
     labelled by whether it moved +50% within 24h. This is the volume source, and it is
     the only way to learn from the ones it skipped.
  2. REAL closed trades - fewer, but they carry actual friction and actual exit timing.
     Weighted 3x because they are the ground truth.

Pure stdlib. No dependencies, nothing to break in CI.
"""
import json, math, os
from . import config
from .features import FEATURES, PRIOR_WEIGHTS
from .scoring import load_weights, save_weights, score
from .shadow import read_outcomes

TRADES = os.path.join(os.path.dirname(__file__), "..", "state", "trades.jsonl")
REAL_TRADE_WEIGHT = 3.0
WIN_THRESHOLD = 0.15


def _read_trades():
    rows = []
    try:
        with open(TRADES) as fh:
            rows = [json.loads(l) for l in fh if l.strip()]
    except FileNotFoundError:
        pass
    return [r for r in rows if isinstance(r.get("features"), dict)]


def build_dataset():
    X, y, w = [], [], []
    for r in read_outcomes():
        X.append([float(r["features"].get(k, 0.0)) for k in FEATURES])
        y.append(1.0 if r.get("win") else 0.0)
        w.append(1.0)
    for r in _read_trades():
        X.append([float(r["features"].get(k, 0.0)) for k in FEATURES])
        y.append(1.0 if r.get("pnl_pct", -1) >= WIN_THRESHOLD else 0.0)
        w.append(REAL_TRADE_WEIGHT)
    return X, y, w


def _fit(X, y, sw, l2=2.0, lr=0.4, epochs=1500):
    n, d = len(X), len(FEATURES)
    wt = [0.0] * d
    b = 0.0
    tot = sum(sw) or 1.0
    for _ in range(epochs):
        gw, gb = [0.0] * d, 0.0
        for xi, yi, si in zip(X, y, sw):
            z = b + sum(wt[j] * xi[j] for j in range(d))
            p = 1 / (1 + math.exp(-max(-30, min(30, z))))
            e = (p - yi) * si
            for j in range(d):
                gw[j] += e * xi[j]
            gb += e
        for j in range(d):
            wt[j] -= lr * (gw[j] / tot + l2 * wt[j] / tot)
        b -= lr * gb / tot
    return wt


def refit(force=False):
    X, y, sw = build_dataset()
    n = len(X)
    n_real = len(_read_trades())
    n_shadow = n - n_real
    if n < config.LEARN_MIN_TRADES and not force:
        return (f"learn: {n} observations ({n_shadow} shadow + {n_real} real), "
                f"need {config.LEARN_MIN_TRADES}. Weights unchanged.")

    wins = int(sum(y))
    if wins < 8 or wins == n:
        return f"learn: {wins}/{n} wins - degenerate labels, weights unchanged."

    fitted = dict(zip(FEATURES, _fit(X, y, sw)))

    # rescale to a sane magnitude, then shrink toward flat. Small samples lie.
    fs = sum(abs(v) for v in fitted.values()) or 1.0
    ps = sum(abs(v) for v in PRIOR_WEIGHTS.values())
    fitted = {k: v * ps / fs for k, v in fitted.items()}
    a = config.LEARN_BLEND
    new = {k: round(a * fitted[k] + (1 - a) * PRIOR_WEIGHTS[k], 4) for k in FEATURES}

    old, meta = load_weights()
    base_rate = wins / n

    # ADAPTIVE THRESHOLD. A fixed number goes stale the moment the weights move, because
    # refitting changes the whole score scale. So set the bar from the new model's own
    # score distribution: trade roughly the top quartile of what the gates let through.
    # Measured on 96 shadow closures: Q1 hit +50% 62.5% of the time with a +93% median
    # peak, vs 29% / +9% for Q4. The top quartile is where the edge lives.
    scores = sorted(score(r["features"], new) for r in read_outcomes())
    if len(scores) >= 40:
        thr = round(scores[int(len(scores) * 0.75)], 3)
        thr = min(max(thr, 0.60), config.THRESHOLD_MAX)
    else:
        thr = config.ENTRY_THRESHOLD

    # ...but if the real trades are actually losing, raise the bar regardless.
    real = _read_trades()
    if len(real) >= 25:
        rwr = sum(1 for r in real if r.get("pnl_pct", -1) >= WIN_THRESHOLD) / len(real)
        if rwr < 0.20:
            thr = min(config.THRESHOLD_MAX, thr + 0.03)

    meta = {
        "version": meta.get("version", 0) + 1,
        "fitted_on": n, "n_shadow": n_shadow, "n_real": n_real,
        "base_rate": round(base_rate, 3), "threshold": round(thr, 3),
        "note": (f"refit on {n} observations ({n_shadow} shadow, {n_real} real), "
                 f"{wins} winners ({base_rate:.0%} base rate)"),
        "prev_weights": old,
    }
    save_weights(new, meta)

    moves = sorted(((k, new[k] - old.get(k, 0)) for k in FEATURES), key=lambda t: -abs(t[1]))
    up = ", ".join(f"{k} {d:+.3f}" for k, d in moves[:3])
    dn = ", ".join(f"{k} {d:+.3f}" for k, d in moves[-2:])
    return (f"learn: v{meta['version']} on {n} obs ({n_shadow}s/{n_real}r), base rate "
            f"{base_rate:.0%}, threshold {thr:.2f}. Up: {up}. Down: {dn}")


if __name__ == "__main__":
    print(refit(force=os.environ.get("FORCE_REFIT") == "1"))
