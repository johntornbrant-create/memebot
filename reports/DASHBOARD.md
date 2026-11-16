# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T22:56:30+00:00`

## Equity

| | |
|---|---|
| Equity | **$354.43** |
| Return | **-29.11%** (start $500.00) |
| Cash | $336.30 |
| Deployed | $18.13 (5.1%) |
| Open positions | 4 / 8 |
| Closed trades | 40 (4W / 36L, WR 10%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $61.72 |
| Ticks run | 2236 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| WISHMAS | solana | $5.00 | $3.80 | -23% | +5% | 22.3h |
| GTA | solana | $5.00 | $5.91 | +20% | +39% | 15.8h |
| Trader | solana | $5.00 | $3.62 | -27% | +36% | 3.2h |
| TE | base | $5.00 | $4.79 | -3% | +10% | 0.6h |

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
  tick bar 0.52 (top 10% of 4, floor 0.45)
  skip COGE: solana concentration cap
  no entries this tick
  shadow: tracking 30, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $356.71 (-28.66% since start)
tick #2226  equity $356.71  cash $336.30  open 4
exits-only pass. equity $357.13 (next scan in 10 min)
tick #2227  equity $357.13  cash $336.30  open 4
exits-only pass. equity $357.36 (next scan in 9 min)
tick #2228  equity $357.36  cash $336.30  open 4
exits-only pass. equity $357.07 (next scan in 8 min)
tick #2229  equity $357.07  cash $336.30  open 4
exits-only pass. equity $356.23 (next scan in 7 min)
tick #2230  equity $356.23  cash $336.30  open 4
exits-only pass. equity $355.67 (next scan in 6 min)
tick #2231  equity $355.67  cash $336.30  open 4
exits-only pass. equity $354.74 (next scan in 5 min)
tick #2232  equity $354.74  cash $336.30  open 4
exits-only pass. equity $354.65 (next scan in 4 min)
tick #2233  equity $354.65  cash $336.30  open 4
exits-only pass. equity $355.12 (next scan in 3 min)
tick #2234  equity $355.12  cash $336.30  open 4
exits-only pass. equity $355.45 (next scan in 2 min)
tick #2235  equity $355.45  cash $336.30  open 4
exits-only pass. equity $354.68 (next scan in 1 min)
tick #2236  equity $354.68  cash $336.30  open 4
  scanning chains + news...
  170 raw candidates across 10 chains, 159 headlines/posts
  5 passed gates | rejected: liquidity too thin x102, no h1 volume x49, too old x9, already discovered x4, unknown age x1
  top: TE 0.52 | COGE 0.46 | CHOP 0.44 | BAWSAQ 0.39 | BAWSAQ 0.30
  tick bar 0.52 (top 10% of 5, floor 0.45)
  skip TE: already held
  no entries this tick
  shadow: tracking 30, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
