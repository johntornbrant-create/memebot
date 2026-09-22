# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T16:06:26+00:00`

## Equity

| | |
|---|---|
| Equity | **$500.00** |
| Return | **+0.00%** (start $500.00) |
| Cash | $470.00 |
| Deployed | $30.00 (6.0%) |
| Open positions | 2 / 8 |
| Closed trades | 0 (0W / 0L, WR 0%) |
| Profit factor | – |
| Fees + slippage paid | $0.91 |
| Ticks run | 1 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $14.54 | +0% | +0% | 0.0h |
| CATEWALK | solana | $15.00 | $14.54 | +0% | +0% | 0.0h |

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
tick #1  equity $500.00  cash $500.00  open 0
  scanning chains + news...
  100 raw candidates across 5 chains, 158 headlines/posts
  7 passed gates | rejected: liquidity too thin x49, too old x16, no h1 volume x15, already discovered x11, too new (bot war) x1
  top: SATOSHINU 0.76 | CATEWALK 0.75 | LOOONGCAT 0.68 | KCAT 0.65 | JEANPHIL 0.63
  BUY[exploit] SATOSHINU  $15.00 @ $0.001066  score 0.76  solana  liq $102,473
  BUY[exploit] CATEWALK   $15.00 @ $0.001171  score 0.75  solana  liq $105,537
  shadow: tracking 7, closed 0 this tick (0 would have won)
```
