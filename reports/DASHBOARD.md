# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T00:57:23+00:00`

## Equity

| | |
|---|---|
| Equity | **$365.46** |
| Return | **-26.91%** (start $500.00) |
| Cash | $346.93 |
| Deployed | $18.54 (5.1%) |
| Open positions | 3 / 8 |
| Closed trades | 63 (17W / 46L, WR 27%) |
| Profit factor | 0.51 |
| Fees + slippage paid | $53.62 |
| Ticks run | 894 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| STOCK | solana | $5.22 | $6.11 | +18% | +18% | 0.8h |
| PAIDINK | solana | $5.19 | $5.11 | +33% | +61% | 0.4h |
| Murphy | solana | $7.31 | $7.24 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| GAVCOIN | $-7.41 | -100% | 0.4h | stop loss -48% |
| INUINK | $-2.90 | -56% | 0.4h | stop loss -54% |
| Q4 | $-0.65 | -11% | 13.7h | ratchet +0% (peak +48%) |
| ZC | $-7.98 | -100% | 6.0h | stop loss -44% |
| XPAD | $+5.34 | +68% | 2.2h | ratchet +74% (peak +149%) |
| e/acc | $-7.96 | -99% | 2.8h | stop loss -98% |
| QPEPE | $-7.87 | -99% | 0.2h | stop loss -37% |
| x/acc | $-7.90 | -99% | 0.2h | stop loss -98% |
| CATSTR | $-4.68 | -56% | 1.1h | stop loss -55% |
| CatGPT | $-7.26 | -88% | 0.4h | stop loss -87% |
| CAKE | $+11.26 | +196% | 2.5h | ratchet +255% (peak +407%) |
| KUNO | $-4.00 | -49% | 0.2h | stop loss -48% |
| poin | $-8.20 | -99% | 0.3h | stop loss -98% |
| CATSTR | $+1.41 | +17% | 1.2h | ratchet +25% (peak +84%) |
| wiffomo | $-3.84 | -46% | 0.0h | stop loss -45% |

## Learned weights (v12)

_refit on 417 observations (357 shadow, 60 real), 151 winners (36% base rate)_

| Feature | Weight |
|---|---|
| buy_pressure | +0.094 |
| not_vertical | -0.084 |
| momentum_accel | +0.073 |
| turnover | +0.054 |
| fdv_sanity | +0.048 |
| dip_in_uptrend | +0.025 |
| paid_boost | -0.025 |
| buzz | -0.021 |
| liq_quality | +0.017 |
| socials | +0.010 |
| age_sweet | +0.007 |
| txn_depth | +0.007 |

## Last run log
```
tick #894  equity $370.23  cash $354.24  open 3
  SELL GAVCOIN    100% @ $3.951e-05  ->  $0.00   [stop loss -48%]
  scanning chains + news...
  181 raw candidates across 9 chains, 156 headlines/posts
  10 passed gates | rejected: liquidity too thin x93, no h1 volume x60, too old x7, already discovered x6, too new (bot war) x3
  top: Murphy 0.70 | SITRUMP 0.67 | PAIDINK 0.66 | TOBEY 0.57 | INUINK 0.42
  tick bar 0.66 (top 30% of 10, floor 0.45)
  BUY[exploit] Murphy     $7.31 @ $0.0002318  score 0.70  solana  liq $47,422
  shadow: tracking 106, closed 3 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
```
