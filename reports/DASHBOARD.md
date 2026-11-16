# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T23:08:29+00:00`

## Equity

| | |
|---|---|
| Equity | **$354.57** |
| Return | **-29.09%** (start $500.00) |
| Cash | $336.30 |
| Deployed | $18.28 (5.2%) |
| Open positions | 4 / 8 |
| Closed trades | 40 (4W / 36L, WR 10%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $61.72 |
| Ticks run | 2247 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| WISHMAS | solana | $5.00 | $3.90 | -21% | +5% | 22.5h |
| GTA | solana | $5.00 | $6.18 | +25% | +39% | 16.0h |
| Trader | solana | $5.00 | $3.45 | -30% | +36% | 3.4h |
| TE | base | $5.00 | $4.74 | -4% | +10% | 0.8h |

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
  tick bar 0.52 (top 10% of 5, floor 0.45)
  skip TE: already held
  no entries this tick
  shadow: tracking 30, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $354.43 (-29.11% since start)
tick #2237  equity $354.43  cash $336.30  open 4
exits-only pass. equity $354.77 (next scan in 10 min)
tick #2238  equity $354.77  cash $336.30  open 4
exits-only pass. equity $354.74 (next scan in 9 min)
tick #2239  equity $354.74  cash $336.30  open 4
exits-only pass. equity $354.80 (next scan in 8 min)
tick #2240  equity $354.80  cash $336.30  open 4
exits-only pass. equity $354.79 (next scan in 7 min)
tick #2241  equity $354.79  cash $336.30  open 4
exits-only pass. equity $354.78 (next scan in 6 min)
tick #2242  equity $354.78  cash $336.30  open 4
exits-only pass. equity $354.77 (next scan in 5 min)
tick #2243  equity $354.77  cash $336.30  open 4
exits-only pass. equity $354.39 (next scan in 4 min)
tick #2244  equity $354.39  cash $336.30  open 4
exits-only pass. equity $354.44 (next scan in 3 min)
tick #2245  equity $354.44  cash $336.30  open 4
exits-only pass. equity $354.71 (next scan in 2 min)
tick #2246  equity $354.71  cash $336.30  open 4
exits-only pass. equity $354.66 (next scan in 1 min)
tick #2247  equity $354.66  cash $336.30  open 4
  scanning chains + news...
  185 raw candidates across 9 chains, 159 headlines/posts
  4 passed gates | rejected: liquidity too thin x118, no h1 volume x49, too old x9, already discovered x5
  top: CHOP 0.49 | COGE 0.48 | BAWSAQ 0.42 | BAWSAQ 0.32
  tick bar 0.49 (top 10% of 4, floor 0.45)
  skip CHOP: solana concentration cap
  no entries this tick
  shadow: tracking 30, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
