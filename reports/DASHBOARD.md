# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T00:08:15+00:00`

## Equity

| | |
|---|---|
| Equity | **$372.93** |
| Return | **-25.41%** (start $500.00) |
| Cash | $362.48 |
| Deployed | $10.44 (2.8%) |
| Open positions | 2 / 8 |
| Closed trades | 61 (17W / 44L, WR 28%) |
| Profit factor | 0.53 |
| Fees + slippage paid | $47.35 |
| Ticks run | 890 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| INUINK | solana | $5.22 | $5.16 | +0% | +0% | 0.0h |
| STOCK | solana | $5.22 | $5.16 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| CHIPS | $-8.54 | -100% | 0.9h | stop loss -100% |

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
tick #890  equity $372.93  cash $372.93  open 0
  scanning chains + news...
  102 raw candidates across 8 chains, 156 headlines/posts
  7 passed gates | rejected: liquidity too thin x49, no h1 volume x40, already discovered x4, too old x2
  top: GAVCOIN 0.85 | MARVIN 0.61 | INUINK 0.58 | STOCK 0.44 | Q4 0.39
  tick bar 0.61 (top 30% of 7, floor 0.45)
  BUY[explore] INUINK     $5.22 @ $0.001384  score 0.58  solana  liq $109,871
  BUY[explore] STOCK      $5.22 @ $0.0002387  score 0.44  solana  liq $43,473
  shadow: tracking 104, closed 1 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
```
