# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T02:05:46+00:00`

## Equity

| | |
|---|---|
| Equity | **$507.01** |
| Return | **+1.40%** (start $500.00) |
| Cash | $466.39 |
| Deployed | $40.62 (8.0%) |
| Open positions | 3 / 8 |
| Closed trades | 10 (3W / 7L, WR 30%) |
| Profit factor | 0.73 |
| Fees + slippage paid | $11.91 |
| Ticks run | 42 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $8.44 | +16% | +37% | 5.7h |
| UPTOBER | solana | $15.04 | $24.17 | +66% | +71% | 2.3h |
| based | solana | $7.48 | $8.02 | +127% | +127% | 0.3h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
tick #42  equity $498.57  cash $458.78  open 3
  SELL based      50% @ $0.0004064  ->  $7.61   [take profit +80% (sold 50%)]
  scanning chains + news...
  154 raw candidates across 8 chains, 160 headlines/posts
  4 passed gates | rejected: liquidity too thin x84, no h1 volume x49, too old x9, already discovered x7, unknown age x1
  top: SATOSHINU 0.75 | CATEWALK 0.73 | UPTOBER 0.71 | based 0.52
  no entries this tick
  shadow: tracking 54, closed 0 this tick (0 would have won)
```
