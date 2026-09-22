import json, os, math
from . import config
from .features import FEATURES, PRIOR_WEIGHTS

WEIGHTS_PATH = os.path.join(os.path.dirname(__file__), "..", "state", "weights.json")


def load_weights():
    try:
        with open(WEIGHTS_PATH) as fh:
            d = json.load(fh)
        w = d.get("weights", {})
        return {k: float(w.get(k, PRIOR_WEIGHTS[k])) for k in FEATURES}, d
    except Exception:
        return dict(PRIOR_WEIGHTS), {"weights": dict(PRIOR_WEIGHTS), "version": 0,
                                     "fitted_on": 0, "note": "prior"}


def save_weights(w, meta):
    meta = dict(meta); meta["weights"] = w
    os.makedirs(os.path.dirname(WEIGHTS_PATH), exist_ok=True)
    with open(WEIGHTS_PATH, "w") as fh:
        json.dump(meta, fh, indent=2)


def score(feats, weights):
    """Weighted sum squashed to 0..1. Centred so a neutral candidate lands near 0.5."""
    raw = sum(weights.get(k, 0.0) * feats.get(k, 0.0) for k in FEATURES)
    pos = sum(v for v in weights.values() if v > 0) or 1.0
    z = (raw / pos - 0.42) * 6.0
    return round(1 / (1 + math.exp(-z)), 4)
