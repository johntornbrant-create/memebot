# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T22:10:55+00:00`

## Equity

| | |
|---|---|
| Equity | **$376.25** |
| Return | **-24.75%** (start $500.00) |
| Cash | $373.84 |
| Deployed | $2.41 (0.6%) |
| Open positions | 1 / 8 |
| Closed trades | 34 (4W / 30L, WR 12%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $52.08 |
| Ticks run | 2010 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.41 | +23% | +29% | 2.4h |

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
  tick bar 0.64 (top 10% of 10, floor 0.45)
  no entries this tick
  shadow: tracking 45, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
done. equity $376.16 (-24.77% since start)
tick #2000  equity $376.16  cash $373.84  open 1
exits-only pass. equity $376.21 (next scan in 10 min)
tick #2001  equity $376.21  cash $373.84  open 1
exits-only pass. equity $376.18 (next scan in 9 min)
tick #2002  equity $376.18  cash $373.84  open 1
exits-only pass. equity $376.18 (next scan in 8 min)
tick #2003  equity $376.18  cash $373.84  open 1
exits-only pass. equity $376.19 (next scan in 7 min)
tick #2004  equity $376.19  cash $373.84  open 1
exits-only pass. equity $376.20 (next scan in 6 min)
tick #2005  equity $376.20  cash $373.84  open 1
exits-only pass. equity $376.21 (next scan in 5 min)
tick #2006  equity $376.21  cash $373.84  open 1
exits-only pass. equity $376.23 (next scan in 4 min)
tick #2007  equity $376.23  cash $373.84  open 1
exits-only pass. equity $376.21 (next scan in 3 min)
tick #2008  equity $376.21  cash $373.84  open 1
exits-only pass. equity $376.23 (next scan in 2 min)
tick #2009  equity $376.23  cash $373.84  open 1
exits-only pass. equity $376.25 (next scan in 1 min)
tick #2010  equity $376.25  cash $373.84  open 1
  scanning chains + news...
  168 raw candidates across 7 chains, 160 headlines/posts
  10 passed gates | rejected: liquidity too thin x104, no h1 volume x40, too old x10, unknown age x2, too new (bot war) x1
  top: BJB 0.71 | BUTTHOLE 0.47 | gtacoin 0.47 | Brian 0.41 | VICE 0.40
  tick bar 0.64 (top 10% of 10, floor 0.45)
  no entries this tick
  shadow: tracking 45, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
```
