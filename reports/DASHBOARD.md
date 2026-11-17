# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T00:20:27+00:00`

## Equity

| | |
|---|---|
| Equity | **$355.28** |
| Return | **-28.94%** (start $500.00) |
| Cash | $336.41 |
| Deployed | $18.87 (5.3%) |
| Open positions | 4 / 8 |
| Closed trades | 41 (4W / 37L, WR 10%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $61.85 |
| Ticks run | 2313 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| WISHMAS | solana | $5.00 | $3.63 | -27% | +5% | 23.7h |
| GTA | solana | $5.00 | $5.70 | +15% | +39% | 17.2h |
| TE | base | $5.00 | $4.17 | -15% | +10% | 2.0h |
| LEOSTAR | solana | $5.00 | $5.37 | +45% | +77% | 0.8h |

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
  tick bar 0.63 (top 10% of 5, floor 0.45)
  skip LEOSTAR: already held
  no entries this tick
  shadow: tracking 34, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $355.33 (-28.93% since start)
tick #2303  equity $355.33  cash $336.41  open 4
exits-only pass. equity $355.49 (next scan in 10 min)
tick #2304  equity $355.49  cash $336.41  open 4
exits-only pass. equity $355.64 (next scan in 9 min)
tick #2305  equity $355.64  cash $336.41  open 4
exits-only pass. equity $355.42 (next scan in 8 min)
tick #2306  equity $355.42  cash $336.41  open 4
exits-only pass. equity $355.51 (next scan in 7 min)
tick #2307  equity $355.51  cash $336.41  open 4
exits-only pass. equity $355.34 (next scan in 6 min)
tick #2308  equity $355.34  cash $336.41  open 4
exits-only pass. equity $355.37 (next scan in 5 min)
tick #2309  equity $355.37  cash $336.41  open 4
exits-only pass. equity $355.75 (next scan in 4 min)
tick #2310  equity $355.75  cash $336.41  open 4
exits-only pass. equity $355.52 (next scan in 3 min)
tick #2311  equity $355.52  cash $336.41  open 4
exits-only pass. equity $355.85 (next scan in 2 min)
tick #2312  equity $355.85  cash $336.41  open 4
exits-only pass. equity $355.59 (next scan in 1 min)
tick #2313  equity $355.59  cash $336.41  open 4
  scanning chains + news...
  212 raw candidates across 11 chains, 159 headlines/posts
  5 passed gates | rejected: liquidity too thin x122, no h1 volume x63, too old x11, already discovered x8, unknown age x3
  top: ETF 0.61 | MEOWL 0.52 | LEOSTAR 0.49 | BAWSAQ 0.44 | COGE 0.42
  tick bar 0.61 (top 10% of 5, floor 0.45)
  skip ETF: solana concentration cap
  no entries this tick
  shadow: tracking 34, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
