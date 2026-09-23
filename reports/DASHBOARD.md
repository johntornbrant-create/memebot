# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T00:07:04+00:00`

## Equity

| | |
|---|---|
| Equity | **$502.29** |
| Return | **+0.46%** (start $500.00) |
| Cash | $470.20 |
| Deployed | $32.09 (6.4%) |
| Open positions | 3 / 8 |
| Closed trades | 8 (3W / 5L, WR 38%) |
| Profit factor | 1.02 |
| Fees + slippage paid | $9.97 |
| Ticks run | 34 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $7.81 | +7% | +25% | 3.7h |
| UPTOBER | solana | $15.04 | $16.75 | +15% | +15% | 0.3h |
| ACAT | solana | $7.53 | $7.13 | +0% | +0% | 0.0h |

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
tick #34  equity $501.18  cash $477.74  open 2
  scanning chains + news...
  127 raw candidates across 7 chains, 158 headlines/posts
  6 passed gates | rejected: liquidity too thin x71, no h1 volume x40, too old x8, too new (bot war) x1, already discovered x1
  top: UPTOBER 0.83 | ACAT 0.72 | CATEWALK 0.64 | EMPLOYIM 0.63 | Archi 0.62
  BUY[explore] ACAT       $7.53 @ $0.0005966  score 0.72  solana  liq $71,465
  shadow: tracking 51, closed 0 this tick (0 would have won)
```
