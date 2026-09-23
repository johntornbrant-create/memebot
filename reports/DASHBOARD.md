# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T04:05:40+00:00`

## Equity

| | |
|---|---|
| Equity | **$499.95** |
| Return | **-0.01%** (start $500.00) |
| Cash | $452.26 |
| Deployed | $47.69 (9.5%) |
| Open positions | 4 / 8 |
| Closed trades | 11 (4W / 7L, WR 36%) |
| Profit factor | 0.78 |
| Fees + slippage paid | $13.54 |
| Ticks run | 50 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $8.37 | +130% | +163% | 7.7h |
| UPTOBER | solana | $15.04 | $16.23 | +11% | +71% | 4.3h |
| 蝴蝶家园 | bsc | $14.96 | $15.84 | +9% | +9% | 0.4h |
| LeoGuigna | solana | $7.46 | $7.24 | +3% | +3% | 0.2h |

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
tick #50  equity $497.46  cash $452.26  open 4
  scanning chains + news...
  81 raw candidates across 5 chains, 158 headlines/posts
  8 passed gates | rejected: liquidity too thin x38, no h1 volume x19, too old x7, already discovered x6, too new (bot war) x2
  top: 蝴蝶家园 0.64 | UPTOBER 0.60 | SATOSHINU 0.53 | LeoGuigna 0.52 | based 0.51
  no entries this tick
  shadow: tracking 65, closed 0 this tick (0 would have won)
```
