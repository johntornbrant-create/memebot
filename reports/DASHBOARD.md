# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T22:05:27+00:00`

## Equity

| | |
|---|---|
| Equity | **$508.87** |
| Return | **+1.77%** (start $500.00) |
| Cash | $482.14 |
| Deployed | $26.73 (5.3%) |
| Open positions | 3 / 8 |
| Closed trades | 5 (2W / 3L, WR 40%) |
| Profit factor | 1.77 |
| Fees + slippage paid | $7.04 |
| Ticks run | 26 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $6.87 | -6% | +9% | 1.7h |
| KCAT | solana | $15.48 | $10.65 | -29% | +11% | 1.2h |
| Archi | solana | $7.66 | $9.21 | +27% | +27% | 0.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| Habibi | $+11.26 | +147% | 2.4h | trailing stop from +394% |
| BOP | $+18.46 | +250% | 4.4h | trailing stop from +526% |
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
tick #26  equity $510.96  cash $482.14  open 3
  scanning chains + news...
  115 raw candidates across 6 chains, 158 headlines/posts
  12 passed gates | rejected: liquidity too thin x72, too old x13, no h1 volume x10, already discovered x6, too new (bot war) x2
  top: SATOSHINU 0.70 | UPTOBER 0.70 | CATEWALK 0.67 | Archi 0.66 | BITCOINU 0.63
  no entries this tick
  shadow: tracking 45, closed 0 this tick (0 would have won)
```
