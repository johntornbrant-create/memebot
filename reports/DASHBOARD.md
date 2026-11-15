# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T20:46:05+00:00`

## Equity

| | |
|---|---|
| Equity | **$378.14** |
| Return | **-24.37%** (start $500.00) |
| Cash | $373.84 |
| Deployed | $4.29 (1.1%) |
| Open positions | 2 / 8 |
| Closed trades | 33 (4W / 29L, WR 12%) |
| Profit factor | 0.38 |
| Fees + slippage paid | $49.06 |
| Ticks run | 1932 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| GATO | ethereum | $5.00 | $2.11 | +43% | +50% | 1.6h |
| Macca | ethereum | $5.00 | $2.18 | +11% | +16% | 1.0h |

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
  shadow: tracking 36, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
done. equity $378.80 (-24.24% since start)
tick #1922  equity $378.80  cash $370.64  open 3
exits-only pass. equity $378.97 (next scan in 10 min)
tick #1923  equity $378.97  cash $370.64  open 3
exits-only pass. equity $379.09 (next scan in 9 min)
tick #1924  equity $379.09  cash $370.64  open 3
  SELL GATO       25% @ $0.0001673  ->  $0.00   [take profit +50% (sold 25%)]
exits-only pass. equity $378.50 (next scan in 8 min)
tick #1925  equity $378.50  cash $370.64  open 3
exits-only pass. equity $378.11 (next scan in 7 min)
tick #1926  equity $378.11  cash $370.64  open 3
exits-only pass. equity $378.13 (next scan in 6 min)
tick #1927  equity $378.13  cash $370.64  open 3
  SELL FOOD       100% @ $0.000228  ->  $3.20   [stop loss -35%]
exits-only pass. equity $377.97 (next scan in 5 min)
tick #1928  equity $377.97  cash $373.84  open 2
exits-only pass. equity $378.08 (next scan in 4 min)
tick #1929  equity $378.08  cash $373.84  open 2
exits-only pass. equity $378.16 (next scan in 3 min)
tick #1930  equity $378.16  cash $373.84  open 2
exits-only pass. equity $377.88 (next scan in 2 min)
tick #1931  equity $377.88  cash $373.84  open 2
exits-only pass. equity $378.16 (next scan in 1 min)
tick #1932  equity $378.16  cash $373.84  open 2
  scanning chains + news...
  157 raw candidates across 8 chains, 160 headlines/posts
  12 passed gates | rejected: liquidity too thin x98, no h1 volume x32, already discovered x7, too old x5, exit-liquidity trap (FDV/liq) x1
  top: rockstar 0.89 | BUTTHOLE 0.79 | Emojis 0.73 | WASTED 0.73 | TAIL 0.71
  tick bar 0.64 (top 10% of 12, floor 0.45)
  no entries this tick
  shadow: tracking 40, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
```
