# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T16:12:41+00:00`

## Equity

| | |
|---|---|
| Equity | **$497.73** |
| Return | **-0.45%** (start $500.00) |
| Cash | $462.53 |
| Deployed | $35.19 (7.1%) |
| Open positions | 3 / 8 |
| Closed trades | 0 (0W / 0L, WR 0%) |
| Profit factor | – |
| Fees + slippage paid | $1.32 |
| Ticks run | 2 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $12.92 | -11% | +0% | 0.1h |
| CATEWALK | solana | $15.00 | $14.80 | +2% | +2% | 0.1h |
| TRUMPTV | solana | $7.47 | $7.06 | +0% | +0% | 0.0h |

## Last closed trades

_none yet_

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
tick #2  equity $500.00  cash $470.00  open 2
  scanning chains + news...
  133 raw candidates across 7 chains, 158 headlines/posts
  7 passed gates | rejected: liquidity too thin x73, no h1 volume x23, too old x18, already discovered x11, too few txns x1
  top: CATEWALK 0.70 | LOOONGCAT 0.69 | SATOSHINU 0.65 | KCAT 0.64 | TRUMPTV 0.61
  BUY[explore] TRUMPTV    $7.47 @ $8.953e-05  score 0.61  solana  liq $27,757
  shadow: tracking 7, closed 0 this tick (0 would have won)
```
