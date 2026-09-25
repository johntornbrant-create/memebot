# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T01:05:44+00:00`

## Equity

| | |
|---|---|
| Equity | **$561.79** |
| Return | **+12.36%** (start $500.00) |
| Cash | $406.87 |
| Deployed | $154.92 (27.6%) |
| Open positions | 4 / 8 |
| Closed trades | 33 (11W / 22L, WR 33%) |
| Profit factor | 0.71 |
| Fees + slippage paid | $24.79 |
| Ticks run | 226 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $114.69 | +1022% | +1023% | 21.7h |
| CATALYST | base | $10.26 | $9.39 | -8% | +10% | 21.4h |
| ARENA | solana | $17.10 | $13.99 | -17% | +0% | 1.0h |
| TUGGIN | solana | $16.85 | $16.70 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| S&P500 | $-8.02 | -67% | 0.9h | stop loss -66% |
| 蝴蝶家园 | $-8.54 | -57% | 34.2h | ratchet +0% (peak +57%) |
| 币安协议 | $-5.79 | -38% | 11.0h | stop loss -37% |
| PURRP | $-4.46 | -43% | 2.2h | stop loss -42% |
| 币安女王 | $-0.58 | -4% | 3.0h | ratchet +0% (peak +67%) |
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
tick #226  equity $566.76  cash $419.78  open 4
  SELL S&P500     100% @ $4.087e-05  ->  $3.95   [stop loss -66%]
  scanning chains + news...
  86 raw candidates across 7 chains, 154 headlines/posts
  4 passed gates | rejected: liquidity too thin x59, no h1 volume x16, too new (bot war) x2, sell pressure x2, already discovered x2
  top: TUGGIN 0.65 | UPTOBER 0.64 | ARENA 0.60 | BRAIN 0.56
  BUY[exploit] TUGGIN     $16.85 @ $0.0001481  score 0.65  solana  liq $33,570
  shadow: tracking 16, closed 6 this tick (3 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED GETF       peak +606%  (scored 0.66)
```
