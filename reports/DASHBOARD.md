# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T12:44:36+00:00`

> 🛑 **HALTED** — KILL SWITCH: equity $324.37 below $325.00. Manual reset required.

## Equity

| | |
|---|---|
| Equity | **$324.37** |
| Return | **-35.13%** (start $500.00) |
| Cash | $306.16 |
| Deployed | $18.21 (5.6%) |
| Open positions | 4 / 8 |
| Closed trades | 53 (5W / 48L, WR 9%) |
| Profit factor | 0.34 |
| Fees + slippage paid | $95.99 |
| Ticks run | 2717 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $3.88 | -21% | +10% | 14.4h |
| GTA | solana | $5.00 | $5.82 | +18% | +26% | 11.4h |
| LEOSTAR | solana | $5.00 | $6.09 | +23% | +36% | 5.0h |
| GTA6 | ethereum | $5.00 | $2.41 | +23% | +39% | 3.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| 1.0 | $-5.00 | -100% | 7.8h | stop loss -99% |

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
  tick bar 0.54 (top 10% of 3, floor 0.45)
  no entries this tick
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $324.09 below $325.00. Manual reset required.
done. equity $324.09 (-35.18% since start)
tick #2707  equity $324.09  cash $306.16  open 4
exits-only pass. equity $324.19 (next scan in 10 min)
tick #2708  equity $324.19  cash $306.16  open 4
exits-only pass. equity $323.85 (next scan in 9 min)
tick #2709  equity $323.85  cash $306.16  open 4
exits-only pass. equity $323.99 (next scan in 8 min)
tick #2710  equity $323.99  cash $306.16  open 4
exits-only pass. equity $324.21 (next scan in 7 min)
tick #2711  equity $324.21  cash $306.16  open 4
exits-only pass. equity $324.10 (next scan in 6 min)
tick #2712  equity $324.10  cash $306.16  open 4
exits-only pass. equity $324.32 (next scan in 5 min)
tick #2713  equity $324.32  cash $306.16  open 4
exits-only pass. equity $324.42 (next scan in 4 min)
tick #2714  equity $324.42  cash $306.16  open 4
exits-only pass. equity $324.49 (next scan in 3 min)
tick #2715  equity $324.49  cash $306.16  open 4
exits-only pass. equity $324.49 (next scan in 2 min)
tick #2716  equity $324.49  cash $306.16  open 4
exits-only pass. equity $324.62 (next scan in 1 min)
tick #2717  equity $324.62  cash $306.16  open 4
  scanning chains + news...
  102 raw candidates across 8 chains, 159 headlines/posts
  4 passed gates | rejected: liquidity too thin x66, no h1 volume x27, too old x4, sell pressure x1
  top: HOGE 0.49 | LEOSTAR 0.39 | GROKIA 0.37 | BAWSAQ 0.31
  tick bar 0.49 (top 10% of 4, floor 0.45)
  no entries this tick
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $324.37 below $325.00. Manual reset required.
```
