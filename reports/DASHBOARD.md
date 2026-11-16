# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T06:21:28+00:00`

## Equity

| | |
|---|---|
| Equity | **$368.82** |
| Return | **-26.24%** (start $500.00) |
| Cash | $353.34 |
| Deployed | $15.49 (4.2%) |
| Open positions | 4 / 8 |
| Closed trades | 36 (4W / 32L, WR 11%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $52.43 |
| Ticks run | 2013 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.13 | +8% | +29% | 10.6h |
| WISHMAS | solana | $5.00 | $4.27 | -14% | +5% | 5.8h |
| Anthropig | solana | $5.00 | $4.74 | -4% | +0% | 4.4h |
| Marvin | solana | $5.00 | $4.35 | -12% | +10% | 0.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| Neil | $-1.94 | -39% | 4.2h | stop loss -37% |
| GTAVI | $-3.57 | -71% | 1.4h | stop loss -70% |
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

## Learned weights (v170)

_refit on 1825 observations (1708 shadow, 117 real), 498 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.145 |
| turnover | +0.117 |
| liq_quality | +0.105 |
| momentum_accel | +0.066 |
| buy_pressure | +0.060 |
| not_vertical | -0.033 |
| paid_boost | +0.029 |
| dip_in_uptrend | +0.029 |
| fdv_sanity | +0.023 |
| buzz | +0.019 |
| age_sweet | +0.018 |
| socials | -0.009 |

## Last run log
```
  tick bar 0.59 (top 10% of 5, floor 0.45)
  BUY[explore] Marvin     $5.00 @ $0.000642  score 0.41  solana  liq $75,165
  skip WISHMAS: already held
  shadow: tracking 47, closed 2 this tick (2 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $369.76 (-26.05% since start)
tick #2003  equity $369.76  cash $353.34  open 4
exits-only pass. equity $370.09 (next scan in 10 min)
tick #2004  equity $370.09  cash $353.34  open 4
exits-only pass. equity $369.59 (next scan in 9 min)
tick #2005  equity $369.59  cash $353.34  open 4
exits-only pass. equity $369.48 (next scan in 8 min)
tick #2006  equity $369.48  cash $353.34  open 4
exits-only pass. equity $369.27 (next scan in 7 min)
tick #2007  equity $369.27  cash $353.34  open 4
exits-only pass. equity $368.32 (next scan in 6 min)
tick #2008  equity $368.32  cash $353.34  open 4
exits-only pass. equity $368.40 (next scan in 5 min)
tick #2009  equity $368.40  cash $353.34  open 4
exits-only pass. equity $368.68 (next scan in 4 min)
tick #2010  equity $368.68  cash $353.34  open 4
exits-only pass. equity $368.78 (next scan in 3 min)
tick #2011  equity $368.78  cash $353.34  open 4
exits-only pass. equity $368.48 (next scan in 2 min)
tick #2012  equity $368.48  cash $353.34  open 4
exits-only pass. equity $368.25 (next scan in 1 min)
tick #2013  equity $368.25  cash $353.34  open 4
  scanning chains + news...
  88 raw candidates across 4 chains, 160 headlines/posts
  6 passed gates | rejected: liquidity too thin x50, no h1 volume x23, too old x5, already discovered x4
  top: 6STAR 0.50 | BUTTHOLE 0.45 | Anthropig 0.41 | GTA 0.37 | Marvin 0.35
  tick bar 0.50 (top 10% of 6, floor 0.45)
  skip 6STAR: solana concentration cap
  no entries this tick
  shadow: tracking 46, closed 1 this tick (1 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
