# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T02:24:18+00:00`

## Equity

| | |
|---|---|
| Equity | **$543.21** |
| Return | **+8.64%** (start $500.00) |
| Cash | $378.65 |
| Deployed | $164.55 (30.3%) |
| Open positions | 5 / 8 |
| Closed trades | 35 (11W / 24L, WR 31%) |
| Profit factor | 0.63 |
| Fees + slippage paid | $25.31 |
| Ticks run | 231 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $112.44 | +1000% | +1041% | 23.0h |
| CATALYST | base | $10.26 | $9.28 | -9% | +10% | 22.8h |
| ARENA | solana | $17.10 | $16.57 | -2% | +0% | 2.3h |
| COD | bsc | $16.42 | $14.85 | -9% | +1% | 0.8h |
| MDP | bsc | $11.41 | $11.27 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| BRAIN | $-0.64 | -6% | 1.0h | ratchet +0% (peak +57%) |
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
tick #231  equity $547.79  cash $379.17  open 5
  SELL BRAIN      100% @ $0.0002029  ->  $10.89   [ratchet +0% (peak +57%)]
  scanning chains + news...
  134 raw candidates across 6 chains, 154 headlines/posts
  9 passed gates | rejected: liquidity too thin x59, no h1 volume x31, too old x23, already discovered x10, sell pressure x1
  top: ARENA 0.73 | MDP 0.66 | REVS 0.66 | OG 0.64 | TTP 0.63
  BUY[explore] MDP        $11.41 @ $0.0001321  score 0.66  bsc  liq $33,362
  shadow: tracking 23, closed 3 this tick (0 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED GETF       peak +606%  (scored 0.66)
```
