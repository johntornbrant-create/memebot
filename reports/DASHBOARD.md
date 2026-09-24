# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-24T03:38:57+00:00`

## Equity

| | |
|---|---|
| Equity | **$488.76** |
| Return | **-2.25%** (start $500.00) |
| Cash | $412.86 |
| Deployed | $75.90 (15.5%) |
| Open positions | 6 / 8 |
| Closed trades | 28 (11W / 17L, WR 39%) |
| Profit factor | 0.89 |
| Fees + slippage paid | $23.91 |
| Ticks run | 143 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| 蝴蝶家园 | bsc | $14.96 | $20.58 | +42% | +45% | 24.0h |
| 币安协议 | bsc | $15.04 | $12.05 | -19% | +0% | 1.2h |
| 币安女王 | bsc | $15.09 | $12.30 | -18% | +0% | 1.0h |
| JEANCOIN | solana | $10.32 | $10.44 | +2% | +2% | 0.2h |
| CATALYST | base | $10.26 | $10.16 | +0% | +0% | 0.0h |
| PURRP | solana | $10.26 | $10.17 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| PURRP | $+3.56 | +35% | 2.2h | ratchet +41% (peak +101%) |
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
tick #143  equity $491.32  cash $419.55  open 5
  SELL PURRP      100% @ $0.0004775  ->  $13.83   [ratchet +41% (peak +101%)]
  scanning chains + news...
  138 raw candidates across 6 chains, 158 headlines/posts
  5 passed gates | rejected: liquidity too thin x79, no h1 volume x38, too old x7, already discovered x6, too new (bot war) x2
  top: PURRP 0.57 | BLUF 0.53 | JEANCOIN 0.53 | NPC 0.51 | CATALYST 0.36
  BUY[explore] CATALYST   $10.26 @ $1.85  score 0.36  base  liq $1,153,658
  BUY[explore] PURRP      $10.26 @ $0.0004775  score 0.57  solana  liq $63,371
  shadow: tracking 34, closed 4 this tick (2 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED JEANPHIL   peak +284%  (scored 0.63)
```
