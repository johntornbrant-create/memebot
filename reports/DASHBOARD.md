# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-26T15:24:22+00:00`

## Equity

| | |
|---|---|
| Equity | **$415.23** |
| Return | **-16.95%** (start $500.00) |
| Cash | $415.23 |
| Deployed | $0.00 (0.0%) |
| Open positions | 0 / 8 |
| Closed trades | 48 (14W / 34L, WR 29%) |
| Profit factor | 0.60 |
| Fees + slippage paid | $33.51 |
| Ticks run | 472 |

## Open positions

_flat_

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| SJP | $-3.21 | -38% | 1.4h | stop loss -36% |
| CHIPS | $-8.54 | -100% | 0.9h | stop loss -100% |
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
tick #472  equity $415.23  cash $415.23  open 0
  scanning chains + news...
  135 raw candidates across 8 chains, 160 headlines/posts
  8 passed gates | rejected: liquidity too thin x75, no h1 volume x39, too old x5, already discovered x5, unknown age x2
  top: QUACC 0.89 | GSTOCK 0.83 | ARENA 0.81 | $TAPE 0.77 | 黄鞋 0.69
  no entries this tick
  shadow: tracking 128, closed 1 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED TTP        peak +1244%  (scored 0.58)
    MISSED NPC        peak +1110%  (scored 0.49)
  entries blocked: weekly loss -17.0% <= -15%
```
