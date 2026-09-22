import json, time, urllib.request, urllib.error
from . import config

def get_json(url, tries=3, backoff=1.6):
    """Plain stdlib GET. Returns parsed JSON or None. Never raises."""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": config.USER_AGENT, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=config.HTTP_TIMEOUT) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except Exception:
            if i == tries - 1:
                return None
            time.sleep(backoff ** i)
    return None

def get_text(url, tries=2, backoff=1.6):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": config.USER_AGENT})
            with urllib.request.urlopen(req, timeout=config.HTTP_TIMEOUT) as r:
                return r.read().decode("utf-8", "replace")
        except Exception:
            if i == tries - 1:
                return ""
            time.sleep(backoff ** i)
    return ""
