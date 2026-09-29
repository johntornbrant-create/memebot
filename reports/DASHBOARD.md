# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T01:37:56+00:00`

## Equity

| | |
|---|---|
| Equity | **$356.74** |
| Return | **-28.65%** (start $500.00) |
| Cash | $329.22 |
| Deployed | $27.53 (7.7%) |
| Open positions | 4 / 8 |
| Closed trades | 65 (17W / 48L, WR 26%) |
| Profit factor | 0.50 |
| Fees + slippage paid | $53.93 |
| Ticks run | 899 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| STOCK | solana | $5.22 | $7.06 | +37% | +41% | 1.5h |
| SITRUMP | solana | $7.23 | $6.21 | -13% | +4% | 0.5h |
| 鹅次元 | bsc | $7.13 | $7.03 | +0% | +0% | 0.0h |
| Adventures | solana | $7.13 | $7.06 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| poin | $-8.20 | -99% | 0.3h | stop loss -98% |

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
tick #899  equity $355.81  cash $343.48  open 2
  scanning chains + news...
  123 raw candidates across 6 chains, 156 headlines/posts
  12 passed gates | rejected: liquidity too thin x58, no h1 volume x28, too old x14, already discovered x11
  top: 鹅次元 0.70 | Adventures 0.68 | INUINK 0.51 | SNOWMOON 0.49 | HOOKEDCAT 0.39
  tick bar 0.51 (top 30% of 12, floor 0.45)
  BUY[exploit] 鹅次元        $7.13 @ $8.629e-05  score 0.70  bsc  liq $26,346
  BUY[exploit] Adventures $7.13 @ $0.0002758  score 0.68  solana  liq $52,066
  shadow: tracking 103, closed 6 this tick (2 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
```
