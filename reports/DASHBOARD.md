# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-28T01:51:49+00:00`

## Equity

| | |
|---|---|
| Equity | **$403.21** |
| Return | **-19.36%** (start $500.00) |
| Cash | $382.44 |
| Deployed | $20.78 (5.2%) |
| Open positions | 3 / 8 |
| Closed trades | 54 (16W / 38L, WR 30%) |
| Profit factor | 0.59 |
| Fees + slippage paid | $34.65 |
| Ticks run | 740 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Q4 | solana | $5.76 | $4.98 | -13% | +4% | 2.8h |
| CATSTR | solana | $8.35 | $7.73 | -6% | +25% | 0.9h |
| e/acc | solana | $8.06 | $7.98 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| Shurikane | $-6.92 | -41% | 1.8h | stop loss -40% |
| IMU | $+24.04 | +211% | 2.0h | ratchet +391% (peak +602%) |

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
tick #740  equity $403.24  cash $390.50  open 2
  scanning chains + news...
  111 raw candidates across 6 chains, 156 headlines/posts
  12 passed gates | rejected: liquidity too thin x61, no h1 volume x34, too old x3, already discovered x1
  top: e/acc 0.87 | TOIN 0.83 | OMNINU 0.80 | x/acc 0.79 | SUPERCAPY 0.76
  tick bar 0.80 (top 30% of 12, floor 0.45)
  BUY[exploit] e/acc      $8.06 @ $0.0001533  score 0.87  solana  liq $34,533
  shadow: tracking 102, closed 2 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
```
