# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-27T23:23:40+00:00`

## Equity

| | |
|---|---|
| Equity | **$418.36** |
| Return | **-16.33%** (start $500.00) |
| Cash | $394.84 |
| Deployed | $23.52 (5.6%) |
| Open positions | 3 / 8 |
| Closed trades | 49 (14W / 35L, WR 29%) |
| Profit factor | 0.59 |
| Fees + slippage paid | $33.88 |
| Ticks run | 723 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| CATSTR | solana | $8.30 | $9.89 | +60% | +60% | 0.6h |
| CAKE | solana | $5.74 | $7.80 | +37% | +43% | 0.5h |
| Q4 | solana | $5.76 | $5.83 | +2% | +2% | 0.3h |

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
tick #723  equity $413.74  cash $391.59  open 3
  SELL CATSTR     25% @ $0.0003093  ->  $3.25   [take profit +50% (sold 25%)]
  scanning chains + news...
  68 raw candidates across 6 chains, 156 headlines/posts
  7 passed gates | rejected: liquidity too thin x35, no h1 volume x23, too old x2, too new (bot war) x1
  top: CATSTR 0.86 | X VAULT 0.86 | Q4 0.62 | 20xx 0.49 | ZC 0.40
  tick bar 0.79 (top 30% of 7, floor 0.45)
  no entries this tick
  shadow: tracking 103, closed 1 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
```
