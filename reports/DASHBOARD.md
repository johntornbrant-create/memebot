# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-28T02:53:34+00:00`

## Equity

| | |
|---|---|
| Equity | **$396.43** |
| Return | **-20.71%** (start $500.00) |
| Cash | $367.86 |
| Deployed | $28.57 (7.2%) |
| Open positions | 4 / 8 |
| Closed trades | 56 (16W / 40L, WR 29%) |
| Profit factor | 0.56 |
| Fees + slippage paid | $35.00 |
| Ticks run | 747 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Q4 | solana | $5.76 | $5.42 | -5% | +4% | 3.8h |
| e/acc | solana | $8.06 | $8.25 | +3% | +30% | 1.0h |
| XPAD | solana | $7.87 | $9.35 | +60% | +60% | 0.5h |
| CASH | bsc | $5.55 | $5.46 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| MDP | $-4.70 | -41% | 10.7h | stop loss -40% |
| JEANCOIN | $-8.71 | -84% | 30.2h | ratchet +767% (peak +1139%) |
| 币安月饼 | $-4.90 | -42% | 2.6h | stop loss -40% |

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
tick #747  equity $392.80  cash $370.34  open 3
  SELL XPAD       25% @ $0.0008403  ->  $3.07   [take profit +50% (sold 25%)]
  scanning chains + news...
  118 raw candidates across 9 chains, 156 headlines/posts
  10 passed gates | rejected: no h1 volume x47, liquidity too thin x43, already discovered x9, too old x5, unknown age x3
  top: XPAD 0.75 | INSTA 0.53 | Q4 0.53 | MT 0.46 | e/acc 0.38
  tick bar 0.53 (top 30% of 10, floor 0.45)
  BUY[explore] CASH       $5.55 @ $7.359e-05  score 0.38  bsc  liq $27,655
  shadow: tracking 101, closed 2 this tick (2 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
```
