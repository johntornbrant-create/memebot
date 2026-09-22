# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T21:50:32+00:00`

## Equity

| | |
|---|---|
| Equity | **$510.96** |
| Return | **+2.19%** (start $500.00) |
| Cash | $482.14 |
| Deployed | $28.82 (5.6%) |
| Open positions | 3 / 8 |
| Closed trades | 5 (2W / 3L, WR 40%) |
| Profit factor | 1.77 |
| Fees + slippage paid | $7.04 |
| Ticks run | 25 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $7.45 | +2% | +9% | 1.4h |
| KCAT | solana | $15.48 | $13.71 | -9% | +11% | 1.0h |
| Archi | solana | $7.66 | $7.26 | +0% | +0% | 0.0h |

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
tick #25  equity $514.87  cash $472.08  open 4
  SELL BOP        100% @ $0.0004572  ->  $9.21   [trailing stop from +526%]
  SELL Habibi     100% @ $0.001655  ->  $8.50   [trailing stop from +394%]
  scanning chains + news...
  54 raw candidates across 3 chains, 158 headlines/posts
  8 passed gates | rejected: liquidity too thin x29, no h1 volume x16, too old x1
  top: BITCOINU 0.73 | SATOSHINU 0.70 | Archi 0.67 | CATEWALK 0.67 | UPTOBER 0.61
  BUY[explore] Archi      $7.66 @ $0.0002775  score 0.67  solana  liq $47,360
  shadow: tracking 42, closed 0 this tick (0 would have won)
```
