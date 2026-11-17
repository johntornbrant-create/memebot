# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T10:08:37+00:00`

## Equity

| | |
|---|---|
| Equity | **$337.11** |
| Return | **-32.58%** (start $500.00) |
| Cash | $307.32 |
| Deployed | $29.79 (8.8%) |
| Open positions | 7 / 8 |
| Closed trades | 47 (5W / 42L, WR 11%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $83.56 |
| Ticks run | 2574 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $3.62 | -27% | +10% | 11.8h |
| ETF | solana | $5.00 | $4.19 | -15% | +19% | 9.4h |
| GTA | solana | $5.00 | $4.98 | +1% | +10% | 8.8h |
| LEOSTAR | solana | $5.00 | $5.05 | +2% | +3% | 2.4h |
| GTAPEPE | ethereum | $5.00 | $2.95 | +101% | +113% | 1.4h |
| BLG Champion | bsc | $5.00 | $6.60 | +34% | +44% | 0.8h |
| GTA6 | ethereum | $5.00 | $2.41 | +23% | +23% | 0.4h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| KATIA | $-5.00 | -100% | 1.0h | stop loss -79% |
| BAWSAQ | $-5.00 | -100% | 3.9h | stop loss -99% |
| GTA | $-0.33 | -7% | 24.6h | time stop 25h, only -4% |
| 现货不怕 | $-1.95 | -39% | 1.5h | stop loss -37% |
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
  tick bar 0.66 (top 10% of 9, floor 0.45)
  skip GTA6: already held
  no entries this tick
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $334.86 (-33.03% since start)
tick #2564  equity $334.86  cash $307.32  open 7
exits-only pass. equity $336.54 (next scan in 10 min)
tick #2565  equity $336.54  cash $307.32  open 7
exits-only pass. equity $335.90 (next scan in 9 min)
tick #2566  equity $335.90  cash $307.32  open 7
exits-only pass. equity $335.93 (next scan in 8 min)
tick #2567  equity $335.93  cash $307.32  open 7
exits-only pass. equity $336.04 (next scan in 7 min)
tick #2568  equity $336.04  cash $307.32  open 7
exits-only pass. equity $336.28 (next scan in 6 min)
tick #2569  equity $336.28  cash $307.32  open 7
exits-only pass. equity $336.90 (next scan in 5 min)
tick #2570  equity $336.90  cash $307.32  open 7
exits-only pass. equity $336.27 (next scan in 4 min)
tick #2571  equity $336.27  cash $307.32  open 7
exits-only pass. equity $336.80 (next scan in 3 min)
tick #2572  equity $336.80  cash $307.32  open 7
exits-only pass. equity $336.53 (next scan in 2 min)
tick #2573  equity $336.53  cash $307.32  open 7
exits-only pass. equity $336.86 (next scan in 1 min)
tick #2574  equity $336.86  cash $307.32  open 7
  scanning chains + news...
  117 raw candidates across 6 chains, 159 headlines/posts
  9 passed gates | rejected: liquidity too thin x75, no h1 volume x15, too old x13, already discovered x5
  top: GTA6 0.86 | BLG Champion 0.64 | Rocco 0.52 | HOGE 0.48 | GTA 0.43
  tick bar 0.66 (top 10% of 9, floor 0.45)
  skip GTA6: already held
  no entries this tick
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
