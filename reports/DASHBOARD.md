# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T19:04:57+00:00`

## Equity

| | |
|---|---|
| Equity | **$513.94** |
| Return | **+2.79%** (start $500.00) |
| Cash | $475.85 |
| Deployed | $38.09 (7.4%) |
| Open positions | 3 / 8 |
| Closed trades | 1 (0W / 1L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $2.93 |
| Ticks run | 14 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $10.66 | -27% | +5% | 3.0h |
| CATEWALK | solana | $15.00 | $11.95 | -18% | +0% | 3.0h |
| BOP | solana | $7.39 | $15.48 | +491% | +526% | 1.7h |

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
tick #14  equity $512.28  cash $475.85  open 3
  scanning chains + news...
  114 raw candidates across 7 chains, 158 headlines/posts
  8 passed gates | rejected: liquidity too thin x64, no h1 volume x22, too old x9, already discovered x9, too new (bot war) x1
  top: LOOONGCAT 0.73 | CATEWALK 0.72 | WCAT 0.69 | SOL 0.67 | SI 0.66
  no entries this tick
  shadow: tracking 21, closed 0 this tick (0 would have won)
```
