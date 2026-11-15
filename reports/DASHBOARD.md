# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T09:23:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$415.34** |
| Return | **-16.93%** (start $500.00) |
| Cash | $405.22 |
| Deployed | $10.12 (2.4%) |
| Open positions | 2 / 8 |
| Closed trades | 23 (3W / 20L, WR 13%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $9.24 |
| Ticks run | 1742 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $4.84 | -3% | +17% | 10.1h |
| GTA | solana | $5.00 | $5.27 | +7% | +20% | 3.0h |

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
  2 passed gates | rejected: liquidity too thin x106, no h1 volume x32, too old x6, already discovered x4, unknown age x3
  top: CLOCKED 0.36 | HOGE 0.34
  tick bar 0.45 (top 10% of 2, floor 0.45)
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $415.14 (-16.97% since start)
tick #1732  equity $415.14  cash $405.22  open 2
exits-only pass. equity $415.16 (next scan in 10 min)
tick #1733  equity $415.16  cash $405.22  open 2
exits-only pass. equity $415.41 (next scan in 9 min)
tick #1734  equity $415.41  cash $405.22  open 2
exits-only pass. equity $415.51 (next scan in 8 min)
tick #1735  equity $415.51  cash $405.22  open 2
exits-only pass. equity $415.31 (next scan in 7 min)
tick #1736  equity $415.31  cash $405.22  open 2
exits-only pass. equity $415.26 (next scan in 6 min)
tick #1737  equity $415.26  cash $405.22  open 2
exits-only pass. equity $415.34 (next scan in 5 min)
tick #1738  equity $415.34  cash $405.22  open 2
exits-only pass. equity $415.11 (next scan in 4 min)
tick #1739  equity $415.11  cash $405.22  open 2
exits-only pass. equity $415.16 (next scan in 3 min)
tick #1740  equity $415.16  cash $405.22  open 2
exits-only pass. equity $415.25 (next scan in 2 min)
tick #1741  equity $415.25  cash $405.22  open 2
exits-only pass. equity $415.44 (next scan in 1 min)
tick #1742  equity $415.44  cash $405.22  open 2
  scanning chains + news...
  153 raw candidates across 6 chains, 160 headlines/posts
  1 passed gates | rejected: liquidity too thin x106, no h1 volume x34, too old x5, already discovered x4, unknown age x3
  top: HOGE 0.40
  tick bar 0.45 (top 10% of 1, floor 0.45)
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
