"""Writes reports/DASHBOARD.md - the thing you actually read on your phone."""
import json, os
from . import config, portfolio as pf_mod
from .scoring import load_weights

ROOT = os.path.join(os.path.dirname(__file__), "..")
DASH = os.path.join(ROOT, "reports", "DASHBOARD.md")
TRADES = os.path.join(ROOT, "state", "trades.jsonl")


def _trades(n=15):
    rows = []
    try:
        with open(TRADES) as fh:
            rows = [json.loads(l) for l in fh if l.strip()]
    except FileNotFoundError:
        pass
    return rows[-n:][::-1], rows


def write_dashboard(pf, log_lines):
    recent, allt = _trades()
    w, meta = load_weights()
    eq, ret = pf["equity"], pf["equity"] / config.START_EQUITY - 1
    st = pf["stats"]
    closed = st["closed"] or 1
    wr = st["wins"] / closed
    peak = max([eq] + [config.START_EQUITY])
    gains = [t["pnl_usd"] for t in allt if t["pnl_usd"] > 0]
    losses = [t["pnl_usd"] for t in allt if t["pnl_usd"] <= 0]
    pfactor = (sum(gains) / abs(sum(losses))) if losses and sum(losses) else float("nan")

    L = []
    L.append("# MEMEBOT — paper trading dashboard\n")
    L.append(f"_Fake money. No broker, no keys, no real orders._  \nUpdated `{pf['updated']}`\n")
    if pf.get("halted"):
        L.append(f"> 🛑 **HALTED** — {pf.get('halt_reason','')}\n")

    L.append("## Equity\n")
    L.append("| | |\n|---|---|")
    L.append(f"| Equity | **${eq:,.2f}** |")
    L.append(f"| Return | **{ret:+.2%}** (start ${config.START_EQUITY:,.2f}) |")
    L.append(f"| Cash | ${pf['cash']:,.2f} |")
    L.append(f"| Deployed | ${eq - pf['cash']:,.2f} ({(eq-pf['cash'])/eq if eq else 0:.1%}) |")
    L.append(f"| Open positions | {len(pf['positions'])} / {config.MAX_CONCURRENT} |")
    L.append(f"| Closed trades | {st['closed']} ({st['wins']}W / {st['losses']}L, WR {wr:.0%}) |")
    L.append(f"| Profit factor | {pfactor:.2f} |" if pfactor == pfactor else "| Profit factor | – |")
    L.append(f"| Fees + slippage paid | ${st['fees_paid']:,.2f} |")
    L.append(f"| Ticks run | {st['ticks']} |\n")

    L.append("## Open positions\n")
    if pf["positions"]:
        L.append("| Token | Chain | Cost | Now | P&L | Peak | Held |")
        L.append("|---|---|---|---|---|---|---|")
        for p in pf["positions"].values():
            val = p["tokens"] * p["last_price"]
            g = (p["last_price"] / p["entry_price"] - 1) if p["entry_price"] else -1
            L.append(f"| {p['symbol']} | {p['chain']} | ${p['cost_usd']:.2f} | ${val:.2f} | "
                     f"{g:+.0%} | {p['peak_gain']:+.0%} | {pf_mod.hours_since(p['opened']):.1f}h |")
    else:
        L.append("_flat_")
    L.append("")

    L.append("## Last closed trades\n")
    if recent:
        L.append("| Token | P&L | % | Held | Exit reason |")
        L.append("|---|---|---|---|---|")
        for t in recent:
            L.append(f"| {t['symbol']} | ${t['pnl_usd']:+.2f} | {t['pnl_pct']:+.0%} | "
                     f"{t['hold_h']:.1f}h | {t['reason']} |")
    else:
        L.append("_none yet_")
    L.append("")

    L.append(f"## Learned weights (v{meta.get('version',0)})\n")
    L.append(f"_{meta.get('note','prior — not yet refit on own trades')}_\n")
    L.append("| Feature | Weight |\n|---|---|")
    for k, v in sorted(w.items(), key=lambda t: -abs(t[1])):
        L.append(f"| {k} | {v:+.3f} |")
    L.append("")

    L.append("## Last run log\n```")
    L.extend(log_lines[-40:])
    L.append("```")

    os.makedirs(os.path.dirname(DASH), exist_ok=True)
    with open(DASH, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
