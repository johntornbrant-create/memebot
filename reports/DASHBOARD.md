# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T01:53:08+00:00`

## Equity

| | |
|---|---|
| Equity | **$349.82** |
| Return | **-30.04%** (start $500.00) |
| Cash | $332.78 |
| Deployed | $17.04 (4.9%) |
| Open positions | 3 / 8 |
| Closed trades | 66 (17W / 49L, WR 26%) |
| Profit factor | 0.49 |
| Fees + slippage paid | $53.97 |
| Ticks run | 901 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| STOCK | solana | $5.22 | $6.55 | +27% | +41% | 1.7h |
| SITRUMP | solana | $7.23 | $5.42 | -24% | +4% | 0.7h |
| 鹅次元 | bsc | $7.13 | $5.06 | -28% | +11% | 0.3h |

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
tick #901  equity $355.24  cash $329.22  open 4
  SELL Adventures 100% @ $0.0001408  ->  $3.56   [stop loss -49%]
  scanning chains + news...
  120 raw candidates across 7 chains, 156 headlines/posts
  12 passed gates | rejected: liquidity too thin x47, no h1 volume x35, too old x15, already discovered x11
  top: SNOWBALL 0.76 | PARASITE 0.70 | Adventures 0.53 | SNOWMOON 0.51 | INUINK 0.45
  tick bar 0.53 (top 30% of 12, floor 0.45)
  no entries this tick
  shadow: tracking 101, closed 3 this tick (1 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
  entries blocked: daily loss -6.2% <= -6%; 7d loss -15.8% <= -15%
```
