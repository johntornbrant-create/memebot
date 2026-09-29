# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T01:25:08+00:00`

## Equity

| | |
|---|---|
| Equity | **$356.61** |
| Return | **-28.68%** (start $500.00) |
| Cash | $343.48 |
| Deployed | $13.13 (3.7%) |
| Open positions | 2 / 8 |
| Closed trades | 65 (17W / 48L, WR 26%) |
| Profit factor | 0.50 |
| Fees + slippage paid | $53.75 |
| Ticks run | 897 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| STOCK | solana | $5.22 | $6.85 | +33% | +41% | 1.3h |
| SITRUMP | solana | $7.23 | $6.28 | -12% | +4% | 0.3h |

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
tick #897  equity $361.33  cash $339.84  open 3
  SELL Murphy     100% @ $0.0001148  ->  $3.63   [stop loss -49%]
  scanning chains + news...
  155 raw candidates across 7 chains, 160 headlines/posts
  12 passed gates | rejected: liquidity too thin x72, no h1 volume x42, too old x13, already discovered x13, too new (bot war) x3
  top: INUINK 0.49 | SNOWBALL 0.39 | SITRUMP 0.35 | SNOWMOON 0.34 | HOOKEDCAT 0.27
  tick bar 0.45 (top 30% of 12, floor 0.45)
  no entries this tick
  shadow: tracking 107, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
```
