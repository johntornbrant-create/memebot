# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-21T20:53:13+00:00`

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
| Ticks run | 4300 |

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

## Learned weights (v178)

_refit on 2056 observations (1919 shadow, 137 real), 555 winners (27% base rate)_

| Feature | Weight |
|---|---|
| liq_quality | +0.136 |
| turnover | +0.134 |
| txn_depth | +0.130 |
| momentum_accel | +0.059 |
| not_vertical | -0.052 |
| buy_pressure | +0.052 |
| fdv_sanity | +0.045 |
| dip_in_uptrend | +0.033 |
| socials | +0.025 |
| buzz | +0.024 |
| paid_boost | +0.019 |
| age_sweet | +0.009 |

## Last run log
```
  tick bar 0.49 (top 10% of 4, floor 0.45)
  no entries this tick
  shadow: tracking 25, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $315.19 below $325.00. Manual reset required.
done. equity $315.19 (-36.96% since start)
tick #4290  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 10 min)
tick #4291  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 9 min)
tick #4292  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 8 min)
tick #4293  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 7 min)
tick #4294  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 6 min)
tick #4295  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 5 min)
tick #4296  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 4 min)
tick #4297  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 3 min)
tick #4298  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 2 min)
tick #4299  equity $315.19  cash $315.19  open 0
exits-only pass. equity $315.19 (next scan in 1 min)
tick #4300  equity $315.19  cash $315.19  open 0
  scanning chains + news...
  143 raw candidates across 7 chains, 157 headlines/posts
  4 passed gates | rejected: liquidity too thin x93, no h1 volume x31, too old x9, already discovered x3, too new (bot war) x2
  top: PUNANI 0.44 | chud 0.44 | MAYA 0.39 | HOUSE 0.32
  tick bar 0.45 (top 10% of 4, floor 0.45)
  no entries this tick
  shadow: tracking 23, closed 2 this tick (1 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $315.19 below $325.00. Manual reset required.
```
