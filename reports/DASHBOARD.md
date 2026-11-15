# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T09:59:32+00:00`

## Equity

| | |
|---|---|
| Equity | **$414.09** |
| Return | **-17.18%** (start $500.00) |
| Cash | $400.22 |
| Deployed | $13.87 (3.3%) |
| Open positions | 3 / 8 |
| Closed trades | 23 (3W / 20L, WR 13%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $9.30 |
| Ticks run | 1775 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $4.42 | -11% | +17% | 10.7h |
| GTA | solana | $5.00 | $5.49 | +11% | +20% | 3.6h |
| HOGE | solana | $5.00 | $3.96 | -20% | +1% | 0.2h |

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
  scanning chains + news...
  157 raw candidates across 8 chains, 160 headlines/posts
  1 passed gates | rejected: liquidity too thin x110, no h1 volume x33, too old x6, already discovered x4, unknown age x3
  top: HOGE 0.42
  tick bar 0.45 (top 10% of 1, floor 0.45)
  BUY[explore] HOGE       $5.00 @ $7.486e-05  score 0.42  solana  liq $26,391
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $414.91 (-17.02% since start)
tick #1765  equity $414.91  cash $400.22  open 3
exits-only pass. equity $414.95 (next scan in 10 min)
tick #1766  equity $414.95  cash $400.22  open 3
exits-only pass. equity $414.68 (next scan in 9 min)
tick #1767  equity $414.68  cash $400.22  open 3
exits-only pass. equity $415.15 (next scan in 8 min)
tick #1768  equity $415.15  cash $400.22  open 3
exits-only pass. equity $414.38 (next scan in 7 min)
tick #1769  equity $414.38  cash $400.22  open 3
exits-only pass. equity $414.45 (next scan in 6 min)
tick #1770  equity $414.45  cash $400.22  open 3
exits-only pass. equity $414.08 (next scan in 5 min)
tick #1771  equity $414.08  cash $400.22  open 3
exits-only pass. equity $414.25 (next scan in 4 min)
tick #1772  equity $414.25  cash $400.22  open 3
exits-only pass. equity $414.31 (next scan in 3 min)
tick #1773  equity $414.31  cash $400.22  open 3
exits-only pass. equity $414.07 (next scan in 2 min)
tick #1774  equity $414.07  cash $400.22  open 3
exits-only pass. equity $413.94 (next scan in 1 min)
tick #1775  equity $413.94  cash $400.22  open 3
  scanning chains + news...
  158 raw candidates across 8 chains, 160 headlines/posts
  0 passed gates | rejected: liquidity too thin x112, no h1 volume x32, too old x6, already discovered x4, unknown age x3
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
