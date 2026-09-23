# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T04:39:06+00:00`

## Equity

| | |
|---|---|
| Equity | **$521.76** |
| Return | **+4.35%** (start $500.00) |
| Cash | $469.04 |
| Deployed | $52.72 (10.1%) |
| Open positions | 4 / 8 |
| Closed trades | 11 (4W / 7L, WR 36%) |
| Profit factor | 0.78 |
| Fees + slippage paid | $14.72 |
| Ticks run | 52 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $8.57 | +214% | +248% | 8.3h |
| UPTOBER | solana | $15.04 | $18.85 | +29% | +71% | 4.8h |
| 蝴蝶家园 | bsc | $14.96 | $14.60 | +1% | +9% | 1.0h |
| LeoGuigna | solana | $7.46 | $10.71 | +304% | +304% | 0.8h |

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
tick #52  equity $518.94  cash $465.84  open 4
  SELL LeoGuigna  25% @ $0.0004619  ->  $3.19   [take profit +200% (sold 25%)]
  scanning chains + news...
  102 raw candidates across 7 chains, 160 headlines/posts
  7 passed gates | rejected: liquidity too thin x41, no h1 volume x38, too old x9, already discovered x6, unknown age x1
  top: based 0.72 | UPTOBER 0.72 | SATOSHINU 0.70 | LeoGuigna 0.64 | niketyson 0.60
  no entries this tick
  shadow: tracking 66, closed 0 this tick (0 would have won)
```
