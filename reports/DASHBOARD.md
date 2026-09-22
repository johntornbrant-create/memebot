# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T19:22:55+00:00`

## Equity

| | |
|---|---|
| Equity | **$511.54** |
| Return | **+2.31%** (start $500.00) |
| Cash | $468.18 |
| Deployed | $43.36 (8.5%) |
| Open positions | 4 / 8 |
| Closed trades | 1 (0W / 1L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $3.33 |
| Ticks run | 15 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $12.96 | -11% | +5% | 3.3h |
| CATEWALK | solana | $15.00 | $11.76 | -19% | +0% | 3.3h |
| BOP | solana | $7.39 | $10.97 | +319% | +526% | 2.0h |
| Habibi | bsc | $7.67 | $7.27 | +0% | +0% | 0.0h |

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
tick #15  equity $513.94  cash $475.85  open 3
  scanning chains + news...
  104 raw candidates across 7 chains, 158 headlines/posts
  5 passed gates | rejected: liquidity too thin x69, no h1 volume x21, already discovered x4, too new (bot war) x2, too old x2
  top: LOOONGCAT 0.85 | SATOSHINU 0.76 | Habibi 0.74 | CATEWALK 0.72 | WHT  0.59
  BUY[explore] Habibi     $7.67 @ $0.0005059  score 0.74  bsc  liq $40,045
  shadow: tracking 23, closed 0 this tick (0 would have won)
```
