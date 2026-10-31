# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-31T06:53:31+00:00`

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
| Ticks run | 1491 |

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

## Learned weights (v125)

_refit on 1521 observations (1420 shadow, 101 real), 437 winners (29% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.141 |
| turnover | +0.137 |
| buy_pressure | +0.061 |
| momentum_accel | +0.059 |
| liq_quality | +0.054 |
| not_vertical | -0.049 |
| paid_boost | +0.036 |
| dip_in_uptrend | +0.033 |
| buzz | +0.008 |
| fdv_sanity | +0.007 |
| age_sweet | +0.005 |
| socials | -0.004 |

## Last run log
```
tick #1491  equity $412.87  cash $412.87  open 0
  scanning chains + news...
  103 raw candidates across 4 chains, 158 headlines/posts
  7 passed gates | rejected: liquidity too thin x61, no h1 volume x23, too old x7, already discovered x3, too new (bot war) x2
  top: BNB 0.57 | TITTYVERSE 0.56 | AgenC 0.54 | MONEKO 0.50 | iCat 0.42
  tick bar 0.57 (top 10% of 7, floor 0.45)
  no entries this tick
  shadow: tracking 17, closed 5 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
