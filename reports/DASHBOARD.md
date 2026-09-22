# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T17:24:06+00:00`

## Equity

| | |
|---|---|
| Equity | **$492.51** |
| Return | **-1.50%** (start $500.00) |
| Cash | $459.22 |
| Deployed | $33.28 (6.8%) |
| Open positions | 3 / 8 |
| Closed trades | 1 (0W / 1L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $2.10 |
| Ticks run | 7 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $12.36 | -15% | +5% | 1.3h |
| CATEWALK | solana | $15.00 | $13.54 | -7% | +0% | 1.3h |
| BOP | solana | $7.39 | $6.98 | +0% | +0% | 0.0h |

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
tick #7  equity $494.30  cash $462.54  open 3
  SELL TRUMPTV    100% @ $6.094e-05  ->  $4.07   [stop loss -37%]
  scanning chains + news...
  109 raw candidates across 7 chains, 158 headlines/posts
  5 passed gates | rejected: liquidity too thin x80, no h1 volume x15, too old x4, too new (bot war) x2, sell pressure x1
  top: PCAT 0.74 | LOOONGCAT 0.72 | BOP 0.67 | CATEWALK 0.63 | MARSCZ 0.61
  BUY[explore] BOP        $7.39 @ $0.0001243  score 0.67  solana  liq $32,444
  shadow: tracking 14, closed 0 this tick (0 would have won)
```
