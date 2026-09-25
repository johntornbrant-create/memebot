# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T01:23:49+00:00`

## Equity

| | |
|---|---|
| Equity | **$548.94** |
| Return | **+9.79%** (start $500.00) |
| Cash | $395.59 |
| Deployed | $153.35 (27.9%) |
| Open positions | 4 / 8 |
| Closed trades | 34 (11W / 23L, WR 32%) |
| Profit factor | 0.63 |
| Fees + slippage paid | $24.91 |
| Ticks run | 227 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $116.64 | +1041% | +1041% | 22.0h |
| CATALYST | base | $10.26 | $9.45 | -7% | +10% | 21.7h |
| ARENA | solana | $17.10 | $15.74 | -7% | +0% | 1.3h |
| BRAIN | solana | $11.53 | $11.42 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| TUGGIN | $-16.60 | -99% | 0.3h | stop loss -98% |
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
tick #227  equity $561.79  cash $406.87  open 4
  SELL TUGGIN     100% @ $2.393e-06  ->  $0.25   [stop loss -98%]
  scanning chains + news...
  86 raw candidates across 7 chains, 154 headlines/posts
  9 passed gates | rejected: liquidity too thin x55, no h1 volume x20, too new (bot war) x1, too old x1
  top: OG 0.64 | ARENA 0.64 | STREET 0.63 | COD 0.63 | REVS 0.58
  BUY[explore] BRAIN      $11.53 @ $0.000211  score 0.49  solana  liq $43,649
  shadow: tracking 22, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED GETF       peak +606%  (scored 0.66)
```
