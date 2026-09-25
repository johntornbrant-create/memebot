# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T02:37:48+00:00`

## Equity

| | |
|---|---|
| Equity | **$538.63** |
| Return | **+7.73%** (start $500.00) |
| Cash | $367.34 |
| Deployed | $171.28 (31.8%) |
| Open positions | 6 / 8 |
| Closed trades | 35 (11W / 24L, WR 31%) |
| Profit factor | 0.63 |
| Fees + slippage paid | $25.44 |
| Ticks run | 232 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $108.70 | +963% | +1041% | 23.2h |
| CATALYST | base | $10.26 | $9.28 | -9% | +10% | 23.0h |
| ARENA | solana | $17.10 | $16.51 | -3% | +0% | 2.5h |
| COD | bsc | $16.42 | $12.81 | -21% | +1% | 1.0h |
| MDP | bsc | $11.41 | $12.67 | +12% | +12% | 0.2h |
| 币安女英雄 | bsc | $11.31 | $11.18 | +0% | +0% | 0.0h |

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
tick #232  equity $543.21  cash $378.65  open 5
  scanning chains + news...
  94 raw candidates across 4 chains, 154 headlines/posts
  9 passed gates | rejected: liquidity too thin x55, no h1 volume x14, too old x12, already discovered x4
  top: ARENA 0.74 | BRAIN 0.73 | MDP 0.70 | 币安女英雄 0.69 | COD 0.68
  BUY[explore] 币安女英雄      $11.31 @ $0.0001967  score 0.69  bsc  liq $25,555
  shadow: tracking 22, closed 2 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED GETF       peak +606%  (scored 0.66)
```
