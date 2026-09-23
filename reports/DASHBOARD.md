# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-23T08:05:36+00:00`

## Equity

| | |
|---|---|
| Equity | **$485.13** |
| Return | **-2.97%** (start $500.00) |
| Cash | $443.00 |
| Deployed | $42.12 (8.7%) |
| Open positions | 4 / 8 |
| Closed trades | 18 (6W / 12L, WR 33%) |
| Profit factor | 0.75 |
| Fees + slippage paid | $20.90 |
| Ticks run | 65 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| UPTOBER | solana | $15.04 | $15.17 | +4% | +71% | 8.3h |
| 蝴蝶家园 | bsc | $14.96 | $14.27 | -2% | +10% | 4.4h |
| MSTOCK | bsc | $15.52 | $5.41 | -28% | +118% | 2.0h |
| GROKBOTIFY | solana | $7.28 | $6.87 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| MOUSE | $-7.41 | -100% | 0.2h | stop loss -96% |
| LeoGuigna | $-15.38 | -100% | 0.8h | stop loss -99% |
| 币安的守护者 | $-4.02 | -52% | 1.5h | stop loss -44% |
| based | $-6.45 | -42% | 1.2h | stop loss -37% |
| DURIAN | $-5.02 | -64% | 0.5h | stop loss -57% |
| LeoGuigna | $+19.66 | +263% | 2.0h | trailing stop from +724% |
| BITCOINU | $+7.57 | +99% | 9.2h | trailing stop from +248% |
| based | $+1.95 | +26% | 2.0h | stop loss -38% |
| SHIELD | $-3.94 | -53% | 0.3h | stop loss -45% |
| ACAT | $-7.53 | -100% | 0.9h | stop loss -100% |
| MORE | $-6.18 | -40% | 1.2h | stop loss -35% |
| Archi | $+0.08 | +1% | 1.9h | stop loss -76% |
| KCAT | $-6.40 | -41% | 1.7h | stop loss -37% |
| Habibi | $+11.26 | +147% | 2.4h | trailing stop from +394% |
| BOP | $+18.46 | +250% | 4.4h | trailing stop from +526% |

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
tick #65  equity $493.88  cash $450.28  open 4
  SELL MOUSE      100% @ $4.808e-06  ->  $0.00   [stop loss -96%]
  scanning chains + news...
  72 raw candidates across 5 chains, 160 headlines/posts
  3 passed gates | rejected: liquidity too thin x52, no h1 volume x14, too old x2, too new (bot war) x1
  top: based 0.73 | UPTOBER 0.61 | GROKBOTIFY 0.48
  BUY[explore] GROKBOTIFY $7.28 @ $0.0001156  score 0.48  solana  liq $29,515
  no entry: daily trade cap reached
  shadow: tracking 75, closed 0 this tick (0 would have won)
```
