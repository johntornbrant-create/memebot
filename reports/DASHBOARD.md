# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-28T09:44:51+00:00`

## Equity

| | |
|---|---|
| Equity | **$373.49** |
| Return | **-25.30%** (start $500.00) |
| Cash | $367.81 |
| Deployed | $5.68 (1.5%) |
| Open positions | 1 / 8 |
| Closed trades | 60 (17W / 43L, WR 28%) |
| Profit factor | 0.53 |
| Fees + slippage paid | $47.18 |
| Ticks run | 791 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Q4 | solana | $5.76 | $5.68 | -0% | +10% | 10.7h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| ARENA | $+6.10 | +36% | 23.6h | ratchet +56% (peak +123%) |

## Learned weights (v11)

_refit on 397 observations (338 shadow, 59 real), 147 winners (37% base rate)_

| Feature | Weight |
|---|---|
| buy_pressure | +0.091 |
| not_vertical | -0.082 |
| momentum_accel | +0.074 |
| fdv_sanity | +0.059 |
| turnover | +0.048 |
| buzz | -0.034 |
| paid_boost | -0.033 |
| dip_in_uptrend | +0.023 |
| liq_quality | +0.022 |
| socials | +0.019 |
| txn_depth | +0.018 |
| age_sweet | +0.005 |

## Last run log
```
tick #791  equity $373.65  cash $367.81  open 1
  scanning chains + news...
  76 raw candidates across 7 chains, 160 headlines/posts
  4 passed gates | rejected: liquidity too thin x48, no h1 volume x22, unknown age x1, too old x1
  top: 中国人飞往火星 0.40 | XPAD 0.33 | INSTA 0.24 | Q4 0.18
  tick bar 0.45 (top 30% of 4, floor 0.45)
  no entries this tick
  shadow: tracking 100, closed 1 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
  entries blocked: daily loss -10.1% <= -6%
```
