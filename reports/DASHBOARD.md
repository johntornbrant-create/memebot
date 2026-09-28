# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-28T07:11:56+00:00`

## Equity

| | |
|---|---|
| Equity | **$376.34** |
| Return | **-24.73%** (start $500.00) |
| Cash | $367.81 |
| Deployed | $8.53 (2.3%) |
| Open positions | 2 / 8 |
| Closed trades | 59 (17W / 42L, WR 29%) |
| Profit factor | 0.55 |
| Fees + slippage paid | $44.16 |
| Ticks run | 775 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Q4 | solana | $5.76 | $4.91 | -14% | +10% | 8.1h |
| ZC | ethereum | $7.98 | $3.63 | -26% | +34% | 4.1h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| BRAIN | $-5.41 | -46% | 9.2h | stop loss -45% |

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
tick #775  equity $376.31  cash $367.81  open 2
  scanning chains + news...
  148 raw candidates across 6 chains, 156 headlines/posts
  9 passed gates | rejected: liquidity too thin x100, no h1 volume x30, already discovered x5, too old x2, too new (bot war) x1
  top: LEVERAGE 0.78 | QNTCAT 0.49 | CROCS 0.47 | DELREY 0.46 | INSTA 0.39
  tick bar 0.49 (top 30% of 9, floor 0.45)
  no entries this tick
  shadow: tracking 106, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
  entries blocked: daily loss -9.5% <= -6%
```
