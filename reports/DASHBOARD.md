# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T17:49:40+00:00`

## Equity

| | |
|---|---|
| Equity | **$511.77** |
| Return | **+2.35%** (start $500.00) |
| Cash | $472.78 |
| Deployed | $38.99 (7.6%) |
| Open positions | 3 / 8 |
| Closed trades | 1 (0W / 1L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $2.55 |
| Ticks run | 9 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $11.66 | -20% | +5% | 1.7h |
| CATEWALK | solana | $15.00 | $13.33 | -8% | +0% | 1.7h |
| BOP | solana | $7.39 | $14.01 | +301% | +301% | 0.4h |

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
tick #9  equity $494.68  cash $459.22  open 3
  SELL BOP        50% @ $0.0004985  ->  $13.55   [take profit +80% (sold 50%)]
  scanning chains + news...
  100 raw candidates across 5 chains, 160 headlines/posts
  6 passed gates | rejected: liquidity too thin x82, no h1 volume x10, sell pressure x1, too old x1
  top: LOOONGCAT 0.72 | BOP 0.71 | CATEWALK 0.63 | SATOSHINU 0.63 | PCAT 0.58
  no entries this tick
  shadow: tracking 17, closed 0 this tick (0 would have won)
```
