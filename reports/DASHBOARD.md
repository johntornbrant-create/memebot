# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T09:57:30+00:00`

## Equity

| | |
|---|---|
| Equity | **$368.11** |
| Return | **-26.38%** (start $500.00) |
| Cash | $346.30 |
| Deployed | $21.82 (5.9%) |
| Open positions | 5 / 8 |
| Closed trades | 37 (4W / 33L, WR 11%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $52.61 |
| Ticks run | 2211 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.33 | +19% | +29% | 14.2h |
| WISHMAS | solana | $5.00 | $4.76 | -4% | +5% | 9.4h |
| Anthropig | solana | $5.00 | $4.06 | -18% | +13% | 8.0h |
| GTA | solana | $5.00 | $5.39 | +9% | +17% | 2.8h |
| mihao | bsc | $5.00 | $5.27 | +7% | +23% | 0.4h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| Marvin | $-2.04 | -41% | 0.8h | stop loss -39% |
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
  skip GTA: already held
  no entries this tick
  shadow: tracking 46, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $368.22 (-26.36% since start)
tick #2201  equity $368.22  cash $346.30  open 5
exits-only pass. equity $368.60 (next scan in 10 min)
tick #2202  equity $368.60  cash $346.30  open 5
exits-only pass. equity $368.71 (next scan in 9 min)
tick #2203  equity $368.71  cash $346.30  open 5
exits-only pass. equity $368.57 (next scan in 8 min)
tick #2204  equity $368.57  cash $346.30  open 5
exits-only pass. equity $368.33 (next scan in 7 min)
tick #2205  equity $368.33  cash $346.30  open 5
exits-only pass. equity $367.90 (next scan in 6 min)
tick #2206  equity $367.90  cash $346.30  open 5
exits-only pass. equity $367.87 (next scan in 5 min)
tick #2207  equity $367.87  cash $346.30  open 5
exits-only pass. equity $367.97 (next scan in 4 min)
tick #2208  equity $367.97  cash $346.30  open 5
exits-only pass. equity $368.39 (next scan in 3 min)
tick #2209  equity $368.39  cash $346.30  open 5
exits-only pass. equity $367.95 (next scan in 2 min)
tick #2210  equity $367.95  cash $346.30  open 5
exits-only pass. equity $368.40 (next scan in 1 min)
tick #2211  equity $368.40  cash $346.30  open 5
  scanning chains + news...
  149 raw candidates across 7 chains, 160 headlines/posts
  6 passed gates | rejected: liquidity too thin x83, no h1 volume x37, too old x10, already discovered x10, unknown age x2
  top: mihao 0.74 | gtacoin 0.55 | WASTED 0.53 | Macca 0.38 | GTA 0.38
  tick bar 0.64 (top 10% of 6, floor 0.45)
  skip Macca: already held
  skip Anthropig: already held
  no entries this tick
  shadow: tracking 46, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
