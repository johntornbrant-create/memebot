# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T08:08:36+00:00`

## Equity

| | |
|---|---|
| Equity | **$343.99** |
| Return | **-31.20%** (start $500.00) |
| Cash | $322.32 |
| Deployed | $21.66 (6.3%) |
| Open positions | 5 / 8 |
| Closed trades | 46 (5W / 41L, WR 11%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $71.40 |
| Ticks run | 2464 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $3.66 | -26% | +10% | 9.8h |
| ETF | solana | $5.00 | $3.87 | -22% | +19% | 7.4h |
| GTA | solana | $5.00 | $4.05 | -18% | +1% | 6.8h |
| LEOSTAR | solana | $5.00 | $5.09 | +3% | +3% | 0.4h |
| KATIA | ethereum | $5.00 | $1.96 | +0% | +0% | 0.0h |

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
  4 passed gates | rejected: liquidity too thin x81, no h1 volume x23, too old x15, already discovered x4, too new (bot war) x2
  top: BAWSAQ 0.44 | LEOSTAR 0.39 | ETF 0.37 | HOGE 0.34
  tick bar 0.45 (top 10% of 4, floor 0.45)
  no entries this tick
  shadow: tracking 32, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $343.70 (-31.26% since start)
tick #2454  equity $343.70  cash $327.32  open 4
exits-only pass. equity $343.58 (next scan in 10 min)
tick #2455  equity $343.58  cash $327.32  open 4
exits-only pass. equity $343.95 (next scan in 9 min)
tick #2456  equity $343.95  cash $327.32  open 4
exits-only pass. equity $344.03 (next scan in 8 min)
tick #2457  equity $344.03  cash $327.32  open 4
exits-only pass. equity $344.17 (next scan in 7 min)
tick #2458  equity $344.17  cash $327.32  open 4
exits-only pass. equity $344.41 (next scan in 6 min)
tick #2459  equity $344.41  cash $327.32  open 4
exits-only pass. equity $344.50 (next scan in 5 min)
tick #2460  equity $344.50  cash $327.32  open 4
exits-only pass. equity $344.46 (next scan in 4 min)
tick #2461  equity $344.46  cash $327.32  open 4
exits-only pass. equity $344.43 (next scan in 3 min)
tick #2462  equity $344.43  cash $327.32  open 4
exits-only pass. equity $344.25 (next scan in 2 min)
tick #2463  equity $344.25  cash $327.32  open 4
exits-only pass. equity $344.13 (next scan in 1 min)
tick #2464  equity $344.13  cash $327.32  open 4
  scanning chains + news...
  154 raw candidates across 6 chains, 159 headlines/posts
  5 passed gates | rejected: liquidity too thin x96, no h1 volume x33, too old x15, already discovered x4, sell pressure x1
  top: KATIA 0.64 | BAWSAQ 0.47 | HOGE 0.34 | ETF 0.33 | LEOSTAR 0.32
  tick bar 0.64 (top 10% of 5, floor 0.45)
  BUY[exploit] KATIA      $5.00 @ $0.0001648  score 0.64  ethereum  liq $32,958
  shadow: tracking 33, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
