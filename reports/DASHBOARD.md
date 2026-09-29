# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T02:24:36+00:00`

## Equity

| | |
|---|---|
| Equity | **$362.61** |
| Return | **-27.48%** (start $500.00) |
| Cash | $331.21 |
| Deployed | $31.41 (8.7%) |
| Open positions | 4 / 8 |
| Closed trades | 67 (17W / 50L, WR 25%) |
| Profit factor | 0.49 |
| Fees + slippage paid | $57.28 |
| Ticks run | 905 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| STOCK | solana | $5.22 | $6.75 | +31% | +41% | 2.3h |
| 鹅次元 | bsc | $7.13 | $10.59 | +168% | +168% | 0.8h |
| SNOWBALL | solana | $7.13 | $8.99 | +27% | +27% | 0.3h |
| WOOF | ethereum | $5.08 | $2.04 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| CAKE | $+11.26 | +196% | 2.5h | ratchet +255% (peak +407%) |

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
tick #905  equity $356.46  cash $332.83  open 3
  SELL 鹅次元        25% @ $0.0002312  ->  $3.46   [take profit +150% (sold 25%)]
  scanning chains + news...
  87 raw candidates across 5 chains, 156 headlines/posts
  9 passed gates | rejected: liquidity too thin x46, no h1 volume x28, too old x3, already discovered x1
  top: SNOWBALL 0.71 | PARASITE 0.70 | 鹅次元 0.65 | WOOF 0.61 | INUINK 0.46
  tick bar 0.70 (top 30% of 9, floor 0.45)
  BUY[explore] WOOF       $5.08 @ $0.0005382  score 0.61  ethereum  liq $119,641
  shadow: tracking 101, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
```
