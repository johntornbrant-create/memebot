# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-25T23:14:44+00:00`

## Equity

| | |
|---|---|
| Equity | **$438.81** |
| Return | **-12.24%** (start $500.00) |
| Cash | $429.69 |
| Deployed | $9.12 (2.1%) |
| Open positions | 1 / 8 |
| Closed trades | 14 (1W / 13L, WR 7%) |
| Profit factor | 0.41 |
| Fees + slippage paid | $7.78 |
| Ticks run | 1440 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| 币安AiPro | bsc | $6.41 | $9.12 | +44% | +44% | 11.3h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| CATTLEAXE | $-2.39 | -38% | 7.9h | stop loss -37% |
| BTC | $-2.59 | -42% | 4.0h | stop loss -40% |
| SWORDOPE | $-2.42 | -38% | 4.8h | stop loss -36% |
| REACHY | $-6.23 | -99% | 13.8h | stop loss -99% |
| KURUMI | $+5.28 | +58% | 6.0h | ratchet +65% (peak +136%) |
| MAYA | $-3.58 | -57% | 10.4h | ratchet +25% (peak +94%) |
| LUCIA | $-9.39 | -99% | 1.9h | stop loss -99% |
| ODIE | $-9.47 | -100% | 1.9h | stop loss -100% |
| WRHND | $-1.81 | -19% | 4.1h | ratchet +25% (peak +93%) |
| HCAT | $-9.53 | -100% | 2.1h | stop loss -99% |
| TRUMP | $-6.53 | -67% | 0.3h | stop loss -67% |
| Leonida | $-6.82 | -99% | 0.5h | stop loss -99% |
| MI | $-3.37 | -48% | 1.0h | stop loss -47% |
| PRIVACY | $-5.06 | -72% | 1.0h | stop loss -71% |
| APU | $-3.72 | -57% | 6.8h | stop loss -56% |

## Learned weights (v106)

_refit on 1380 observations (1285 shadow, 95 real), 401 winners (29% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.142 |
| txn_depth | +0.105 |
| momentum_accel | +0.077 |
| buy_pressure | +0.074 |
| not_vertical | -0.070 |
| paid_boost | +0.040 |
| age_sweet | +0.028 |
| dip_in_uptrend | +0.021 |
| liq_quality | +0.019 |
| buzz | +0.018 |
| fdv_sanity | +0.015 |
| socials | -0.004 |

## Last run log
```
tick #1440  equity $438.93  cash $425.86  open 2
  SELL CATTLEAXE  100% @ $0.001047  ->  $3.83   [stop loss -37%]
  scanning chains + news...
  133 raw candidates across 5 chains, 160 headlines/posts
  6 passed gates | rejected: liquidity too thin x90, no h1 volume x32, too new (bot war) x2, already discovered x2, too old x1
  top: GTA 0.54 | Chop 0.46 | LAUNCH 0.39 | CATTLEAXE 0.28 | REMUS 0.16
  tick bar 0.50 (top 30% of 6, floor 0.45)
  no entries this tick
  shadow: tracking 30, closed 9 this tick (4 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
  entries blocked: daily loss -6.8% <= -6%
```
