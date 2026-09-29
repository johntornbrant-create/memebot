# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T01:08:42+00:00`

## Equity

| | |
|---|---|
| Equity | **$361.60** |
| Return | **-27.68%** (start $500.00) |
| Cash | $339.84 |
| Deployed | $21.76 (6.0%) |
| Open positions | 3 / 8 |
| Closed trades | 64 (17W / 47L, WR 27%) |
| Profit factor | 0.51 |
| Fees + slippage paid | $53.71 |
| Ticks run | 895 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| STOCK | solana | $5.22 | $7.30 | +41% | +41% | 1.0h |
| SITRUMP | solana | $7.23 | $7.16 | +0% | +0% | 0.0h |
| Murphy | solana | $7.23 | $7.16 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| CATSTR | $+1.41 | +17% | 1.2h | ratchet +25% (peak +84%) |

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
tick #895  equity $366.04  cash $354.24  open 2
  SELL PAIDINK    100% @ $2.587e-06  ->  $0.07   [ratchet +0% (peak +61%)]
  scanning chains + news...
  102 raw candidates across 5 chains, 156 headlines/posts
  9 passed gates | rejected: liquidity too thin x49, no h1 volume x26, too old x8, already discovered x5, too new (bot war) x4
  top: SITRUMP 0.71 | Murphy 0.70 | TOBEY 0.56 | INUINK 0.42 | HOOKEDCAT 0.38
  tick bar 0.70 (top 30% of 9, floor 0.45)
  BUY[exploit] SITRUMP    $7.23 @ $0.0001598  score 0.71  solana  liq $35,211
  BUY[exploit] Murphy     $7.23 @ $0.0002233  score 0.70  solana  liq $46,536
  shadow: tracking 105, closed 4 this tick (1 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
```
