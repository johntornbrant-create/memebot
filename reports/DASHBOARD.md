# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-28T02:40:25+00:00`

## Equity

| | |
|---|---|
| Equity | **$392.80** |
| Return | **-21.44%** (start $500.00) |
| Cash | $370.34 |
| Deployed | $22.46 (5.7%) |
| Open positions | 3 / 8 |
| Closed trades | 56 (16W / 40L, WR 29%) |
| Profit factor | 0.56 |
| Fees + slippage paid | $34.87 |
| Ticks run | 746 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Q4 | solana | $5.76 | $5.40 | -5% | +4% | 3.6h |
| e/acc | solana | $8.06 | $8.14 | +2% | +30% | 0.8h |
| XPAD | solana | $7.87 | $8.92 | +14% | +14% | 0.2h |

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
tick #746  equity $391.68  cash $370.34  open 3
  scanning chains + news...
  85 raw candidates across 6 chains, 156 headlines/posts
  9 passed gates | rejected: liquidity too thin x41, no h1 volume x26, too old x5, already discovered x4
  top: XPAD 0.79 | e/acc 0.67 | Q4 0.54 | DELREY 0.41 | INSTA 0.39
  tick bar 0.67 (top 30% of 9, floor 0.45)
  no entries this tick
  shadow: tracking 102, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
```
