# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T21:23:06+00:00`

## Equity

| | |
|---|---|
| Equity | **$519.68** |
| Return | **+3.94%** (start $500.00) |
| Cash | $472.08 |
| Deployed | $47.59 (9.2%) |
| Open positions | 4 / 8 |
| Closed trades | 3 (0W / 3L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $5.81 |
| Ticks run | 23 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BOP | solana | $7.39 | $12.16 | +364% | +526% | 4.0h |
| Habibi | bsc | $7.67 | $13.47 | +394% | +394% | 2.0h |
| BITCOINU | solana | $7.67 | $7.77 | +7% | +9% | 1.0h |
| KCAT | solana | $15.48 | $14.19 | -6% | +11% | 0.5h |

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
tick #23  equity $522.37  cash $472.08  open 4
  scanning chains + news...
  71 raw candidates across 6 chains, 160 headlines/posts
  9 passed gates | rejected: liquidity too thin x35, no h1 volume x23, too old x3, already discovered x1
  top: BITCOINU 0.72 | CATEWALK 0.72 | SATOSHINU 0.70 | APECAT 0.64 | UNIPCS 0.61
  no entries this tick
  shadow: tracking 41, closed 0 this tick (0 would have won)
```
