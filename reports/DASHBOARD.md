# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T01:44:33+00:00`

## Equity

| | |
|---|---|
| Equity | **$351.43** |
| Return | **-29.71%** (start $500.00) |
| Cash | $329.60 |
| Deployed | $21.83 (6.2%) |
| Open positions | 5 / 8 |
| Closed trades | 43 (5W / 38L, WR 12%) |
| Profit factor | 0.36 |
| Fees + slippage paid | $62.14 |
| Ticks run | 2390 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| GTA | solana | $5.00 | $4.75 | -4% | +39% | 18.6h |
| TE | base | $5.00 | $3.72 | -25% | +10% | 3.4h |
| ETF | solana | $5.00 | $4.50 | -9% | +13% | 1.0h |
| 现货不怕 | bsc | $5.00 | $4.00 | -19% | +0% | 0.6h |
| GTA | solana | $5.00 | $4.86 | -2% | +1% | 0.4h |

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
  skip BAWSAQ: solana concentration cap
  skip GTA: already held
  no entries this tick
  shadow: tracking 33, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $351.25 (-29.75% since start)
tick #2380  equity $351.25  cash $329.60  open 5
exits-only pass. equity $350.82 (next scan in 10 min)
tick #2381  equity $350.82  cash $329.60  open 5
exits-only pass. equity $351.11 (next scan in 9 min)
tick #2382  equity $351.11  cash $329.60  open 5
exits-only pass. equity $351.53 (next scan in 8 min)
tick #2383  equity $351.53  cash $329.60  open 5
exits-only pass. equity $351.60 (next scan in 7 min)
tick #2384  equity $351.60  cash $329.60  open 5
exits-only pass. equity $351.39 (next scan in 6 min)
tick #2385  equity $351.39  cash $329.60  open 5
exits-only pass. equity $351.23 (next scan in 5 min)
tick #2386  equity $351.23  cash $329.60  open 5
exits-only pass. equity $351.24 (next scan in 4 min)
tick #2387  equity $351.24  cash $329.60  open 5
exits-only pass. equity $351.27 (next scan in 3 min)
tick #2388  equity $351.27  cash $329.60  open 5
exits-only pass. equity $351.15 (next scan in 2 min)
tick #2389  equity $351.15  cash $329.60  open 5
exits-only pass. equity $351.26 (next scan in 1 min)
tick #2390  equity $351.26  cash $329.60  open 5
  scanning chains + news...
  165 raw candidates across 10 chains, 159 headlines/posts
  4 passed gates | rejected: liquidity too thin x88, no h1 volume x52, too old x13, already discovered x7, unknown age x1
  top: GTA 0.53 | ETF 0.52 | BAWSAQ 0.48 | LEOSTAR 0.39
  tick bar 0.53 (top 10% of 4, floor 0.45)
  skip GTA: already held
  no entries this tick
  shadow: tracking 33, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
