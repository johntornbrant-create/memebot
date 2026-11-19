# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-19T12:58:20+00:00`

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
| Ticks run | 3669 |

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
  tick bar 0.69 (top 10% of 11, floor 0.45)
  no entries this tick
  shadow: tracking 44, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $315.19 below $325.00. Manual reset required.
done. equity $315.19 (-36.96% since start)
tick #3659  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 10 min)
tick #3660  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 9 min)
tick #3661  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 8 min)
tick #3662  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 7 min)
tick #3663  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 6 min)
tick #3664  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 5 min)
tick #3665  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 4 min)
tick #3666  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 3 min)
tick #3667  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 2 min)
tick #3668  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 1 min)
tick #3669  equity $315.19  cash $315.19  open 0
  scanning chains + news...
  107 raw candidates across 7 chains, 156 headlines/posts
  9 passed gates | rejected: liquidity too thin x56, no h1 volume x22, too old x13, already discovered x5, unknown age x2
  top: DCTY 0.73 | TAPEX 0.72 | CIHOW 0.63 | Trump 0.61 | 幸运羊  0.57
  tick bar 0.69 (top 10% of 9, floor 0.45)
  no entries this tick
  shadow: tracking 44, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $315.19 below $325.00. Manual reset required.
```
