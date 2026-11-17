# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T01:20:34+00:00`

## Equity

| | |
|---|---|
| Equity | **$352.19** |
| Return | **-29.56%** (start $500.00) |
| Cash | $329.60 |
| Deployed | $22.58 (6.4%) |
| Open positions | 5 / 8 |
| Closed trades | 43 (5W / 38L, WR 12%) |
| Profit factor | 0.36 |
| Fees + slippage paid | $62.14 |
| Ticks run | 2368 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| GTA | solana | $5.00 | $5.31 | +7% | +39% | 18.2h |
| TE | base | $5.00 | $3.72 | -25% | +10% | 3.0h |
| ETF | solana | $5.00 | $4.63 | -6% | +13% | 0.6h |
| 现货不怕 | bsc | $5.00 | $3.93 | -20% | +0% | 0.2h |
| GTA | solana | $5.00 | $4.94 | +0% | +0% | 0.0h |

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
  skip ETF: already held
  BUY[exploit] 现货不怕       $5.00 @ $0.0001577  score 0.75  bsc  liq $37,538
  shadow: tracking 33, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $355.33 (-28.93% since start)
tick #2358  equity $355.33  cash $330.05  open 5
exits-only pass. equity $354.07 (next scan in 10 min)
tick #2359  equity $354.07  cash $330.05  open 5
exits-only pass. equity $353.72 (next scan in 9 min)
tick #2360  equity $353.72  cash $330.05  open 5
exits-only pass. equity $353.62 (next scan in 8 min)
tick #2361  equity $353.62  cash $330.05  open 5
exits-only pass. equity $353.65 (next scan in 7 min)
tick #2362  equity $353.65  cash $330.05  open 5
exits-only pass. equity $353.19 (next scan in 6 min)
tick #2363  equity $353.19  cash $330.05  open 5
exits-only pass. equity $353.35 (next scan in 5 min)
tick #2364  equity $353.35  cash $330.05  open 5
exits-only pass. equity $352.84 (next scan in 4 min)
tick #2365  equity $352.84  cash $330.05  open 5
exits-only pass. equity $353.05 (next scan in 3 min)
tick #2366  equity $353.05  cash $330.05  open 5
  SELL LEOSTAR    100% @ $0.0008845  ->  $4.55   [ratchet +25% (peak +77%)]
exits-only pass. equity $352.90 (next scan in 2 min)
tick #2367  equity $352.90  cash $334.60  open 4
exits-only pass. equity $352.55 (next scan in 1 min)
tick #2368  equity $352.55  cash $334.60  open 4
  scanning chains + news...
  224 raw candidates across 10 chains, 159 headlines/posts
  4 passed gates | rejected: liquidity too thin x122, no h1 volume x69, too old x13, already discovered x10, unknown age x5
  top: GTA 0.58 | ETF 0.57 | BAWSAQ 0.53 | LEOSTAR 0.37
  tick bar 0.58 (top 10% of 4, floor 0.45)
  BUY[exploit] GTA        $5.00 @ $0.001204  score 0.58  solana  liq $79,450
  skip LEOSTAR: solana concentration cap
  shadow: tracking 33, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
