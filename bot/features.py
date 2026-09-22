"""Feature extraction. Every feature is scaled to 0..1 so weights stay interpretable
and the learner can compare them directly."""
import math
from . import config
from .sources import buzz as buzzmod

# order matters - learn.py aligns vectors to this list
FEATURES = [
    "liq_quality", "turnover", "buy_pressure", "momentum_accel", "not_vertical",
    "age_sweet", "socials", "fdv_sanity", "txn_depth", "dip_in_uptrend",
    "buzz", "paid_boost",
]

# NO PRIORS. Every feature starts at the same weight and the bot earns its own opinions
# from its own closed trades and its own shadow book. Nothing here is imported from
# research, from the internet, or from anyone else's strategy.
PRIOR_WEIGHTS = {k: round(1.0 / len(FEATURES), 4) for k in FEATURES}


def _clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def _bell(x, center, width):
    """1.0 at center, decaying either side. Used for 'sweet spot' features."""
    if x is None or width <= 0:
        return 0.0
    return math.exp(-((x - center) ** 2) / (2 * width ** 2))


def passes_gates(c):
    """Hard filters. Returns (ok, reason). Nothing scores until it passes these."""
    if c["liquidity"] < config.MIN_LIQUIDITY_USD:   return False, "liquidity too thin"
    if c["liquidity"] > config.MAX_LIQUIDITY_USD:   return False, "already discovered"
    if c["vol_h1"] < config.MIN_VOL_H1_USD:         return False, "no h1 volume"
    if c["price"] <= 0:                             return False, "no price"
    age = c.get("age_min")
    if age is None:                                 return False, "unknown age"
    if age < config.MIN_AGE_MIN:                    return False, "too new (bot war)"
    if age > config.MAX_AGE_H * 60:                 return False, "too old"
    txns = c["buys_h1"] + c["sells_h1"]
    if txns < config.MIN_TXNS_H1:                   return False, "too few txns"
    if txns and c["buys_h1"] / txns < config.MIN_BUYERS_RATIO:
        return False, "sell pressure"
    if c["fdv"] and c["liquidity"] and c["fdv"] / c["liquidity"] > config.MAX_FDV_LIQ_RATIO:
        return False, "exit-liquidity trap (FDV/liq)"
    return True, ""


def extract(c, buzz=None):
    liq, vol1 = c["liquidity"], c["vol_h1"]
    txns = c["buys_h1"] + c["sells_h1"]
    f = {}

    # 50k-500k liquidity is the workable band: deep enough to exit, small enough to move
    f["liq_quality"] = _bell(math.log10(max(liq, 1)), math.log10(150_000), 0.55)

    # h1 turnover: real trading relative to pool size. 1.0x turnover is healthy, 8x is a churn bot
    tr = vol1 / liq if liq else 0
    f["turnover"] = _clamp(tr / 2.0) if tr <= 2 else _clamp(1.0 - (tr - 2) / 8.0)

    f["buy_pressure"] = _clamp((c["buys_h1"] / txns - 0.45) / 0.30) if txns else 0.0

    # accelerating, not exhausted: h1 gain outpacing the h6 average
    h1, h6 = c["chg_h1"], c["chg_h6"]
    f["momentum_accel"] = _clamp((h1 - h6 / 6.0) / 25.0)

    # chasing a vertical candle is how retail donates. +40% h1 already prices it in
    f["not_vertical"] = _clamp(1.0 - max(0.0, h1 - 40.0) / 160.0)

    age_h = (c.get("age_min") or 0) / 60.0
    f["age_sweet"] = _bell(math.log10(max(age_h, 0.05)), math.log10(6.0), 0.5)

    s = set(x.lower() for x in c.get("socials", []))
    f["socials"] = _clamp(0.45 * ("twitter" in s) + 0.35 * ("telegram" in s)
                          + 0.20 * bool(c.get("has_website")))

    ratio = (c["fdv"] / liq) if (liq and c["fdv"]) else 20.0
    f["fdv_sanity"] = _clamp(1.0 - (ratio - 5.0) / 45.0)

    avg_trade = vol1 / txns if txns else 0
    f["txn_depth"] = _clamp(1.0 - abs(math.log10(max(avg_trade, 1)) - math.log10(250)) / 1.3)

    # buying the dip inside an uptrend rather than the top of the candle
    f["dip_in_uptrend"] = 1.0 if (h1 > 5 and -18 < c["chg_m5"] < -1) else (0.5 if h1 > 5 else 0.0)

    f["buzz"] = buzzmod.mentions(buzz, c["symbol"], c.get("name", "")) if buzz else 0.0
    f["paid_boost"] = _clamp(c.get("boosts", 0) / 500.0)

    return {k: round(float(f.get(k, 0.0)), 4) for k in FEATURES}
