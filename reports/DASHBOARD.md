# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T07:06:13+00:00`

## Equity

| | |
|---|---|
| Equity | **$514.41** |
| Return | **+2.88%** (start $500.00) |
| Cash | $438.01 |
| Deployed | $76.40 (14.9%) |
| Open positions | 5 / 8 |
| Closed trades | 15 (6W / 9L, WR 40%) |
| Profit factor | 1.13 |
| Fees + slippage paid | $18.55 |
| Ticks run | 61 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| UPTOBER | solana | $15.04 | $15.48 | +6% | +71% | 7.3h |
| 蝴蝶家园 | bsc | $14.96 | $14.44 | -0% | +10% | 3.5h |
| 币安的守护者 | bsc | $7.76 | $5.52 | -25% | +0% | 1.0h |
| MSTOCK | bsc | $15.52 | $25.85 | +72% | +72% | 1.0h |
| LeoGuigna | solana | $15.38 | $15.11 | +1% | +1% | 0.3h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| based | $-6.45 | -42% | 1.2h | stop loss -37% |
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
tick #61  equity $512.65  cash $428.92  open 6
  SELL based      100% @ $0.0001839  ->  $9.10   [stop loss -37%]
  scanning chains + news...
  143 raw candidates across 6 chains, 157 headlines/posts
  3 passed gates | rejected: liquidity too thin x65, no h1 volume x45, too old x16, already discovered x9, unknown age x2
  top: based 0.67 | LeoGuigna 0.67 | UPTOBER 0.60
  no entries this tick
  shadow: tracking 73, closed 0 this tick (0 would have won)
```
