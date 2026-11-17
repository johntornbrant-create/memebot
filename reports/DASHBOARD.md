# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T02:20:42+00:00`

## Equity

| | |
|---|---|
| Equity | **$351.86** |
| Return | **-29.63%** (start $500.00) |
| Cash | $329.60 |
| Deployed | $22.26 (6.3%) |
| Open positions | 5 / 8 |
| Closed trades | 43 (5W / 38L, WR 12%) |
| Profit factor | 0.36 |
| Fees + slippage paid | $62.14 |
| Ticks run | 2423 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| GTA | solana | $5.00 | $5.02 | +2% | +39% | 19.2h |
| TE | base | $5.00 | $3.67 | -26% | +10% | 4.0h |
| ETF | solana | $5.00 | $5.87 | +19% | +19% | 1.6h |
| 现货不怕 | bsc | $5.00 | $3.54 | -28% | +0% | 1.2h |
| GTA | solana | $5.00 | $4.16 | -16% | +1% | 1.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| LEOSTAR | $+1.63 | +33% | 1.8h | ratchet +25% (peak +77%) |
| WISHMAS | $-1.36 | -27% | 24.0h | time stop 24h, only -25% |
| Trader | $-1.97 | -39% | 3.6h | stop loss -38% |
| Macca | $-5.00 | -100% | 26.6h | time stop 27h, only +10% |
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
  skip ETF: already held
  no entries this tick
  shadow: tracking 32, closed 3 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $351.92 (-29.62% since start)
tick #2413  equity $351.92  cash $329.60  open 5
exits-only pass. equity $351.84 (next scan in 10 min)
tick #2414  equity $351.84  cash $329.60  open 5
exits-only pass. equity $351.77 (next scan in 9 min)
tick #2415  equity $351.77  cash $329.60  open 5
exits-only pass. equity $351.71 (next scan in 8 min)
tick #2416  equity $351.71  cash $329.60  open 5
exits-only pass. equity $351.50 (next scan in 7 min)
tick #2417  equity $351.50  cash $329.60  open 5
exits-only pass. equity $351.24 (next scan in 6 min)
tick #2418  equity $351.24  cash $329.60  open 5
exits-only pass. equity $351.02 (next scan in 5 min)
tick #2419  equity $351.02  cash $329.60  open 5
exits-only pass. equity $351.09 (next scan in 4 min)
tick #2420  equity $351.09  cash $329.60  open 5
exits-only pass. equity $350.76 (next scan in 3 min)
tick #2421  equity $350.76  cash $329.60  open 5
exits-only pass. equity $350.63 (next scan in 2 min)
tick #2422  equity $350.63  cash $329.60  open 5
exits-only pass. equity $350.68 (next scan in 1 min)
tick #2423  equity $350.68  cash $329.60  open 5
  scanning chains + news...
  115 raw candidates across 7 chains, 159 headlines/posts
  6 passed gates | rejected: liquidity too thin x70, no h1 volume x24, too old x13, already discovered x2
  top: ETF 0.59 | HOGE 0.54 | LEOSTAR 0.51 | BAWSAQ 0.48 | GTA 0.48
  tick bar 0.59 (top 10% of 6, floor 0.45)
  skip ETF: already held
  skip BAWSAQ: solana concentration cap
  no entries this tick
  shadow: tracking 32, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
