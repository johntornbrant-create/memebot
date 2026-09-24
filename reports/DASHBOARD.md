# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-24T02:38:29+00:00`

## Equity

| | |
|---|---|
| Equity | **$503.02** |
| Return | **+0.60%** (start $500.00) |
| Cash | $423.92 |
| Deployed | $79.11 (15.7%) |
| Open positions | 5 / 8 |
| Closed trades | 26 (10W / 16L, WR 38%) |
| Profit factor | 0.90 |
| Fees + slippage paid | $23.43 |
| Ticks run | 139 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| 蝴蝶家园 | bsc | $14.96 | $19.92 | +37% | +38% | 23.0h |
| UPTOBER | solana | $10.19 | $9.91 | -2% | +3% | 2.1h |
| PURRP | solana | $10.28 | $19.74 | +94% | +94% | 1.2h |
| 币安协议 | bsc | $15.04 | $14.45 | -3% | +0% | 0.2h |
| 币安女王 | bsc | $15.09 | $14.93 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| CZBUILDER | $-4.25 | -40% | 0.8h | ratchet +25% (peak +98%) |
| BLUF | $-4.62 | -44% | 1.5h | stop loss -42% |
| 币安女王 | $+12.82 | +121% | 1.0h | ratchet +148% (peak +254%) |
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
tick #139  equity $501.33  cash $439.01  open 4
  scanning chains + news...
  154 raw candidates across 7 chains, 120 headlines/posts
  8 passed gates | rejected: liquidity too thin x100, no h1 volume x42, too old x2, already discovered x2
  top: 币安女王 0.72 | 币安协议 0.71 | PURRP 0.71 | SHARTCOIN 0.68 | BLUF 0.62
  BUY[exploit] 币安女王       $15.09 @ $0.002684  score 0.72  bsc  liq $90,641
  shadow: tracking 38, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED JEANPHIL   peak +284%  (scored 0.63)
```
