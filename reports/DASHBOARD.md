# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T23:32:32+00:00`

## Equity

| | |
|---|---|
| Equity | **$353.34** |
| Return | **-29.33%** (start $500.00) |
| Cash | $334.33 |
| Deployed | $19.01 (5.4%) |
| Open positions | 4 / 8 |
| Closed trades | 41 (4W / 37L, WR 10%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $61.81 |
| Ticks run | 2269 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| WISHMAS | solana | $5.00 | $3.58 | -27% | +5% | 22.9h |
| GTA | solana | $5.00 | $6.42 | +30% | +39% | 16.4h |
| TE | base | $5.00 | $4.01 | -19% | +10% | 1.2h |
| LEOSTAR | solana | $5.00 | $4.94 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| GTA | $-5.00 | -100% | 1.1h | stop loss -99% |
| LETSWIN | $-5.00 | -100% | 5.6h | stop loss -83% |

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
  skip CHOP: solana concentration cap
  no entries this tick
  shadow: tracking 31, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $353.80 (-29.24% since start)
tick #2259  equity $353.80  cash $336.30  open 4
exits-only pass. equity $353.59 (next scan in 10 min)
tick #2260  equity $353.59  cash $336.30  open 4
exits-only pass. equity $353.62 (next scan in 9 min)
tick #2261  equity $353.62  cash $336.30  open 4
exits-only pass. equity $353.76 (next scan in 8 min)
tick #2262  equity $353.76  cash $336.30  open 4
exits-only pass. equity $353.35 (next scan in 7 min)
tick #2263  equity $353.35  cash $336.30  open 4
  SELL Trader     100% @ $0.0001271  ->  $3.03   [stop loss -38%]
exits-only pass. equity $353.05 (next scan in 6 min)
tick #2264  equity $353.05  cash $339.33  open 3
exits-only pass. equity $353.04 (next scan in 5 min)
tick #2265  equity $353.04  cash $339.33  open 3
exits-only pass. equity $353.10 (next scan in 4 min)
tick #2266  equity $353.10  cash $339.33  open 3
exits-only pass. equity $353.07 (next scan in 3 min)
tick #2267  equity $353.07  cash $339.33  open 3
exits-only pass. equity $353.14 (next scan in 2 min)
tick #2268  equity $353.14  cash $339.33  open 3
exits-only pass. equity $353.01 (next scan in 1 min)
tick #2269  equity $353.01  cash $339.33  open 3
  scanning chains + news...
  183 raw candidates across 9 chains, 159 headlines/posts
  4 passed gates | rejected: liquidity too thin x115, no h1 volume x51, too old x8, already discovered x5
  top: LEOSTAR 0.71 | COGE 0.49 | BAWSAQ 0.42 | BAWSAQ 0.33
  tick bar 0.66 (top 10% of 4, floor 0.45)
  BUY[exploit] LEOSTAR    $5.00 @ $0.0007127  score 0.71  solana  liq $60,159
  shadow: tracking 32, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
