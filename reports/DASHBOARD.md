# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T22:23:33+00:00`

## Equity

| | |
|---|---|
| Equity | **$513.42** |
| Return | **+2.68%** (start $500.00) |
| Cash | $482.14 |
| Deployed | $31.28 (6.1%) |
| Open positions | 3 / 8 |
| Closed trades | 5 (2W / 3L, WR 40%) |
| Profit factor | 1.77 |
| Fees + slippage paid | $7.04 |
| Ticks run | 27 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $9.08 | +25% | +25% | 2.0h |
| KCAT | solana | $15.48 | $10.92 | -27% | +11% | 1.5h |
| Archi | solana | $7.66 | $11.28 | +55% | +55% | 0.6h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
tick #27  equity $508.87  cash $482.14  open 3
  scanning chains + news...
  156 raw candidates across 9 chains, 158 headlines/posts
  12 passed gates | rejected: liquidity too thin x64, no h1 volume x50, too old x19, already discovered x10, too new (bot war) x1
  top: UPTOBER 0.74 | Archi 0.74 | TIKCAT 0.73 | BITCOINU 0.70 | CLIP 0.68
  no entries this tick
  shadow: tracking 47, closed 0 this tick (0 would have won)
```
