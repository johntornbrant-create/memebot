# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T06:46:48+00:00`

## Equity

| | |
|---|---|
| Equity | **$512.65** |
| Return | **+2.53%** (start $500.00) |
| Cash | $428.92 |
| Deployed | $83.73 (16.3%) |
| Open positions | 6 / 8 |
| Closed trades | 14 (6W / 8L, WR 43%) |
| Profit factor | 1.29 |
| Fees + slippage paid | $18.13 |
| Ticks run | 60 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| UPTOBER | solana | $15.04 | $15.31 | +5% | +71% | 7.0h |
| 蝴蝶家园 | bsc | $14.96 | $14.16 | -2% | +10% | 3.1h |
| based | solana | $15.55 | $11.42 | -24% | +25% | 0.9h |
| 币安的守护者 | bsc | $7.76 | $7.26 | -1% | +0% | 0.7h |
| MSTOCK | bsc | $15.52 | $20.20 | +34% | +35% | 0.7h |
| LeoGuigna | solana | $15.38 | $14.92 | +0% | +0% | 0.0h |

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
tick #60  equity $516.39  cash $444.30  open 5
  scanning chains + news...
  121 raw candidates across 7 chains, 157 headlines/posts
  5 passed gates | rejected: liquidity too thin x72, no h1 volume x38, too old x4, sell pressure x1, already discovered x1
  top: MSTOCK 0.74 | LeoGuigna 0.68 | based 0.67 | 币安的守护者 0.67 | UPTOBER 0.59
  BUY[exploit] LeoGuigna  $15.38 @ $0.0004355  score 0.68  solana  liq $62,451
  shadow: tracking 73, closed 0 this tick (0 would have won)
```
