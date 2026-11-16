# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T10:33:29+00:00`

## Equity

| | |
|---|---|
| Equity | **$368.29** |
| Return | **-26.34%** (start $500.00) |
| Cash | $346.30 |
| Deployed | $21.99 (6.0%) |
| Open positions | 5 / 8 |
| Closed trades | 37 (4W / 33L, WR 11%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $52.61 |
| Ticks run | 2244 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.37 | +21% | +29% | 14.8h |
| WISHMAS | solana | $5.00 | $5.11 | +3% | +5% | 10.0h |
| Anthropig | solana | $5.00 | $3.49 | -29% | +13% | 8.6h |
| GTA | solana | $5.00 | $6.84 | +38% | +38% | 3.4h |
| mihao | bsc | $5.00 | $4.18 | -15% | +23% | 1.0h |

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
  skip gtacoin: solana concentration cap
  skip mihao: already held
  no entries this tick
  shadow: tracking 46, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $367.52 (-26.50% since start)
tick #2234  equity $367.52  cash $346.30  open 5
exits-only pass. equity $367.13 (next scan in 10 min)
tick #2235  equity $367.13  cash $346.30  open 5
exits-only pass. equity $367.30 (next scan in 9 min)
tick #2236  equity $367.30  cash $346.30  open 5
exits-only pass. equity $367.23 (next scan in 8 min)
tick #2237  equity $367.23  cash $346.30  open 5
exits-only pass. equity $367.47 (next scan in 7 min)
tick #2238  equity $367.47  cash $346.30  open 5
exits-only pass. equity $367.19 (next scan in 6 min)
tick #2239  equity $367.19  cash $346.30  open 5
exits-only pass. equity $367.06 (next scan in 5 min)
tick #2240  equity $367.06  cash $346.30  open 5
exits-only pass. equity $367.45 (next scan in 4 min)
tick #2241  equity $367.45  cash $346.30  open 5
exits-only pass. equity $367.25 (next scan in 3 min)
tick #2242  equity $367.25  cash $346.30  open 5
exits-only pass. equity $367.77 (next scan in 2 min)
tick #2243  equity $367.77  cash $346.30  open 5
exits-only pass. equity $367.92 (next scan in 1 min)
tick #2244  equity $367.92  cash $346.30  open 5
  scanning chains + news...
  151 raw candidates across 7 chains, 160 headlines/posts
  4 passed gates | rejected: liquidity too thin x96, no h1 volume x44, already discovered x5, too old x1, unknown age x1
  top: mihao 0.76 | gtacoin 0.55 | GTA 0.49 | Anthropig 0.36
  tick bar 0.64 (top 10% of 4, floor 0.45)
  skip mihao: already held
  no entries this tick
  shadow: tracking 45, closed 1 this tick (1 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
