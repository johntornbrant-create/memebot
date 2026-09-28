# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-28T00:07:13+00:00`

## Equity

| | |
|---|---|
| Equity | **$415.21** |
| Return | **-16.96%** (start $500.00) |
| Cash | $395.24 |
| Deployed | $19.97 (4.8%) |
| Open positions | 3 / 8 |
| Closed trades | 50 (15W / 35L, WR 30%) |
| Profit factor | 0.59 |
| Fees + slippage paid | $34.07 |
| Ticks run | 728 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| CAKE | solana | $5.74 | $6.11 | +44% | +60% | 1.3h |
| Q4 | solana | $5.76 | $5.56 | -2% | +1% | 1.0h |
| poin | solana | $8.30 | $8.22 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| CATSTR | $+1.41 | +17% | 1.2h | ratchet +25% (peak +84%) |
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
tick #728  equity $415.66  cash $403.54  open 2
  scanning chains + news...
  139 raw candidates across 8 chains, 160 headlines/posts
  8 passed gates | rejected: liquidity too thin x81, no h1 volume x39, too old x7, already discovered x3, sell pressure x1
  top: poin 0.80 | INSTA 0.55 | CATSTR 0.45 | 20xx 0.26 | e/acc 0.25
  tick bar 0.55 (top 30% of 8, floor 0.45)
  BUY[exploit] poin       $8.30 @ $0.0001635  score 0.80  solana  liq $36,061
  shadow: tracking 100, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
```
