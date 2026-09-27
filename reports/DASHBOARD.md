# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-27T23:36:40+00:00`

## Equity

| | |
|---|---|
| Equity | **$419.75** |
| Return | **-16.05%** (start $500.00) |
| Cash | $386.69 |
| Deployed | $33.06 (7.9%) |
| Open positions | 4 / 8 |
| Closed trades | 49 (14W / 35L, WR 29%) |
| Profit factor | 0.59 |
| Fees + slippage paid | $36.95 |
| Ticks run | 724 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| CATSTR | solana | $8.30 | $11.76 | +91% | +91% | 0.8h |
| CAKE | solana | $5.74 | $7.42 | +31% | +45% | 0.8h |
| Q4 | solana | $5.76 | $5.48 | -4% | +1% | 0.5h |
| 1 | ethereum | $8.39 | $5.33 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| wiffomo | $-3.84 | -46% | 0.0h | stop loss -45% |
| SJP | $-3.21 | -38% | 1.4h | stop loss -36% |
| CHIPS | $-8.54 | -100% | 0.9h | stop loss -100% |
| ARENA | $+6.10 | +36% | 23.6h | ratchet +56% (peak +123%) |
| BRAIN | $-5.41 | -46% | 9.2h | stop loss -45% |
| MDP | $-4.70 | -41% | 10.7h | stop loss -40% |
| JEANCOIN | $-8.71 | -84% | 30.2h | ratchet +767% (peak +1139%) |
| 币安月饼 | $-4.90 | -42% | 2.6h | stop loss -40% |
| Shurikane | $-6.92 | -41% | 1.8h | stop loss -40% |
| IMU | $+24.04 | +211% | 2.0h | ratchet +391% (peak +602%) |
| COD | $+1.52 | +9% | 2.2h | ratchet +25% (peak +71%) |
| CATALYST | $-1.08 | -10% | 24.2h | time stop 24h, only -9% |
| OG | $-11.64 | -99% | 0.2h | stop loss -98% |
| 币安女英雄 | $-5.48 | -48% | 1.0h | ratchet +83% (peak +161%) |
| BRAIN | $-0.64 | -6% | 1.0h | ratchet +0% (peak +57%) |

## Learned weights (v9)

_refit on 352 observations (304 shadow, 48 real), 132 winners (38% base rate)_

| Feature | Weight |
|---|---|
| buy_pressure | +0.120 |
| not_vertical | -0.091 |
| momentum_accel | +0.090 |
| dip_in_uptrend | +0.082 |
| fdv_sanity | +0.055 |
| turnover | +0.051 |
| txn_depth | +0.026 |
| socials | +0.026 |
| liq_quality | +0.018 |
| age_sweet | +0.012 |
| paid_boost | -0.009 |
| buzz | -0.000 |

## Last run log
```
tick #724  equity $419.65  cash $395.08  open 3
  scanning chains + news...
  87 raw candidates across 8 chains, 156 headlines/posts
  8 passed gates | rejected: liquidity too thin x44, no h1 volume x34, too new (bot war) x1
  top: 1 0.90 | CATSTR 0.83 | INSTA 0.76 | Q4 0.73 | 20xx 0.31
  tick bar 0.79 (top 30% of 8, floor 0.45)
  BUY[exploit] 1          $8.39 @ $4.874e-05  score 0.90  ethereum  liq $25,151
  shadow: tracking 105, closed 2 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
```
