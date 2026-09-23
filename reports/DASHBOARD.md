# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T01:05:44+00:00`

## Equity

| | |
|---|---|
| Equity | **$499.27** |
| Return | **-0.15%** (start $500.00) |
| Cash | $462.71 |
| Deployed | $36.56 (7.3%) |
| Open positions | 3 / 8 |
| Closed trades | 9 (3W / 6L, WR 33%) |
| Profit factor | 0.81 |
| Fees + slippage paid | $10.73 |
| Ticks run | 38 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $9.88 | +36% | +36% | 4.7h |
| UPTOBER | solana | $15.04 | $19.19 | +32% | +32% | 1.3h |
| SHIELD | solana | $7.49 | $7.09 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
tick #38  equity $509.27  cash $470.20  open 3
  SELL ACAT       100% @ $2.521e-06  ->  $0.00   [stop loss -100%]
  scanning chains + news...
  125 raw candidates across 6 chains, 160 headlines/posts
  5 passed gates | rejected: liquidity too thin x80, no h1 volume x32, too old x7, unknown age x1
  top: CATEWALK 0.82 | UPTOBER 0.71 | SATOSHINU 0.60 | HACKA 0.58 | SHIELD 0.49
  BUY[explore] SHIELD     $7.49 @ $0.0001257  score 0.49  solana  liq $32,104
  shadow: tracking 53, closed 0 this tick (0 would have won)
```
