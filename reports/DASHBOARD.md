# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T00:56:41+00:00`

## Equity

| | |
|---|---|
| Equity | **$355.29** |
| Return | **-28.94%** (start $500.00) |
| Cash | $335.05 |
| Deployed | $20.23 (5.7%) |
| Open positions | 4 / 8 |
| Closed trades | 42 (4W / 38L, WR 10%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $61.95 |
| Ticks run | 2346 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| GTA | solana | $5.00 | $5.27 | +7% | +39% | 17.8h |
| TE | base | $5.00 | $3.88 | -21% | +10% | 2.6h |
| LEOSTAR | solana | $5.00 | $5.88 | +59% | +77% | 1.4h |
| ETF | solana | $5.00 | $5.20 | +5% | +12% | 0.2h |

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
  top: ETF 0.59 | BAWSAQ 0.45 | LEOSTAR 0.44 | GTA 0.36
  tick bar 0.59 (top 10% of 4, floor 0.45)
  BUY[exploit] ETF        $5.00 @ $0.0002363  score 0.59  solana  liq $35,513
  shadow: tracking 31, closed 3 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $355.04 (-28.99% since start)
tick #2336  equity $355.04  cash $335.05  open 4
exits-only pass. equity $355.33 (next scan in 10 min)
tick #2337  equity $355.33  cash $335.05  open 4
exits-only pass. equity $355.72 (next scan in 9 min)
tick #2338  equity $355.72  cash $335.05  open 4
exits-only pass. equity $355.54 (next scan in 8 min)
tick #2339  equity $355.54  cash $335.05  open 4
exits-only pass. equity $355.73 (next scan in 7 min)
tick #2340  equity $355.73  cash $335.05  open 4
exits-only pass. equity $355.58 (next scan in 6 min)
tick #2341  equity $355.58  cash $335.05  open 4
exits-only pass. equity $355.68 (next scan in 5 min)
tick #2342  equity $355.68  cash $335.05  open 4
exits-only pass. equity $355.38 (next scan in 4 min)
tick #2343  equity $355.38  cash $335.05  open 4
exits-only pass. equity $355.21 (next scan in 3 min)
tick #2344  equity $355.21  cash $335.05  open 4
exits-only pass. equity $355.41 (next scan in 2 min)
tick #2345  equity $355.41  cash $335.05  open 4
exits-only pass. equity $354.93 (next scan in 1 min)
tick #2346  equity $354.93  cash $335.05  open 4
  scanning chains + news...
  134 raw candidates across 8 chains, 159 headlines/posts
  3 passed gates | rejected: liquidity too thin x85, no h1 volume x30, already discovered x7, too old x6, unknown age x2
  top: ETF 0.77 | BAWSAQ 0.45 | LEOSTAR 0.39
  tick bar 0.66 (top 10% of 3, floor 0.45)
  skip ETF: already held
  no entries this tick
  shadow: tracking 31, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
