# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-19T07:34:18+00:00`

> 🛑 **HALTED** — KILL SWITCH: equity $315.19 below $325.00. Manual reset required.

## Equity

| | |
|---|---|
| Equity | **$315.19** |
| Return | **-36.96%** (start $500.00) |
| Cash | $315.19 |
| Deployed | $0.00 (0.0%) |
| Open positions | 0 / 8 |
| Closed trades | 55 (5W / 50L, WR 9%) |
| Profit factor | 0.33 |
| Fees + slippage paid | $95.95 |
| Ticks run | 3372 |

## Open positions

_flat_

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| GTA6 | $-5.00 | -100% | 12.8h | ratchet +0% (peak +62%) |
| TE | $-1.35 | -27% | 24.0h | time stop 24h, only -25% |
| GTA | $-5.00 | -100% | 19.4h | stop loss -100% |
| BLG Champion | $-3.53 | -71% | 2.6h | stop loss -69% |
| LEOSTAR | $-5.00 | -100% | 5.8h | stop loss -100% |
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

## Learned weights (v174)

_refit on 1962 observations (1825 shadow, 137 real), 532 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.152 |
| liq_quality | +0.132 |
| turnover | +0.127 |
| momentum_accel | +0.064 |
| buy_pressure | +0.049 |
| not_vertical | -0.048 |
| fdv_sanity | +0.041 |
| dip_in_uptrend | +0.032 |
| buzz | +0.026 |
| paid_boost | +0.025 |
| socials | +0.019 |
| age_sweet | +0.012 |

## Last run log
```
  tick bar 0.59 (top 10% of 7, floor 0.45)
  no entries this tick
  shadow: tracking 38, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $315.19 below $325.00. Manual reset required.
done. equity $315.19 (-36.96% since start)
tick #3362  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 10 min)
tick #3363  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 9 min)
tick #3364  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 8 min)
tick #3365  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 7 min)
tick #3366  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 6 min)
tick #3367  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 5 min)
tick #3368  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 4 min)
tick #3369  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 3 min)
tick #3370  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 2 min)
tick #3371  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 1 min)
tick #3372  equity $315.19  cash $315.19  open 0
  scanning chains + news...
  101 raw candidates across 8 chains, 157 headlines/posts
  7 passed gates | rejected: liquidity too thin x55, no h1 volume x30, too old x6, unknown age x2, already discovered x1
  top: GTASZN 0.61 | Leonida 0.56 | GRAND 0.55 | GTA6IRL 0.51 | GTA 0.45
  tick bar 0.61 (top 10% of 7, floor 0.45)
  no entries this tick
  shadow: tracking 38, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $315.19 below $325.00. Manual reset required.
```
