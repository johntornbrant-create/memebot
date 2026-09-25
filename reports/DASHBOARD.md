# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T15:06:08+00:00`

## Equity

| | |
|---|---|
| Equity | **$425.19** |
| Return | **-14.96%** (start $500.00) |
| Cash | $397.34 |
| Deployed | $27.85 (6.6%) |
| Open positions | 2 / 8 |
| Closed trades | 44 (13W / 31L, WR 30%) |
| Profit factor | 0.62 |
| Fees + slippage paid | $27.03 |
| Ticks run | 287 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| ARENA | solana | $17.10 | $18.16 | +7% | +28% | 15.0h |
| BRAIN | solana | $11.85 | $9.69 | -17% | +30% | 7.7h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| TUGGIN | $-16.60 | -99% | 0.3h | stop loss -98% |
| S&P500 | $-8.02 | -67% | 0.9h | stop loss -66% |
| 蝴蝶家园 | $-8.54 | -57% | 34.2h | ratchet +0% (peak +57%) |
| 币安协议 | $-5.79 | -38% | 11.0h | stop loss -37% |
| PURRP | $-4.46 | -43% | 2.2h | stop loss -42% |

## Learned weights (v2)

_refit on 140 observations (96 shadow, 44 real), 51 winners (36% base rate)_

| Feature | Weight |
|---|---|
| buy_pressure | +0.129 |
| dip_in_uptrend | +0.092 |
| momentum_accel | +0.083 |
| fdv_sanity | +0.056 |
| turnover | +0.054 |
| not_vertical | -0.040 |
| buzz | +0.019 |
| age_sweet | +0.014 |
| paid_boost | +0.005 |
| socials | -0.001 |
| liq_quality | +0.001 |
| txn_depth | +0.000 |

## Last run log
```
tick #287  equity $424.66  cash $397.34  open 2
  scanning chains + news...
  99 raw candidates across 8 chains, 154 headlines/posts
  5 passed gates | rejected: liquidity too thin x56, no h1 volume x29, too old x7, sell pressure x1, too new (bot war) x1
  top: BONGO 0.88 | LFG 0.81 | Poocoin 0.63 | SWARM 0.59 | UPTOBER 0.38
  no entries this tick
  shadow: tracking 47, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED NPC        peak +1110%  (scored 0.49)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
  entries blocked: daily loss -24.9% <= -6%; daily trade cap reached
```
