# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T01:08:38+00:00`

## Equity

| | |
|---|---|
| Equity | **$355.33** |
| Return | **-28.93%** (start $500.00) |
| Cash | $330.05 |
| Deployed | $25.28 (7.1%) |
| Open positions | 5 / 8 |
| Closed trades | 42 (4W / 38L, WR 10%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $62.03 |
| Ticks run | 2357 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| GTA | solana | $5.00 | $4.96 | +0% | +39% | 18.0h |
| TE | base | $5.00 | $3.84 | -22% | +10% | 2.8h |
| LEOSTAR | solana | $5.00 | $6.13 | +65% | +77% | 1.6h |
| ETF | solana | $5.00 | $5.34 | +8% | +13% | 0.4h |
| 现货不怕 | bsc | $5.00 | $4.91 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| GTA | $-5.00 | -100% | 1.1h | stop loss -99% |

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
  tick bar 0.66 (top 10% of 3, floor 0.45)
  skip ETF: already held
  no entries this tick
  shadow: tracking 31, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $355.29 (-28.94% since start)
tick #2347  equity $355.29  cash $335.05  open 4
exits-only pass. equity $355.72 (next scan in 10 min)
tick #2348  equity $355.72  cash $335.05  open 4
exits-only pass. equity $355.76 (next scan in 9 min)
tick #2349  equity $355.76  cash $335.05  open 4
exits-only pass. equity $355.36 (next scan in 8 min)
tick #2350  equity $355.36  cash $335.05  open 4
exits-only pass. equity $355.57 (next scan in 7 min)
tick #2351  equity $355.57  cash $335.05  open 4
exits-only pass. equity $355.44 (next scan in 6 min)
tick #2352  equity $355.44  cash $335.05  open 4
exits-only pass. equity $355.37 (next scan in 5 min)
tick #2353  equity $355.37  cash $335.05  open 4
exits-only pass. equity $355.31 (next scan in 4 min)
tick #2354  equity $355.31  cash $335.05  open 4
exits-only pass. equity $355.41 (next scan in 3 min)
tick #2355  equity $355.41  cash $335.05  open 4
exits-only pass. equity $355.81 (next scan in 2 min)
tick #2356  equity $355.81  cash $335.05  open 4
exits-only pass. equity $355.44 (next scan in 1 min)
tick #2357  equity $355.44  cash $335.05  open 4
  scanning chains + news...
  201 raw candidates across 9 chains, 159 headlines/posts
  5 passed gates | rejected: liquidity too thin x103, no h1 volume x62, too old x15, already discovered x10, unknown age x4
  top: ETF 0.78 | 现货不怕 0.75 | LUCIA 0.49 | BAWSAQ 0.47 | LEOSTAR 0.37
  tick bar 0.66 (top 10% of 5, floor 0.45)
  skip ETF: already held
  BUY[exploit] 现货不怕       $5.00 @ $0.0001577  score 0.75  bsc  liq $37,538
  shadow: tracking 33, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
