# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T21:36:43+00:00`

## Equity

| | |
|---|---|
| Equity | **$514.87** |
| Return | **+2.97%** (start $500.00) |
| Cash | $472.08 |
| Deployed | $42.79 (8.3%) |
| Open positions | 4 / 8 |
| Closed trades | 3 (0W / 3L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $5.81 |
| Ticks run | 24 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BOP | solana | $7.39 | $12.10 | +362% | +526% | 4.2h |
| Habibi | bsc | $7.67 | $10.56 | +288% | +394% | 2.2h |
| BITCOINU | solana | $7.67 | $6.90 | -5% | +9% | 1.2h |
| KCAT | solana | $15.48 | $13.22 | -12% | +11% | 0.8h |

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
tick #24  equity $519.68  cash $472.08  open 4
  scanning chains + news...
  72 raw candidates across 4 chains, 158 headlines/posts
  10 passed gates | rejected: liquidity too thin x32, no h1 volume x29, too old x1
  top: CATEWALK 0.70 | SATOSHINU 0.69 | TIKCAT 0.67 | BAKARI 0.66 | APECAT 0.63
  no entries this tick
  shadow: tracking 42, closed 0 this tick (0 would have won)
```
