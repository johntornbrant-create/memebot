# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T03:38:53+00:00`

## Equity

| | |
|---|---|
| Equity | **$498.55** |
| Return | **-0.29%** (start $500.00) |
| Cash | $457.91 |
| Deployed | $40.63 (8.2%) |
| Open positions | 4 / 8 |
| Closed trades | 10 (3W / 7L, WR 30%) |
| Profit factor | 0.73 |
| Fees + slippage paid | $12.77 |
| Ticks run | 48 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $8.41 | +131% | +163% | 7.3h |
| UPTOBER | solana | $15.04 | $14.62 | +0% | +71% | 3.8h |
| based | solana | $7.48 | $2.64 | -25% | +133% | 1.8h |
| 蝴蝶家园 | bsc | $14.96 | $14.50 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| SHIELD | $-3.94 | -53% | 0.3h | stop loss -45% |
| ACAT | $-7.53 | -100% | 0.9h | stop loss -100% |
| MORE | $-6.18 | -40% | 1.2h | stop loss -35% |
| Archi | $+0.08 | +1% | 1.9h | stop loss -76% |
| KCAT | $-6.40 | -41% | 1.7h | stop loss -37% |
| Habibi | $+11.26 | +147% | 2.4h | trailing stop from +394% |
| BOP | $+18.46 | +250% | 4.4h | trailing stop from +526% |
| CATEWALK | $-6.25 | -42% | 4.7h | stop loss -37% |
| SATOSHINU | $-7.12 | -47% | 4.3h | stop loss -43% |
| TRUMPTV | $-3.39 | -45% | 1.1h | stop loss -37% |

## Learned weights (v0)

_prior_

| Feature | Weight |
|---|---|
| liq_quality | +0.083 |
| turnover | +0.083 |
| buy_pressure | +0.083 |
| momentum_accel | +0.083 |
| not_vertical | +0.083 |
| age_sweet | +0.083 |
| socials | +0.083 |
| fdv_sanity | +0.083 |
| txn_depth | +0.083 |
| dip_in_uptrend | +0.083 |
| buzz | +0.083 |
| paid_boost | +0.083 |

## Last run log
```
tick #48  equity $500.34  cash $472.87  open 3
  scanning chains + news...
  172 raw candidates across 10 chains, 158 headlines/posts
  7 passed gates | rejected: liquidity too thin x92, no h1 volume x63, too old x7, unknown age x1, already discovered x1
  top: 蝴蝶家园 0.73 | CATEWALK 0.67 | PHAT 0.60 | UPTOBER 0.59 | LeoGuigna 0.49
  BUY[exploit] 蝴蝶家园       $14.96 @ $0.0002308  score 0.73  bsc  liq $44,383
  shadow: tracking 62, closed 0 this tick (0 would have won)
```
