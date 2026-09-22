# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T18:28:42+00:00`

## Equity

| | |
|---|---|
| Equity | **$514.98** |
| Return | **+3.00%** (start $500.00) |
| Cash | $475.85 |
| Deployed | $39.13 (7.6%) |
| Open positions | 3 / 8 |
| Closed trades | 1 (0W / 1L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $2.93 |
| Ticks run | 11 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $9.48 | -35% | +5% | 2.4h |
| CATEWALK | solana | $15.00 | $13.25 | -9% | +0% | 2.4h |
| BOP | solana | $7.39 | $16.40 | +526% | +526% | 1.1h |

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
tick #11  equity $509.59  cash $475.85  open 3
  scanning chains + news...
  100 raw candidates across 6 chains, 158 headlines/posts
  9 passed gates | rejected: liquidity too thin x44, no h1 volume x33, too old x8, already discovered x6
  top: LOOONGCAT 0.74 | CATEWALK 0.66 | SI 0.66 | SATOSHINU 0.62 | KCAT 0.59
  no entries this tick
  shadow: tracking 19, closed 0 this tick (0 would have won)
```
