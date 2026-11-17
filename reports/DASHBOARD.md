# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T08:32:36+00:00`

## Equity

| | |
|---|---|
| Equity | **$341.37** |
| Return | **-31.73%** (start $500.00) |
| Cash | $322.32 |
| Deployed | $19.05 (5.6%) |
| Open positions | 5 / 8 |
| Closed trades | 46 (5W / 41L, WR 11%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $71.40 |
| Ticks run | 2486 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $3.66 | -26% | +10% | 10.2h |
| ETF | solana | $5.00 | $4.08 | -18% | +19% | 7.8h |
| GTA | solana | $5.00 | $4.54 | -8% | +1% | 7.2h |
| LEOSTAR | solana | $5.00 | $4.76 | -4% | +3% | 0.8h |
| KATIA | ethereum | $5.00 | $2.01 | +3% | +8% | 0.4h |

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
  skip BAWSAQ: solana concentration cap
  skip LEOSTAR: already held
  no entries this tick
  shadow: tracking 32, closed 1 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $341.22 (-31.76% since start)
tick #2476  equity $341.22  cash $322.32  open 5
exits-only pass. equity $341.08 (next scan in 10 min)
tick #2477  equity $341.08  cash $322.32  open 5
exits-only pass. equity $341.38 (next scan in 9 min)
tick #2478  equity $341.38  cash $322.32  open 5
exits-only pass. equity $341.64 (next scan in 8 min)
tick #2479  equity $341.64  cash $322.32  open 5
exits-only pass. equity $341.52 (next scan in 7 min)
tick #2480  equity $341.52  cash $322.32  open 5
exits-only pass. equity $341.54 (next scan in 6 min)
tick #2481  equity $341.54  cash $322.32  open 5
exits-only pass. equity $341.38 (next scan in 5 min)
tick #2482  equity $341.38  cash $322.32  open 5
exits-only pass. equity $341.41 (next scan in 4 min)
tick #2483  equity $341.41  cash $322.32  open 5
exits-only pass. equity $341.66 (next scan in 3 min)
tick #2484  equity $341.66  cash $322.32  open 5
exits-only pass. equity $341.57 (next scan in 2 min)
tick #2485  equity $341.57  cash $322.32  open 5
exits-only pass. equity $341.40 (next scan in 1 min)
tick #2486  equity $341.40  cash $322.32  open 5
  scanning chains + news...
  147 raw candidates across 6 chains, 159 headlines/posts
  4 passed gates | rejected: liquidity too thin x96, no h1 volume x26, too old x16, already discovered x4, sell pressure x1
  top: BAWSAQ 0.61 | KATIA 0.46 | HOGE 0.36 | LEOSTAR 0.22
  tick bar 0.61 (top 10% of 4, floor 0.45)
  skip BAWSAQ: solana concentration cap
  no entries this tick
  shadow: tracking 32, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
