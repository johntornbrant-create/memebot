# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-14T23:19:06+00:00`

## Equity

| | |
|---|---|
| Equity | **$420.57** |
| Return | **-15.89%** (start $500.00) |
| Cash | $397.17 |
| Deployed | $23.40 (5.6%) |
| Open positions | 4 / 8 |
| Closed trades | 19 (1W / 18L, WR 5%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $8.82 |
| Ticks run | 1563 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SHIT | solana | $5.00 | $6.55 | +77% | +77% | 5.4h |
| 牛逼 | bsc | $5.00 | $6.80 | +85% | +85% | 5.4h |
| J*B | solana | $5.00 | $4.94 | +0% | +0% | 0.0h |
| FOOD | solana | $5.05 | $4.99 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| FLAPAI | $-6.90 | -79% | 6.7h | stop loss -78% |
| GTA | $-5.00 | -57% | 6.7h | stop loss -56% |
| GTA | $-2.64 | -43% | 11.7h | ratchet +65% (peak +135%) |
| TIT | $-7.07 | -80% | 4.9h | stop loss -79% |
| 币安AiPro | $-1.62 | -25% | 18.2h | ratchet +47% (peak +109%) |
| CATTLEAXE | $-2.39 | -38% | 7.9h | stop loss -37% |
| BTC | $-2.59 | -42% | 4.0h | stop loss -40% |
| SWORDOPE | $-2.42 | -38% | 4.8h | stop loss -36% |
| REACHY | $-6.23 | -99% | 13.8h | stop loss -99% |
| KURUMI | $+5.28 | +58% | 6.0h | ratchet +65% (peak +136%) |
| MAYA | $-3.58 | -57% | 10.4h | ratchet +25% (peak +94%) |
| LUCIA | $-9.39 | -99% | 1.9h | stop loss -99% |
| ODIE | $-9.47 | -100% | 1.9h | stop loss -100% |
| WRHND | $-1.81 | -19% | 4.1h | ratchet +25% (peak +93%) |
| HCAT | $-9.53 | -100% | 2.1h | stop loss -99% |

## Learned weights (v167)

_refit on 1777 observations (1676 shadow, 101 real), 490 winners (28% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.145 |
| turnover | +0.129 |
| liq_quality | +0.088 |
| momentum_accel | +0.062 |
| buy_pressure | +0.059 |
| paid_boost | +0.032 |
| dip_in_uptrend | +0.031 |
| not_vertical | -0.030 |
| buzz | +0.020 |
| fdv_sanity | +0.012 |
| age_sweet | +0.007 |
| socials | -0.006 |

## Last run log
```
tick #1563  equity $412.42  cash $402.87  open 2
  SELL SHIT       25% @ $0.0001441  ->  $2.15   [take profit +50% (sold 25%)]
  SELL 牛逼         25% @ $0.0002779  ->  $2.20   [take profit +50% (sold 25%)]
  scanning chains + news...
  110 raw candidates across 4 chains, 160 headlines/posts
  4 passed gates | rejected: liquidity too thin x63, no h1 volume x30, too old x10, too new (bot war) x2, already discovered x1
  top: FOOD 0.50 | JENSEN 0.43 | GTA$ 0.34 | J*B 0.21
  tick bar 0.50 (top 10% of 4, floor 0.45)
  BUY[explore] J*B        $5.00 @ $7.193e-05  score 0.21  solana  liq $25,070
  BUY[exploit] FOOD       $5.05 @ $0.0003512  score 0.50  solana  liq $55,455
  shadow: tracking 15, closed 4 this tick (2 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
