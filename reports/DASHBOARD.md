# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-26T01:23:08+00:00`

## Equity

| | |
|---|---|
| Equity | **$415.94** |
| Return | **-16.81%** (start $500.00) |
| Cash | $409.90 |
| Deployed | $6.04 (1.5%) |
| Open positions | 1 / 8 |
| Closed trades | 47 (14W / 33L, WR 30%) |
| Profit factor | 0.61 |
| Fees + slippage paid | $33.45 |
| Ticks run | 361 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SJP | solana | $8.54 | $6.04 | -29% | +11% | 1.3h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| S&P500 | $-8.02 | -67% | 0.9h | stop loss -66% |

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
tick #361  equity $415.76  cash $409.90  open 1
  scanning chains + news...
  144 raw candidates across 7 chains, 154 headlines/posts
  7 passed gates | rejected: liquidity too thin x105, no h1 volume x28, too old x2, already discovered x2
  top: TRUMP 0.83 | roon 0.62 | SJP 0.41 | Cream 0.33 | MINT 0.30
  no entries this tick
  shadow: tracking 97, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED NPC        peak +1110%  (scored 0.49)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
  entries blocked: weekly loss -16.8% <= -15%
```
