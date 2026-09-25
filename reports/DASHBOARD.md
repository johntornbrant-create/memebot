# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-25T03:38:42+00:00`

## Equity

| | |
|---|---|
| Equity | **$542.86** |
| Return | **+8.57%** (start $500.00) |
| Cash | $350.13 |
| Deployed | $192.72 (35.5%) |
| Open positions | 6 / 8 |
| Closed trades | 37 (11W / 26L, WR 30%) |
| Profit factor | 0.56 |
| Fees + slippage paid | $25.77 |
| Ticks run | 236 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| JEANCOIN | solana | $10.32 | $113.40 | +1009% | +1041% | 24.2h |
| CATALYST | base | $10.26 | $9.28 | -9% | +10% | 24.0h |
| ARENA | solana | $17.10 | $17.73 | +5% | +5% | 3.5h |
| COD | bsc | $16.42 | $27.84 | +71% | +71% | 2.0h |
| MDP | bsc | $11.41 | $13.07 | +16% | +32% | 1.2h |
| IMU | solana | $11.40 | $11.30 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| OG | $-11.64 | -99% | 0.2h | stop loss -98% |
| 币安女英雄 | $-5.48 | -48% | 1.0h | ratchet +83% (peak +161%) |
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
tick #236  equity $561.94  cash $355.54  open 7
  SELL 币安女英雄      100% @ $0.0001042  ->  $5.83   [ratchet +83% (peak +161%)]
  SELL OG         100% @ $2.359e-06  ->  $0.16   [stop loss -98%]
  scanning chains + news...
  83 raw candidates across 5 chains, 160 headlines/posts
  6 passed gates | rejected: liquidity too thin x50, no h1 volume x21, too old x2, unknown age x2, too new (bot war) x1
  top: ARENA 0.70 | BRAIN 0.62 | MDP 0.53 | UPTOBER 0.52 | Shurikane 0.51
  BUY[explore] IMU        $11.40 @ $0.0001926  score 0.45  solana  liq $38,582
  shadow: tracking 22, closed 1 this tick (1 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED NPC        peak +1110%  (scored 0.49)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
```
