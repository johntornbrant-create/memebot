# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-24T18:55:36+00:00`

## Equity

| | |
|---|---|
| Equity | **$484.76** |
| Return | **-3.05%** (start $500.00) |
| Cash | $475.06 |
| Deployed | $9.70 (2.0%) |
| Open positions | 1 / 8 |
| Closed trades | 3 (0W / 3L, WR 0%) |
| Profit factor | 0.46 |
| Fees + slippage paid | $0.40 |
| Ticks run | 1422 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TRUMP | solana | $9.70 | $9.61 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| Leonida | $-6.82 | -99% | 0.5h | stop loss -99% |
| MI | $-3.37 | -48% | 1.0h | stop loss -47% |
| PRIVACY | $-5.06 | -72% | 1.0h | stop loss -71% |
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

## Learned weights (v101)

_refit on 1321 observations (1239 shadow, 82 real), 391 winners (30% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.139 |
| txn_depth | +0.098 |
| buy_pressure | +0.091 |
| not_vertical | -0.086 |
| momentum_accel | +0.070 |
| paid_boost | +0.049 |
| buzz | +0.037 |
| fdv_sanity | +0.031 |
| liq_quality | +0.024 |
| dip_in_uptrend | +0.017 |
| age_sweet | +0.011 |
| socials | -0.003 |

## Last run log
```
tick #1422  equity $484.76  cash $484.76  open 0
  scanning chains + news...
  86 raw candidates across 5 chains, 160 headlines/posts
  8 passed gates | rejected: liquidity too thin x45, no h1 volume x14, already discovered x9, too old x6, unknown age x4
  top: PRIVACY 0.60 | TRUMP 0.45 | GDC 0.34 | 牛币 0.31 | TRUMPE 0.27
  tick bar 0.45 (top 30% of 8, floor 0.45)
  BUY[exploit] TRUMP      $9.70 @ $0.0002547  score 0.45  solana  liq $46,166
  shadow: tracking 35, closed 4 this tick (1 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
