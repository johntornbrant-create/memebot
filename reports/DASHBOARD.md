# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T23:48:45+00:00`

## Equity

| | |
|---|---|
| Equity | **$501.18** |
| Return | **+0.24%** (start $500.00) |
| Cash | $477.74 |
| Deployed | $23.44 (4.7%) |
| Open positions | 2 / 8 |
| Closed trades | 8 (3W / 5L, WR 38%) |
| Profit factor | 1.02 |
| Fees + slippage paid | $9.57 |
| Ticks run | 33 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $8.40 | +16% | +25% | 3.4h |
| UPTOBER | solana | $15.04 | $14.58 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
tick #33  equity $505.61  cash $483.00  open 3
  SELL Archi      100% @ $6.69e-05  ->  $0.52   [stop loss -76%]
  SELL MORE       100% @ $7.521e-05  ->  $9.26   [stop loss -35%]
  scanning chains + news...
  125 raw candidates across 7 chains, 158 headlines/posts
  5 passed gates | rejected: liquidity too thin x70, no h1 volume x39, too old x9, too new (bot war) x1, already discovered x1
  top: CATEWALK 0.82 | UPTOBER 0.76 | ACAT 0.65 | TIKCAT 0.56 | EMPLOYIM 0.55
  BUY[exploit] UPTOBER    $15.04 @ $0.0001312  score 0.76  solana  liq $31,599
  shadow: tracking 49, closed 0 this tick (0 would have won)
```
