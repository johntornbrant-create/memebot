# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T00:53:45+00:00`

## Equity

| | |
|---|---|
| Equity | **$566.76** |
| Return | **+13.35%** (start $500.00) |
| Cash | $419.78 |
| Deployed | $146.99 (25.9%) |
| Open positions | 4 / 8 |
| Closed trades | 32 (11W / 21L, WR 34%) |
| Profit factor | 0.75 |
| Fees + slippage paid | $24.59 |
| Ticks run | 225 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $114.77 | +1023% | +1023% | 21.5h |
| CATALYST | base | $10.26 | $9.39 | -8% | +10% | 21.2h |
| S&P500 | solana | $11.97 | $8.72 | -26% | +14% | 0.8h |
| ARENA | solana | $17.10 | $14.10 | -17% | +0% | 0.8h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| MOUSE | $-7.41 | -100% | 0.2h | stop loss -96% |

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
tick #225  equity $572.36  cash $419.78  open 4
  scanning chains + news...
  92 raw candidates across 6 chains, 154 headlines/posts
  4 passed gates | rejected: liquidity too thin x45, no h1 volume x25, too old x13, already discovered x4, sell pressure x1
  top: TUGGIN 0.67 | UPTOBER 0.61 | ARENA 0.60 | BRAIN 0.55
  no entries this tick
  shadow: tracking 22, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED JEANPHIL   peak +284%  (scored 0.63)
```
