# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T02:51:36+00:00`

## Equity

| | |
|---|---|
| Equity | **$547.60** |
| Return | **+9.52%** (start $500.00) |
| Cash | $367.34 |
| Deployed | $180.26 (32.9%) |
| Open positions | 6 / 8 |
| Closed trades | 35 (11W / 24L, WR 31%) |
| Profit factor | 0.63 |
| Fees + slippage paid | $25.44 |
| Ticks run | 233 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $109.29 | +969% | +1041% | 23.4h |
| CATALYST | base | $10.26 | $9.28 | -9% | +10% | 23.2h |
| ARENA | solana | $17.10 | $16.54 | -2% | +0% | 2.7h |
| COD | bsc | $16.42 | $12.39 | -24% | +1% | 1.3h |
| MDP | bsc | $11.41 | $14.91 | +32% | +32% | 0.5h |
| 币安女英雄 | bsc | $11.31 | $17.84 | +60% | +60% | 0.2h |

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
tick #233  equity $538.63  cash $367.34  open 6
  scanning chains + news...
  157 raw candidates across 7 chains, 160 headlines/posts
  9 passed gates | rejected: liquidity too thin x92, no h1 volume x34, too old x15, already discovered x6, too new (bot war) x1
  top: 币安女英雄 0.70 | ARENA 0.69 | MDP 0.68 | BRAIN 0.62 | OG 0.57
  no entries this tick
  shadow: tracking 23, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED GETF       peak +606%  (scored 0.66)
```
