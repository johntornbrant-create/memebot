# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T20:23:44+00:00`

## Equity

| | |
|---|---|
| Equity | **$511.62** |
| Return | **+2.32%** (start $500.00) |
| Cash | $475.21 |
| Deployed | $36.42 (7.1%) |
| Open positions | 4 / 8 |
| Closed trades | 2 (0W / 2L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $4.55 |
| Ticks run | 19 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| CATEWALK | solana | $15.00 | $12.22 | -16% | +0% | 4.3h |
| BOP | solana | $7.39 | $12.80 | +389% | +526% | 3.0h |
| Habibi | bsc | $7.67 | $3.72 | +2% | +168% | 1.0h |
| BITCOINU | solana | $7.67 | $7.27 | +0% | +0% | 0.0h |

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
tick #19  equity $522.39  cash $475.01  open 4
  SELL SATOSHINU  100% @ $0.0006073  ->  $7.88   [stop loss -43%]
  scanning chains + news...
  81 raw candidates across 6 chains, 158 headlines/posts
  7 passed gates | rejected: liquidity too thin x41, no h1 volume x28, too old x3, already discovered x2
  top: CATEWALK 0.73 | fomopay 0.71 | SCHRÖDINGER 0.66 | SATOSHINU 0.65 | Archi 0.64
  BUY[explore] BITCOINU   $7.67 @ $0.0001405  score 0.55  solana  liq $32,988
  shadow: tracking 34, closed 0 this tick (0 would have won)
```
