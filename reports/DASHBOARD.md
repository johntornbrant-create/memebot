# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T20:05:36+00:00`

## Equity

| | |
|---|---|
| Equity | **$522.39** |
| Return | **+4.48%** (start $500.00) |
| Cash | $475.01 |
| Deployed | $47.39 (9.1%) |
| Open positions | 4 / 8 |
| Closed trades | 1 (0W / 1L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $3.73 |
| Ticks run | 18 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $10.60 | -27% | +5% | 4.0h |
| CATEWALK | solana | $15.00 | $13.36 | -8% | +0% | 4.0h |
| BOP | solana | $7.39 | $13.68 | +422% | +526% | 2.7h |
| Habibi | bsc | $7.67 | $9.75 | +168% | +168% | 0.7h |

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
tick #18  equity $519.69  cash $475.01  open 4
  scanning chains + news...
  77 raw candidates across 6 chains, 158 headlines/posts
  9 passed gates | rejected: liquidity too thin x40, no h1 volume x24, too old x2, sell pressure x1, already discovered x1
  top: CATEWALK 0.78 | BITCOINU 0.69 | BetCat 0.68 | fomopay 0.67 | LOOONGCAT 0.63
  no entries this tick
  shadow: tracking 33, closed 0 this tick (0 would have won)
```
