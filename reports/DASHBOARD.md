# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T06:35:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$415.47** |
| Return | **-16.91%** (start $500.00) |
| Cash | $397.81 |
| Deployed | $17.66 (4.2%) |
| Open positions | 3 / 8 |
| Closed trades | 22 (2W / 20L, WR 9%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $9.15 |
| Ticks run | 1588 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SHIT | solana | $5.00 | $8.12 | +119% | +144% | 12.6h |
| FOOD | solana | $5.05 | $5.38 | +8% | +17% | 7.3h |
| GTA | solana | $5.00 | $4.15 | -16% | +4% | 0.2h |

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
  BUY[explore] GTA        $5.00 @ $8.931e-05  score 0.70  solana  liq $27,555
  skip GTA$: solana concentration cap
  shadow: tracking 17, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $417.16 (-16.57% since start)
tick #1578  equity $417.16  cash $397.81  open 3
exits-only pass. equity $416.95 (next scan in 10 min)
tick #1579  equity $416.95  cash $397.81  open 3
exits-only pass. equity $416.99 (next scan in 9 min)
tick #1580  equity $416.99  cash $397.81  open 3
exits-only pass. equity $416.88 (next scan in 8 min)
tick #1581  equity $416.88  cash $397.81  open 3
exits-only pass. equity $417.36 (next scan in 7 min)
tick #1582  equity $417.36  cash $397.81  open 3
exits-only pass. equity $417.46 (next scan in 6 min)
tick #1583  equity $417.46  cash $397.81  open 3
exits-only pass. equity $417.00 (next scan in 5 min)
tick #1584  equity $417.00  cash $397.81  open 3
exits-only pass. equity $416.62 (next scan in 4 min)
tick #1585  equity $416.62  cash $397.81  open 3
exits-only pass. equity $416.40 (next scan in 3 min)
tick #1586  equity $416.40  cash $397.81  open 3
exits-only pass. equity $416.43 (next scan in 2 min)
tick #1587  equity $416.43  cash $397.81  open 3
exits-only pass. equity $415.43 (next scan in 1 min)
tick #1588  equity $415.43  cash $397.81  open 3
  scanning chains + news...
  106 raw candidates across 3 chains, 160 headlines/posts
  3 passed gates | rejected: liquidity too thin x79, no h1 volume x16, too old x6, too new (bot war) x2
  top: bill 0.67 | GTA 0.47 | GTA$ 0.31
  tick bar 0.62 (top 10% of 3, floor 0.45)
  skip bill: solana concentration cap
  skip GTA$: solana concentration cap
  no entries this tick
  shadow: tracking 17, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
