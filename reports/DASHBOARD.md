# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T05:24:19+00:00`

## Equity

| | |
|---|---|
| Equity | **$531.40** |
| Return | **+6.28%** (start $500.00) |
| Cash | $469.04 |
| Deployed | $62.36 (11.7%) |
| Open positions | 4 / 8 |
| Closed trades | 11 (4W / 7L, WR 36%) |
| Profit factor | 0.78 |
| Fees + slippage paid | $14.72 |
| Ticks run | 55 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $8.04 | +195% | +248% | 9.0h |
| UPTOBER | solana | $15.04 | $17.16 | +18% | +71% | 5.6h |
| 蝴蝶家园 | bsc | $14.96 | $15.36 | +6% | +10% | 1.8h |
| LeoGuigna | solana | $7.46 | $21.81 | +724% | +724% | 1.5h |

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
tick #55  equity $526.66  cash $469.04  open 4
  scanning chains + news...
  135 raw candidates across 7 chains, 158 headlines/posts
  9 passed gates | rejected: liquidity too thin x58, no h1 volume x45, too old x14, already discovered x7, unknown age x2
  top: niketyson 0.77 | MSTOCK 0.72 | based 0.72 | 币安的守护者 0.70 | SATOSHINU 0.68
  no entries this tick
  shadow: tracking 72, closed 0 this tick (0 would have won)
```
