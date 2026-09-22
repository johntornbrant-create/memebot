# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T20:37:53+00:00`

## Equity

| | |
|---|---|
| Equity | **$517.83** |
| Return | **+3.57%** (start $500.00) |
| Cash | $475.21 |
| Deployed | $42.62 (8.2%) |
| Open positions | 4 / 8 |
| Closed trades | 2 (0W / 2L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $4.55 |
| Ticks run | 20 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| CATEWALK | solana | $15.00 | $10.40 | -28% | +0% | 4.5h |
| BOP | solana | $7.39 | $14.31 | +446% | +526% | 3.2h |
| Habibi | bsc | $7.67 | $10.17 | +180% | +180% | 1.2h |
| BITCOINU | solana | $7.67 | $7.75 | +7% | +7% | 0.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
tick #20  equity $511.62  cash $475.21  open 4
  scanning chains + news...
  98 raw candidates across 7 chains, 158 headlines/posts
  7 passed gates | rejected: liquidity too thin x60, no h1 volume x24, already discovered x5, sell pressure x1, too old x1
  top: CATEWALK 0.74 | SOL 0.73 | SATOSHINU 0.68 | Archi 0.67 | fomopay 0.60
  no entries this tick
  shadow: tracking 36, closed 0 this tick (0 would have won)
```
