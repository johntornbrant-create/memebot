# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-05T05:33:41+00:00`

## Equity

| | |
|---|---|
| Equity | **$345.14** |
| Return | **-30.97%** (start $500.00) |
| Cash | $338.24 |
| Deployed | $6.90 (2.0%) |
| Open positions | 1 / 8 |
| Closed trades | 78 (22W / 56L, WR 28%) |
| Profit factor | 0.51 |
| Fees + slippage paid | $67.69 |
| Ticks run | 1210 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| XMAN | solana | $6.90 | $6.83 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| SITRUMP | $-3.03 | -42% | 1.1h | stop loss -41% |
| Adventures | $-3.57 | -50% | 0.2h | stop loss -49% |
| Murphy | $-3.60 | -50% | 0.2h | stop loss -49% |
| PAIDINK | $-3.09 | -60% | 0.6h | ratchet +0% (peak +61%) |

## Learned weights (v32)

_refit on 854 observations (776 shadow, 78 real), 293 winners (34% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.101 |
| buy_pressure | +0.087 |
| not_vertical | -0.077 |
| momentum_accel | +0.043 |
| txn_depth | +0.043 |
| buzz | -0.036 |
| dip_in_uptrend | +0.032 |
| fdv_sanity | +0.023 |
| socials | +0.021 |
| liq_quality | -0.015 |
| paid_boost | -0.004 |
| age_sweet | -0.002 |

## Last run log
```
tick #1210  equity $345.14  cash $345.14  open 0
  scanning chains + news...
  178 raw candidates across 9 chains, 159 headlines/posts
  18 passed gates | rejected: liquidity too thin x106, no h1 volume x41, too old x9, too new (bot war) x2, sell pressure x1
  top: XMAN 0.63 | AGENTCAT 0.42 | HIGGS 0.38 | Gizmo 0.36 | MEMEAGENCY 0.33
  tick bar 0.45 (top 30% of 18, floor 0.45)
  BUY[exploit] XMAN       $6.90 @ $0.0004882  score 0.63  solana  liq $65,155
  shadow: tracking 35, closed 5 this tick (1 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
