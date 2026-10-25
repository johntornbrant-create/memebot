# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-25T18:31:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$441.90** |
| Return | **-11.62%** (start $500.00) |
| Cash | $422.23 |
| Deployed | $19.66 (4.4%) |
| Open positions | 3 / 8 |
| Closed trades | 12 (1W / 11L, WR 8%) |
| Profit factor | 0.41 |
| Fees + slippage paid | $7.69 |
| Ticks run | 1436 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| 币安AiPro | bsc | $6.41 | $8.95 | +42% | +42% | 6.6h |
| BTC | solana | $6.22 | $4.76 | -23% | +1% | 3.2h |
| CATTLEAXE | solana | $6.22 | $5.96 | -3% | +3% | 3.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| SWAP | $-6.55 | -98% | 6.4h | stop loss -98% |
| TIT | $-5.43 | -80% | 8.5h | stop loss -80% |

## Learned weights (v105)

_refit on 1369 observations (1276 shadow, 93 real), 401 winners (29% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.144 |
| txn_depth | +0.099 |
| momentum_accel | +0.080 |
| buy_pressure | +0.076 |
| not_vertical | -0.072 |
| paid_boost | +0.052 |
| age_sweet | +0.032 |
| buzz | +0.022 |
| dip_in_uptrend | +0.022 |
| liq_quality | +0.019 |
| fdv_sanity | +0.015 |
| socials | -0.005 |

## Last run log
```
tick #1436  equity $443.75  cash $422.23  open 3
  scanning chains + news...
  138 raw candidates across 6 chains, 160 headlines/posts
  10 passed gates | rejected: liquidity too thin x92, no h1 volume x30, too old x2, already discovered x2, too new (bot war) x2
  top: SQK 0.82 | ZERO 0.73 | MAGA 0.52 | CAKE 0.51 | PUMP 0.48
  tick bar 0.47 (top 30% of 10, floor 0.45)
  no entries this tick
  shadow: tracking 37, closed 9 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
  entries blocked: daily loss -6.1% <= -6%
```
