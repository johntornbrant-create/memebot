# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T08:56:37+00:00`

## Equity

| | |
|---|---|
| Equity | **$339.32** |
| Return | **-32.14%** (start $500.00) |
| Cash | $317.32 |
| Deployed | $22.00 (6.5%) |
| Open positions | 6 / 8 |
| Closed trades | 46 (5W / 41L, WR 11%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $74.43 |
| Ticks run | 2508 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $3.64 | -26% | +10% | 10.6h |
| ETF | solana | $5.00 | $4.01 | -19% | +19% | 8.2h |
| GTA | solana | $5.00 | $5.07 | +2% | +2% | 7.6h |
| LEOSTAR | solana | $5.00 | $4.86 | -2% | +3% | 1.2h |
| KATIA | ethereum | $5.00 | $2.31 | +18% | +18% | 0.8h |
| GTAPEPE | ethereum | $5.00 | $2.11 | +7% | +7% | 0.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| WASTED | $-5.00 | -100% | 1.6h | ratchet +190% (peak +314%) |

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
  tick bar 0.66 (top 10% of 4, floor 0.45)
  skip LEOSTAR: already held
  BUY[exploit] GTAPEPE    $5.00 @ $0.0001172  score 0.68  ethereum  liq $27,406
  shadow: tracking 33, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $341.55 (-31.69% since start)
tick #2498  equity $341.55  cash $317.32  open 6
exits-only pass. equity $338.71 (next scan in 10 min)
tick #2499  equity $338.71  cash $317.32  open 6
exits-only pass. equity $338.27 (next scan in 9 min)
tick #2500  equity $338.27  cash $317.32  open 6
exits-only pass. equity $338.62 (next scan in 8 min)
tick #2501  equity $338.62  cash $317.32  open 6
exits-only pass. equity $338.52 (next scan in 7 min)
tick #2502  equity $338.52  cash $317.32  open 6
exits-only pass. equity $338.53 (next scan in 6 min)
tick #2503  equity $338.53  cash $317.32  open 6
exits-only pass. equity $338.71 (next scan in 5 min)
tick #2504  equity $338.71  cash $317.32  open 6
exits-only pass. equity $338.80 (next scan in 4 min)
tick #2505  equity $338.80  cash $317.32  open 6
exits-only pass. equity $338.64 (next scan in 3 min)
tick #2506  equity $338.64  cash $317.32  open 6
exits-only pass. equity $338.78 (next scan in 2 min)
tick #2507  equity $338.78  cash $317.32  open 6
exits-only pass. equity $338.90 (next scan in 1 min)
tick #2508  equity $338.90  cash $317.32  open 6
  scanning chains + news...
  152 raw candidates across 6 chains, 159 headlines/posts
  6 passed gates | rejected: liquidity too thin x92, no h1 volume x32, too old x16, already discovered x4, too new (bot war) x2
  top: GTAPEPE 0.67 | BLG Champion 0.61 | BAWSAQ 0.60 | GTA 0.58 | HOGE 0.30
  tick bar 0.66 (top 10% of 6, floor 0.45)
  skip GTAPEPE: already held
  no entries this tick
  shadow: tracking 33, closed 1 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
