# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-27T22:33:37+00:00`

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
| Ticks run | 714 |

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

## Learned weights (v7)

_refit on 352 observations (304 shadow, 48 real), 132 winners (38% base rate)_

| Feature | Weight |
|---|---|
| buy_pressure | +0.120 |
| not_vertical | -0.091 |
| momentum_accel | +0.090 |
| dip_in_uptrend | +0.082 |
| fdv_sanity | +0.055 |
| turnover | +0.051 |
| txn_depth | +0.026 |
| socials | +0.026 |
| liq_quality | +0.018 |
| age_sweet | +0.012 |
| paid_boost | -0.009 |
| buzz | -0.000 |

## Last run log
```
tick #714  equity $415.23  cash $415.23  open 0
  scanning chains + news...
  107 raw candidates across 5 chains, 156 headlines/posts
  9 passed gates | rejected: liquidity too thin x60, no h1 volume x27, too old x8, already discovered x2, sell pressure x1
  top: wiffomo 0.81 | PKMN50 0.81 | VBUCKS 0.61 | MS70 0.55 | NEARPAD 0.51
  no entries this tick
  shadow: tracking 103, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
  entries blocked: weekly loss -17.0% <= -15%
```
