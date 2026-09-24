# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-24T09:25:04+00:00`

## Equity

| | |
|---|---|
| Equity | **$530.50** |
| Return | **+6.10%** (start $500.00) |
| Cash | $433.18 |
| Deployed | $97.32 (18.3%) |
| Open positions | 4 / 8 |
| Closed trades | 30 (11W / 19L, WR 37%) |
| Profit factor | 0.85 |
| Fees + slippage paid | $24.12 |
| Ticks run | 165 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| 蝴蝶家园 | bsc | $14.96 | $21.00 | +45% | +57% | 29.8h |
| 币安协议 | bsc | $15.04 | $13.58 | -9% | +36% | 7.0h |
| JEANCOIN | solana | $10.32 | $52.02 | +409% | +409% | 6.0h |
| CATALYST | base | $10.26 | $10.71 | +5% | +5% | 5.8h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| PURRP | $-4.46 | -43% | 2.2h | stop loss -42% |
| 币安女王 | $-0.58 | -4% | 3.0h | ratchet +0% (peak +67%) |
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
tick #165  equity $528.08  cash $433.18  open 4
  entries blocked: daily trade cap reached
```
