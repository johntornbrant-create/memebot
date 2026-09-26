# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-26T00:30:51+00:00`

## Equity

| | |
|---|---|
| Equity | **$424.20** |
| Return | **-15.16%** (start $500.00) |
| Cash | $409.90 |
| Deployed | $14.30 (3.4%) |
| Open positions | 2 / 8 |
| Closed trades | 46 (14W / 32L, WR 30%) |
| Profit factor | 0.63 |
| Fees + slippage paid | $30.45 |
| Ticks run | 354 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| CHIPS | ethereum | $8.54 | $5.00 | -9% | +0% | 0.4h |
| SJP | solana | $8.54 | $9.31 | +10% | +10% | 0.4h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| ARENA | $+6.10 | +36% | 23.6h | ratchet +56% (peak +123%) |
| BRAIN | $-5.41 | -46% | 9.2h | stop loss -45% |
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

## Learned weights (v4)

_refit on 142 observations (96 shadow, 46 real), 52 winners (37% base rate)_

| Feature | Weight |
|---|---|
| buy_pressure | +0.134 |
| dip_in_uptrend | +0.100 |
| turnover | +0.072 |
| momentum_accel | +0.070 |
| fdv_sanity | +0.062 |
| not_vertical | -0.029 |
| buzz | +0.015 |
| txn_depth | +0.014 |
| socials | +0.013 |
| paid_boost | +0.011 |
| age_sweet | -0.004 |
| liq_quality | +0.002 |

## Last run log
```
tick #354  equity $423.66  cash $409.90  open 2
  scanning chains + news...
  108 raw candidates across 6 chains, 154 headlines/posts
  9 passed gates | rejected: liquidity too thin x60, no h1 volume x22, too old x10, already discovered x5, sell pressure x1
  top: SJP 0.70 | E/ACC 0.63 | MINT 0.53 | GME 0.42 | ARENA 0.37
  no entries this tick
  shadow: tracking 94, closed 4 this tick (2 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED NPC        peak +1110%  (scored 0.49)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
  entries blocked: weekly loss -15.2% <= -15%
```
