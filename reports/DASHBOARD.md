# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-28T04:27:48+00:00`

## Equity

| | |
|---|---|
| Equity | **$388.95** |
| Return | **-22.21%** (start $500.00) |
| Cash | $357.79 |
| Deployed | $31.16 (8.0%) |
| Open positions | 4 / 8 |
| Closed trades | 57 (16W / 41L, WR 28%) |
| Profit factor | 0.54 |
| Fees + slippage paid | $44.04 |
| Ticks run | 757 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Q4 | solana | $5.76 | $5.98 | +5% | +5% | 5.4h |
| e/acc | solana | $8.06 | $7.77 | -3% | +38% | 2.6h |
| XPAD | solana | $7.87 | $12.87 | +120% | +149% | 2.0h |
| ZC | ethereum | $7.98 | $4.54 | -8% | +0% | 1.4h |

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
tick #757  equity $388.59  cash $357.79  open 4
  scanning chains + news...
  90 raw candidates across 7 chains, 156 headlines/posts
  7 passed gates | rejected: liquidity too thin x51, no h1 volume x30, too new (bot war) x1, sell pressure x1
  top: QPEPE 0.42 | MT 0.39 | DELREY 0.39 | XPAD 0.37 | CLAUDECHAN 0.36
  tick bar 0.45 (top 30% of 7, floor 0.45)
  no entries this tick
  shadow: tracking 100, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED Moon       peak +2942%  (scored 0.86)
    MISSED GSTOCK     peak +2491%  (scored 0.88)
  entries blocked: daily loss -6.4% <= -6%
```
