"""One tick of the bot. Idempotent-ish: safe to run on any schedule."""
import sys, random, traceback
from . import config, portfolio as pf_mod, risk, scoring, features, shadow
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


def scan(pf, allow_entries=True):
    weights, meta = scoring.load_weights()
    thr = float(meta.get("threshold", config.ENTRY_THRESHOLD))

    log("  scanning chains + news...")
    cands = onchain.discover()
    buzz = buzzmod.build()
    log(f"  {len(cands)} raw candidates across {len(set(c['chain'] for c in cands))} chains, "
        f"{buzz['n_docs']} headlines/posts")

    scored, rejected = [], {}
    for c in cands:
        ok, why = features.passes_gates(c)
        if not ok:
            rejected[why] = rejected.get(why, 0) + 1
            continue
        f = features.extract(c, buzz)
        scored.append((scoring.score(f, weights), c, f))

    scored.sort(key=lambda t: -t[0])
    log(f"  {len(scored)} passed gates | rejected: " +
        ", ".join(f"{k} x{v}" for k, v in sorted(rejected.items(), key=lambda t: -t[1])[:5]))
    if scored:
        log("  top: " + " | ".join(f"{c['symbol']} {s:.2f}" for s, c, _ in scored[:5]))

    # ---- explore vs exploit -------------------------------------------------
    # Some slots go to the best-scoring candidate. Some go to a RANDOM gate-passer,
    # score ignored, so the bot keeps discovering what its own model is blind to.
    closed = pf["stats"]["closed"]
    ex_rate = config.EXPLORE_RATE_COLD if closed < config.COLD_TRADES else config.EXPLORE_RATE_WARM

    plan = []
    pool = list(scored)
    for _ in range(config.MAX_NEW_PER_TICK):
        if not pool:
            break
        if random.random() < ex_rate:
            pick = pool.pop(random.randrange(len(pool)))
            plan.append((pick, "explore"))
        else:
            best = pool[0]
            if best[0] < thr:
                break
            plan.append((pool.pop(0), "exploit"))

    opened, taken_keys = 0, set()
    for (s, c, f), mode in (plan if allow_entries else []):
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
        if mode == "explore":
            size = min(size, pf["equity"] * config.MAX_POS_PCT * 0.7)   # smaller bets on what we know nothing about
            if size < config.MIN_POS_USD:
                continue
        pf_mod.open_position(pf, c, size, f, s)
        taken_keys.add(f"{c['chain']}:{c['address']}")
        opened += 1
        log(f"  BUY[{mode}] {c['symbol']:<10} ${size:.2f} @ ${c['price']:.8g}  "
            f"score {s:.2f}  {c['chain']}  liq ${c['liquidity']:,.0f}")
    if opened == 0:
        log("  no entries this tick")

    # ---- shadow book: follow EVERYTHING it saw, bought or not ---------------
    if config.SHADOW_ENABLED:
        book = shadow.load()
        for s, c, f in scored:
            shadow.track(book, c, f, s, f"{c['chain']}:{c['address']}" in taken_keys)
        done, wins = shadow.update(book)
        shadow.save(book)
        log(f"  shadow: tracking {len(book)}, closed {done} this tick ({wins} would have won)")
        for m in shadow.missed_report(3):
            log(f"    MISSED {m['symbol']:<10} peak {m['peak_gain']:+.0%}  (scored {m['score']:.2f})")


def tick(exits_only=False):
    pf = pf_mod.load()
    risk.roll_marks(pf)
    pf["stats"]["ticks"] += 1
    log(f"tick #{pf['stats']['ticks']}  equity ${pf['equity']:.2f}  "
        f"cash ${pf['cash']:.2f}  open {len(pf['positions'])}")

    try:
        manage_exits(pf)
    except Exception:
        log("  exit management failed:\n" + traceback.format_exc())

    if exits_only:
        pf_mod.save(pf)
        log(f"exit sweep done. equity ${pf['equity']:.2f}")
        return pf

    can, reasons = risk.equity_curve_checks(pf)
    try:
        # Entries are gated by risk. The shadow book is NOT - it is pure research and it is
        # the most valuable thing this bot produces, so it keeps collecting even when the
        # kill switch has stopped all trading.
        scan(pf, allow_entries=can)
    except Exception:
        log("  scan failed: " + traceback.format_exc())
    if not can:
        log(f"  entries blocked: {'; '.join(reasons)}")

    pf_mod.save(pf)
    write_dashboard(pf, LOG)
    ret = pf["equity"] / config.START_EQUITY - 1
    log(f"done. equity ${pf['equity']:.2f} ({ret:+.2%} since start)")
    return pf


if __name__ == "__main__":
    try:
        tick(exits_only="--exits-only" in sys.argv)
    except Exception:
        traceback.print_exc()
        sys.exit(1)
