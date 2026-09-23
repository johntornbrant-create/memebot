# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T03:25:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$500.34** |
| Return | **+0.07%** (start $500.00) |
| Cash | $472.87 |
| Deployed | $27.47 (5.5%) |
| Open positions | 3 / 8 |
| Closed trades | 10 (3W / 7L, WR 30%) |
| Profit factor | 0.73 |
| Fees + slippage paid | $12.31 |
| Ticks run | 47 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $9.28 | +155% | +163% | 7.0h |
| UPTOBER | solana | $15.04 | $14.93 | +2% | +71% | 3.6h |
| based | solana | $7.48 | $3.26 | -8% | +133% | 1.6h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| SHIELD | $-3.94 | -53% | 0.3h | stop loss -45% |
| ACAT | $-7.53 | -100% | 0.9h | stop loss -100% |
| MORE | $-6.18 | -40% | 1.2h | stop loss -35% |
| Archi | $+0.08 | +1% | 1.9h | stop loss -76% |
| KCAT | $-6.40 | -41% | 1.7h | stop loss -37% |
| Habibi | $+11.26 | +147% | 2.4h | trailing stop from +394% |
| BOP | $+18.46 | +250% | 4.4h | trailing stop from +526% |
| CATEWALK | $-6.25 | -42% | 4.7h | stop loss -37% |
| SATOSHINU | $-7.12 | -47% | 4.3h | stop loss -43% |
| TRUMPTV | $-3.39 | -45% | 1.1h | stop loss -37% |

## Learned weights (v0)

_prior_

| Feature | Weight |
|---|---|
| liq_quality | +0.083 |
| turnover | +0.083 |
| buy_pressure | +0.083 |
| momentum_accel | +0.083 |
| not_vertical | +0.083 |
| age_sweet | +0.083 |
| socials | +0.083 |
| fdv_sanity | +0.083 |
| txn_depth | +0.083 |
| dip_in_uptrend | +0.083 |
| buzz | +0.083 |
| paid_boost | +0.083 |

## Last run log
```
tick #47  equity $503.52  cash $472.87  open 3
  scanning chains + news...
  71 raw candidates across 5 chains, 158 headlines/posts
  9 passed gates | rejected: liquidity too thin x31, no h1 volume x16, too old x8, already discovered x6, too new (bot war) x1
  top: 蝴蝶家园 0.79 | CATEWALK 0.66 | BASEDDOG 0.65 | UPTOBER 0.58 | SATOSHINU 0.57
  no entries this tick
  shadow: tracking 62, closed 0 this tick (0 would have won)
```
