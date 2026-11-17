# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T00:32:45+00:00`

## Equity

| | |
|---|---|
| Equity | **$354.65** |
| Return | **-29.07%** (start $500.00) |
| Cash | $336.41 |
| Deployed | $18.25 (5.1%) |
| Open positions | 4 / 8 |
| Closed trades | 41 (4W / 37L, WR 10%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $61.85 |
| Ticks run | 2324 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| WISHMAS | solana | $5.00 | $3.69 | -25% | +5% | 23.9h |
| GTA | solana | $5.00 | $5.25 | +6% | +39% | 17.4h |
| TE | base | $5.00 | $4.16 | -16% | +10% | 2.2h |
| LEOSTAR | solana | $5.00 | $5.15 | +39% | +77% | 1.0h |

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
  tick bar 0.61 (top 10% of 5, floor 0.45)
  skip ETF: solana concentration cap
  no entries this tick
  shadow: tracking 34, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $355.28 (-28.94% since start)
tick #2314  equity $355.28  cash $336.41  open 4
exits-only pass. equity $355.59 (next scan in 10 min)
tick #2315  equity $355.59  cash $336.41  open 4
exits-only pass. equity $355.41 (next scan in 9 min)
tick #2316  equity $355.41  cash $336.41  open 4
exits-only pass. equity $355.67 (next scan in 8 min)
tick #2317  equity $355.67  cash $336.41  open 4
exits-only pass. equity $355.15 (next scan in 7 min)
tick #2318  equity $355.15  cash $336.41  open 4
exits-only pass. equity $355.16 (next scan in 6 min)
tick #2319  equity $355.16  cash $336.41  open 4
exits-only pass. equity $355.32 (next scan in 5 min)
tick #2320  equity $355.32  cash $336.41  open 4
exits-only pass. equity $355.31 (next scan in 4 min)
tick #2321  equity $355.31  cash $336.41  open 4
exits-only pass. equity $355.09 (next scan in 3 min)
tick #2322  equity $355.09  cash $336.41  open 4
exits-only pass. equity $354.47 (next scan in 2 min)
tick #2323  equity $354.47  cash $336.41  open 4
exits-only pass. equity $355.03 (next scan in 1 min)
tick #2324  equity $355.03  cash $336.41  open 4
  scanning chains + news...
  133 raw candidates across 8 chains, 159 headlines/posts
  5 passed gates | rejected: liquidity too thin x82, no h1 volume x27, too old x9, already discovered x7, unknown age x3
  top: COGE 0.64 | MEOWL 0.59 | ETF 0.59 | LEOSTAR 0.44 | BAWSAQ 0.43
  tick bar 0.64 (top 10% of 5, floor 0.45)
  skip COGE: solana concentration cap
  no entries this tick
  shadow: tracking 34, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
