# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-24T00:53:52+00:00`

## Equity

| | |
|---|---|
| Equity | **$505.67** |
| Return | **+1.13%** (start $500.00) |
| Cash | $425.56 |
| Deployed | $80.11 (15.8%) |
| Open positions | 4 / 8 |
| Closed trades | 22 (8W / 14L, WR 36%) |
| Profit factor | 0.69 |
| Fees + slippage paid | $22.19 |
| Ticks run | 132 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| 蝴蝶家园 | bsc | $14.96 | $15.17 | +5% | +27% | 21.3h |
| familiars | solana | $10.06 | $43.94 | +341% | +341% | 0.8h |
| UPTOBER | solana | $10.19 | $10.38 | +3% | +3% | 0.4h |
| BLUF | solana | $10.62 | $10.52 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| GAYMF | $-5.60 | -56% | 0.8h | stop loss -55% |
| UPTOBER | $+2.38 | +16% | 13.4h | ratchet +25% (peak +71%) |
| GROKBOTIFY | $-7.28 | -100% | 0.3h | stop loss -98% |
| MSTOCK | $+2.04 | +13% | 2.3h | stop loss -74% |
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
tick #132  equity $485.34  cash $431.73  open 4
  SELL GAYMF      100% @ $0.0002574  ->  $4.46   [stop loss -55%]
  scanning chains + news...
  93 raw candidates across 4 chains, 160 headlines/posts
  5 passed gates | rejected: liquidity too thin x35, no h1 volume x28, too old x12, already discovered x9, sell pressure x2
  top: CHROME 0.69 | JEANCOIN 0.60 | BLUF 0.58 | UPTOBER 0.54 | parafactual 0.50
  BUY[explore] BLUF       $10.62 @ $0.0003386  score 0.58  solana  liq $58,369
  shadow: tracking 31, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED JEANPHIL   peak +284%  (scored 0.63)
```
