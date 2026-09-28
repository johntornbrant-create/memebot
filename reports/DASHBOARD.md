# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-28T02:05:41+00:00`

## Equity

| | |
|---|---|
| Equity | **$400.27** |
| Return | **-19.95%** (start $500.00) |
| Cash | $378.10 |
| Deployed | $22.17 (5.5%) |
| Open positions | 3 / 8 |
| Closed trades | 55 (16W / 39L, WR 29%) |
| Profit factor | 0.58 |
| Fees + slippage paid | $34.77 |
| Ticks run | 742 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Q4 | solana | $5.76 | $5.12 | -10% | +4% | 3.0h |
| e/acc | solana | $8.06 | $9.04 | +13% | +13% | 0.2h |
| x/acc | solana | $8.01 | $7.93 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| Shurikane | $-6.92 | -41% | 1.8h | stop loss -40% |

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
tick #742  equity $403.43  cash $382.44  open 3
  SELL CATSTR     100% @ $0.0001505  ->  $3.67   [stop loss -55%]
  scanning chains + news...
  105 raw candidates across 6 chains, 156 headlines/posts
  9 passed gates | rejected: liquidity too thin x63, no h1 volume x29, already discovered x2, sell pressure x1, too old x1
  top: e/acc 0.91 | x/acc 0.78 | TOIN 0.76 | INSTA 0.37 | CATSTR 0.32
  tick bar 0.78 (top 30% of 9, floor 0.45)
  BUY[exploit] x/acc      $8.01 @ $0.000153  score 0.78  solana  liq $35,149
  shadow: tracking 100, closed 2 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
```
