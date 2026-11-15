# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T21:22:09+00:00`

## Equity

| | |
|---|---|
| Equity | **$378.83** |
| Return | **-24.23%** (start $500.00) |
| Cash | $373.84 |
| Deployed | $4.99 (1.3%) |
| Open positions | 2 / 8 |
| Closed trades | 33 (4W / 29L, WR 12%) |
| Profit factor | 0.38 |
| Fees + slippage paid | $49.06 |
| Ticks run | 1965 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| GATO | ethereum | $5.00 | $2.61 | +77% | +121% | 2.2h |
| Macca | ethereum | $5.00 | $2.38 | +21% | +25% | 1.6h |

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
  tick bar 0.64 (top 10% of 9, floor 0.45)
  no entries this tick
  shadow: tracking 42, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
done. equity $379.52 (-24.10% since start)
tick #1955  equity $379.52  cash $373.84  open 2
exits-only pass. equity $379.15 (next scan in 10 min)
tick #1956  equity $379.15  cash $373.84  open 2
exits-only pass. equity $379.15 (next scan in 9 min)
tick #1957  equity $379.15  cash $373.84  open 2
exits-only pass. equity $379.17 (next scan in 8 min)
tick #1958  equity $379.17  cash $373.84  open 2
exits-only pass. equity $379.08 (next scan in 7 min)
tick #1959  equity $379.08  cash $373.84  open 2
exits-only pass. equity $379.22 (next scan in 6 min)
tick #1960  equity $379.22  cash $373.84  open 2
exits-only pass. equity $379.12 (next scan in 5 min)
tick #1961  equity $379.12  cash $373.84  open 2
exits-only pass. equity $379.22 (next scan in 4 min)
tick #1962  equity $379.22  cash $373.84  open 2
exits-only pass. equity $379.19 (next scan in 3 min)
tick #1963  equity $379.19  cash $373.84  open 2
exits-only pass. equity $378.90 (next scan in 2 min)
tick #1964  equity $378.90  cash $373.84  open 2
exits-only pass. equity $378.88 (next scan in 1 min)
tick #1965  equity $378.88  cash $373.84  open 2
  scanning chains + news...
  129 raw candidates across 7 chains, 160 headlines/posts
  7 passed gates | rejected: liquidity too thin x83, no h1 volume x24, too old x12, too new (bot war) x1, sell pressure x1
  top: BUTTHOLE 0.82 | Brian 0.70 | bill 0.49 | Emojis 0.49 | Socks 0.40
  tick bar 0.64 (top 10% of 7, floor 0.45)
  no entries this tick
  shadow: tracking 43, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
```
