# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-28T01:06:13+00:00`

## Equity

| | |
|---|---|
| Equity | **$414.96** |
| Return | **-17.01%** (start $500.00) |
| Cash | $390.84 |
| Deployed | $24.12 (5.8%) |
| Open positions | 3 / 8 |
| Closed trades | 52 (15W / 37L, WR 29%) |
| Profit factor | 0.56 |
| Fees + slippage paid | $34.39 |
| Ticks run | 734 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| CAKE | solana | $5.74 | $8.72 | +264% | +407% | 2.2h |
| Q4 | solana | $5.76 | $5.54 | -3% | +4% | 2.0h |
| CATSTR | solana | $8.35 | $9.86 | +19% | +19% | 0.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| KUNO | $-4.00 | -49% | 0.2h | stop loss -48% |
| poin | $-8.20 | -99% | 0.3h | stop loss -98% |
| CATSTR | $+1.41 | +17% | 1.2h | ratchet +25% (peak +84%) |
| wiffomo | $-3.84 | -46% | 0.0h | stop loss -45% |
| SJP | $-3.21 | -38% | 1.4h | stop loss -36% |
| CHIPS | $-8.54 | -100% | 0.9h | stop loss -100% |
| ARENA | $+6.10 | +36% | 23.6h | ratchet +56% (peak +123%) |
| BRAIN | $-5.41 | -46% | 9.2h | stop loss -45% |
| MDP | $-4.70 | -41% | 10.7h | stop loss -40% |
| JEANCOIN | $-8.71 | -84% | 30.2h | ratchet +767% (peak +1139%) |
| 币安月饼 | $-4.90 | -42% | 2.6h | stop loss -40% |
| Shurikane | $-6.92 | -41% | 1.8h | stop loss -40% |
| IMU | $+24.04 | +211% | 2.0h | ratchet +391% (peak +602%) |
| COD | $+1.52 | +9% | 2.2h | ratchet +25% (peak +71%) |
| CATALYST | $-1.08 | -10% | 24.2h | time stop 24h, only -9% |

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
tick #734  equity $414.30  cash $390.84  open 3
  scanning chains + news...
  122 raw candidates across 8 chains, 156 headlines/posts
  8 passed gates | rejected: liquidity too thin x65, no h1 volume x45, too old x3, already discovered x1
  top: e/acc 0.61 | CATSTR 0.59 | BOB 0.53 | Q4 0.35 | INSTA 0.33
  tick bar 0.59 (top 30% of 8, floor 0.45)
  no entries this tick
  shadow: tracking 99, closed 2 this tick (2 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
```
