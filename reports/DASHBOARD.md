# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T07:38:42+00:00`

## Equity

| | |
|---|---|
| Equity | **$497.69** |
| Return | **-0.46%** (start $500.00) |
| Cash | $457.69 |
| Deployed | $40.01 (8.0%) |
| Open positions | 3 / 8 |
| Closed trades | 17 (6W / 11L, WR 35%) |
| Profit factor | 0.82 |
| Fees + slippage paid | $19.74 |
| Ticks run | 63 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| UPTOBER | solana | $15.04 | $15.04 | +3% | +71% | 7.8h |
| 蝴蝶家园 | bsc | $14.96 | $13.44 | -7% | +10% | 4.0h |
| MSTOCK | bsc | $15.52 | $11.52 | +53% | +118% | 1.5h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| LeoGuigna | $-15.38 | -100% | 0.8h | stop loss -99% |
| 币安的守护者 | $-4.02 | -52% | 1.5h | stop loss -44% |
| based | $-6.45 | -42% | 1.2h | stop loss -37% |
| DURIAN | $-5.02 | -64% | 0.5h | stop loss -57% |
| LeoGuigna | $+19.66 | +263% | 2.0h | trailing stop from +724% |
| BITCOINU | $+7.57 | +99% | 9.2h | trailing stop from +248% |
| based | $+1.95 | +26% | 2.0h | stop loss -38% |
| SHIELD | $-3.94 | -53% | 0.3h | stop loss -45% |
| ACAT | $-7.53 | -100% | 0.9h | stop loss -100% |
| MORE | $-6.18 | -40% | 1.2h | stop loss -35% |
| Archi | $+0.08 | +1% | 1.9h | stop loss -76% |
| KCAT | $-6.40 | -41% | 1.7h | stop loss -37% |
| Habibi | $+11.26 | +147% | 2.4h | trailing stop from +394% |
| BOP | $+18.46 | +250% | 4.4h | trailing stop from +526% |
| CATEWALK | $-6.25 | -42% | 4.7h | stop loss -37% |

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
tick #63  equity $515.07  cash $453.95  open 5
  SELL 币安的守护者     100% @ $0.00374  ->  $3.74   [stop loss -44%]
  SELL LeoGuigna  100% @ $2.958e-06  ->  $0.00   [stop loss -99%]
  scanning chains + news...
  118 raw candidates across 4 chains, 160 headlines/posts
  2 passed gates | rejected: liquidity too thin x80, no h1 volume x21, too old x7, already discovered x4, unknown age x2
  top: based 0.70 | MOUSE 0.56
  no entries this tick
  shadow: tracking 74, closed 0 this tick (0 would have won)
```
