# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-27T22:38:14+00:00`

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
| Ticks run | 1460 |

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

## Learned weights (v113)

_refit on 1443 observations (1342 shadow, 101 real), 420 winners (29% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.132 |
| txn_depth | +0.125 |
| buy_pressure | +0.081 |
| momentum_accel | +0.059 |
| not_vertical | -0.058 |
| liq_quality | +0.036 |
| dip_in_uptrend | +0.036 |
| paid_boost | +0.035 |
| socials | -0.018 |
| fdv_sanity | +0.013 |
| age_sweet | +0.011 |
| buzz | +0.009 |

## Last run log
```
tick #1460  equity $412.87  cash $412.87  open 0
  scanning chains + news...
  160 raw candidates across 9 chains, 155 headlines/posts
  19 passed gates | rejected: liquidity too thin x96, no h1 volume x30, too old x9, already discovered x6
  top: FRONGUS 0.72 | Rollcage 0.68 | PEPUS 0.58 | Nothing 0.53 | SI 0.50
  tick bar 0.50 (top 30% of 19, floor 0.45)
  no entries this tick
  shadow: tracking 33, closed 4 this tick (1 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
  entries blocked: 7d loss -17.4% <= -15%
```
