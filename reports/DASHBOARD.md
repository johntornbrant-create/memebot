# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T23:05:02+00:00`

## Equity

| | |
|---|---|
| Equity | **$514.70** |
| Return | **+2.94%** (start $500.00) |
| Cash | $483.00 |
| Deployed | $31.70 (6.2%) |
| Open positions | 3 / 8 |
| Closed trades | 6 (2W / 4L, WR 33%) |
| Profit factor | 1.28 |
| Fees + slippage paid | $8.33 |
| Ticks run | 30 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $8.25 | +13% | +25% | 2.7h |
| Archi | solana | $7.66 | $6.85 | +89% | +110% | 1.2h |
| MORE | solana | $15.44 | $16.60 | +11% | +11% | 0.5h |

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
tick #30  equity $512.38  cash $483.00  open 3
  scanning chains + news...
  104 raw candidates across 8 chains, 158 headlines/posts
  7 passed gates | rejected: liquidity too thin x59, no h1 volume x35, too old x2, too new (bot war) x1
  top: CATEWALK 0.84 | SATOSHINU 0.72 | Archi 0.71 | MORE 0.70 | UPTOBER 0.68
  no entries this tick
  shadow: tracking 48, closed 0 this tick (0 would have won)
```
