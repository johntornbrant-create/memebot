# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-13T18:25:32+00:00`

> 🛑 **HALTED** — KILL SWITCH: equity $322.57 below $325.00. Manual reset required.

## Equity

| | |
|---|---|
| Equity | **$322.57** |
| Return | **-35.49%** (start $500.00) |
| Cash | $322.57 |
| Deployed | $0.00 (0.0%) |
| Open positions | 0 / 8 |
| Closed trades | 82 (22W / 60L, WR 27%) |
| Profit factor | 0.48 |
| Fees + slippage paid | $68.00 |
| Ticks run | 1283 |

## Open positions

_flat_

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| APU | $-3.72 | -57% | 6.8h | stop loss -56% |
| SWAP | $-6.55 | -98% | 6.4h | stop loss -98% |
| TIT | $-5.43 | -80% | 8.5h | stop loss -80% |
| XMAN | $-6.88 | -100% | 7.1h | stop loss -99% |
| SS | $+1.46 | +21% | 9.3h | ratchet +25% (peak +95%) |
| NUTFLEX | $-4.20 | -59% | 1.1h | stop loss -58% |
| FKCANCER | $-2.88 | -41% | 0.8h | stop loss -39% |
| SAI | $-3.50 | -49% | 1.5h | stop loss -48% |
| ARTHUR | $-4.77 | -66% | 0.3h | stop loss -66% |
| WOOF | $-4.47 | -88% | 12.8h | ratchet +222% (peak +360%) |
| STOCK | $+5.89 | +113% | 9.5h | ratchet +120% (peak +214%) |
| SNOWBALL | $-2.98 | -41% | 1.1h | stop loss -40% |
| INKCHAN | $+0.60 | +8% | 1.0h | ratchet +0% (peak +69%) |
| SNOWBALL | $+7.23 | +101% | 0.8h | ratchet +78% (peak +154%) |
| 鹅次元 | $+3.43 | +48% | 0.9h | ratchet +88% (peak +168%) |

## Learned weights (v58)

_refit on 1053 observations (971 shadow, 82 real), 336 winners (32% base rate)_

| Feature | Weight |
|---|---|
| buy_pressure | +0.102 |
| turnover | +0.097 |
| not_vertical | -0.072 |
| momentum_accel | +0.061 |
| txn_depth | +0.059 |
| fdv_sanity | +0.027 |
| paid_boost | +0.018 |
| buzz | +0.015 |
| age_sweet | -0.009 |
| dip_in_uptrend | +0.005 |
| liq_quality | +0.002 |
| socials | +0.001 |

## Last run log
```
tick #1283  equity $322.57  cash $322.57  open 0
  scanning chains + news...
  158 raw candidates across 10 chains, 155 headlines/posts
  8 passed gates | rejected: liquidity too thin x104, no h1 volume x32, too old x10, already discovered x3, unknown age x1
  top: DOPEUS 0.43 | CATGPT 0.43 | LouLou 0.38 | HUMPH 0.28 | BATONA 0.20
  tick bar 0.45 (top 30% of 8, floor 0.45)
  no entries this tick
  shadow: tracking 16, closed 1 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
  entries blocked: KILL SWITCH: equity $322.57 below $325.00. Manual reset required.
```
