# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T12:56:37+00:00`

> 🛑 **HALTED** — KILL SWITCH: equity $324.37 below $325.00. Manual reset required.

## Equity

| | |
|---|---|
| Equity | **$325.60** |
| Return | **-34.88%** (start $500.00) |
| Cash | $307.99 |
| Deployed | $17.61 (5.4%) |
| Open positions | 4 / 8 |
| Closed trades | 53 (5W / 48L, WR 9%) |
| Profit factor | 0.34 |
| Fees + slippage paid | $96.02 |
| Ticks run | 2728 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $4.03 | -18% | +10% | 14.6h |
| GTA | solana | $5.00 | $6.31 | +28% | +29% | 11.6h |
| LEOSTAR | solana | $5.00 | $5.00 | +35% | +50% | 5.2h |
| GTA6 | ethereum | $5.00 | $2.27 | +16% | +39% | 3.2h |

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
  no entries this tick
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $324.37 below $325.00. Manual reset required.
done. equity $324.37 (-35.13% since start)
tick #2718  equity $324.37  cash $306.16  open 4
exits-only pass. equity $324.93 (next scan in 10 min)
tick #2719  equity $324.93  cash $306.16  open 4
exits-only pass. equity $325.44 (next scan in 9 min)
tick #2720  equity $325.44  cash $306.16  open 4
exits-only pass. equity $324.49 (next scan in 8 min)
tick #2721  equity $324.49  cash $306.16  open 4
exits-only pass. equity $323.94 (next scan in 7 min)
tick #2722  equity $323.94  cash $306.16  open 4
exits-only pass. equity $325.48 (next scan in 6 min)
tick #2723  equity $325.48  cash $306.16  open 4
  SELL LEOSTAR    25% @ $0.00174  ->  $1.82   [take profit +50% (sold 25%)]
exits-only pass. equity $325.98 (next scan in 5 min)
tick #2724  equity $325.98  cash $307.99  open 4
exits-only pass. equity $325.79 (next scan in 4 min)
tick #2725  equity $325.79  cash $307.99  open 4
exits-only pass. equity $325.52 (next scan in 3 min)
tick #2726  equity $325.52  cash $307.99  open 4
exits-only pass. equity $325.48 (next scan in 2 min)
tick #2727  equity $325.48  cash $307.99  open 4
exits-only pass. equity $325.13 (next scan in 1 min)
tick #2728  equity $325.13  cash $307.99  open 4
  scanning chains + news...
  100 raw candidates across 8 chains, 159 headlines/posts
  4 passed gates | rejected: liquidity too thin x63, no h1 volume x27, too old x5, sell pressure x1
  top: LEOSTAR 0.63 | HOGE 0.50 | GROKIA 0.46 | BAWSAQ 0.34
  tick bar 0.63 (top 10% of 4, floor 0.45)
  no entries this tick
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $324.37 below $325.00. Manual reset required.
```
