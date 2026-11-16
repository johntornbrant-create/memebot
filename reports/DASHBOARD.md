# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T11:09:30+00:00`

## Equity

| | |
|---|---|
| Equity | **$366.34** |
| Return | **-26.73%** (start $500.00) |
| Cash | $354.36 |
| Deployed | $11.98 (3.3%) |
| Open positions | 3 / 8 |
| Closed trades | 39 (4W / 35L, WR 10%) |
| Profit factor | 0.36 |
| Fees + slippage paid | $52.76 |
| Ticks run | 2277 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.41 | +23% | +29% | 15.4h |
| WISHMAS | solana | $5.00 | $4.36 | -12% | +5% | 10.6h |
| GTA | solana | $5.00 | $5.21 | +41% | +51% | 4.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| Anthropig | $-1.85 | -37% | 8.9h | stop loss -35% |
| mihao | $-1.92 | -38% | 1.1h | stop loss -36% |
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
  tick bar 0.64 (top 10% of 5, floor 0.45)
  skip mihao: blacklisted (previously stopped out)
  no entries this tick
  shadow: tracking 45, closed 1 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $366.08 (-26.78% since start)
tick #2267  equity $366.08  cash $354.36  open 3
exits-only pass. equity $366.25 (next scan in 10 min)
tick #2268  equity $366.25  cash $354.36  open 3
exits-only pass. equity $366.22 (next scan in 9 min)
tick #2269  equity $366.22  cash $354.36  open 3
exits-only pass. equity $366.28 (next scan in 8 min)
tick #2270  equity $366.28  cash $354.36  open 3
exits-only pass. equity $366.41 (next scan in 7 min)
tick #2271  equity $366.41  cash $354.36  open 3
exits-only pass. equity $366.39 (next scan in 6 min)
tick #2272  equity $366.39  cash $354.36  open 3
exits-only pass. equity $366.42 (next scan in 5 min)
tick #2273  equity $366.42  cash $354.36  open 3
exits-only pass. equity $366.30 (next scan in 4 min)
tick #2274  equity $366.30  cash $354.36  open 3
exits-only pass. equity $366.43 (next scan in 3 min)
tick #2275  equity $366.43  cash $354.36  open 3
exits-only pass. equity $366.18 (next scan in 2 min)
tick #2276  equity $366.18  cash $354.36  open 3
exits-only pass. equity $366.27 (next scan in 1 min)
tick #2277  equity $366.27  cash $354.36  open 3
  scanning chains + news...
  126 raw candidates across 6 chains, 160 headlines/posts
  5 passed gates | rejected: liquidity too thin x78, no h1 volume x36, too old x3, already discovered x3, unknown age x1
  top: mihao 0.76 | gtacoin 0.47 | 1.0 0.42 | GTA 0.41 | Anthropig 0.33
  tick bar 0.64 (top 10% of 5, floor 0.45)
  skip mihao: blacklisted (previously stopped out)
  no entries this tick
  shadow: tracking 45, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
