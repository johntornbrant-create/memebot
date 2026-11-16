# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T09:33:29+00:00`

## Equity

| | |
|---|---|
| Equity | **$366.81** |
| Return | **-26.64%** (start $500.00) |
| Cash | $346.30 |
| Deployed | $20.51 (5.6%) |
| Open positions | 5 / 8 |
| Closed trades | 37 (4W / 33L, WR 11%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $52.61 |
| Ticks run | 2189 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.26 | +15% | +29% | 13.8h |
| WISHMAS | solana | $5.00 | $4.84 | -2% | +5% | 9.0h |
| Anthropig | solana | $5.00 | $3.74 | -24% | +13% | 7.6h |
| GTA | solana | $5.00 | $4.66 | -6% | +17% | 2.4h |
| mihao | bsc | $5.00 | $4.91 | +0% | +0% | 0.0h |

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
  skip GTA: already held
  no entries this tick
  shadow: tracking 45, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $367.71 (-26.46% since start)
tick #2179  equity $367.71  cash $351.30  open 4
exits-only pass. equity $367.96 (next scan in 10 min)
tick #2180  equity $367.96  cash $351.30  open 4
exits-only pass. equity $367.55 (next scan in 9 min)
tick #2181  equity $367.55  cash $351.30  open 4
exits-only pass. equity $367.46 (next scan in 8 min)
tick #2182  equity $367.46  cash $351.30  open 4
exits-only pass. equity $367.24 (next scan in 7 min)
tick #2183  equity $367.24  cash $351.30  open 4
exits-only pass. equity $367.19 (next scan in 6 min)
tick #2184  equity $367.19  cash $351.30  open 4
exits-only pass. equity $367.24 (next scan in 5 min)
tick #2185  equity $367.24  cash $351.30  open 4
exits-only pass. equity $367.31 (next scan in 4 min)
tick #2186  equity $367.31  cash $351.30  open 4
exits-only pass. equity $367.30 (next scan in 3 min)
tick #2187  equity $367.30  cash $351.30  open 4
exits-only pass. equity $366.96 (next scan in 2 min)
tick #2188  equity $366.96  cash $351.30  open 4
exits-only pass. equity $366.90 (next scan in 1 min)
tick #2189  equity $366.90  cash $351.30  open 4
  scanning chains + news...
  135 raw candidates across 6 chains, 160 headlines/posts
  6 passed gates | rejected: liquidity too thin x74, no h1 volume x35, too old x10, already discovered x8, unknown age x1
  top: mihao 0.76 | WASTED 0.50 | gtacoin 0.48 | Macca 0.38 | Anthropig 0.35
  tick bar 0.64 (top 10% of 6, floor 0.45)
  skip Anthropig: already held
  BUY[exploit] mihao      $5.00 @ $0.01512  score 0.76  bsc  liq $385,546
  shadow: tracking 46, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
