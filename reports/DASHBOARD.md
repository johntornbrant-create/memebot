# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T10:09:30+00:00`

## Equity

| | |
|---|---|
| Equity | **$368.46** |
| Return | **-26.31%** (start $500.00) |
| Cash | $346.30 |
| Deployed | $22.16 (6.0%) |
| Open positions | 5 / 8 |
| Closed trades | 37 (4W / 33L, WR 11%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $52.61 |
| Ticks run | 2222 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.38 | +21% | +29% | 14.4h |
| WISHMAS | solana | $5.00 | $4.81 | -3% | +5% | 9.6h |
| Anthropig | solana | $5.00 | $4.03 | -19% | +13% | 8.2h |
| GTA | solana | $5.00 | $6.12 | +24% | +24% | 3.0h |
| mihao | bsc | $5.00 | $4.82 | -2% | +23% | 0.6h |

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
  skip Anthropig: already held
  no entries this tick
  shadow: tracking 46, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $368.11 (-26.38% since start)
tick #2212  equity $368.11  cash $346.30  open 5
exits-only pass. equity $367.90 (next scan in 10 min)
tick #2213  equity $367.90  cash $346.30  open 5
exits-only pass. equity $367.69 (next scan in 9 min)
tick #2214  equity $367.69  cash $346.30  open 5
exits-only pass. equity $367.71 (next scan in 8 min)
tick #2215  equity $367.71  cash $346.30  open 5
exits-only pass. equity $368.03 (next scan in 7 min)
tick #2216  equity $368.03  cash $346.30  open 5
exits-only pass. equity $367.92 (next scan in 6 min)
tick #2217  equity $367.92  cash $346.30  open 5
exits-only pass. equity $367.94 (next scan in 5 min)
tick #2218  equity $367.94  cash $346.30  open 5
exits-only pass. equity $367.78 (next scan in 4 min)
tick #2219  equity $367.78  cash $346.30  open 5
exits-only pass. equity $367.60 (next scan in 3 min)
tick #2220  equity $367.60  cash $346.30  open 5
exits-only pass. equity $367.57 (next scan in 2 min)
tick #2221  equity $367.57  cash $346.30  open 5
exits-only pass. equity $367.93 (next scan in 1 min)
tick #2222  equity $367.93  cash $346.30  open 5
  scanning chains + news...
  134 raw candidates across 6 chains, 160 headlines/posts
  4 passed gates | rejected: liquidity too thin x90, no h1 volume x30, already discovered x6, too old x3, unknown age x1
  top: mihao 0.79 | GTA 0.45 | gtacoin 0.43 | Anthropig 0.36
  tick bar 0.64 (top 10% of 4, floor 0.45)
  skip mihao: already held
  skip Anthropig: already held
  no entries this tick
  shadow: tracking 46, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
