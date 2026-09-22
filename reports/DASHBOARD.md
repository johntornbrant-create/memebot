# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T18:53:44+00:00`

## Equity

| | |
|---|---|
| Equity | **$512.28** |
| Return | **+2.46%** (start $500.00) |
| Cash | $475.85 |
| Deployed | $36.43 (7.1%) |
| Open positions | 3 / 8 |
| Closed trades | 1 (0W / 1L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $2.93 |
| Ticks run | 13 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $11.01 | -24% | +5% | 2.8h |
| CATEWALK | solana | $15.00 | $12.44 | -14% | +0% | 2.8h |
| BOP | solana | $7.39 | $12.97 | +395% | +526% | 1.5h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
tick #13  equity $515.75  cash $475.85  open 3
  scanning chains + news...
  103 raw candidates across 6 chains, 158 headlines/posts
  9 passed gates | rejected: liquidity too thin x49, no h1 volume x30, too old x9, already discovered x5, too new (bot war) x1
  top: CATEWALK 0.80 | LOOONGCAT 0.72 | WCAT 0.70 | SI 0.65 | SATOSHINU 0.64
  no entries this tick
  shadow: tracking 20, closed 0 this tick (0 would have won)
```
