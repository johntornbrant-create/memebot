# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T22:36:30+00:00`

## Equity

| | |
|---|---|
| Equity | **$514.57** |
| Return | **+2.91%** (start $500.00) |
| Cash | $483.00 |
| Deployed | $31.57 (6.1%) |
| Open positions | 3 / 8 |
| Closed trades | 6 (2W / 4L, WR 33%) |
| Profit factor | 1.28 |
| Fees + slippage paid | $8.33 |
| Ticks run | 28 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $8.51 | +17% | +25% | 2.2h |
| Archi | solana | $7.66 | $7.63 | +110% | +110% | 0.8h |
| MORE | solana | $15.44 | $14.98 | +0% | +0% | 0.0h |

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
tick #28  equity $513.42  cash $482.14  open 3
  SELL KCAT       100% @ $0.0001102  ->  $9.08   [stop loss -37%]
  SELL Archi      50% @ $0.0005831  ->  $7.22   [take profit +80% (sold 50%)]
  scanning chains + news...
  114 raw candidates across 7 chains, 158 headlines/posts
  12 passed gates | rejected: liquidity too thin x50, no h1 volume x28, too old x12, already discovered x10, too new (bot war) x2
  top: MORE 0.74 | BITCOINU 0.71 | CLIP 0.71 | Archi 0.68 | SATOSHINU 0.68
  BUY[exploit] MORE       $15.44 @ $0.0001164  score 0.74  solana  liq $36,518
  shadow: tracking 48, closed 0 this tick (0 would have won)
```
