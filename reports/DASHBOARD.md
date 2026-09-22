# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T19:35:50+00:00`

## Equity

| | |
|---|---|
| Equity | **$516.42** |
| Return | **+3.28%** (start $500.00) |
| Cash | $468.18 |
| Deployed | $48.24 (9.3%) |
| Open positions | 4 / 8 |
| Closed trades | 1 (0W / 1L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $3.33 |
| Ticks run | 16 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $11.88 | -18% | +5% | 3.5h |
| CATEWALK | solana | $15.00 | $10.45 | -28% | +0% | 3.5h |
| BOP | solana | $7.39 | $14.95 | +471% | +526% | 2.2h |
| Habibi | bsc | $7.67 | $10.96 | +51% | +51% | 0.2h |

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
tick #16  equity $511.54  cash $468.18  open 4
  scanning chains + news...
  68 raw candidates across 6 chains, 158 headlines/posts
  3 passed gates | rejected: liquidity too thin x37, no h1 volume x21, too new (bot war) x2, sell pressure x2, too old x2
  top: LOOONGCAT 0.81 | CATEWALK 0.72 | APEZCAT 0.48
  no entries this tick
  shadow: tracking 24, closed 0 this tick (0 would have won)
```
