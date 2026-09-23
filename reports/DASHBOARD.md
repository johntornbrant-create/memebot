# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T06:30:43+00:00`

## Equity

| | |
|---|---|
| Equity | **$516.39** |
| Return | **+3.28%** (start $500.00) |
| Cash | $444.30 |
| Deployed | $72.10 (14.0%) |
| Open positions | 5 / 8 |
| Closed trades | 14 (6W / 8L, WR 43%) |
| Profit factor | 1.29 |
| Fees + slippage paid | $17.67 |
| Ticks run | 59 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| UPTOBER | solana | $15.04 | $16.16 | +11% | +71% | 6.7h |
| 蝴蝶家园 | bsc | $14.96 | $14.14 | -2% | +10% | 2.9h |
| based | solana | $15.55 | $15.67 | +4% | +25% | 0.7h |
| 币安的守护者 | bsc | $7.76 | $5.83 | -21% | +0% | 0.4h |
| MSTOCK | bsc | $15.52 | $20.30 | +35% | +35% | 0.4h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| DURIAN | $-5.02 | -64% | 0.5h | stop loss -57% |
| LeoGuigna | $+19.66 | +263% | 2.0h | trailing stop from +724% |
| BITCOINU | $+7.57 | +99% | 9.2h | trailing stop from +248% |
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
tick #59  equity $517.38  cash $444.30  open 5
  scanning chains + news...
  136 raw candidates across 6 chains, 158 headlines/posts
  7 passed gates | rejected: liquidity too thin x79, no h1 volume x31, too old x11, already discovered x6, unknown age x1
  top: based 0.77 | MSTOCK 0.71 | LeoGuigna 0.69 | 币安的守护者 0.66 | MAU 0.60
  no entries this tick
  shadow: tracking 73, closed 0 this tick (0 would have won)
```
