# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T06:47:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$415.57** |
| Return | **-16.89%** (start $500.00) |
| Cash | $397.81 |
| Deployed | $17.76 (4.3%) |
| Open positions | 3 / 8 |
| Closed trades | 22 (2W / 20L, WR 9%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $9.15 |
| Ticks run | 1599 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SHIT | solana | $5.00 | $8.10 | +118% | +144% | 12.8h |
| FOOD | solana | $5.05 | $5.08 | +2% | +17% | 7.5h |
| GTA | solana | $5.00 | $4.58 | -7% | +4% | 0.4h |

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
  skip GTA$: solana concentration cap
  no entries this tick
  shadow: tracking 17, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $415.47 (-16.91% since start)
tick #1589  equity $415.47  cash $397.81  open 3
exits-only pass. equity $415.60 (next scan in 10 min)
tick #1590  equity $415.60  cash $397.81  open 3
exits-only pass. equity $415.67 (next scan in 9 min)
tick #1591  equity $415.67  cash $397.81  open 3
exits-only pass. equity $415.68 (next scan in 8 min)
tick #1592  equity $415.68  cash $397.81  open 3
exits-only pass. equity $416.02 (next scan in 7 min)
tick #1593  equity $416.02  cash $397.81  open 3
exits-only pass. equity $416.11 (next scan in 6 min)
tick #1594  equity $416.11  cash $397.81  open 3
exits-only pass. equity $416.11 (next scan in 5 min)
tick #1595  equity $416.11  cash $397.81  open 3
exits-only pass. equity $416.30 (next scan in 4 min)
tick #1596  equity $416.30  cash $397.81  open 3
exits-only pass. equity $416.15 (next scan in 3 min)
tick #1597  equity $416.15  cash $397.81  open 3
exits-only pass. equity $416.16 (next scan in 2 min)
tick #1598  equity $416.16  cash $397.81  open 3
exits-only pass. equity $415.87 (next scan in 1 min)
tick #1599  equity $415.87  cash $397.81  open 3
  scanning chains + news...
  106 raw candidates across 3 chains, 160 headlines/posts
  3 passed gates | rejected: liquidity too thin x80, no h1 volume x16, too old x7
  top: bill 0.81 | penny 0.65 | GTA 0.29
  tick bar 0.62 (top 10% of 3, floor 0.45)
  skip penny: solana concentration cap
  skip bill: solana concentration cap
  no entries this tick
  shadow: tracking 18, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
