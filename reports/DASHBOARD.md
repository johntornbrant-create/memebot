# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T06:59:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$415.38** |
| Return | **-16.92%** (start $500.00) |
| Cash | $397.81 |
| Deployed | $17.56 (4.2%) |
| Open positions | 3 / 8 |
| Closed trades | 22 (2W / 20L, WR 9%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $9.15 |
| Ticks run | 1610 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SHIT | solana | $5.00 | $7.63 | +106% | +144% | 13.0h |
| FOOD | solana | $5.05 | $5.17 | +4% | +17% | 7.7h |
| GTA | solana | $5.00 | $4.76 | -4% | +4% | 0.6h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| worth | $-1.96 | -39% | 3.0h | stop loss -37% |
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
  skip penny: solana concentration cap
  skip bill: solana concentration cap
  no entries this tick
  shadow: tracking 18, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $415.57 (-16.89% since start)
tick #1600  equity $415.57  cash $397.81  open 3
exits-only pass. equity $415.68 (next scan in 10 min)
tick #1601  equity $415.68  cash $397.81  open 3
exits-only pass. equity $415.66 (next scan in 9 min)
tick #1602  equity $415.66  cash $397.81  open 3
exits-only pass. equity $415.81 (next scan in 8 min)
tick #1603  equity $415.81  cash $397.81  open 3
exits-only pass. equity $415.68 (next scan in 7 min)
tick #1604  equity $415.68  cash $397.81  open 3
exits-only pass. equity $415.13 (next scan in 6 min)
tick #1605  equity $415.13  cash $397.81  open 3
exits-only pass. equity $414.96 (next scan in 5 min)
tick #1606  equity $414.96  cash $397.81  open 3
exits-only pass. equity $414.84 (next scan in 4 min)
tick #1607  equity $414.84  cash $397.81  open 3
exits-only pass. equity $415.07 (next scan in 3 min)
tick #1608  equity $415.07  cash $397.81  open 3
exits-only pass. equity $415.07 (next scan in 2 min)
tick #1609  equity $415.07  cash $397.81  open 3
exits-only pass. equity $415.42 (next scan in 1 min)
tick #1610  equity $415.42  cash $397.81  open 3
  scanning chains + news...
  101 raw candidates across 3 chains, 160 headlines/posts
  3 passed gates | rejected: liquidity too thin x76, no h1 volume x15, too old x7
  top: bill 0.73 | FOOD 0.34 | GTA 0.32
  tick bar 0.62 (top 10% of 3, floor 0.45)
  skip bill: solana concentration cap
  no entries this tick
  shadow: tracking 18, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
