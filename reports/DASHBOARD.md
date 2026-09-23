# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T01:49:50+00:00`

## Equity

| | |
|---|---|
| Equity | **$498.57** |
| Return | **-0.29%** (start $500.00) |
| Cash | $458.78 |
| Deployed | $39.79 (8.0%) |
| Open positions | 3 / 8 |
| Closed trades | 10 (3W / 7L, WR 30%) |
| Profit factor | 0.73 |
| Fees + slippage paid | $11.51 |
| Ticks run | 41 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $9.93 | +37% | +37% | 5.4h |
| UPTOBER | solana | $15.04 | $22.38 | +54% | +71% | 2.0h |
| based | solana | $7.48 | $7.07 | +0% | +0% | 0.0h |

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
tick #41  equity $500.02  cash $466.26  open 2
  scanning chains + news...
  161 raw candidates across 7 chains, 158 headlines/posts
  4 passed gates | rejected: liquidity too thin x85, no h1 volume x57, too old x9, already discovered x4, unknown age x2
  top: CATEWALK 0.82 | UPTOBER 0.71 | SATOSHINU 0.70 | based 0.49
  BUY[explore] based      $7.48 @ $0.0001793  score 0.49  solana  liq $38,226
  shadow: tracking 54, closed 0 this tick (0 would have won)
```
