# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T18:42:24+00:00`

## Equity

| | |
|---|---|
| Equity | **$515.75** |
| Return | **+3.15%** (start $500.00) |
| Cash | $475.85 |
| Deployed | $39.89 (7.7%) |
| Open positions | 3 / 8 |
| Closed trades | 1 (0W / 1L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $2.93 |
| Ticks run | 12 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $10.28 | -29% | +5% | 2.6h |
| CATEWALK | solana | $15.00 | $14.20 | -2% | +0% | 2.6h |
| BOP | solana | $7.39 | $15.42 | +489% | +526% | 1.3h |

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
tick #12  equity $514.98  cash $475.85  open 3
  scanning chains + news...
  79 raw candidates across 7 chains, 158 headlines/posts
  5 passed gates | rejected: liquidity too thin x48, no h1 volume x22, too old x2, unknown age x1, already discovered x1
  top: CATEWALK 0.84 | LOOONGCAT 0.74 | SATOSHINU 0.64 | ⠁⠏⠑ 0.57 | sPL.001 0.43
  no entries this tick
  shadow: tracking 19, closed 0 this tick (0 would have won)
```
