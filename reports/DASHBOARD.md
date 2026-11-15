# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T10:11:32+00:00`

## Equity

| | |
|---|---|
| Equity | **$414.18** |
| Return | **-17.16%** (start $500.00) |
| Cash | $403.29 |
| Deployed | $10.89 (2.6%) |
| Open positions | 2 / 8 |
| Closed trades | 24 (3W / 21L, WR 12%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $9.34 |
| Ticks run | 1786 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $4.46 | -11% | +17% | 10.9h |
| GTA | solana | $5.00 | $6.44 | +30% | +32% | 3.8h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| HOGE | $-1.94 | -39% | 0.2h | stop loss -37% |
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
tick #1775  equity $413.94  cash $400.22  open 3
  scanning chains + news...
  158 raw candidates across 8 chains, 160 headlines/posts
  0 passed gates | rejected: liquidity too thin x112, no h1 volume x32, too old x6, already discovered x4, unknown age x3
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $414.09 (-17.18% since start)
tick #1776  equity $414.09  cash $400.22  open 3
exits-only pass. equity $414.01 (next scan in 10 min)
tick #1777  equity $414.01  cash $400.22  open 3
  SELL HOGE       100% @ $4.702e-05  ->  $3.06   [stop loss -37%]
exits-only pass. equity $413.82 (next scan in 9 min)
tick #1778  equity $413.82  cash $403.29  open 2
exits-only pass. equity $413.79 (next scan in 8 min)
tick #1779  equity $413.79  cash $403.29  open 2
exits-only pass. equity $413.87 (next scan in 7 min)
tick #1780  equity $413.87  cash $403.29  open 2
exits-only pass. equity $414.04 (next scan in 6 min)
tick #1781  equity $414.04  cash $403.29  open 2
exits-only pass. equity $414.15 (next scan in 5 min)
tick #1782  equity $414.15  cash $403.29  open 2
exits-only pass. equity $414.28 (next scan in 4 min)
tick #1783  equity $414.28  cash $403.29  open 2
exits-only pass. equity $414.28 (next scan in 3 min)
tick #1784  equity $414.28  cash $403.29  open 2
exits-only pass. equity $414.06 (next scan in 2 min)
tick #1785  equity $414.06  cash $403.29  open 2
exits-only pass. equity $414.05 (next scan in 1 min)
tick #1786  equity $414.05  cash $403.29  open 2
  scanning chains + news...
  142 raw candidates across 7 chains, 160 headlines/posts
  0 passed gates | rejected: liquidity too thin x106, no h1 volume x26, already discovered x6, too old x4
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
