# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T05:51:10+00:00`

## Equity

| | |
|---|---|
| Equity | **$518.24** |
| Return | **+3.65%** (start $500.00) |
| Cash | $464.76 |
| Deployed | $53.48 (10.3%) |
| Open positions | 4 / 8 |
| Closed trades | 13 (6W / 7L, WR 46%) |
| Profit factor | 1.45 |
| Fees + slippage paid | $16.43 |
| Ticks run | 57 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| UPTOBER | solana | $15.04 | $16.81 | +15% | +71% | 6.0h |
| 蝴蝶家园 | bsc | $14.96 | $15.33 | +6% | +10% | 2.2h |
| DURIAN | solana | $7.84 | $5.79 | -22% | +0% | 0.2h |
| based | solana | $15.55 | $15.09 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
tick #57  equity $522.34  cash $467.18  open 4
  SELL LeoGuigna  100% @ $0.0005861  ->  $13.14   [trailing stop from +724%]
  scanning chains + news...
  118 raw candidates across 8 chains, 158 headlines/posts
  7 passed gates | rejected: no h1 volume x52, liquidity too thin x44, too old x11, already discovered x3, too new (bot war) x1
  top: based 0.76 | MSTOCK 0.71 | 币安的守护者 0.68 | SATOSHINU 0.66 | DURIAN 0.65
  BUY[exploit] based      $15.55 @ $0.0002916  score 0.76  solana  liq $54,769
  shadow: tracking 72, closed 0 this tick (0 would have won)
```
