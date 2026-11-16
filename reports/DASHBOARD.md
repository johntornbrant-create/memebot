# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T22:08:29+00:00`

## Equity

| | |
|---|---|
| Equity | **$358.87** |
| Return | **-28.23%** (start $500.00) |
| Cash | $341.30 |
| Deployed | $17.57 (4.9%) |
| Open positions | 4 / 8 |
| Closed trades | 39 (4W / 35L, WR 10%) |
| Profit factor | 0.36 |
| Fees + slippage paid | $58.63 |
| Ticks run | 2192 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.22 | +13% | +29% | 26.4h |
| WISHMAS | solana | $5.00 | $3.97 | -20% | +5% | 21.5h |
| GTA | solana | $5.00 | $6.22 | +26% | +39% | 15.0h |
| Trader | solana | $5.00 | $5.17 | +5% | +36% | 2.4h |

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
  skip WIGGLES: solana concentration cap
  skip CHOP: solana concentration cap
  no entries this tick
  shadow: tracking 28, closed 14 this tick (2 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $360.29 (-27.94% since start)
tick #2182  equity $360.29  cash $341.30  open 4
exits-only pass. equity $359.74 (next scan in 10 min)
tick #2183  equity $359.74  cash $341.30  open 4
exits-only pass. equity $359.61 (next scan in 9 min)
tick #2184  equity $359.61  cash $341.30  open 4
exits-only pass. equity $359.52 (next scan in 8 min)
tick #2185  equity $359.52  cash $341.30  open 4
exits-only pass. equity $359.32 (next scan in 7 min)
tick #2186  equity $359.32  cash $341.30  open 4
exits-only pass. equity $358.88 (next scan in 6 min)
tick #2187  equity $358.88  cash $341.30  open 4
exits-only pass. equity $358.78 (next scan in 5 min)
tick #2188  equity $358.78  cash $341.30  open 4
exits-only pass. equity $358.85 (next scan in 4 min)
tick #2189  equity $358.85  cash $341.30  open 4
exits-only pass. equity $358.53 (next scan in 3 min)
tick #2190  equity $358.53  cash $341.30  open 4
exits-only pass. equity $358.56 (next scan in 2 min)
tick #2191  equity $358.56  cash $341.30  open 4
exits-only pass. equity $358.51 (next scan in 1 min)
tick #2192  equity $358.51  cash $341.30  open 4
  scanning chains + news...
  165 raw candidates across 10 chains, 119 headlines/posts
  4 passed gates | rejected: liquidity too thin x92, no h1 volume x54, too old x9, already discovered x5, unknown age x1
  top: CHOP 0.65 | BAWSAQ 0.50 | BAWSAQ 0.49 | COGE 0.45
  tick bar 0.65 (top 10% of 4, floor 0.45)
  skip CHOP: solana concentration cap
  no entries this tick
  shadow: tracking 29, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
