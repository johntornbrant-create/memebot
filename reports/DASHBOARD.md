# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T04:25:47+00:00`

## Equity

| | |
|---|---|
| Equity | **$518.94** |
| Return | **+3.79%** (start $500.00) |
| Cash | $465.84 |
| Deployed | $53.09 (10.2%) |
| Open positions | 4 / 8 |
| Closed trades | 11 (4W / 7L, WR 36%) |
| Profit factor | 0.78 |
| Fees + slippage paid | $14.35 |
| Ticks run | 51 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $9.50 | +248% | +248% | 8.0h |
| UPTOBER | solana | $15.04 | $16.58 | +14% | +71% | 4.6h |
| 蝴蝶家园 | bsc | $14.96 | $15.80 | +9% | +9% | 0.8h |
| LeoGuigna | solana | $7.46 | $11.22 | +218% | +218% | 0.6h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| based | $+1.95 | +26% | 2.0h | stop loss -38% |
| SHIELD | $-3.94 | -53% | 0.3h | stop loss -45% |
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
tick #51  equity $499.95  cash $452.26  open 4
  SELL BITCOINU   25% @ $0.0004895  ->  $2.79   [take profit +200% (sold 25%)]
  SELL LeoGuigna  50% @ $0.0003631  ->  $10.79   [take profit +80% (sold 50%)]
  scanning chains + news...
  73 raw candidates across 6 chains, 158 headlines/posts
  7 passed gates | rejected: liquidity too thin x37, no h1 volume x26, too old x3
  top: UPTOBER 0.68 | LeoGuigna 0.67 | SATOSHINU 0.65 | niketyson 0.62 | based 0.58
  no entries this tick
  shadow: tracking 66, closed 0 this tick (0 would have won)
```
