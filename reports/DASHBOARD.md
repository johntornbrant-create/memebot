# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T23:25:11+00:00`

## Equity

| | |
|---|---|
| Equity | **$376.10** |
| Return | **-24.78%** (start $500.00) |
| Cash | $373.84 |
| Deployed | $2.25 (0.6%) |
| Open positions | 1 / 8 |
| Closed trades | 34 (4W / 30L, WR 12%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $52.08 |
| Ticks run | 2078 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.25 | +15% | +29% | 3.7h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| GATO | $-5.00 | -100% | 2.3h | ratchet +55% (peak +121%) |
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
  shadow: tracking 48, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
done. equity $376.17 (-24.77% since start)
tick #2067  equity $376.17  cash $373.84  open 1
exits-only pass. equity $376.18 (next scan in 10 min)
tick #2068  equity $376.18  cash $373.84  open 1
exits-only pass. equity $376.17 (next scan in 9 min)
tick #2069  equity $376.17  cash $373.84  open 1
exits-only pass. equity $376.21 (next scan in 8 min)
tick #2070  equity $376.21  cash $373.84  open 1
exits-only pass. equity $376.20 (next scan in 7 min)
tick #2071  equity $376.20  cash $373.84  open 1
exits-only pass. equity $376.19 (next scan in 6 min)
tick #2072  equity $376.19  cash $373.84  open 1
exits-only pass. equity $376.19 (next scan in 5 min)
tick #2073  equity $376.19  cash $373.84  open 1
exits-only pass. equity $376.17 (next scan in 4 min)
tick #2074  equity $376.17  cash $373.84  open 1
exits-only pass. equity $376.19 (next scan in 3 min)
tick #2075  equity $376.19  cash $373.84  open 1
exits-only pass. equity $376.13 (next scan in 2 min)
tick #2076  equity $376.13  cash $373.84  open 1
exits-only pass. equity $376.12 (next scan in 1 min)
tick #2077  equity $376.12  cash $373.84  open 1
exits-only pass. equity $376.05 (next scan in 0 min)
tick #2078  equity $376.05  cash $373.84  open 1
  scanning chains + news...
  91 raw candidates across 7 chains, 160 headlines/posts
  5 passed gates | rejected: liquidity too thin x55, no h1 volume x22, too old x7, already discovered x1, unknown age x1
  top: BUTTHOLE 0.67 | BJB 0.55 | WISHMAS 0.46 | Socks 0.28 | GTAVI 0.24
  tick bar 0.64 (top 10% of 5, floor 0.45)
  no entries this tick
  shadow: tracking 45, closed 3 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
```
