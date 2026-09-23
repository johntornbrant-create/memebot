# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T00:56:01+00:00`

## Equity

| | |
|---|---|
| Equity | **$509.27** |
| Return | **+1.85%** (start $500.00) |
| Cash | $470.20 |
| Deployed | $39.06 (7.7%) |
| Open positions | 3 / 8 |
| Closed trades | 8 (3W / 5L, WR 38%) |
| Profit factor | 1.02 |
| Fees + slippage paid | $9.97 |
| Ticks run | 37 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| BITCOINU | solana | $7.67 | $9.90 | +36% | +36% | 4.5h |
| UPTOBER | solana | $15.04 | $19.16 | +31% | +31% | 1.1h |
| ACAT | solana | $7.53 | $10.01 | +40% | +59% | 0.8h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| MORE | $-6.18 | -40% | 1.2h | stop loss -35% |
| Archi | $+0.08 | +1% | 1.9h | stop loss -76% |
| KCAT | $-6.40 | -41% | 1.7h | stop loss -37% |
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
tick #37  equity $508.82  cash $470.20  open 3
  scanning chains + news...
  121 raw candidates across 6 chains, 158 headlines/posts
  5 passed gates | rejected: liquidity too thin x72, no h1 volume x29, too old x10, already discovered x4, unknown age x1
  top: CATEWALK 0.68 | ACAT 0.63 | UPTOBER 0.60 | SATOSHINU 0.52 | SHIELD 0.46
  no entries this tick
  shadow: tracking 52, closed 0 this tick (0 would have won)
```
