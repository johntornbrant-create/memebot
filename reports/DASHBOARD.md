# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T09:44:37+00:00`

## Equity

| | |
|---|---|
| Equity | **$337.25** |
| Return | **-32.55%** (start $500.00) |
| Cash | $307.32 |
| Deployed | $29.93 (8.9%) |
| Open positions | 7 / 8 |
| Closed trades | 47 (5W / 42L, WR 11%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $80.55 |
| Ticks run | 2552 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $3.62 | -27% | +10% | 11.4h |
| ETF | solana | $5.00 | $4.06 | -18% | +19% | 9.0h |
| GTA | solana | $5.00 | $5.15 | +4% | +10% | 8.4h |
| LEOSTAR | solana | $5.00 | $4.73 | -4% | +3% | 2.0h |
| GTAPEPE | ethereum | $5.00 | $2.93 | +49% | +49% | 1.0h |
| BLG Champion | bsc | $5.00 | $4.44 | -10% | +38% | 0.4h |
| GTA6 | ethereum | $5.00 | $1.96 | +0% | +0% | 0.0h |

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
  top: BLG Champion 0.65 | GTAPEPE 0.60 | GTA 0.52 | Rocco 0.51 | BAWSAQ 0.44
  tick bar 0.65 (top 10% of 9, floor 0.45)
  skip BLG Champion: already held
  no entries this tick
  shadow: tracking 36, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $337.09 (-32.58% since start)
tick #2542  equity $337.09  cash $312.32  open 6
exits-only pass. equity $336.19 (next scan in 10 min)
tick #2543  equity $336.19  cash $312.32  open 6
exits-only pass. equity $336.84 (next scan in 9 min)
tick #2544  equity $336.84  cash $312.32  open 6
exits-only pass. equity $337.40 (next scan in 8 min)
tick #2545  equity $337.40  cash $312.32  open 6
exits-only pass. equity $337.54 (next scan in 7 min)
tick #2546  equity $337.54  cash $312.32  open 6
exits-only pass. equity $337.41 (next scan in 6 min)
tick #2547  equity $337.41  cash $312.32  open 6
exits-only pass. equity $337.13 (next scan in 5 min)
tick #2548  equity $337.13  cash $312.32  open 6
exits-only pass. equity $337.41 (next scan in 4 min)
tick #2549  equity $337.41  cash $312.32  open 6
exits-only pass. equity $337.66 (next scan in 3 min)
tick #2550  equity $337.66  cash $312.32  open 6
exits-only pass. equity $337.38 (next scan in 2 min)
tick #2551  equity $337.38  cash $312.32  open 6
exits-only pass. equity $337.42 (next scan in 1 min)
tick #2552  equity $337.42  cash $312.32  open 6
  scanning chains + news...
  150 raw candidates across 7 chains, 159 headlines/posts
  8 passed gates | rejected: liquidity too thin x88, no h1 volume x31, too old x14, already discovered x8, sell pressure x1
  top: GTA6 0.82 | BLG Champion 0.57 | Rocco 0.54 | GTA 0.54 | BAWSAQ 0.43
  tick bar 0.66 (top 10% of 8, floor 0.45)
  BUY[exploit] GTA6       $5.00 @ $0.0001453  score 0.82  ethereum  liq $30,678
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
