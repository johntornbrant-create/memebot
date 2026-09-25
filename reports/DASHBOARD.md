# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T07:26:27+00:00`

## Equity

| | |
|---|---|
| Equity | **$564.23** |
| Return | **+12.85%** (start $500.00) |
| Cash | $382.19 |
| Deployed | $182.04 (32.3%) |
| Open positions | 5 / 8 |
| Closed trades | 41 (13W / 28L, WR 32%) |
| Profit factor | 0.68 |
| Fees + slippage paid | $26.80 |
| Ticks run | 250 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $126.63 | +1139% | +1139% | 28.0h |
| ARENA | solana | $17.10 | $20.79 | +23% | +23% | 7.3h |
| MDP | bsc | $11.41 | $11.61 | +3% | +35% | 5.0h |
| 币安月饼 | bsc | $11.73 | $11.17 | -4% | +8% | 0.6h |
| BRAIN | solana | $11.85 | $11.74 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| Shurikane | $-6.92 | -41% | 1.8h | stop loss -40% |
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
tick #250  equity $558.86  cash $384.12  open 5
  SELL Shurikane  100% @ $0.0002855  ->  $9.92   [stop loss -40%]
  scanning chains + news...
  82 raw candidates across 7 chains, 154 headlines/posts
  6 passed gates | rejected: liquidity too thin x43, no h1 volume x31, too old x2
  top: Shurikane 0.73 | 拉布布 0.73 | IMU 0.70 | BRAIN 0.63 | UPTOBER 0.55
  BUY[explore] BRAIN      $11.85 @ $0.0004787  score 0.63  solana  liq $69,561
  no entry: daily trade cap reached
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED NPC        peak +1110%  (scored 0.49)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
```
