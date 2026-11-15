# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T07:47:30+00:00`

## Equity

| | |
|---|---|
| Equity | **$417.35** |
| Return | **-16.53%** (start $500.00) |
| Cash | $400.13 |
| Deployed | $17.21 (4.1%) |
| Open positions | 3 / 8 |
| Closed trades | 22 (2W / 20L, WR 9%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $9.18 |
| Ticks run | 1654 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SHIT | solana | $5.00 | $6.91 | +149% | +154% | 13.8h |
| FOOD | solana | $5.05 | $5.20 | +4% | +17% | 8.5h |
| GTA | solana | $5.00 | $5.11 | +3% | +4% | 1.4h |

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
  skip bill: solana concentration cap
  no entries this tick
  shadow: tracking 19, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $416.65 (-16.67% since start)
tick #1644  equity $416.65  cash $400.13  open 3
exits-only pass. equity $416.89 (next scan in 10 min)
tick #1645  equity $416.89  cash $400.13  open 3
exits-only pass. equity $416.06 (next scan in 9 min)
tick #1646  equity $416.06  cash $400.13  open 3
exits-only pass. equity $416.68 (next scan in 8 min)
tick #1647  equity $416.68  cash $400.13  open 3
exits-only pass. equity $416.61 (next scan in 7 min)
tick #1648  equity $416.61  cash $400.13  open 3
exits-only pass. equity $416.69 (next scan in 6 min)
tick #1649  equity $416.69  cash $400.13  open 3
exits-only pass. equity $416.83 (next scan in 5 min)
tick #1650  equity $416.83  cash $400.13  open 3
exits-only pass. equity $417.18 (next scan in 4 min)
tick #1651  equity $417.18  cash $400.13  open 3
exits-only pass. equity $417.06 (next scan in 3 min)
tick #1652  equity $417.06  cash $400.13  open 3
exits-only pass. equity $417.12 (next scan in 2 min)
tick #1653  equity $417.12  cash $400.13  open 3
exits-only pass. equity $417.13 (next scan in 1 min)
tick #1654  equity $417.13  cash $400.13  open 3
  scanning chains + news...
  132 raw candidates across 4 chains, 160 headlines/posts
  3 passed gates | rejected: liquidity too thin x87, no h1 volume x31, too old x8, already discovered x2, unknown age x1
  top: bill 0.54 | HOGE 0.50 | GTA 0.31
  tick bar 0.54 (top 10% of 3, floor 0.45)
  skip bill: solana concentration cap
  skip HOGE: solana concentration cap
  no entries this tick
  shadow: tracking 19, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
