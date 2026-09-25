# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T05:05:05+00:00`

## Equity

| | |
|---|---|
| Equity | **$598.84** |
| Return | **+19.77%** (start $500.00) |
| Cash | $377.26 |
| Deployed | $221.58 (37.0%) |
| Open positions | 4 / 8 |
| Closed trades | 39 (12W / 27L, WR 31%) |
| Profit factor | 0.57 |
| Fees + slippage paid | $26.04 |
| Ticks run | 242 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $112.84 | +1004% | +1041% | 25.7h |
| ARENA | solana | $17.10 | $17.89 | +6% | +6% | 5.0h |
| MDP | bsc | $11.41 | $11.55 | +2% | +32% | 2.7h |
| IMU | solana | $11.40 | $79.30 | +602% | +602% | 1.4h |

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
tick #242  equity $592.88  cash $377.26  open 4
  scanning chains + news...
  114 raw candidates across 7 chains, 154 headlines/posts
  6 passed gates | rejected: liquidity too thin x85, no h1 volume x19, too old x2, already discovered x2
  top: Shurikane 0.67 | BRAIN 0.66 | BONGO 0.66 | IMU 0.57 | SNDK 0.54
  no entries this tick
  shadow: tracking 31, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED NPC        peak +1110%  (scored 0.49)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
```
