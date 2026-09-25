# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T00:33:07+00:00`

## Equity

| | |
|---|---|
| Equity | **$572.36** |
| Return | **+14.47%** (start $500.00) |
| Cash | $419.78 |
| Deployed | $152.58 (26.7%) |
| Open positions | 4 / 8 |
| Closed trades | 32 (11W / 21L, WR 34%) |
| Profit factor | 0.75 |
| Fees + slippage paid | $24.59 |
| Ticks run | 224 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $113.15 | +1007% | +1007% | 21.1h |
| CATALYST | base | $10.26 | $9.28 | -9% | +10% | 20.9h |
| S&P500 | solana | $11.97 | $13.56 | +14% | +14% | 0.4h |
| ARENA | solana | $17.10 | $16.59 | -2% | +0% | 0.4h |

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
tick #224  equity $570.11  cash $419.78  open 4
  scanning chains + news...
  116 raw candidates across 8 chains, 154 headlines/posts
  3 passed gates | rejected: liquidity too thin x73, no h1 volume x34, too new (bot war) x3, too old x1, sell pressure x1
  top: ARENA 0.80 | BRAIN 0.53 | UPTOBER 0.50
  no entries this tick
  shadow: tracking 20, closed 2 this tick (2 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED JEANPHIL   peak +284%  (scored 0.63)
```
