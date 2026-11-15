# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T21:10:09+00:00`

## Equity

| | |
|---|---|
| Equity | **$379.52** |
| Return | **-24.10%** (start $500.00) |
| Cash | $373.84 |
| Deployed | $5.68 (1.5%) |
| Open positions | 2 / 8 |
| Closed trades | 33 (4W / 29L, WR 12%) |
| Profit factor | 0.38 |
| Fees + slippage paid | $49.06 |
| Ticks run | 1954 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| GATO | ethereum | $5.00 | $3.26 | +121% | +121% | 2.0h |
| Macca | ethereum | $5.00 | $2.42 | +23% | +25% | 1.4h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| FOOD | $-1.85 | -37% | 21.4h | stop loss -35% |
| WASTED | $-5.00 | -100% | 1.6h | ratchet +190% (peak +314%) |
| BEAR | $-4.85 | -97% | 1.1h | stop loss -97% |
| GTA | $-0.17 | -3% | 13.4h | ratchet +0% (peak +43%) |
| JASON | $-5.00 | -100% | 0.6h | stop loss -41% |
| GTA | $-5.00 | -100% | 1.1h | stop loss -99% |
| LETSWIN | $-5.00 | -100% | 5.6h | stop loss -83% |
| Socks | $+0.41 | +8% | 7.2h | ratchet +42% (peak +103%) |
| Macca | $-3.03 | -61% | 1.2h | stop loss -59% |
| HOGE | $-1.94 | -39% | 0.2h | stop loss -37% |
| SHIT | $+4.56 | +91% | 14.6h | ratchet +90% (peak +172%) |
| worth | $-1.96 | -39% | 3.0h | stop loss -37% |
| 牛逼 | $+3.99 | +80% | 12.2h | ratchet +88% (peak +168%) |
| J*B | $-4.19 | -84% | 3.8h | stop loss -83% |
| FLAPAI | $-6.90 | -79% | 6.7h | stop loss -78% |

## Learned weights (v169)

_refit on 1806 observations (1699 shadow, 107 real), 494 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.152 |
| turnover | +0.127 |
| liq_quality | +0.096 |
| momentum_accel | +0.065 |
| buy_pressure | +0.062 |
| paid_boost | +0.034 |
| fdv_sanity | +0.030 |
| not_vertical | -0.029 |
| dip_in_uptrend | +0.025 |
| buzz | +0.019 |
| age_sweet | +0.009 |
| socials | -0.004 |

## Last run log
```
  tick bar 0.64 (top 10% of 14, floor 0.45)
  no entries this tick
  shadow: tracking 41, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
done. equity $378.25 (-24.35% since start)
tick #1944  equity $378.25  cash $373.84  open 2
exits-only pass. equity $378.49 (next scan in 10 min)
tick #1945  equity $378.49  cash $373.84  open 2
exits-only pass. equity $378.62 (next scan in 9 min)
tick #1946  equity $378.62  cash $373.84  open 2
exits-only pass. equity $378.59 (next scan in 8 min)
tick #1947  equity $378.59  cash $373.84  open 2
exits-only pass. equity $378.73 (next scan in 7 min)
tick #1948  equity $378.73  cash $373.84  open 2
exits-only pass. equity $378.68 (next scan in 6 min)
tick #1949  equity $378.68  cash $373.84  open 2
exits-only pass. equity $378.76 (next scan in 5 min)
tick #1950  equity $378.76  cash $373.84  open 2
exits-only pass. equity $379.01 (next scan in 4 min)
tick #1951  equity $379.01  cash $373.84  open 2
exits-only pass. equity $379.19 (next scan in 3 min)
tick #1952  equity $379.19  cash $373.84  open 2
exits-only pass. equity $379.52 (next scan in 2 min)
tick #1953  equity $379.52  cash $373.84  open 2
exits-only pass. equity $379.40 (next scan in 1 min)
tick #1954  equity $379.40  cash $373.84  open 2
  scanning chains + news...
  129 raw candidates across 8 chains, 160 headlines/posts
  9 passed gates | rejected: liquidity too thin x82, no h1 volume x26, too old x10, too new (bot war) x1, already discovered x1
  top: BUTTHOLE 0.81 | HENSEN 0.60 | NCAT 0.54 | Emojis 0.50 | bill 0.47
  tick bar 0.64 (top 10% of 9, floor 0.45)
  no entries this tick
  shadow: tracking 42, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
```
