# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-14T23:42:16+00:00`

## Equity

| | |
|---|---|
| Equity | **$422.01** |
| Return | **-15.60%** (start $500.00) |
| Cash | $397.17 |
| Deployed | $24.85 (5.9%) |
| Open positions | 4 / 8 |
| Closed trades | 19 (1W / 18L, WR 5%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $8.82 |
| Ticks run | 1564 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SHIT | solana | $5.00 | $6.33 | +71% | +77% | 5.7h |
| 牛逼 | bsc | $5.00 | $7.81 | +112% | +112% | 5.7h |
| J*B | solana | $5.00 | $5.92 | +20% | +20% | 0.4h |
| FOOD | solana | $5.05 | $4.78 | -4% | +0% | 0.4h |

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
tick #1564  equity $420.57  cash $397.17  open 4
  scanning chains + news...
  151 raw candidates across 6 chains, 160 headlines/posts
  3 passed gates | rejected: liquidity too thin x107, no h1 volume x27, too old x9, already discovered x3, too new (bot war) x1
  top: SWIF 0.59 | J*B 0.58 | JENSEN 0.33
  tick bar 0.59 (top 10% of 3, floor 0.45)
  skip SWIF: solana concentration cap
  skip J*B: already held
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
