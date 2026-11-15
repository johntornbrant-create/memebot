# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T09:11:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$415.14** |
| Return | **-16.97%** (start $500.00) |
| Cash | $405.22 |
| Deployed | $9.91 (2.4%) |
| Open positions | 2 / 8 |
| Closed trades | 23 (3W / 20L, WR 13%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $9.24 |
| Ticks run | 1731 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $4.86 | -3% | +17% | 9.9h |
| GTA | solana | $5.00 | $5.05 | +2% | +20% | 2.8h |

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
  3 passed gates | rejected: liquidity too thin x93, no h1 volume x31, too old x3, already discovered x3
  top: CLOCKED 0.37 | HOGE 0.23 | GTA 0.19
  tick bar 0.45 (top 10% of 3, floor 0.45)
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $415.74 (-16.85% since start)
tick #1721  equity $415.74  cash $405.22  open 2
exits-only pass. equity $415.73 (next scan in 10 min)
tick #1722  equity $415.73  cash $405.22  open 2
exits-only pass. equity $415.57 (next scan in 9 min)
tick #1723  equity $415.57  cash $405.22  open 2
exits-only pass. equity $415.69 (next scan in 8 min)
tick #1724  equity $415.69  cash $405.22  open 2
exits-only pass. equity $415.27 (next scan in 7 min)
tick #1725  equity $415.27  cash $405.22  open 2
exits-only pass. equity $415.27 (next scan in 6 min)
tick #1726  equity $415.27  cash $405.22  open 2
exits-only pass. equity $415.20 (next scan in 5 min)
tick #1727  equity $415.20  cash $405.22  open 2
exits-only pass. equity $415.13 (next scan in 4 min)
tick #1728  equity $415.13  cash $405.22  open 2
exits-only pass. equity $415.12 (next scan in 3 min)
tick #1729  equity $415.12  cash $405.22  open 2
exits-only pass. equity $414.99 (next scan in 2 min)
tick #1730  equity $414.99  cash $405.22  open 2
exits-only pass. equity $415.07 (next scan in 1 min)
tick #1731  equity $415.07  cash $405.22  open 2
  scanning chains + news...
  153 raw candidates across 6 chains, 160 headlines/posts
  2 passed gates | rejected: liquidity too thin x106, no h1 volume x32, too old x6, already discovered x4, unknown age x3
  top: CLOCKED 0.36 | HOGE 0.34
  tick bar 0.45 (top 10% of 2, floor 0.45)
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
