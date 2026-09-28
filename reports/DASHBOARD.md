# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-28T03:55:15+00:00`

## Equity

| | |
|---|---|
| Equity | **$387.73** |
| Return | **-22.45%** (start $500.00) |
| Cash | $357.79 |
| Deployed | $29.95 (7.7%) |
| Open positions | 4 / 8 |
| Closed trades | 57 (16W / 41L, WR 28%) |
| Profit factor | 0.54 |
| Fees + slippage paid | $44.04 |
| Ticks run | 753 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Q4 | solana | $5.76 | $5.74 | +1% | +4% | 4.8h |
| e/acc | solana | $8.06 | $8.13 | +2% | +38% | 2.1h |
| XPAD | solana | $7.87 | $11.74 | +101% | +149% | 1.5h |
| ZC | ethereum | $7.98 | $4.34 | -12% | +0% | 0.8h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| MDP | $-4.70 | -41% | 10.7h | stop loss -40% |
| JEANCOIN | $-8.71 | -84% | 30.2h | ratchet +767% (peak +1139%) |

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
tick #753  equity $394.47  cash $357.72  open 5
  SELL QPEPE      100% @ $9.888e-05  ->  $0.06   [stop loss -37%]
  scanning chains + news...
  134 raw candidates across 9 chains, 156 headlines/posts
  9 passed gates | rejected: liquidity too thin x75, no h1 volume x43, too old x4, too new (bot war) x2, already discovered x1
  top: QPEPE 0.75 | two 0.69 | XPAD 0.54 | Q4 0.52 | MT 0.41
  tick bar 0.69 (top 30% of 9, floor 0.45)
  no entries this tick
  shadow: tracking 99, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
  entries blocked: daily loss -6.7% <= -6%
```
