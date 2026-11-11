# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-11T01:26:04+00:00`

## Equity

| | |
|---|---|
| Equity | **$412.87** |
| Return | **-17.43%** (start $500.00) |
| Cash | $412.87 |
| Deployed | $-0.00 (-0.0%) |
| Open positions | 0 / 8 |
| Closed trades | 19 (1W / 18L, WR 5%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $8.47 |
| Ticks run | 1535 |

## Open positions

_flat_

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| FLAPAI | $-6.90 | -79% | 6.7h | stop loss -78% |
| GTA | $-5.00 | -57% | 6.7h | stop loss -56% |
| GTA | $-2.64 | -43% | 11.7h | ratchet +65% (peak +135%) |
| TIT | $-7.07 | -80% | 4.9h | stop loss -79% |
| 币安AiPro | $-1.62 | -25% | 18.2h | ratchet +47% (peak +109%) |
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

## Learned weights (v156)

_refit on 1731 observations (1630 shadow, 101 real), 479 winners (28% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.146 |
| turnover | +0.138 |
| liq_quality | +0.089 |
| momentum_accel | +0.062 |
| buy_pressure | +0.050 |
| paid_boost | +0.039 |
| dip_in_uptrend | +0.038 |
| not_vertical | -0.036 |
| buzz | +0.019 |
| fdv_sanity | +0.016 |
| socials | -0.008 |
| age_sweet | +0.001 |

## Last run log
```
tick #1535  equity $412.87  cash $412.87  open 0
  scanning chains + news...
  104 raw candidates across 8 chains, 158 headlines/posts
  6 passed gates | rejected: liquidity too thin x62, no h1 volume x29, too old x6, already discovered x1
  top: 咪好 0.69 | NIHAO 0.65 | BABYMINHAO 0.61 | 哈基仙人 0.61 | DACITY 0.41
  tick bar 0.57 (top 10% of 6, floor 0.45)
  no entries this tick
  shadow: tracking 13, closed 7 this tick (3 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
