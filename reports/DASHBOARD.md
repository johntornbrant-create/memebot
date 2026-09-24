# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-24T04:50:24+00:00`

## Equity

| | |
|---|---|
| Equity | **$502.72** |
| Return | **+0.54%** (start $500.00) |
| Cash | $412.86 |
| Deployed | $89.86 (17.9%) |
| Open positions | 6 / 8 |
| Closed trades | 28 (11W / 17L, WR 39%) |
| Profit factor | 0.89 |
| Fees + slippage paid | $23.91 |
| Ticks run | 148 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| 蝴蝶家园 | bsc | $14.96 | $20.14 | +39% | +45% | 25.2h |
| 币安协议 | bsc | $15.04 | $12.96 | -13% | +0% | 2.4h |
| 币安女王 | bsc | $15.09 | $21.39 | +43% | +67% | 2.2h |
| JEANCOIN | solana | $10.32 | $15.07 | +47% | +53% | 1.4h |
| CATALYST | base | $10.26 | $8.68 | -15% | +0% | 1.2h |
| PURRP | solana | $10.26 | $11.63 | +14% | +18% | 1.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| PURRP | $+3.56 | +35% | 2.2h | ratchet +41% (peak +101%) |
| UPTOBER | $-4.23 | -42% | 2.9h | stop loss -40% |
| CZBUILDER | $-4.25 | -40% | 0.8h | ratchet +25% (peak +98%) |
| BLUF | $-4.62 | -44% | 1.5h | stop loss -42% |
| 币安女王 | $+12.82 | +121% | 1.0h | ratchet +148% (peak +254%) |
| familiars | $+14.14 | +141% | 1.3h | ratchet +208% (peak +341%) |
| GAYMF | $-5.60 | -56% | 0.8h | stop loss -55% |
| UPTOBER | $+2.38 | +16% | 13.4h | ratchet +25% (peak +71%) |
| GROKBOTIFY | $-7.28 | -100% | 0.3h | stop loss -98% |
| MSTOCK | $+2.04 | +13% | 2.3h | stop loss -74% |
| MOUSE | $-7.41 | -100% | 0.2h | stop loss -96% |
| LeoGuigna | $-15.38 | -100% | 0.8h | stop loss -99% |
| 币安的守护者 | $-4.02 | -52% | 1.5h | stop loss -44% |
| based | $-6.45 | -42% | 1.2h | stop loss -37% |
| DURIAN | $-5.02 | -64% | 0.5h | stop loss -57% |

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
tick #148  equity $504.00  cash $412.86  open 6
  entries blocked: daily trade cap reached
```
