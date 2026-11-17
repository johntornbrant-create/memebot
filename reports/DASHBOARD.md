# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T11:08:37+00:00`

## Equity

| | |
|---|---|
| Equity | **$332.22** |
| Return | **-33.56%** (start $500.00) |
| Cash | $310.07 |
| Deployed | $22.15 (6.7%) |
| Open positions | 5 / 8 |
| Closed trades | 50 (5W / 45L, WR 10%) |
| Profit factor | 0.34 |
| Fees + slippage paid | $89.78 |
| Ticks run | 2629 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $3.60 | -27% | +10% | 12.8h |
| GTA | solana | $5.00 | $5.29 | +7% | +10% | 9.8h |
| LEOSTAR | solana | $5.00 | $6.71 | +36% | +36% | 3.4h |
| GTA6 | ethereum | $5.00 | $2.31 | +17% | +39% | 1.4h |
| BLG Champion | bsc | $5.00 | $4.25 | -13% | +0% | 0.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| ETF | $-2.06 | -41% | 10.2h | stop loss -40% |
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
  top: BLG Champion 0.57 | Rocco 0.49 | GTA 0.45 | Macca 0.39 | BAWSAQ 0.35
  tick bar 0.57 (top 10% of 8, floor 0.45)
  BUY[exploit] BLG Champion $5.00 @ $4.3  score 0.57  bsc  liq $567,505
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $331.22 (-33.76% since start)
tick #2619  equity $331.22  cash $310.07  open 5
exits-only pass. equity $330.52 (next scan in 10 min)
tick #2620  equity $330.52  cash $310.07  open 5
exits-only pass. equity $330.26 (next scan in 9 min)
tick #2621  equity $330.26  cash $310.07  open 5
exits-only pass. equity $330.62 (next scan in 8 min)
tick #2622  equity $330.62  cash $310.07  open 5
exits-only pass. equity $331.06 (next scan in 7 min)
tick #2623  equity $331.06  cash $310.07  open 5
exits-only pass. equity $330.71 (next scan in 6 min)
tick #2624  equity $330.71  cash $310.07  open 5
exits-only pass. equity $330.45 (next scan in 5 min)
tick #2625  equity $330.45  cash $310.07  open 5
exits-only pass. equity $330.24 (next scan in 4 min)
tick #2626  equity $330.24  cash $310.07  open 5
exits-only pass. equity $329.77 (next scan in 3 min)
tick #2627  equity $329.77  cash $310.07  open 5
exits-only pass. equity $330.68 (next scan in 2 min)
tick #2628  equity $330.68  cash $310.07  open 5
exits-only pass. equity $331.86 (next scan in 1 min)
tick #2629  equity $331.86  cash $310.07  open 5
  scanning chains + news...
  112 raw candidates across 7 chains, 159 headlines/posts
  9 passed gates | rejected: liquidity too thin x67, no h1 volume x21, too old x11, already discovered x4
  top: BLG Champion 0.57 | GTA 0.51 | Millionaires 0.43 | BAWSAQ 0.39 | LEOSTAR 0.37
  tick bar 0.57 (top 10% of 9, floor 0.45)
  skip BLG Champion: already held
  no entries this tick
  shadow: tracking 38, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
