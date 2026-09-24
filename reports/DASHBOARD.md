# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-24T03:05:15+00:00`

## Equity

| | |
|---|---|
| Equity | **$498.13** |
| Return | **-0.37%** (start $500.00) |
| Cash | $423.92 |
| Deployed | $74.22 (14.9%) |
| Open positions | 5 / 8 |
| Closed trades | 26 (10W / 16L, WR 38%) |
| Profit factor | 0.90 |
| Fees + slippage paid | $23.43 |
| Ticks run | 141 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| 蝴蝶家园 | bsc | $14.96 | $20.97 | +45% | +45% | 23.4h |
| UPTOBER | solana | $10.19 | $9.86 | -2% | +3% | 2.6h |
| PURRP | solana | $10.28 | $18.06 | +77% | +101% | 1.7h |
| 币安协议 | bsc | $15.04 | $12.98 | -13% | +0% | 0.7h |
| 币安女王 | bsc | $15.09 | $12.36 | -17% | +0% | 0.4h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| LeoGuigna | $+19.66 | +263% | 2.0h | trailing stop from +724% |
| BITCOINU | $+7.57 | +99% | 9.2h | trailing stop from +248% |

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
tick #141  equity $501.75  cash $423.92  open 5
  scanning chains + news...
  170 raw candidates across 6 chains, 160 headlines/posts
  6 passed gates | rejected: liquidity too thin x89, no h1 volume x45, too old x16, already discovered x11, unknown age x1
  top: 币安协议 0.73 | PURRP 0.72 | JEANCOIN 0.59 | BLUF 0.58 | UPTOBER 0.56
  no entries this tick
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED JEANPHIL   peak +284%  (scored 0.63)
```
