# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T00:32:46+00:00`

## Equity

| | |
|---|---|
| Equity | **$370.49** |
| Return | **-25.90%** (start $500.00) |
| Cash | $352.21 |
| Deployed | $18.29 (4.9%) |
| Open positions | 3 / 8 |
| Closed trades | 62 (17W / 45L, WR 27%) |
| Profit factor | 0.52 |
| Fees + slippage paid | $50.49 |
| Ticks run | 892 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| STOCK | solana | $5.22 | $5.69 | +10% | +10% | 0.4h |
| PAIDINK | solana | $5.19 | $5.13 | +0% | +0% | 0.0h |
| GAVCOIN | ethereum | $7.41 | $4.36 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| SJP | $-3.21 | -38% | 1.4h | stop loss -36% |

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
tick #892  equity $371.76  cash $362.48  open 2
  SELL INUINK     100% @ $0.0006321  ->  $2.32   [stop loss -54%]
  scanning chains + news...
  181 raw candidates across 9 chains, 156 headlines/posts
  12 passed gates | rejected: liquidity too thin x90, no h1 volume x59, already discovered x10, too old x4, too new (bot war) x3
  top: GAVCOIN 0.81 | MARVIN 0.78 | OnlyCats 0.76 | SITRUMP 0.73 | PAIDINK 0.54
  tick bar 0.76 (top 30% of 12, floor 0.45)
  BUY[explore] PAIDINK    $5.19 @ $0.0001121  score 0.54  solana  liq $29,195
  BUY[exploit] GAVCOIN    $7.41 @ $7.57e-05  score 0.81  ethereum  liq $30,630
  shadow: tracking 108, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
```
