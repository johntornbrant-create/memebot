"""Off-chain attention: news RSS + Reddit public JSON.

Honest scope: X and Instagram have no free API (X = $200/mo, IG = none), so this is a
proxy for attention, not a replacement. It is a tie-breaker in scoring, never a trigger.
"""
import re, time, html
from collections import Counter
from .. import config
from ..http import get_json, get_text

STOP = set("""the a an and or of to in for on with at by from is are was were be been this that
crypto bitcoin btc eth ethereum solana sol price news market markets coin coins token tokens
new now how why what when will can could should says say said after before over under up down
million billion trillion usd dollar year week day today first last top best worst""".split())

WORD = re.compile(r"[A-Za-z][A-Za-z0-9]{2,14}")
TAG  = re.compile(r"<[^>]+>")
ITEM = re.compile(r"<(?:item|entry)\b.*?</(?:item|entry)>", re.S | re.I)
TITLE= re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)


def _clean(s):
    s = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", s, flags=re.S)
    return html.unescape(TAG.sub(" ", s)).strip()


def news_headlines():
    out = []
    for url in config.NEWS_FEEDS:
        raw = get_text(url)
        if not raw:
            continue
        for chunk in ITEM.findall(raw)[:40]:
            m = TITLE.search(chunk)
            if m:
                t = _clean(m.group(1))
                if t:
                    out.append(t)
        time.sleep(0.4)
    return out


def reddit_titles():
    out = []
    for sub in config.REDDIT_SUBS:
        d = get_json(f"https://www.reddit.com/r/{sub}/hot.json?limit=50", tries=2)
        for ch in ((d or {}).get("data", {}) or {}).get("children", []) or []:
            p = ch.get("data") or {}
            t = p.get("title")
            if t:
                out.append(f"{t} [score:{p.get('score', 0)}]")
        time.sleep(0.8)
    return out


def build():
    """-> {'terms': Counter, 'n_docs': int, 'headlines': [...]}"""
    heads = []
    try:
        heads += news_headlines()
    except Exception:
        pass
    try:
        heads += reddit_titles()
    except Exception:
        pass
    terms = Counter()
    for h in heads:
        for w in set(WORD.findall(h.lower())):
            if w not in STOP:
                terms[w] += 1
    return {"terms": terms, "n_docs": len(heads), "headlines": heads[:60]}


def mentions(buzz, symbol, name=""):
    """How loudly is this token being talked about right now? 0..1"""
    if not buzz or not buzz["terms"]:
        return 0.0
    t = buzz["terms"]
    keys = {symbol.lower()} | {w.lower() for w in WORD.findall(name)}
    keys = {k for k in keys if len(k) >= 3 and k not in STOP}
    if not keys:
        return 0.0
    hits = sum(t.get(k, 0) for k in keys)
    if hits == 0:
        return 0.0
    return min(1.0, hits / 6.0)
