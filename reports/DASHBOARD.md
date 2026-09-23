# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T05:37:20+00:00`

## Equity

| | |
|---|---|
| Equity | **$522.34** |
| Return | **+4.47%** (start $500.00) |
| Cash | $467.18 |
| Deployed | $55.16 (10.6%) |
| Open positions | 4 / 8 |
| Closed trades | 12 (5W / 7L, WR 42%) |
| Profit factor | 0.96 |
| Fees + slippage paid | $15.52 |
| Ticks run | 56 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| UPTOBER | solana | $15.04 | $16.75 | +15% | +71% | 5.8h |
| 蝴蝶家园 | bsc | $14.96 | $15.27 | +5% | +10% | 2.0h |
| LeoGuigna | solana | $7.46 | $15.31 | +478% | +724% | 1.8h |
| DURIAN | solana | $7.84 | $7.43 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
tick #56  equity $531.40  cash $469.04  open 4
  SELL BITCOINU   100% @ $0.0003282  ->  $5.97   [trailing stop from +248%]
  scanning chains + news...
  146 raw candidates across 7 chains, 158 headlines/posts
  8 passed gates | rejected: liquidity too thin x67, no h1 volume x56, too old x12, already discovered x3
  top: MSTOCK 0.76 | 币安的守护者 0.75 | niketyson 0.74 | based 0.71 | LeoGuigna 0.70
  BUY[explore] DURIAN     $7.84 @ $0.0003162  score 0.49  solana  liq $50,779
  shadow: tracking 72, closed 0 this tick (0 would have won)
```
