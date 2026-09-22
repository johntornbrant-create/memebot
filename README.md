# MEMEBOT — autonomous paper-trading memecoin bot

**$500 of fake money. No broker, no wallet, no keys, no real orders — ever.**
It runs on GitHub Actions every 15 minutes, so it works while your PC is off.

---

## What it actually does, each tick

1. **Discovers** new/trending pairs on Solana, Base, Ethereum and BSC
   (DexScreener + GeckoTerminal — both free, no API key).
2. **Reads attention** from news RSS (CoinDesk, Cointelegraph, Decrypt, Fox, Google News)
   and Reddit's public JSON.
3. **Gates hard** — kills ~90% of candidates before scoring: thin liquidity, no volume,
   too new (the first 20 min is a bot war we lose), too old, sell pressure,
   FDV/liquidity exit-liquidity traps.
4. **Scores** survivors on 12 features and buys the top ones above threshold.
5. **Manages exits** — stop loss, two-step take-profit ladder, trailing stop, time stop.
6. **Logs everything** and rewrites `reports/DASHBOARD.md`.
7. **Weekly**, refits its own scoring weights on its own closed trades.

## Honest limits — read these

- **X and Instagram are not in here.** X's API is $200/month and Instagram has no usable
  API. News RSS + Reddit is a *proxy* for attention, not a replacement, and it only ever
  acts as a tie-breaker (weight `buzz` = 0.04), never as a trigger.
- **Paper fills are modelled, not real.** Fees = 0.30% DEX + priority fee + slippage
  scaled by position/pool size. Real fills on a hot memecoin are worse.
- **The prior evidence is bad.** Our own copy-trade sim (2026-08-19) put $1,000 into the
  top-10 BSC wallets and got **0.555x in four days — 58% of positions went to zero**, with
  the bankroll dead in six hours. This bot is built assuming that is the base rate.
- **Expect to lose money.** The realistic outcome is a slow bleed from fees and stops.
  Treat a positive number after 200+ trades as the surprise, not the plan.

## Why it cannot lose everything

| Guard | Setting | Effect on $500 |
|---|---|---|
| Max per position | 3% of equity | $15 |
| Max concurrent | 8 | 24% max at risk |
| Max deployed | 35% of equity | ≥65% always in cash |
| Max new per tick | 2 | can't get eaten by a burst |
| Max trades/day | 12 | |
| Per-chain cap | 4 | |
| Stop loss | −35% | ~−$5.25 per trade |
| Daily breaker | −6% | no new entries 24h |
| Weekly breaker | −15% | no new entries 7d |
| **Kill switch** | **equity < $325** | **hard halt, manual reset only** |

Every position is sized as if it could go to **−100%**, because in this market it can.
Worst realistic tick: 8 open positions all rug at once = −24%. The kill switch fires
at −35% and the bot stops opening anything.

**Exits always run, even when halted.** A kill switch must never trap you in positions.

## How it develops its own tactics

**It starts with zero opinions.** All 12 features begin at identical weight. Nothing is
imported from research, from the internet, or from anyone else's strategy. Every opinion it
ends up with, it earned from its own results.

### 1. It explores on purpose

A bot that only buys what it already believes never discovers what it was wrong about. So
a share of every tick is spent on deliberate exploration — a **random** pick among
candidates that cleared the safety gates, score ignored completely, at half size.

| Phase | Explore rate |
|---|---|
| First 80 closed trades | **60%** — mostly learning |
| After that, forever | **20%** — never stops learning |

### 2. The shadow book — it learns from what it did NOT buy

This is the important one. A normal bot only ever sees the outcome of its own picks, so it
can never find out that the coin it rejected went 40x. It repeats that miss forever.

So **every candidate that clears the gates is tracked for 24 hours, bought or not.** It
records the peak move, the final move, and whether it would have won. The dashboard shows
its own mistake list: the biggest misses and what it scored them.

That produces one number that tells you whether any of this works:

> **Selection edge** = hit-rate of what it bought − hit-rate of what it skipped.
> Above zero, it is picking better than its own reject pile. At or below zero, it is not
> yet beating random, no matter what the equity curve says.

### 3. It refits weekly on both

| Training set | Volume | Why |
|---|---|---|
| Shadow outcomes | ~50–200/day | Learns from misses; enough data to actually fit |
| Real closed trades | a handful/day | Ground truth — carries real friction and exit timing, weighted **3x** |

Logistic regression, pure stdlib. Fitted weights get shrunk 50% toward flat, because small
samples lie. Entry threshold moves on its own: real win rate under 20% raises the bar,
over 40% lowers it.

## Chains

All 20 that DexScreener and GeckoTerminal cover between them — solana, base, ethereum, bsc,
arbitrum, polygon, avalanche, sui, ton, tron, blast, optimism, hyperliquid, abstract,
berachain, sonic, unichain, linea, mantle, cronos. GeckoTerminal network IDs are resolved
at runtime from its own API, so new chains get picked up without a code change.

Max 3 positions per chain, so one chain can't eat the book.

## Deploy

```bash
gh repo create memebot --public --source . --push
```

Then **Settings → Actions → General → Workflow permissions → Read and write**.
It starts ticking within 15 minutes. Watch `reports/DASHBOARD.md`.

Public repo = unlimited free Actions minutes. If you make it private, the free tier is
2,000 min/month — change the cron in `.github/workflows/trade.yml` to `0 * * * *` (hourly).

There are no secrets in this repo and nothing to leak — that is why public is safe here.

## Manual controls

| Want | Do |
|---|---|
| Run now | Actions → *memebot tick* → Run workflow |
| Force a refit early | Actions → *memebot weekly refit* → Run workflow → force ✓ |
| Stop it | Actions → *memebot tick* → ⋯ → Disable workflow |
| Reset after a kill switch | delete `state/portfolio.json`, commit |
| Change any rule | `bot/config.py` — everything is in that one file |

## Run locally

```bash
python -m bot.run
```
