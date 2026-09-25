# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T01:35:55+00:00`

## Equity

| | |
|---|---|
| Equity | **$547.48** |
| Return | **+9.50%** (start $500.00) |
| Cash | $379.17 |
| Deployed | $168.31 (30.7%) |
| Open positions | 5 / 8 |
| Closed trades | 34 (11W / 23L, WR 32%) |
| Profit factor | 0.63 |
| Fees + slippage paid | $25.08 |
| Ticks run | 228 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $113.38 | +1009% | +1041% | 22.2h |
| CATALYST | base | $10.26 | $9.45 | -7% | +10% | 22.0h |
| ARENA | solana | $17.10 | $15.62 | -8% | +0% | 1.5h |
| BRAIN | solana | $11.53 | $13.43 | +18% | +18% | 0.2h |
| COD | bsc | $16.42 | $16.25 | +0% | +0% | 0.0h |

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
tick #228  equity $548.94  cash $395.59  open 4
  scanning chains + news...
  83 raw candidates across 5 chains, 154 headlines/posts
  9 passed gates | rejected: liquidity too thin x35, no h1 volume x21, too old x13, already discovered x4, too new (bot war) x1
  top: COD 0.69 | ARENA 0.64 | STREET 0.63 | REVS 0.61 | OG 0.58
  BUY[exploit] COD        $16.42 @ $0.001404  score 0.69  bsc  liq $114,686
  shadow: tracking 22, closed 0 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED GETF       peak +606%  (scored 0.66)
```
