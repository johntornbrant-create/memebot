# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T03:20:28+00:00`

## Equity

| | |
|---|---|
| Equity | **$350.54** |
| Return | **-29.89%** (start $500.00) |
| Cash | $327.65 |
| Deployed | $22.89 (6.5%) |
| Open positions | 5 / 8 |
| Closed trades | 44 (5W / 39L, WR 11%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $65.25 |
| Ticks run | 2478 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| GTA | solana | $5.00 | $5.53 | +12% | +39% | 20.2h |
| TE | base | $5.00 | $3.75 | -24% | +10% | 5.0h |
| ETF | solana | $5.00 | $4.37 | -12% | +19% | 2.6h |
| GTA | solana | $5.00 | $4.24 | -14% | +1% | 2.0h |
| BAWSAQ | ethereum | $5.00 | $1.96 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| BEAR | $-4.85 | -97% | 1.1h | stop loss -97% |
| GTA | $-0.17 | -3% | 13.4h | ratchet +0% (peak +43%) |

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
  tick bar 0.66 (top 10% of 7, floor 0.45)
  skip HOGE: blacklisted (previously stopped out)
  no entries this tick
  shadow: tracking 34, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $350.02 (-30.00% since start)
tick #2468  equity $350.02  cash $332.65  open 4
exits-only pass. equity $350.09 (next scan in 10 min)
tick #2469  equity $350.09  cash $332.65  open 4
exits-only pass. equity $350.36 (next scan in 9 min)
tick #2470  equity $350.36  cash $332.65  open 4
exits-only pass. equity $350.44 (next scan in 8 min)
tick #2471  equity $350.44  cash $332.65  open 4
exits-only pass. equity $350.55 (next scan in 7 min)
tick #2472  equity $350.55  cash $332.65  open 4
exits-only pass. equity $350.61 (next scan in 6 min)
tick #2473  equity $350.61  cash $332.65  open 4
exits-only pass. equity $350.82 (next scan in 5 min)
tick #2474  equity $350.82  cash $332.65  open 4
exits-only pass. equity $350.61 (next scan in 4 min)
tick #2475  equity $350.61  cash $332.65  open 4
exits-only pass. equity $350.35 (next scan in 3 min)
tick #2476  equity $350.35  cash $332.65  open 4
exits-only pass. equity $350.54 (next scan in 2 min)
tick #2477  equity $350.54  cash $332.65  open 4
exits-only pass. equity $350.66 (next scan in 1 min)
tick #2478  equity $350.66  cash $332.65  open 4
  scanning chains + news...
  193 raw candidates across 8 chains, 159 headlines/posts
  7 passed gates | rejected: liquidity too thin x106, no h1 volume x63, too old x9, unknown age x4, already discovered x4
  top: BAWSAQ 0.83 | HOGE 0.79 | BAWSAQ 0.66 | ETF 0.55 | GTA 0.49
  tick bar 0.66 (top 10% of 7, floor 0.45)
  BUY[exploit] BAWSAQ     $5.00 @ $0.0001262  score 0.83  ethereum  liq $28,521
  skip HOGE: blacklisted (previously stopped out)
  shadow: tracking 35, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
