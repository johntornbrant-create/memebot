# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-30T00:34:50+00:00`

## Equity

| | |
|---|---|
| Equity | **$356.21** |
| Return | **-28.76%** (start $500.00) |
| Cash | $339.95 |
| Deployed | $16.26 (4.6%) |
| Open positions | 2 / 8 |
| Closed trades | 74 (21W / 53L, WR 28%) |
| Profit factor | 0.52 |
| Fees + slippage paid | $67.24 |
| Ticks run | 1051 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SAI | solana | $7.18 | $9.14 | +29% | +40% | 0.5h |
| SS | solana | $7.12 | $7.05 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| INUINK | $-2.90 | -56% | 0.4h | stop loss -54% |
| Q4 | $-0.65 | -11% | 13.7h | ratchet +0% (peak +48%) |
| ZC | $-7.98 | -100% | 6.0h | stop loss -44% |

## Learned weights (v14)

_refit on 590 observations (517 shadow, 73 real), 210 winners (36% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.089 |
| buy_pressure | +0.074 |
| not_vertical | -0.071 |
| momentum_accel | +0.061 |
| fdv_sanity | +0.053 |
| buzz | -0.048 |
| paid_boost | -0.038 |
| txn_depth | +0.032 |
| liq_quality | +0.021 |
| age_sweet | +0.021 |
| socials | +0.015 |
| dip_in_uptrend | +0.012 |

## Last run log
```
tick #1051  equity $357.01  cash $347.07  open 1
  scanning chains + news...
  105 raw candidates across 6 chains, 160 headlines/posts
  12 passed gates | rejected: liquidity too thin x72, no h1 volume x19, too new (bot war) x1, sell pressure x1
  top: SS 0.86 | SAI 0.74 | ARTHUR 0.67 | FKCANCER 0.67 | BEE 0.52
  tick bar 0.67 (top 30% of 12, floor 0.45)
  BUY[exploit] SS         $7.12 @ $0.0009926  score 0.86  solana  liq $91,232
  shadow: tracking 108, closed 5 this tick (2 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
```
