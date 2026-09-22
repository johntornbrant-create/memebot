# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-22T19:50:00+00:00`

## Equity

| | |
|---|---|
| Equity | **$519.69** |
| Return | **+3.94%** (start $500.00) |
| Cash | $475.01 |
| Deployed | $44.68 (8.6%) |
| Open positions | 4 / 8 |
| Closed trades | 1 (0W / 1L, WR 0%) |
| Profit factor | 0.00 |
| Fees + slippage paid | $3.73 |
| Ticks run | 17 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SATOSHINU | solana | $15.00 | $11.74 | -19% | +5% | 3.7h |
| CATEWALK | solana | $15.00 | $10.51 | -28% | +0% | 3.7h |
| BOP | solana | $7.39 | $15.21 | +481% | +526% | 2.4h |
| Habibi | bsc | $7.67 | $7.23 | +99% | +99% | 0.5h |

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
tick #17  equity $516.42  cash $468.18  open 4
  SELL Habibi     50% @ $0.001006  ->  $6.83   [take profit +80% (sold 50%)]
  scanning chains + news...
  141 raw candidates across 9 chains, 158 headlines/posts
  10 passed gates | rejected: liquidity too thin x79, no h1 volume x39, already discovered x6, too new (bot war) x3, sell pressure x2
  top: fomopay 0.80 | LOOONGCAT 0.77 | CATEWALK 0.70 | UPTOBER 0.68 | BITCOINU 0.63
  no entries this tick
  shadow: tracking 32, closed 0 this tick (0 would have won)
```
