# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T13:35:12+00:00`

> 🛑 **HALTED** — KILL SWITCH: equity $323.80 below $325.00. Manual reset required.

## Equity

| | |
|---|---|
| Equity | **$323.80** |
| Return | **-35.24%** (start $500.00) |
| Cash | $311.54 |
| Deployed | $12.26 (3.8%) |
| Open positions | 3 / 8 |
| Closed trades | 52 (5W / 47L, WR 10%) |
| Profit factor | 0.34 |
| Fees + slippage paid | $89.86 |
| Ticks run | 2630 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $4.03 | -18% | +10% | 15.2h |
| GTA | solana | $5.00 | $5.89 | +19% | +19% | 12.2h |
| GTA6 | ethereum | $5.00 | $2.34 | +19% | +39% | 3.8h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| Anthropig | $-5.00 | -100% | 17.8h | stop loss -100% |

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
tick #2630  equity $332.22  cash $310.07  open 5
  SELL LEOSTAR    100% @ $1.972e-06  ->  $0.00   [stop loss -100%]
  SELL BLG Champion 100% @ $1.34  ->  $1.47   [stop loss -69%]
  scanning chains + news...
  117 raw candidates across 7 chains, 119 headlines/posts
  3 passed gates | rejected: liquidity too thin x82, no h1 volume x23, too old x6, already discovered x3
  top: HOGE 0.65 | GROKIA 0.59 | GTA 0.39
  tick bar 0.65 (top 10% of 3, floor 0.45)
  no entries this tick
  shadow: tracking 36, closed 3 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: KILL SWITCH: equity $323.80 below $325.00. Manual reset required.
```
