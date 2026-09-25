# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T03:24:06+00:00`

## Equity

| | |
|---|---|
| Equity | **$561.94** |
| Return | **+12.39%** (start $500.00) |
| Cash | $355.54 |
| Deployed | $206.40 (36.7%) |
| Open positions | 7 / 8 |
| Closed trades | 35 (11W / 24L, WR 31%) |
| Profit factor | 0.63 |
| Fees + slippage paid | $25.55 |
| Ticks run | 235 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $107.86 | +955% | +1041% | 24.0h |
| CATALYST | base | $10.26 | $9.28 | -9% | +10% | 23.8h |
| ARENA | solana | $17.10 | $17.82 | +5% | +5% | 3.3h |
| COD | bsc | $16.42 | $21.88 | +35% | +35% | 1.8h |
| MDP | bsc | $11.41 | $11.87 | +5% | +32% | 1.0h |
| 币安女英雄 | bsc | $11.31 | $25.88 | +132% | +161% | 0.8h |
| OG | solana | $11.80 | $11.69 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| 币安女王 | $+12.82 | +121% | 1.0h | ratchet +148% (peak +254%) |
| familiars | $+14.14 | +141% | 1.3h | ratchet +208% (peak +341%) |
| GAYMF | $-5.60 | -56% | 0.8h | stop loss -55% |
| UPTOBER | $+2.38 | +16% | 13.4h | ratchet +25% (peak +71%) |

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
tick #235  equity $552.51  cash $367.34  open 6
  scanning chains + news...
  102 raw candidates across 6 chains, 154 headlines/posts
  7 passed gates | rejected: liquidity too thin x69, no h1 volume x21, too old x2, unknown age x2, already discovered x1
  top: ARENA 0.72 | 币安女英雄 0.69 | BRAIN 0.64 | Shurikane 0.60 | MDP 0.58
  BUY[explore] OG         $11.80 @ $0.0001501  score 0.55  solana  liq $34,978
  shadow: tracking 22, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED GETF       peak +606%  (scored 0.66)
```
