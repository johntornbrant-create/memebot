# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T06:11:43+00:00`

## Equity

| | |
|---|---|
| Equity | **$416.41** |
| Return | **-16.72%** (start $500.00) |
| Cash | $399.73 |
| Deployed | $16.67 (4.0%) |
| Open positions | 3 / 8 |
| Closed trades | 21 (2W / 19L, WR 10%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $9.05 |
| Ticks run | 1566 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SHIT | solana | $5.00 | $7.93 | +114% | +114% | 12.2h |
| FOOD | solana | $5.05 | $5.49 | +10% | +17% | 6.9h |
| worth | solana | $5.04 | $3.25 | -35% | +0% | 3.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| 牛逼 | $+3.99 | +80% | 12.2h | ratchet +88% (peak +168%) |
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

## Learned weights (v168)

_refit on 1797 observations (1695 shadow, 102 real), 492 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.149 |
| turnover | +0.126 |
| liq_quality | +0.089 |
| momentum_accel | +0.064 |
| buy_pressure | +0.061 |
| paid_boost | +0.035 |
| dip_in_uptrend | +0.031 |
| not_vertical | -0.029 |
| buzz | +0.020 |
| fdv_sanity | +0.011 |
| age_sweet | +0.007 |
| socials | -0.003 |

## Last run log
```
tick #1566  equity $420.39  cash $395.34  open 4
  SELL 牛逼         100% @ $0.0002436  ->  $4.39   [ratchet +88% (peak +168%)]
  scanning chains + news...
  83 raw candidates across 3 chains, 160 headlines/posts
  1 passed gates | rejected: liquidity too thin x67, no h1 volume x14, too old x1
  top: GTA 0.74
  tick bar 0.62 (top 10% of 1, floor 0.45)
  skip GTA: solana concentration cap
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
