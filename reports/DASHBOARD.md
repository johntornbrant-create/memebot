# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-24T01:37:04+00:00`

## Equity

| | |
|---|---|
| Equity | **$500.58** |
| Return | **+0.12%** (start $500.00) |
| Cash | $418.42 |
| Deployed | $82.17 (16.4%) |
| Open positions | 6 / 8 |
| Closed trades | 23 (9W / 14L, WR 39%) |
| Profit factor | 0.84 |
| Fees + slippage paid | $22.73 |
| Ticks run | 135 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| 蝴蝶家园 | bsc | $14.96 | $19.99 | +38% | +38% | 22.0h |
| UPTOBER | solana | $10.19 | $9.89 | -2% | +3% | 1.1h |
| BLUF | solana | $10.62 | $9.51 | -10% | +4% | 0.7h |
| 币安女王 | bsc | $10.56 | $19.93 | +91% | +91% | 0.5h |
| PURRP | solana | $10.28 | $12.33 | +21% | +21% | 0.2h |
| CZBUILDER | bsc | $10.51 | $10.39 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| familiars | $+14.14 | +141% | 1.3h | ratchet +208% (peak +341%) |
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
tick #135  equity $489.47  cash $428.93  open 5
  scanning chains + news...
  122 raw candidates across 6 chains, 160 headlines/posts
  5 passed gates | rejected: liquidity too thin x60, no h1 volume x47, too new (bot war) x4, too old x4, sell pressure x1
  top: BLUF 0.74 | PURRP 0.62 | JEANCOIN 0.61 | CZBUILDER 0.59 | UPTOBER 0.53
  BUY[explore] CZBUILDER  $10.51 @ $0.001784  score 0.59  bsc  liq $104,264
  shadow: tracking 33, closed 1 this tick (1 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED JEANPHIL   peak +284%  (scored 0.63)
```
