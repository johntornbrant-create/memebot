# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-02T02:35:40+00:00`

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
| Ticks run | 1179 |

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

## Learned weights (v19)

_refit on 770 observations (692 shadow, 78 real), 275 winners (36% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.095 |
| not_vertical | -0.089 |
| buy_pressure | +0.080 |
| txn_depth | +0.060 |
| momentum_accel | +0.049 |
| dip_in_uptrend | +0.036 |
| buzz | -0.024 |
| age_sweet | +0.022 |
| socials | +0.021 |
| paid_boost | -0.015 |
| liq_quality | -0.010 |
| fdv_sanity | +0.009 |

## Last run log
```
tick #1179  equity $345.14  cash $345.14  open 0
  scanning chains + news...
  106 raw candidates across 4 chains, 159 headlines/posts
  12 passed gates | rejected: liquidity too thin x61, no h1 volume x21, too old x6, already discovered x3, sell pressure x2
  top: SACC 0.57 | Jane 0.48 | test 0.44 | e/acc 0.39 | SHIT 0.28
  tick bar 0.45 (top 30% of 12, floor 0.45)
  no entries this tick
  shadow: tracking 33, closed 7 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
  entries blocked: 7d loss -16.9% <= -15%
```
