# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-30T05:41:07+00:00`

## Equity

| | |
|---|---|
| Equity | **$353.42** |
| Return | **-29.32%** (start $500.00) |
| Cash | $336.31 |
| Deployed | $17.11 (4.8%) |
| Open positions | 2 / 8 |
| Closed trades | 76 (21W / 55L, WR 28%) |
| Profit factor | 0.51 |
| Fees + slippage paid | $67.51 |
| Ticks run | 1087 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SS | solana | $7.12 | $10.04 | +90% | +90% | 5.1h |
| NUTFLEX | solana | $7.07 | $7.00 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| INUINK | $-2.90 | -56% | 0.4h | stop loss -54% |

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
tick #1087  equity $352.23  cash $343.38  open 1
  scanning chains + news...
  118 raw candidates across 6 chains, 160 headlines/posts
  12 passed gates | rejected: liquidity too thin x77, no h1 volume x23, sell pressure x2, already discovered x2, too old x1
  top: NUTFLEX 0.52 | RESI 0.41 | POTUS 0.35 | SS 0.35 | PARASITE 0.32
  tick bar 0.45 (top 30% of 12, floor 0.45)
  BUY[exploit] NUTFLEX    $7.07 @ $0.0001809  score 0.52  solana  liq $42,227
  shadow: tracking 112, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
```
