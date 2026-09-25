# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T03:50:30+00:00`

## Equity

| | |
|---|---|
| Equity | **$529.38** |
| Return | **+5.88%** (start $500.00) |
| Cash | $377.26 |
| Deployed | $152.13 (28.7%) |
| Open positions | 4 / 8 |
| Closed trades | 39 (12W / 27L, WR 31%) |
| Profit factor | 0.57 |
| Fees + slippage paid | $26.04 |
| Ticks run | 237 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $111.14 | +987% | +1041% | 24.4h |
| ARENA | solana | $17.10 | $17.70 | +4% | +5% | 3.7h |
| MDP | bsc | $11.41 | $12.38 | +10% | +32% | 1.4h |
| IMU | solana | $11.40 | $10.91 | -3% | +0% | 0.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| COD | $+1.52 | +9% | 2.2h | ratchet +25% (peak +71%) |
| CATALYST | $-1.08 | -10% | 24.2h | time stop 24h, only -9% |
| OG | $-11.64 | -99% | 0.2h | stop loss -98% |
| 币安女英雄 | $-5.48 | -48% | 1.0h | ratchet +83% (peak +161%) |
| BRAIN | $-0.64 | -6% | 1.0h | ratchet +0% (peak +57%) |
| TUGGIN | $-16.60 | -99% | 0.3h | stop loss -98% |
| S&P500 | $-8.02 | -67% | 0.9h | stop loss -66% |
| 蝴蝶家园 | $-8.54 | -57% | 34.2h | ratchet +0% (peak +57%) |
| 币安协议 | $-5.79 | -38% | 11.0h | stop loss -37% |
| PURRP | $-4.46 | -43% | 2.2h | stop loss -42% |
| 币安女王 | $-0.58 | -4% | 3.0h | ratchet +0% (peak +67%) |
| PURRP | $+3.56 | +35% | 2.2h | ratchet +41% (peak +101%) |
| UPTOBER | $-4.23 | -42% | 2.9h | stop loss -40% |
| CZBUILDER | $-4.25 | -40% | 0.8h | ratchet +25% (peak +98%) |
| BLUF | $-4.62 | -44% | 1.5h | stop loss -42% |

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
tick #237  equity $542.86  cash $350.13  open 6
  SELL CATALYST   100% @ $1.69  ->  $9.19   [time stop 24h, only -9%]
  SELL COD        100% @ $0.001565  ->  $17.94   [ratchet +25% (peak +71%)]
  entries blocked: daily loss -6.4% <= -6%
```
