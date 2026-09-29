# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T02:38:24+00:00`

## Equity

| | |
|---|---|
| Equity | **$361.96** |
| Return | **-27.61%** (start $500.00) |
| Cash | $335.55 |
| Deployed | $26.42 (7.3%) |
| Open positions | 4 / 8 |
| Closed trades | 68 (18W / 50L, WR 26%) |
| Profit factor | 0.50 |
| Fees + slippage paid | $57.52 |
| Ticks run | 907 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| STOCK | solana | $5.22 | $6.90 | +34% | +41% | 2.5h |
| SNOWBALL | solana | $7.13 | $10.10 | +154% | +154% | 0.5h |
| WOOF | ethereum | $5.08 | $2.18 | +7% | +7% | 0.2h |
| INKCHAN | solana | $7.24 | $7.17 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| 鹅次元 | $+3.43 | +48% | 0.9h | ratchet +88% (peak +168%) |
| SITRUMP | $-3.03 | -42% | 1.1h | stop loss -41% |
| Adventures | $-3.57 | -50% | 0.2h | stop loss -49% |
| Murphy | $-3.60 | -50% | 0.2h | stop loss -49% |
| PAIDINK | $-3.09 | -60% | 0.6h | ratchet +0% (peak +61%) |
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
tick #907  equity $361.08  cash $339.47  open 3
  SELL SNOWBALL   25% @ $0.0004816  ->  $3.32   [take profit +150% (sold 25%)]
  scanning chains + news...
  118 raw candidates across 7 chains, 160 headlines/posts
  8 passed gates | rejected: liquidity too thin x77, no h1 volume x28, too old x3, already discovered x2
  top: SNOWBALL 0.82 | INKCHAN 0.72 | WOOF 0.66 | INUINK 0.46 | SITRUMP 0.42
  tick bar 0.72 (top 30% of 8, floor 0.45)
  BUY[exploit] INKCHAN    $7.24 @ $0.0001569  score 0.72  solana  liq $34,556
  shadow: tracking 101, closed 1 this tick (1 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
```
