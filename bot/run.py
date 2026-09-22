"""One tick of the bot. Idempotent-ish: safe to run on any schedule."""
import sys, traceback
from . import config, portfolio as pf_mod, risk, scoring, features
from .sources import onchain, buzz as buzzmod
from .report import write_dashboard

LOG = []


def log(msg):
    LOG.append(msg)
    print(msg, flush=True)


def manage_exits(pf):
    """Runs even when halted - a kill switch must never trap us in positions."""
    if not pf["positions"]:
        pf_mod.mark_to_market(pf, {})
        return
    quotes = {}
    for key, p in list(pf["positions"].items()):
        try:
            quotes[key] = onchain.quote(p["chain"], p["address"])
        except Exception:
            quotes[key] = None
    pf_mod.mark_to_market(pf, quotes)

    for key in list(pf["positions"].keys()):
        p = pf["positions"][key]
        q = quotes.get(key)
        price = p["last_price"]
        liq = q["liquidity"] if q else 0.0
        for frac, reason in pf_mod.exit_rules(p, price, liq):
            net, closed = pf_mod.sell(pf, key, price, liq, frac, reason)
            log(f"  SELL {p['symbol']:<10} {frac:.0%} @ ${price:.8g}  ->  ${net:.2f}   [{reason}]")
            if closed:
                break
    pf_mod.mark_to_market(pf, quotes)


def find_entries(pf):
    weights, meta = scoring.load_weights()
    thr = float(meta.get("threshold", config.ENTRY_THRESHOLD))

    log("  scanning chains + news...")
    cands = onchain.discover()
    buzz = buzzmod.build()
    log(f"  {len(cands)} raw candidates, {buzz['n_docs']} headlines/posts")

    scored, rejected = [], {}
    for c in cands:
        ok, why = features.passes_gates(c)
        if not ok:
            rejected[why] = rejected.get(why, 0) + 1
            continue
        f = features.extract(c, buzz)
        s = scoring.score(f, weights)
        scored.append((s, c, f))

    scored.sort(key=lambda t: -t[0])
    log(f"  {len(scored)} passed gates | rejected: " +
        ", ".join(f"{k} x{v}" for k, v in sorted(rejected.items(), key=lambda t: -t[1])[:5]))
    if scored:
        log("  top: " + " | ".join(f"{c['symbol']} {s:.2f}" for s, c, _ in scored[:5]))

    opened = 0
    for s, c, f in scored:
        if opened >= config.MAX_NEW_PER_TICK:
            break
        pf_mod.log_signal({"t": pf_mod.now_iso(), "symbol": c["symbol"], "chain": c["chain"],
                           "address": c["address"], "score": s, "features": f,
                           "liq": c["liquidity"], "taken": False})
        if s < thr:
            break                                    # list is sorted; nothing below clears
        ok, reasons = risk.equity_curve_checks(pf)
        if not ok:
            log(f"  no entry: {'; '.join(reasons)}")
            break
        ok, why = risk.can_open(pf, c)
        if not ok:
            continue
        size = risk.size_position(pf, c)
        if size < config.MIN_POS_USD:
            continue
        p = pf_mod.open_position(pf, c, size, f, s)
        opened += 1
        log(f"  BUY  {c['symbol']:<10} ${size:.2f} @ ${c['price']:.8g}  score {s:.2f}  "
            f"liq ${c['liquidity']:,.0f}  socials {c['socials']}")
    if opened == 0:
        log("  no entries this tick")


def tick():
    pf = pf_mod.load()
    risk.roll_marks(pf)
    pf["stats"]["ticks"] += 1
    log(f"tick #{pf['stats']['ticks']}  equity ${pf['equity']:.2f}  "
        f"cash ${pf['cash']:.2f}  open {len(pf['positions'])}")

    try:
        manage_exits(pf)
    except Exception:
        log("  exit management failed:\n" + traceback.format_exc())

    can, reasons = risk.equity_curve_checks(pf)
    if can:
        try:
            find_entries(pf)
        except Exception:
            log("  entry scan failed:\n" + traceback.format_exc())
    else:
        log(f"  entries blocked: {'; '.join(reasons)}")

    pf_mod.save(pf)
    write_dashboard(pf, LOG)
    ret = pf["equity"] / config.START_EQUITY - 1
    log(f"done. equity ${pf['equity']:.2f} ({ret:+.2%} since start)")
    return pf


if __name__ == "__main__":
    try:
        tick()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
