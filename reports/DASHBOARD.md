# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-24T03:25:02+00:00`

## Equity

| | |
|---|---|
| Equity | **$491.32** |
| Return | **-1.74%** (start $500.00) |
| Cash | $419.55 |
| Deployed | $71.77 (14.6%) |
| Open positions | 5 / 8 |
| Closed trades | 27 (10W / 17L, WR 37%) |
| Profit factor | 0.86 |
| Fees + slippage paid | $23.59 |
| Ticks run | 142 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| 蝴蝶家园 | bsc | $14.96 | $20.06 | +38% | +45% | 23.8h |
| PURRP | solana | $10.28 | $14.95 | +47% | +101% | 2.0h |
| 币安协议 | bsc | $15.04 | $12.05 | -19% | +0% | 1.0h |
| 币安女王 | bsc | $15.09 | $14.39 | -4% | +0% | 0.8h |
| JEANCOIN | solana | $10.32 | $10.22 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| UPTOBER | $-4.23 | -42% | 2.9h | stop loss -40% |
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
tick #142  equity $498.13  cash $423.92  open 5
  SELL UPTOBER    100% @ $0.000106  ->  $5.96   [stop loss -40%]
  scanning chains + news...
  122 raw candidates across 6 chains, 158 headlines/posts
  6 passed gates | rejected: liquidity too thin x55, no h1 volume x38, too old x11, already discovered x9, sell pressure x2
  top: BLUF 0.65 | JEANCOIN 0.64 | PURRP 0.55 | ACTSMUSE 0.52 | NPC 0.49
  BUY[explore] JEANCOIN   $10.32 @ $0.0004872  score 0.64  solana  liq $64,036
  shadow: tracking 38, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED JEANPHIL   peak +284%  (scored 0.63)
```
