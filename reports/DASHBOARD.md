# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T17:36:36+00:00`

## Equity

| | |
|---|---|
| Equity | **$494.68** |
| Return | **-1.06%** (start $500.00) |
| Cash | $459.22 |
| Deployed | $35.45 (7.2%) |
| Open positions | 3 / 8 |
| Closed trades | 1 (0W / 1L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $2.10 |
| Ticks run | 8 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $11.68 | -20% | +5% | 1.5h |
| CATEWALK | solana | $15.00 | $13.33 | -8% | +0% | 1.5h |
| BOP | solana | $7.39 | $10.45 | +50% | +50% | 0.2h |

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
tick #8  equity $492.51  cash $459.22  open 3
  scanning chains + news...
  107 raw candidates across 5 chains, 158 headlines/posts
  12 passed gates | rejected: liquidity too thin x70, no h1 volume x9, too old x9, already discovered x6, sell pressure x1
  top: BOP 0.76 | LOOONGCAT 0.71 | CATEWALK 0.70 | JEANPHIL 0.69 | SI 0.64
  no entries this tick
  shadow: tracking 17, closed 0 this tick (0 would have won)
```
