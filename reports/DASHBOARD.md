# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-14T17:57:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$412.87** |
| Return | **-17.43%** (start $500.00) |
| Cash | $402.87 |
| Deployed | $10.00 (2.4%) |
| Open positions | 2 / 8 |
| Closed trades | 19 (1W / 18L, WR 5%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $8.61 |
| Ticks run | 1560 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SHIT | solana | $5.00 | $4.94 | +0% | +0% | 0.0h |
| 牛逼 | bsc | $5.00 | $4.91 | +0% | +0% | 0.0h |

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
tick #1551  equity $412.87  cash $412.87  open 0
exits-only pass. equity $412.87 (next scan in 8 min)
tick #1552  equity $412.87  cash $412.87  open 0
exits-only pass. equity $412.87 (next scan in 7 min)
tick #1553  equity $412.87  cash $412.87  open 0
exits-only pass. equity $412.87 (next scan in 6 min)
tick #1554  equity $412.87  cash $412.87  open 0
exits-only pass. equity $412.87 (next scan in 5 min)
tick #1555  equity $412.87  cash $412.87  open 0
exits-only pass. equity $412.87 (next scan in 4 min)
tick #1556  equity $412.87  cash $412.87  open 0
exits-only pass. equity $412.87 (next scan in 3 min)
tick #1557  equity $412.87  cash $412.87  open 0
exits-only pass. equity $412.87 (next scan in 2 min)
tick #1558  equity $412.87  cash $412.87  open 0
exits-only pass. equity $412.87 (next scan in 1 min)
tick #1559  equity $412.87  cash $412.87  open 0
exits-only pass. equity $412.87 (next scan in 0 min)
tick #1560  equity $412.87  cash $412.87  open 0
  scanning chains + news...
  92 raw candidates across 4 chains, 160 headlines/posts
  6 passed gates | rejected: liquidity too thin x58, no h1 volume x22, too old x4, too new (bot war) x2
  top: 牛逼 0.80 | JENSEN 0.59 | gtacoin 0.57 | SHIT 0.50 | AMC 0.24
  tick bar 0.61 (top 10% of 6, floor 0.45)
  BUY[explore] SHIT       $5.00 @ $8.156e-05  score 0.50  solana  liq $26,241
  BUY[explore] 牛逼         $5.00 @ $0.0001506  score 0.80  bsc  liq $78,746
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
