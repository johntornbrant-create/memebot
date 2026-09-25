# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T06:48:20+00:00`

## Equity

| | |
|---|---|
| Equity | **$558.80** |
| Return | **+11.76%** (start $500.00) |
| Cash | $384.12 |
| Deployed | $174.68 (31.3%) |
| Open positions | 5 / 8 |
| Closed trades | 40 (13W / 27L, WR 32%) |
| Profit factor | 0.71 |
| Fees + slippage paid | $26.60 |
| Ticks run | 248 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $118.11 | +1055% | +1055% | 27.4h |
| ARENA | solana | $17.10 | $18.08 | +7% | +7% | 6.7h |
| MDP | bsc | $11.41 | $12.22 | +8% | +35% | 4.4h |
| Shurikane | solana | $16.84 | $14.54 | -13% | +17% | 1.2h |
| 币安月饼 | bsc | $11.73 | $11.60 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| IMU | $+24.04 | +211% | 2.0h | ratchet +391% (peak +602%) |
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
tick #248  equity $560.37  cash $395.85  open 4
  scanning chains + news...
  81 raw candidates across 7 chains, 160 headlines/posts
  7 passed gates | rejected: liquidity too thin x44, no h1 volume x30
  top: IMU 0.76 | Shurikane 0.72 | 币安月饼 0.68 | 拉布布 0.64 | BRAIN 0.61
  BUY[explore] 币安月饼       $11.73 @ $0.0001018  score 0.68  bsc  liq $66,312
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED NPC        peak +1110%  (scored 0.49)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
```
