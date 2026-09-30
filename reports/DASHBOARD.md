# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-30T08:31:09+00:00`

## Equity

| | |
|---|---|
| Equity | **$346.84** |
| Return | **-30.63%** (start $500.00) |
| Cash | $339.18 |
| Deployed | $7.67 (2.2%) |
| Open positions | 1 / 8 |
| Closed trades | 77 (21W / 56L, WR 27%) |
| Profit factor | 0.51 |
| Fees + slippage paid | $67.55 |
| Ticks run | 1105 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SS | solana | $7.12 | $7.67 | +45% | +95% | 7.9h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| GAVCOIN | $-7.41 | -100% | 0.4h | stop loss -48% |

## Learned weights (v15)

_refit on 613 observations (537 shadow, 76 real), 219 winners (36% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.097 |
| buy_pressure | +0.078 |
| not_vertical | -0.077 |
| paid_boost | -0.060 |
| momentum_accel | +0.053 |
| fdv_sanity | +0.041 |
| txn_depth | +0.038 |
| buzz | -0.035 |
| age_sweet | +0.026 |
| dip_in_uptrend | +0.023 |
| socials | +0.013 |
| liq_quality | +0.008 |

## Last run log
```
tick #1105  equity $346.71  cash $339.18  open 1
  scanning chains + news...
  96 raw candidates across 7 chains, 160 headlines/posts
  7 passed gates | rejected: liquidity too thin x48, no h1 volume x33, already discovered x4, too old x3, sell pressure x1
  top: APE 0.59 | RESI 0.40 | Watermelinu 0.32 | SS 0.28 | AIRPAD 0.26
  tick bar 0.45 (top 30% of 7, floor 0.45)
  no entries this tick
  shadow: tracking 102, closed 1 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
  entries blocked: 7d loss -16.5% <= -15%
```
