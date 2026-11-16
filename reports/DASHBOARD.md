# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T22:20:33+00:00`

## Equity

| | |
|---|---|
| Equity | **$359.07** |
| Return | **-28.19%** (start $500.00) |
| Cash | $336.30 |
| Deployed | $22.77 (6.3%) |
| Open positions | 5 / 8 |
| Closed trades | 39 (4W / 35L, WR 10%) |
| Profit factor | 0.36 |
| Fees + slippage paid | $58.70 |
| Ticks run | 2203 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.20 | +12% | +29% | 26.6h |
| WISHMAS | solana | $5.00 | $3.92 | -21% | +5% | 21.7h |
| GTA | solana | $5.00 | $6.34 | +28% | +39% | 15.2h |
| Trader | solana | $5.00 | $5.30 | +7% | +36% | 2.6h |
| TE | base | $5.00 | $4.93 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| 1.0 | $-5.00 | -100% | 7.8h | stop loss -99% |
| Anthropig | $-5.00 | -100% | 17.8h | stop loss -100% |
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

## Learned weights (v171)

_refit on 1836 observations (1717 shadow, 119 real), 503 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.143 |
| turnover | +0.120 |
| liq_quality | +0.104 |
| momentum_accel | +0.070 |
| buy_pressure | +0.061 |
| paid_boost | +0.028 |
| not_vertical | -0.028 |
| dip_in_uptrend | +0.027 |
| fdv_sanity | +0.024 |
| buzz | +0.023 |
| age_sweet | +0.013 |
| socials | -0.006 |

## Last run log
```
  tick bar 0.65 (top 10% of 4, floor 0.45)
  skip CHOP: solana concentration cap
  no entries this tick
  shadow: tracking 29, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $358.87 (-28.23% since start)
tick #2193  equity $358.87  cash $341.30  open 4
exits-only pass. equity $358.93 (next scan in 10 min)
tick #2194  equity $358.93  cash $341.30  open 4
exits-only pass. equity $358.73 (next scan in 9 min)
tick #2195  equity $358.73  cash $341.30  open 4
exits-only pass. equity $359.12 (next scan in 8 min)
tick #2196  equity $359.12  cash $341.30  open 4
exits-only pass. equity $358.55 (next scan in 7 min)
tick #2197  equity $358.55  cash $341.30  open 4
exits-only pass. equity $358.90 (next scan in 6 min)
tick #2198  equity $358.90  cash $341.30  open 4
exits-only pass. equity $359.03 (next scan in 5 min)
tick #2199  equity $359.03  cash $341.30  open 4
exits-only pass. equity $359.17 (next scan in 4 min)
tick #2200  equity $359.17  cash $341.30  open 4
exits-only pass. equity $358.81 (next scan in 3 min)
tick #2201  equity $358.81  cash $341.30  open 4
exits-only pass. equity $358.69 (next scan in 2 min)
tick #2202  equity $358.69  cash $341.30  open 4
exits-only pass. equity $358.71 (next scan in 1 min)
tick #2203  equity $358.71  cash $341.30  open 4
  scanning chains + news...
  165 raw candidates across 10 chains, 159 headlines/posts
  5 passed gates | rejected: liquidity too thin x93, no h1 volume x56, too old x9, unknown age x1, already discovered x1
  top: TE 0.69 | CHOP 0.62 | BAWSAQ 0.56 | BAWSAQ 0.42 | COGE 0.42
  tick bar 0.66 (top 10% of 5, floor 0.45)
  BUY[exploit] TE         $5.00 @ $0.0002554  score 0.69  base  liq $59,876
  skip BAWSAQ: solana concentration cap
  shadow: tracking 30, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
