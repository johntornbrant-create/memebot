# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T16:14:28+00:00`

## Equity

| | |
|---|---|
| Equity | **$497.14** |
| Return | **-0.57%** (start $500.00) |
| Cash | $462.54 |
| Deployed | $34.59 (7.0%) |
| Open positions | 3 / 8 |
| Closed trades | 0 (0W / 0L, WR 0%) |
| Profit factor | – |
| Fees + slippage paid | $1.32 |
| Ticks run | 2 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $12.84 | -12% | +0% | 0.1h |
| CATEWALK | solana | $15.00 | $14.29 | -2% | +0% | 0.1h |
| TRUMPTV | solana | $7.46 | $7.05 | +0% | +0% | 0.0h |

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
  116 raw candidates across 7 chains, 158 headlines/posts
  7 passed gates | rejected: liquidity too thin x48, no h1 volume x32, too old x16, already discovered x12, too few txns x1
  top: LOOONGCAT 0.69 | SATOSHINU 0.65 | KCAT 0.64 | TRUMPTV 0.63 | CATEWALK 0.62
  BUY[explore] TRUMPTV    $7.46 @ $9.657e-05  score 0.63  solana  liq $28,879
  shadow: tracking 7, closed 0 this tick (0 would have won)
```
