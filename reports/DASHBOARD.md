# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T21:05:18+00:00`

## Equity

| | |
|---|---|
| Equity | **$522.37** |
| Return | **+4.47%** (start $500.00) |
| Cash | $472.08 |
| Deployed | $50.29 (9.6%) |
| Open positions | 4 / 8 |
| Closed trades | 3 (0W / 3L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $5.81 |
| Ticks run | 22 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BOP | solana | $7.39 | $13.80 | +427% | +526% | 3.7h |
| Habibi | bsc | $7.67 | $11.95 | +339% | +339% | 1.7h |
| BITCOINU | solana | $7.67 | $7.94 | +9% | +9% | 0.7h |
| KCAT | solana | $15.48 | $16.59 | +11% | +11% | 0.2h |

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
tick #22  equity $515.90  cash $468.48  open 4
  SELL Habibi     25% @ $0.002219  ->  $3.61   [take profit +200% (sold 25%)]
  scanning chains + news...
  110 raw candidates across 8 chains, 158 headlines/posts
  7 passed gates | rejected: liquidity too thin x74, no h1 volume x22, already discovered x4, too old x2, sell pressure x1
  top: CATEWALK 0.72 | BITCOINU 0.69 | SATOSHINU 0.68 | $CRPAW 0.67 | fomopay 0.65
  no entries this tick
  shadow: tracking 38, closed 0 this tick (0 would have won)
```
