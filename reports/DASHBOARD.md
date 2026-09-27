# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-27T17:05:11+00:00`

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
| Ticks run | 673 |

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

## Learned weights (v6)

_refit on 301 observations (253 shadow, 48 real), 108 winners (36% base rate)_

| Feature | Weight |
|---|---|
| buy_pressure | +0.133 |
| dip_in_uptrend | +0.104 |
| not_vertical | -0.059 |
| fdv_sanity | +0.057 |
| momentum_accel | +0.056 |
| txn_depth | +0.022 |
| turnover | +0.021 |
| buzz | +0.018 |
| age_sweet | +0.018 |
| paid_boost | -0.011 |
| socials | +0.009 |
| liq_quality | -0.002 |

## Last run log
```
tick #673  equity $415.23  cash $415.23  open 0
  scanning chains + news...
  94 raw candidates across 7 chains, 156 headlines/posts
  7 passed gates | rejected: liquidity too thin x60, no h1 volume x19, too old x6, sell pressure x1, already discovered x1
  top: BABYCALI 0.93 | NEARWHAL 0.92 | MIGR 0.72 | WORLD 0.63 | Q4 0.50
  no entries this tick
  shadow: tracking 100, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
  entries blocked: weekly loss -17.0% <= -15%
```
