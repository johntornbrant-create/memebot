# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T10:32:36+00:00`

## Equity

| | |
|---|---|
| Equity | **$332.58** |
| Return | **-33.48%** (start $500.00) |
| Cash | $312.13 |
| Deployed | $20.45 (6.1%) |
| Open positions | 5 / 8 |
| Closed trades | 49 (5W / 44L, WR 10%) |
| Profit factor | 0.34 |
| Fees + slippage paid | $89.65 |
| Ticks run | 2596 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $3.62 | -27% | +10% | 12.2h |
| ETF | solana | $5.00 | $4.24 | -14% | +19% | 9.8h |
| GTA | solana | $5.00 | $5.16 | +4% | +10% | 9.2h |
| LEOSTAR | solana | $5.00 | $4.92 | -0% | +6% | 2.8h |
| GTA6 | ethereum | $5.00 | $2.51 | +28% | +29% | 0.8h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| BLG Champion | $-0.20 | -4% | 1.0h | ratchet +0% (peak +44%) |
| GTAPEPE | $-5.00 | -100% | 1.6h | ratchet +85% (peak +164%) |
| KATIA | $-5.00 | -100% | 1.0h | stop loss -79% |
| BAWSAQ | $-5.00 | -100% | 3.9h | stop loss -99% |
| GTA | $-0.33 | -7% | 24.6h | time stop 25h, only -4% |
| 现货不怕 | $-1.95 | -39% | 1.5h | stop loss -37% |
| LEOSTAR | $+1.63 | +33% | 1.8h | ratchet +25% (peak +77%) |
| WISHMAS | $-1.36 | -27% | 24.0h | time stop 24h, only -25% |
| Trader | $-1.97 | -39% | 3.6h | stop loss -38% |
| Macca | $-5.00 | -100% | 26.6h | time stop 27h, only +10% |
| 1.0 | $-5.00 | -100% | 7.8h | stop loss -99% |
| Anthropig | $-5.00 | -100% | 17.8h | stop loss -100% |
| Marvin | $-2.04 | -41% | 0.8h | stop loss -39% |
| Neil | $-1.94 | -39% | 4.2h | stop loss -37% |
| GTAVI | $-3.57 | -71% | 1.4h | stop loss -70% |

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
  skip GTA6: already held
  no entries this tick
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $332.23 (-33.55% since start)
tick #2586  equity $332.23  cash $312.13  open 5
exits-only pass. equity $332.34 (next scan in 10 min)
tick #2587  equity $332.34  cash $312.13  open 5
exits-only pass. equity $332.11 (next scan in 9 min)
tick #2588  equity $332.11  cash $312.13  open 5
exits-only pass. equity $332.11 (next scan in 8 min)
tick #2589  equity $332.11  cash $312.13  open 5
exits-only pass. equity $332.25 (next scan in 7 min)
tick #2590  equity $332.25  cash $312.13  open 5
exits-only pass. equity $332.15 (next scan in 6 min)
tick #2591  equity $332.15  cash $312.13  open 5
exits-only pass. equity $332.08 (next scan in 5 min)
tick #2592  equity $332.08  cash $312.13  open 5
exits-only pass. equity $331.98 (next scan in 4 min)
tick #2593  equity $331.98  cash $312.13  open 5
exits-only pass. equity $331.99 (next scan in 3 min)
tick #2594  equity $331.99  cash $312.13  open 5
exits-only pass. equity $332.04 (next scan in 2 min)
tick #2595  equity $332.04  cash $312.13  open 5
exits-only pass. equity $332.56 (next scan in 1 min)
tick #2596  equity $332.56  cash $312.13  open 5
  scanning chains + news...
  114 raw candidates across 6 chains, 159 headlines/posts
  9 passed gates | rejected: liquidity too thin x72, no h1 volume x15, too old x13, already discovered x5
  top: GTA6 0.63 | BLG Champion 0.57 | Rocco 0.52 | HOGE 0.49 | GTA 0.47
  tick bar 0.63 (top 10% of 9, floor 0.45)
  skip LEOSTAR: already held
  skip BAWSAQ: solana concentration cap
  no entries this tick
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
