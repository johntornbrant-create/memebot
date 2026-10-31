# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-31T17:53:28+00:00`

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
| Ticks run | 1493 |

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

## Learned weights (v127)

_refit on 1526 observations (1425 shadow, 101 real), 437 winners (29% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.144 |
| turnover | +0.135 |
| buy_pressure | +0.062 |
| momentum_accel | +0.059 |
| liq_quality | +0.053 |
| not_vertical | -0.047 |
| paid_boost | +0.037 |
| dip_in_uptrend | +0.034 |
| buzz | +0.009 |
| fdv_sanity | +0.007 |
| socials | -0.004 |
| age_sweet | +0.002 |

## Last run log
```
tick #1493  equity $412.87  cash $412.87  open 0
  scanning chains + news...
  83 raw candidates across 6 chains, 159 headlines/posts
  9 passed gates | rejected: liquidity too thin x50, no h1 volume x16, too old x5, too new (bot war) x3
  top: BNB 0.82 | FAGENT 0.62 | LUMI 0.57 | SKELLY 0.54 | Leverhedge 0.40
  tick bar 0.57 (top 10% of 9, floor 0.45)
  no entries this tick
  shadow: tracking 27, closed 2 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
