# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-09T06:26:04+00:00`

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
| Ticks run | 1243 |

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

## Learned weights (v44)

_refit on 959 observations (877 shadow, 82 real), 317 winners (33% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.101 |
| buy_pressure | +0.100 |
| not_vertical | -0.085 |
| momentum_accel | +0.058 |
| txn_depth | +0.039 |
| fdv_sanity | +0.022 |
| buzz | -0.020 |
| paid_boost | +0.019 |
| socials | +0.019 |
| dip_in_uptrend | +0.015 |
| age_sweet | -0.005 |
| liq_quality | +0.005 |

## Last run log
```
tick #1243  equity $322.57  cash $322.57  open 0
  scanning chains + news...
  149 raw candidates across 5 chains, 157 headlines/posts
  9 passed gates | rejected: liquidity too thin x110, no h1 volume x19, too old x6, already discovered x5
  top: OctoBul 0.69 | OWLNIGHT 0.63 | ASENSE 0.53 | Gary 0.29 | BNKR 0.22
  tick bar 0.47 (top 30% of 9, floor 0.45)
  no entries this tick
  shadow: tracking 21, closed 6 this tick (3 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
  entries blocked: KILL SWITCH: equity $322.57 below $325.00. Manual reset required.
```
