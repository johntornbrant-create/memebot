# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T22:22:57+00:00`

> 🛑 **HALTED** — KILL SWITCH: equity $316.90 below $325.00. Manual reset required.

## Equity

| | |
|---|---|
| Equity | **$316.90** |
| Return | **-36.62%** (start $500.00) |
| Cash | $315.19 |
| Deployed | $1.70 (0.5%) |
| Open positions | 1 / 8 |
| Closed trades | 54 (5W / 49L, WR 9%) |
| Profit factor | 0.33 |
| Fees + slippage paid | $92.94 |
| Ticks run | 2720 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| GTA6 | ethereum | $5.00 | $1.70 | +16% | +62% | 12.6h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| Macca | $-5.00 | -100% | 26.6h | time stop 27h, only +10% |

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
  no entries this tick
  shadow: tracking 37, closed 1 this tick (1 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $317.32 below $325.00. Manual reset required.
done. equity $317.32 (-36.54% since start)
tick #2710  equity $317.32  cash $311.54  open 2
exits-only pass. equity $317.30 (next scan in 10 min)
tick #2711  equity $317.30  cash $311.54  open 2
exits-only pass. equity $317.30 (next scan in 9 min)
tick #2712  equity $317.30  cash $311.54  open 2
exits-only pass. equity $317.30 (next scan in 8 min)
tick #2713  equity $317.30  cash $311.54  open 2
exits-only pass. equity $317.30 (next scan in 7 min)
tick #2714  equity $317.30  cash $311.54  open 2
exits-only pass. equity $317.12 (next scan in 6 min)
tick #2715  equity $317.12  cash $311.54  open 2
exits-only pass. equity $317.12 (next scan in 5 min)
tick #2716  equity $317.12  cash $311.54  open 2
exits-only pass. equity $317.11 (next scan in 4 min)
tick #2717  equity $317.11  cash $311.54  open 2
exits-only pass. equity $317.01 (next scan in 3 min)
tick #2718  equity $317.01  cash $311.54  open 2
exits-only pass. equity $317.01 (next scan in 2 min)
tick #2719  equity $317.01  cash $311.54  open 2
  SELL TE         100% @ $0.0001918  ->  $3.65   [time stop 24h, only -25%]
exits-only pass. equity $316.90 (next scan in 1 min)
tick #2720  equity $316.90  cash $315.19  open 1
  scanning chains + news...
  256 raw candidates across 9 chains, 157 headlines/posts
  8 passed gates | rejected: liquidity too thin x139, no h1 volume x63, too old x19, already discovered x19, unknown age x7
  top: WSTAR 0.69 | mihao 0.64 | GROKIA 0.63 | GTAVI 0.59 | LUNO 0.59
  tick bar 0.68 (top 10% of 8, floor 0.45)
  no entries this tick
  shadow: tracking 36, closed 1 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $316.90 below $325.00. Manual reset required.
```
