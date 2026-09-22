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

## How "it develops its own tactics"

`bot/learn.py`. Every trade stores its 12-feature vector at entry. Weekly, the bot fits a
logistic regression (pure stdlib, no dependencies) on its own closed trades, labelling a
win as **+15% net**, then:

- rescales the fitted weights to the prior's magnitude,
- **blends 50/50 with the prior** — small samples lie, so it never fully trusts itself,
- moves the entry threshold: win rate under 25% → threshold up; over 45% → threshold down,
- refuses to fit at all below **60 closed trades**.

The only teacher is our own realised PnL. No copied strategies, no web-sourced alpha.

## Features and where they came from

| Feature | Prior weight | Source |
|---|---|---|
| `socials` | +0.18 | arXiv 2607.02823 — socials at mint = 17.4x lift, strongest known single feature |
| `turnover` | +0.14 | h1 volume / liquidity |
| `buy_pressure` | +0.13 | h1 buys / total |
| `not_vertical` | +0.11 | "pullback, don't chase tops" |
| `liq_quality` | +0.10 | bell curve centred on $150k |
| `momentum_accel` | +0.09 | h1 outpacing h6 |
| `age_sweet` | +0.08 | ~6h old: past the bot war, before full discovery |
| `fdv_sanity` | +0.08 | FDV/liquidity ratio |
| `dip_in_uptrend` | +0.07 | m5 red inside an h1 green |
| `txn_depth` | +0.06 | organic trade sizes vs manufactured |
| `buzz` | +0.04 | news/Reddit mentions |
| `paid_boost` | **−0.05** | paid DexScreener boosts = someone buying attention |

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
