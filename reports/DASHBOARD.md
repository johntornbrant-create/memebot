# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T01:56:34+00:00`

## Equity

| | |
|---|---|
| Equity | **$352.02** |
| Return | **-29.60%** (start $500.00) |
| Cash | $329.60 |
| Deployed | $22.42 (6.4%) |
| Open positions | 5 / 8 |
| Closed trades | 43 (5W / 38L, WR 12%) |
| Profit factor | 0.36 |
| Fees + slippage paid | $62.14 |
| Ticks run | 2401 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| GTA | solana | $5.00 | $5.14 | +4% | +39% | 18.8h |
| TE | base | $5.00 | $3.72 | -25% | +10% | 3.6h |
| ETF | solana | $5.00 | $4.83 | -2% | +13% | 1.2h |
| 现货不怕 | bsc | $5.00 | $4.06 | -17% | +0% | 0.8h |
| GTA | solana | $5.00 | $4.67 | -5% | +1% | 0.6h |

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
  tick bar 0.53 (top 10% of 4, floor 0.45)
  skip GTA: already held
  no entries this tick
  shadow: tracking 33, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $351.43 (-29.71% since start)
tick #2391  equity $351.43  cash $329.60  open 5
exits-only pass. equity $351.69 (next scan in 10 min)
tick #2392  equity $351.69  cash $329.60  open 5
exits-only pass. equity $351.89 (next scan in 9 min)
tick #2393  equity $351.89  cash $329.60  open 5
exits-only pass. equity $351.55 (next scan in 8 min)
tick #2394  equity $351.55  cash $329.60  open 5
exits-only pass. equity $351.69 (next scan in 7 min)
tick #2395  equity $351.69  cash $329.60  open 5
exits-only pass. equity $351.60 (next scan in 6 min)
tick #2396  equity $351.60  cash $329.60  open 5
exits-only pass. equity $351.75 (next scan in 5 min)
tick #2397  equity $351.75  cash $329.60  open 5
exits-only pass. equity $352.00 (next scan in 4 min)
tick #2398  equity $352.00  cash $329.60  open 5
exits-only pass. equity $352.14 (next scan in 3 min)
tick #2399  equity $352.14  cash $329.60  open 5
exits-only pass. equity $351.94 (next scan in 2 min)
tick #2400  equity $351.94  cash $329.60  open 5
exits-only pass. equity $351.86 (next scan in 1 min)
tick #2401  equity $351.86  cash $329.60  open 5
  scanning chains + news...
  176 raw candidates across 10 chains, 159 headlines/posts
  5 passed gates | rejected: liquidity too thin x95, no h1 volume x55, too old x13, already discovered x7, unknown age x1
  top: GTA 0.52 | ETF 0.52 | BAWSAQ 0.48 | LEOSTAR 0.41 | COGE 0.37
  tick bar 0.52 (top 10% of 5, floor 0.45)
  skip GTA: already held
  no entries this tick
  shadow: tracking 33, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
