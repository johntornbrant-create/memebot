# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T22:49:52+00:00`

## Equity

| | |
|---|---|
| Equity | **$512.38** |
| Return | **+2.48%** (start $500.00) |
| Cash | $483.00 |
| Deployed | $29.38 (5.7%) |
| Open positions | 3 / 8 |
| Closed trades | 6 (2W / 4L, WR 33%) |
| Profit factor | 1.28 |
| Fees + slippage paid | $8.33 |
| Ticks run | 29 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $8.33 | +15% | +25% | 2.4h |
| Archi | solana | $7.66 | $6.40 | +76% | +110% | 1.0h |
| MORE | solana | $15.44 | $14.65 | -2% | +0% | 0.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
tick #29  equity $514.57  cash $483.00  open 3
  scanning chains + news...
  102 raw candidates across 6 chains, 158 headlines/posts
  11 passed gates | rejected: liquidity too thin x47, no h1 volume x27, too old x10, already discovered x6, too new (bot war) x1
  top: MORE 0.78 | CATEWALK 0.76 | CLIP 0.71 | Archi 0.69 | UPTOBER 0.68
  no entries this tick
  shadow: tracking 48, closed 0 this tick (0 would have won)
```
