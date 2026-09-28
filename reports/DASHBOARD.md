# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-28T06:07:02+00:00`

## Equity

| | |
|---|---|
| Equity | **$377.63** |
| Return | **-24.47%** (start $500.00) |
| Cash | $367.81 |
| Deployed | $9.82 (2.6%) |
| Open positions | 2 / 8 |
| Closed trades | 59 (17W / 42L, WR 29%) |
| Profit factor | 0.55 |
| Fees + slippage paid | $44.16 |
| Ticks run | 769 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Q4 | solana | $5.76 | $5.45 | -4% | +10% | 7.0h |
| ZC | ethereum | $7.98 | $4.37 | -11% | +34% | 3.0h |

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

## Learned weights (v10)

_refit on 364 observations (314 shadow, 50 real), 135 winners (37% base rate)_

| Feature | Weight |
|---|---|
| buy_pressure | +0.123 |
| momentum_accel | +0.088 |
| dip_in_uptrend | +0.075 |
| not_vertical | -0.067 |
| turnover | +0.057 |
| fdv_sanity | +0.051 |
| txn_depth | +0.028 |
| socials | +0.020 |
| buzz | -0.005 |
| paid_boost | -0.003 |
| age_sweet | +0.003 |
| liq_quality | +0.002 |

## Last run log
```
tick #769  equity $377.90  cash $367.81  open 2
  scanning chains + news...
  124 raw candidates across 7 chains, 156 headlines/posts
  9 passed gates | rejected: liquidity too thin x69, no h1 volume x41, already discovered x2, too old x2, too new (bot war) x1
  top: GRAYCAT 0.88 | QCAT 0.67 | NEARCAT 0.65 | GRAYMATTER 0.56 | QNTCAT 0.48
  tick bar 0.67 (top 30% of 9, floor 0.45)
  no entries this tick
  shadow: tracking 107, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
  entries blocked: daily loss -9.1% <= -6%
```
