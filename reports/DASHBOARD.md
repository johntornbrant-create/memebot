# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T20:51:13+00:00`

## Equity

| | |
|---|---|
| Equity | **$515.90** |
| Return | **+3.18%** (start $500.00) |
| Cash | $468.48 |
| Deployed | $47.42 (9.2%) |
| Open positions | 4 / 8 |
| Closed trades | 3 (0W / 3L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $5.43 |
| Ticks run | 21 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BOP | solana | $7.39 | $14.53 | +455% | +526% | 3.5h |
| Habibi | bsc | $7.67 | $10.22 | +181% | +181% | 1.5h |
| BITCOINU | solana | $7.67 | $7.19 | -1% | +7% | 0.5h |
| KCAT | solana | $15.48 | $15.02 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| CATEWALK | $-6.25 | -42% | 4.7h | stop loss -37% |
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
tick #21  equity $517.83  cash $475.21  open 4
  SELL CATEWALK   100% @ $0.0007379  ->  $8.75   [stop loss -37%]
  scanning chains + news...
  111 raw candidates across 8 chains, 158 headlines/posts
  11 passed gates | rejected: liquidity too thin x51, no h1 volume x31, too old x9, already discovered x7, sell pressure x1
  top: KCAT 0.77 | CATEWALK 0.71 | SATOSHINU 0.68 | SI 0.66 | $CRPAW 0.64
  BUY[exploit] KCAT       $15.48 @ $0.0001742  score 0.77  solana  liq $39,761
  shadow: tracking 37, closed 0 this tick (0 would have won)
```
