"""On-chain candidate discovery. Free, keyless: DexScreener + GeckoTerminal."""
import time
from .. import config
from ..http import get_json

DS = "https://api.dexscreener.com"
GT = "https://api.geckoterminal.com/api/v2"
GT_NET = {"solana": "solana", "base": "base", "ethereum": "eth", "bsc": "bsc"}


def _f(x, d=0.0):
    try:
        return float(x)
    except (TypeError, ValueError):
        return d


def _norm_ds(p):
    """DexScreener pair -> our canonical candidate dict."""
    if not isinstance(p, dict):
        return None
    base = p.get("baseToken") or {}
    addr = base.get("address")
    chain = p.get("chainId")
    if not addr or chain not in config.CHAINS:
        return None
    liq = _f((p.get("liquidity") or {}).get("usd"))
    vol = p.get("volume") or {}
    txns = (p.get("txns") or {}).get("h1") or {}
    chg = p.get("priceChange") or {}
    created = p.get("pairCreatedAt")
    age_min = (time.time() - created / 1000.0) / 60.0 if created else None
    info = p.get("info") or {}
    socials = info.get("socials") or []
    return {
        "chain": chain,
        "address": addr,
        "pair": p.get("pairAddress"),
        "symbol": base.get("symbol") or "?",
        "name": base.get("name") or "",
        "price": _f(p.get("priceUsd")),
        "liquidity": liq,
        "fdv": _f(p.get("fdv") or p.get("marketCap")),
        "vol_h1": _f(vol.get("h1")),
        "vol_h6": _f(vol.get("h6")),
        "vol_h24": _f(vol.get("h24")),
        "buys_h1": _f(txns.get("buys")),
        "sells_h1": _f(txns.get("sells")),
        "chg_m5": _f(chg.get("m5")),
        "chg_h1": _f(chg.get("h1")),
        "chg_h6": _f(chg.get("h6")),
        "chg_h24": _f(chg.get("h24")),
        "age_min": age_min,
        "socials": [s.get("type", "") for s in socials if isinstance(s, dict)],
        "has_website": bool(info.get("websites")),
        "boosts": _f((p.get("boosts") or {}).get("active")),
        "src": "dexscreener",
    }


def _pairs_for_tokens(chain, addresses):
    out = []
    for i in range(0, len(addresses), 30):
        chunk = ",".join(addresses[i:i + 30])
        d = get_json(f"{DS}/tokens/v1/{chain}/{chunk}")
        if isinstance(d, list):
            out.extend(d)
        time.sleep(0.3)
    return out


def from_dexscreener():
    """Latest token profiles + boosted tokens -> full pair data."""
    cands, by_chain = [], {}
    for ep in ("/token-profiles/latest/v1", "/token-boosts/latest/v1", "/token-boosts/top/v1"):
        d = get_json(DS + ep)
        if not isinstance(d, list):
            continue
        for t in d:
            ch, ad = t.get("chainId"), t.get("tokenAddress")
            if ch in config.CHAINS and ad:
                by_chain.setdefault(ch, set()).add(ad)
        time.sleep(0.3)
    for ch, addrs in by_chain.items():
        for p in _pairs_for_tokens(ch, sorted(addrs)):
            c = _norm_ds(p)
            if c:
                cands.append(c)
    return cands


def from_geckoterminal():
    """New + trending pools per chain. Hands addresses back to DexScreener for detail."""
    by_chain = {}
    for chain in config.CHAINS:
        net = GT_NET.get(chain)
        for ep in ("new_pools", "trending_pools"):
            d = get_json(f"{GT}/networks/{net}/{ep}?page=1")
            for item in (d or {}).get("data", []) or []:
                rel = (item.get("relationships") or {}).get("base_token", {}).get("data", {})
                tid = rel.get("id", "")          # e.g. "solana_9xQe..."
                addr = tid.split("_", 1)[1] if "_" in tid else None
                if addr:
                    by_chain.setdefault(chain, set()).add(addr)
            time.sleep(2.2)                      # GT free tier ~30 req/min
    cands = []
    for ch, addrs in by_chain.items():
        for p in _pairs_for_tokens(ch, sorted(addrs)[:120]):
            c = _norm_ds(p)
            if c:
                cands.append(c)
    return cands


def discover():
    """All on-chain candidates, de-duplicated on (chain, address), best liquidity wins."""
    seen = {}
    for fn in (from_dexscreener, from_geckoterminal):
        try:
            for c in fn():
                k = (c["chain"], c["address"])
                if k not in seen or c["liquidity"] > seen[k]["liquidity"]:
                    seen[k] = c
        except Exception:
            continue
    return list(seen.values())


def quote(chain, address):
    """Current price + liquidity for an open position. None if it cannot be priced."""
    d = get_json(f"{DS}/tokens/v1/{chain}/{address}")
    if not isinstance(d, list) or not d:
        return None
    best = max(d, key=lambda p: _f((p.get("liquidity") or {}).get("usd")))
    return _norm_ds(best)
