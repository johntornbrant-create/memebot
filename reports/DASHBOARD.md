# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T18:06:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$509.59** |
| Return | **+1.92%** (start $500.00) |
| Cash | $475.85 |
| Deployed | $33.73 (6.6%) |
| Open positions | 3 / 8 |
| Closed trades | 1 (0W / 1L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $2.93 |
| Ticks run | 10 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $10.54 | -27% | +5% | 2.0h |
| CATEWALK | solana | $15.00 | $12.84 | -12% | +0% | 2.0h |
| BOP | solana | $7.39 | $10.35 | +295% | +301% | 0.7h |

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
tick #10  equity $511.77  cash $472.78  open 3
  SELL BOP        25% @ $0.0004911  ->  $3.08   [take profit +200% (sold 25%)]
  scanning chains + news...
  84 raw candidates across 6 chains, 160 headlines/posts
  5 passed gates | rejected: liquidity too thin x46, no h1 volume x30, sell pressure x1, too old x1, too new (bot war) x1
  top: LOOONGCAT 0.76 | CATEWALK 0.63 | SATOSHINU 0.63 | PCAT 0.57 | betbolt 0.39
  no entries this tick
  shadow: tracking 17, closed 0 this tick (0 would have won)
```
