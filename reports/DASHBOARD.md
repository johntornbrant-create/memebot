# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T04:26:41+00:00`

## Equity

| | |
|---|---|
| Equity | **$565.25** |
| Return | **+13.05%** (start $500.00) |
| Cash | $377.26 |
| Deployed | $187.99 (33.3%) |
| Open positions | 4 / 8 |
| Closed trades | 39 (12W / 27L, WR 31%) |
| Profit factor | 0.57 |
| Fees + slippage paid | $26.04 |
| Ticks run | 239 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $113.15 | +1007% | +1041% | 25.0h |
| ARENA | solana | $17.10 | $17.66 | +4% | +5% | 4.3h |
| MDP | bsc | $11.41 | $11.52 | +2% | +32% | 2.0h |
| IMU | solana | $11.40 | $45.66 | +304% | +304% | 0.8h |

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
tick #239  equity $540.24  cash $377.26  open 4
  scanning chains + news...
  113 raw candidates across 4 chains, 154 headlines/posts
  10 passed gates | rejected: liquidity too thin x59, no h1 volume x20, too old x15, already discovered x9
  top: BRAIN 0.74 | IMU 0.64 | familiars 0.60 | Shurikane 0.59 | NPC 0.58
  no entries this tick
  shadow: tracking 28, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED NPC        peak +1110%  (scored 0.49)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
```
