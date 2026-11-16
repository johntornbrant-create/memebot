# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T22:32:35+00:00`

## Equity

| | |
|---|---|
| Equity | **$357.95** |
| Return | **-28.41%** (start $500.00) |
| Cash | $336.30 |
| Deployed | $21.66 (6.0%) |
| Open positions | 4 / 8 |
| Closed trades | 40 (4W / 36L, WR 10%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $61.72 |
| Ticks run | 2214 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| WISHMAS | solana | $5.00 | $3.72 | -25% | +5% | 21.9h |
| GTA | solana | $5.00 | $6.30 | +27% | +39% | 15.4h |
| Trader | solana | $5.00 | $6.74 | +36% | +36% | 2.8h |
| TE | base | $5.00 | $4.89 | -1% | +0% | 0.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| GTA | $-5.00 | -100% | 1.1h | stop loss -99% |
| LETSWIN | $-5.00 | -100% | 5.6h | stop loss -83% |
| Socks | $+0.41 | +8% | 7.2h | ratchet +42% (peak +103%) |

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
  BUY[exploit] TE         $5.00 @ $0.0002554  score 0.69  base  liq $59,876
  skip BAWSAQ: solana concentration cap
  shadow: tracking 30, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $359.07 (-28.19% since start)
tick #2204  equity $359.07  cash $336.30  open 5
exits-only pass. equity $358.79 (next scan in 10 min)
tick #2205  equity $358.79  cash $336.30  open 5
  SELL Macca      100% @ $0.01631  ->  $0.00   [time stop 27h, only +10%]
exits-only pass. equity $356.28 (next scan in 9 min)
tick #2206  equity $356.28  cash $336.30  open 4
exits-only pass. equity $356.51 (next scan in 8 min)
tick #2207  equity $356.51  cash $336.30  open 4
exits-only pass. equity $357.54 (next scan in 7 min)
tick #2208  equity $357.54  cash $336.30  open 4
exits-only pass. equity $357.10 (next scan in 6 min)
tick #2209  equity $357.10  cash $336.30  open 4
exits-only pass. equity $356.90 (next scan in 5 min)
tick #2210  equity $356.90  cash $336.30  open 4
exits-only pass. equity $356.96 (next scan in 4 min)
tick #2211  equity $356.96  cash $336.30  open 4
exits-only pass. equity $357.01 (next scan in 3 min)
tick #2212  equity $357.01  cash $336.30  open 4
exits-only pass. equity $357.35 (next scan in 2 min)
tick #2213  equity $357.35  cash $336.30  open 4
exits-only pass. equity $357.68 (next scan in 1 min)
tick #2214  equity $357.68  cash $336.30  open 4
  scanning chains + news...
  180 raw candidates across 10 chains, 159 headlines/posts
  4 passed gates | rejected: liquidity too thin x99, no h1 volume x62, too old x9, already discovered x5, unknown age x1
  top: CHOP 0.65 | BAWSAQ 0.50 | BAWSAQ 0.43 | COGE 0.42
  tick bar 0.65 (top 10% of 4, floor 0.45)
  skip CHOP: solana concentration cap
  no entries this tick
  shadow: tracking 30, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
