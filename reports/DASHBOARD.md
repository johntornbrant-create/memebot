# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T13:32:36+00:00`

> 🛑 **HALTED** — KILL SWITCH: equity $321.42 below $325.00. Manual reset required.

## Equity

| | |
|---|---|
| Equity | **$321.42** |
| Return | **-35.72%** (start $500.00) |
| Cash | $309.06 |
| Deployed | $12.35 (3.8%) |
| Open positions | 3 / 8 |
| Closed trades | 54 (5W / 49L, WR 9%) |
| Profit factor | 0.34 |
| Fees + slippage paid | $96.05 |
| Ticks run | 2761 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $4.01 | -19% | +10% | 15.2h |
| GTA | solana | $5.00 | $6.00 | +21% | +29% | 12.2h |
| GTA6 | ethereum | $5.00 | $2.34 | +19% | +39% | 3.8h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| LEOSTAR | $-2.10 | -42% | 5.3h | ratchet +25% (peak +85%) |
| BAWSAQ | $-1.98 | -40% | 0.1h | stop loss -38% |
| POPO | $-5.00 | -100% | 0.5h | stop loss -39% |
| BLG Champion | $-1.93 | -39% | 0.2h | stop loss -36% |
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
  tick bar 0.49 (top 10% of 4, floor 0.45)
  no entries this tick
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $321.38 below $325.00. Manual reset required.
done. equity $321.38 (-35.72% since start)
tick #2751  equity $321.38  cash $309.06  open 3
exits-only pass. equity $321.14 (next scan in 10 min)
tick #2752  equity $321.14  cash $309.06  open 3
exits-only pass. equity $321.19 (next scan in 9 min)
tick #2753  equity $321.19  cash $309.06  open 3
exits-only pass. equity $321.23 (next scan in 8 min)
tick #2754  equity $321.23  cash $309.06  open 3
exits-only pass. equity $321.17 (next scan in 7 min)
tick #2755  equity $321.17  cash $309.06  open 3
exits-only pass. equity $321.19 (next scan in 6 min)
tick #2756  equity $321.19  cash $309.06  open 3
exits-only pass. equity $321.22 (next scan in 5 min)
tick #2757  equity $321.22  cash $309.06  open 3
exits-only pass. equity $321.27 (next scan in 4 min)
tick #2758  equity $321.27  cash $309.06  open 3
exits-only pass. equity $321.28 (next scan in 3 min)
tick #2759  equity $321.28  cash $309.06  open 3
exits-only pass. equity $321.34 (next scan in 2 min)
tick #2760  equity $321.34  cash $309.06  open 3
exits-only pass. equity $321.25 (next scan in 1 min)
tick #2761  equity $321.25  cash $309.06  open 3
  scanning chains + news...
  89 raw candidates across 7 chains, 159 headlines/posts
  4 passed gates | rejected: liquidity too thin x62, no h1 volume x16, too old x6, already discovered x1
  top: GROKIA 0.60 | HOGE 0.46 | GTA 0.45 | BAWSAQ 0.39
  tick bar 0.60 (top 10% of 4, floor 0.45)
  no entries this tick
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $321.42 below $325.00. Manual reset required.
```
