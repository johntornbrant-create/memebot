# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T23:35:40+00:00`

## Equity

| | |
|---|---|
| Equity | **$505.61** |
| Return | **+1.12%** (start $500.00) |
| Cash | $483.00 |
| Deployed | $22.61 (4.5%) |
| Open positions | 3 / 8 |
| Closed trades | 6 (2W / 4L, WR 33%) |
| Profit factor | 1.28 |
| Fees + slippage paid | $8.33 |
| Ticks run | 32 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $8.28 | +14% | +25% | 3.2h |
| Archi | solana | $7.66 | $2.83 | -22% | +110% | 1.8h |
| MORE | solana | $15.44 | $11.50 | -23% | +11% | 1.0h |

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
tick #32  equity $508.95  cash $483.00  open 3
  scanning chains + news...
  66 raw candidates across 3 chains, 158 headlines/posts
  6 passed gates | rejected: liquidity too thin x40, no h1 volume x14, too old x5, too new (bot war) x1
  top: ACAT 0.75 | CATEWALK 0.75 | SATOSHINU 0.67 | EMPLOYIM 0.61 | UPTOBER 0.60
  no entries this tick
  shadow: tracking 49, closed 0 this tick (0 would have won)
```
