# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T21:11:03+00:00`

> 🛑 **HALTED** — KILL SWITCH: equity $317.52 below $325.00. Manual reset required.

## Equity

| | |
|---|---|
| Equity | **$317.52** |
| Return | **-36.50%** (start $500.00) |
| Cash | $311.54 |
| Deployed | $5.98 (1.9%) |
| Open positions | 2 / 8 |
| Closed trades | 53 (5W / 48L, WR 9%) |
| Profit factor | 0.33 |
| Fees + slippage paid | $89.88 |
| Ticks run | 2654 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $3.85 | -22% | +10% | 22.8h |
| GTA6 | ethereum | $5.00 | $2.13 | +9% | +39% | 11.4h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| Macca | $-5.00 | -100% | 26.6h | time stop 27h, only +10% |
| 1.0 | $-5.00 | -100% | 7.8h | stop loss -99% |

## Learned weights (v172)

_refit on 1897 observations (1763 shadow, 134 real), 513 winners (27% base rate)_

| Feature | Weight |
|---|---|
| liq_quality | +0.138 |
| txn_depth | +0.135 |
| turnover | +0.127 |
| momentum_accel | +0.072 |
| buy_pressure | +0.049 |
| fdv_sanity | +0.042 |
| not_vertical | -0.041 |
| buzz | +0.029 |
| paid_boost | +0.028 |
| dip_in_uptrend | +0.027 |
| socials | +0.014 |
| age_sweet | +0.006 |

## Last run log
```
  tick bar 0.68 (top 10% of 5, floor 0.45)
  no entries this tick
  shadow: tracking 36, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $317.42 below $325.00. Manual reset required.
done. equity $317.42 (-36.52% since start)
tick #2644  equity $317.42  cash $311.54  open 2
exits-only pass. equity $317.32 (next scan in 10 min)
tick #2645  equity $317.32  cash $311.54  open 2
exits-only pass. equity $317.32 (next scan in 9 min)
tick #2646  equity $317.32  cash $311.54  open 2
exits-only pass. equity $317.32 (next scan in 8 min)
tick #2647  equity $317.32  cash $311.54  open 2
exits-only pass. equity $317.32 (next scan in 7 min)
tick #2648  equity $317.32  cash $311.54  open 2
exits-only pass. equity $317.51 (next scan in 6 min)
tick #2649  equity $317.51  cash $311.54  open 2
exits-only pass. equity $317.48 (next scan in 5 min)
tick #2650  equity $317.48  cash $311.54  open 2
exits-only pass. equity $317.48 (next scan in 4 min)
tick #2651  equity $317.48  cash $311.54  open 2
exits-only pass. equity $317.61 (next scan in 3 min)
tick #2652  equity $317.61  cash $311.54  open 2
exits-only pass. equity $317.52 (next scan in 2 min)
tick #2653  equity $317.52  cash $311.54  open 2
exits-only pass. equity $317.52 (next scan in 1 min)
tick #2654  equity $317.52  cash $311.54  open 2
  scanning chains + news...
  200 raw candidates across 10 chains, 157 headlines/posts
  4 passed gates | rejected: liquidity too thin x118, no h1 volume x58, too old x8, unknown age x7, already discovered x3
  top: LUNO 0.71 | LUCIASS 0.59 | JALU 0.53 | REFU 0.34
  tick bar 0.68 (top 10% of 4, floor 0.45)
  no entries this tick
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $317.52 below $325.00. Manual reset required.
```
