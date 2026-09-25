# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T21:24:45+00:00`

## Equity

| | |
|---|---|
| Equity | **$431.25** |
| Return | **-13.75%** (start $500.00) |
| Cash | $410.29 |
| Deployed | $20.96 (4.9%) |
| Open positions | 1 / 8 |
| Closed trades | 45 (13W / 32L, WR 29%) |
| Profit factor | 0.60 |
| Fees + slippage paid | $27.16 |
| Ticks run | 330 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| ARENA | solana | $17.10 | $20.96 | +65% | +98% | 21.3h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| 币安协议 | $-5.79 | -38% | 11.0h | stop loss -37% |

## Learned weights (v3)

_refit on 141 observations (96 shadow, 45 real), 51 winners (36% base rate)_

| Feature | Weight |
|---|---|
| buy_pressure | +0.130 |
| dip_in_uptrend | +0.092 |
| momentum_accel | +0.083 |
| fdv_sanity | +0.055 |
| turnover | +0.054 |
| not_vertical | -0.039 |
| buzz | +0.021 |
| age_sweet | +0.012 |
| paid_boost | +0.004 |
| socials | -0.001 |
| txn_depth | +0.001 |
| liq_quality | +0.000 |

## Last run log
```
tick #330  equity $431.43  cash $410.29  open 1
  scanning chains + news...
  92 raw candidates across 7 chains, 154 headlines/posts
  12 passed gates | rejected: liquidity too thin x57, no h1 volume x16, sell pressure x3, too old x2, already discovered x2
  top: GOCAT 0.88 | TRUMP 0.85 | $PLAY 0.69 | PHISH 0.62 | merci 0.61
  no entries this tick
  shadow: tracking 78, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED NPC        peak +1110%  (scored 0.49)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
  entries blocked: daily loss -23.8% <= -6%; daily trade cap reached
```
