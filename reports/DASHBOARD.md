# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-02T18:32:24+00:00`

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
| Ticks run | 1502 |

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

## Learned weights (v133)

_refit on 1568 observations (1467 shadow, 101 real), 448 winners (29% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.147 |
| turnover | +0.132 |
| buy_pressure | +0.066 |
| liq_quality | +0.065 |
| momentum_accel | +0.057 |
| not_vertical | -0.044 |
| dip_in_uptrend | +0.037 |
| paid_boost | +0.031 |
| buzz | +0.018 |
| age_sweet | +0.006 |
| fdv_sanity | +0.004 |
| socials | -0.002 |

## Last run log
```
tick #1502  equity $412.87  cash $412.87  open 0
  scanning chains + news...
  115 raw candidates across 5 chains, 160 headlines/posts
  9 passed gates | rejected: liquidity too thin x76, no h1 volume x17, too old x12, unknown age x1
  top: MAMESUKE 0.73 | RICO 0.69 | Slingoor 0.65 | SLINGOOR 0.50 | PEACE 0.41
  tick bar 0.60 (top 10% of 9, floor 0.45)
  no entries this tick
  shadow: tracking 20, closed 6 this tick (2 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
