# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T23:20:35+00:00`

## Equity

| | |
|---|---|
| Equity | **$353.80** |
| Return | **-29.24%** (start $500.00) |
| Cash | $336.30 |
| Deployed | $17.50 (4.9%) |
| Open positions | 4 / 8 |
| Closed trades | 40 (4W / 36L, WR 10%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $61.72 |
| Ticks run | 2258 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| WISHMAS | solana | $5.00 | $3.70 | -25% | +5% | 22.7h |
| GTA | solana | $5.00 | $6.08 | +23% | +39% | 16.2h |
| Trader | solana | $5.00 | $3.40 | -31% | +36% | 3.6h |
| TE | base | $5.00 | $4.32 | -13% | +10% | 1.0h |

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
  skip CHOP: solana concentration cap
  no entries this tick
  shadow: tracking 30, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $354.57 (-29.09% since start)
tick #2248  equity $354.57  cash $336.30  open 4
exits-only pass. equity $354.39 (next scan in 10 min)
tick #2249  equity $354.39  cash $336.30  open 4
exits-only pass. equity $354.59 (next scan in 9 min)
tick #2250  equity $354.59  cash $336.30  open 4
exits-only pass. equity $354.36 (next scan in 8 min)
tick #2251  equity $354.36  cash $336.30  open 4
exits-only pass. equity $354.00 (next scan in 7 min)
tick #2252  equity $354.00  cash $336.30  open 4
exits-only pass. equity $354.17 (next scan in 6 min)
tick #2253  equity $354.17  cash $336.30  open 4
exits-only pass. equity $354.34 (next scan in 5 min)
tick #2254  equity $354.34  cash $336.30  open 4
exits-only pass. equity $354.52 (next scan in 4 min)
tick #2255  equity $354.52  cash $336.30  open 4
exits-only pass. equity $354.26 (next scan in 3 min)
tick #2256  equity $354.26  cash $336.30  open 4
exits-only pass. equity $354.15 (next scan in 2 min)
tick #2257  equity $354.15  cash $336.30  open 4
exits-only pass. equity $354.24 (next scan in 1 min)
tick #2258  equity $354.24  cash $336.30  open 4
  scanning chains + news...
  194 raw candidates across 9 chains, 159 headlines/posts
  5 passed gates | rejected: liquidity too thin x109, no h1 volume x60, too old x8, already discovered x8, too new (bot war) x2
  top: CHOP 0.47 | COGE 0.46 | BAWSAQ 0.40 | MEOWL 0.37 | BAWSAQ 0.31
  tick bar 0.47 (top 10% of 5, floor 0.45)
  skip BAWSAQ: solana concentration cap
  skip CHOP: solana concentration cap
  no entries this tick
  shadow: tracking 31, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
