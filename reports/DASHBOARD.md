# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T03:11:05+00:00`

## Equity

| | |
|---|---|
| Equity | **$420.39** |
| Return | **-15.92%** (start $500.00) |
| Cash | $395.34 |
| Deployed | $25.04 (6.0%) |
| Open positions | 4 / 8 |
| Closed trades | 20 (1W / 19L, WR 5%) |
| Profit factor | 0.38 |
| Fees + slippage paid | $8.97 |
| Ticks run | 1565 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SHIT | solana | $5.00 | $6.73 | +82% | +82% | 9.2h |
| 牛逼 | bsc | $5.00 | $7.41 | +168% | +168% | 9.2h |
| FOOD | solana | $5.05 | $5.86 | +17% | +17% | 3.9h |
| worth | solana | $5.04 | $4.98 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| J*B | $-4.19 | -84% | 3.8h | stop loss -83% |
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
tick #1565  equity $422.01  cash $397.17  open 4
  SELL 牛逼         25% @ $0.0004036  ->  $2.40   [take profit +150% (sold 25%)]
  SELL J*B        100% @ $1.222e-05  ->  $0.81   [stop loss -83%]
  scanning chains + news...
  104 raw candidates across 5 chains, 160 headlines/posts
  2 passed gates | rejected: liquidity too thin x72, no h1 volume x21, too old x6, sell pressure x1, already discovered x1
  top: worth 0.68 | WANTED 0.41
  tick bar 0.61 (top 10% of 2, floor 0.45)
  BUY[exploit] worth      $5.04 @ $0.0001345  score 0.68  solana  liq $25,469
  skip WANTED: solana concentration cap
  shadow: tracking 15, closed 3 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
