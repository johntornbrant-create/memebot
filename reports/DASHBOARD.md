# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T02:05:29+00:00`

## Equity

| | |
|---|---|
| Equity | **$356.48** |
| Return | **-28.70%** (start $500.00) |
| Cash | $325.65 |
| Deployed | $30.84 (8.7%) |
| Open positions | 4 / 8 |
| Closed trades | 66 (17W / 49L, WR 26%) |
| Profit factor | 0.49 |
| Fees + slippage paid | $54.04 |
| Ticks run | 903 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| STOCK | solana | $5.22 | $6.59 | +28% | +41% | 2.0h |
| SITRUMP | solana | $7.23 | $7.29 | +2% | +4% | 0.9h |
| 鹅次元 | bsc | $7.13 | $9.83 | +40% | +40% | 0.5h |
| SNOWBALL | solana | $7.13 | $7.06 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| KUNO | $-4.00 | -49% | 0.2h | stop loss -48% |

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
tick #903  equity $353.05  cash $332.78  open 3
  scanning chains + news...
  111 raw candidates across 5 chains, 156 headlines/posts
  12 passed gates | rejected: liquidity too thin x63, no h1 volume x23, too old x7, already discovered x6
  top: SNOWBALL 0.75 | PARASITE 0.75 | 鹅次元 0.64 | SNOWMOON 0.60 | Adventures 0.58
  tick bar 0.64 (top 30% of 12, floor 0.45)
  BUY[exploit] SNOWBALL   $7.13 @ $0.0001894  score 0.75  solana  liq $40,471
  shadow: tracking 101, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
```
