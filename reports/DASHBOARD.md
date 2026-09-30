# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-30T22:29:57+00:00`

## Equity

| | |
|---|---|
| Equity | **$345.14** |
| Return | **-30.97%** (start $500.00) |
| Cash | $345.14 |
| Deployed | $-0.00 (-0.0%) |
| Open positions | 0 / 8 |
| Closed trades | 78 (22W / 56L, WR 28%) |
| Profit factor | 0.51 |
| Fees + slippage paid | $67.62 |
| Ticks run | 1167 |

## Open positions

_flat_

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

## Learned weights (v16)

_refit on 664 observations (586 shadow, 78 real), 237 winners (36% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.095 |
| buy_pressure | +0.083 |
| not_vertical | -0.081 |
| paid_boost | -0.051 |
| momentum_accel | +0.045 |
| txn_depth | +0.038 |
| fdv_sanity | +0.036 |
| buzz | -0.035 |
| age_sweet | +0.024 |
| dip_in_uptrend | +0.023 |
| socials | +0.014 |
| liq_quality | +0.004 |

## Last run log
```
tick #1167  equity $345.14  cash $345.14  open 0
  scanning chains + news...
  143 raw candidates across 8 chains, 160 headlines/posts
  5 passed gates | rejected: liquidity too thin x96, no h1 volume x26, too old x7, sell pressure x4, already discovered x3
  top: SAW 0.90 | .si 0.50 | SI 0.46 | SS 0.32 | AIRPAD 0.08
  tick bar 0.58 (top 30% of 5, floor 0.45)
  no entries this tick
  shadow: tracking 79, closed 28 this tick (10 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
  entries blocked: 7d loss -16.9% <= -15%
```
