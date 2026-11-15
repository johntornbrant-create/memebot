# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T08:47:30+00:00`

## Equity

| | |
|---|---|
| Equity | **$415.89** |
| Return | **-16.82%** (start $500.00) |
| Cash | $405.22 |
| Deployed | $10.67 (2.6%) |
| Open positions | 2 / 8 |
| Closed trades | 23 (3W / 20L, WR 13%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $9.24 |
| Ticks run | 1709 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $5.15 | +3% | +17% | 9.5h |
| GTA | solana | $5.00 | $5.52 | +12% | +20% | 2.4h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| SHIT | $+4.56 | +91% | 14.6h | ratchet +90% (peak +172%) |
| worth | $-1.96 | -39% | 3.0h | stop loss -37% |
| 牛逼 | $+3.99 | +80% | 12.2h | ratchet +88% (peak +168%) |
| J*B | $-4.19 | -84% | 3.8h | stop loss -83% |
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

## Learned weights (v168)

_refit on 1797 observations (1695 shadow, 102 real), 492 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.149 |
| turnover | +0.126 |
| liq_quality | +0.089 |
| momentum_accel | +0.064 |
| buy_pressure | +0.061 |
| paid_boost | +0.035 |
| dip_in_uptrend | +0.031 |
| not_vertical | -0.029 |
| buzz | +0.020 |
| fdv_sanity | +0.011 |
| age_sweet | +0.007 |
| socials | -0.003 |

## Last run log
```
  3 passed gates | rejected: liquidity too thin x92, no h1 volume x31, too old x3, already discovered x3
  top: CLOCKED 0.38 | GTA 0.33 | HOGE 0.19
  tick bar 0.45 (top 10% of 3, floor 0.45)
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $416.22 (-16.76% since start)
tick #1699  equity $416.22  cash $405.22  open 2
exits-only pass. equity $416.26 (next scan in 10 min)
tick #1700  equity $416.26  cash $405.22  open 2
exits-only pass. equity $416.29 (next scan in 9 min)
tick #1701  equity $416.29  cash $405.22  open 2
exits-only pass. equity $416.28 (next scan in 8 min)
tick #1702  equity $416.28  cash $405.22  open 2
exits-only pass. equity $416.38 (next scan in 7 min)
tick #1703  equity $416.38  cash $405.22  open 2
exits-only pass. equity $416.10 (next scan in 6 min)
tick #1704  equity $416.10  cash $405.22  open 2
exits-only pass. equity $415.82 (next scan in 5 min)
tick #1705  equity $415.82  cash $405.22  open 2
exits-only pass. equity $415.93 (next scan in 4 min)
tick #1706  equity $415.93  cash $405.22  open 2
exits-only pass. equity $415.84 (next scan in 3 min)
tick #1707  equity $415.84  cash $405.22  open 2
exits-only pass. equity $415.73 (next scan in 2 min)
tick #1708  equity $415.73  cash $405.22  open 2
exits-only pass. equity $415.84 (next scan in 1 min)
tick #1709  equity $415.84  cash $405.22  open 2
  scanning chains + news...
  131 raw candidates across 6 chains, 160 headlines/posts
  3 passed gates | rejected: liquidity too thin x91, no h1 volume x31, too old x3, already discovered x3
  top: CLOCKED 0.39 | GTA 0.27 | HOGE 0.23
  tick bar 0.45 (top 10% of 3, floor 0.45)
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
