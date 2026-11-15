# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T07:11:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$414.93** |
| Return | **-17.01%** (start $500.00) |
| Cash | $397.81 |
| Deployed | $17.11 (4.1%) |
| Open positions | 3 / 8 |
| Closed trades | 22 (2W / 20L, WR 9%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $9.15 |
| Ticks run | 1621 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SHIT | solana | $5.00 | $7.42 | +100% | +144% | 13.2h |
| FOOD | solana | $5.05 | $4.96 | -1% | +17% | 7.9h |
| GTA | solana | $5.00 | $4.74 | -4% | +4% | 0.8h |

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
  shadow: tracking 18, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $415.38 (-16.92% since start)
tick #1611  equity $415.38  cash $397.81  open 3
exits-only pass. equity $415.28 (next scan in 10 min)
tick #1612  equity $415.28  cash $397.81  open 3
exits-only pass. equity $415.30 (next scan in 9 min)
tick #1613  equity $415.30  cash $397.81  open 3
exits-only pass. equity $415.54 (next scan in 8 min)
tick #1614  equity $415.54  cash $397.81  open 3
exits-only pass. equity $415.30 (next scan in 7 min)
tick #1615  equity $415.30  cash $397.81  open 3
exits-only pass. equity $415.21 (next scan in 6 min)
tick #1616  equity $415.21  cash $397.81  open 3
exits-only pass. equity $415.43 (next scan in 5 min)
tick #1617  equity $415.43  cash $397.81  open 3
exits-only pass. equity $415.16 (next scan in 4 min)
tick #1618  equity $415.16  cash $397.81  open 3
exits-only pass. equity $415.25 (next scan in 3 min)
tick #1619  equity $415.25  cash $397.81  open 3
exits-only pass. equity $415.11 (next scan in 2 min)
tick #1620  equity $415.11  cash $397.81  open 3
exits-only pass. equity $414.86 (next scan in 1 min)
tick #1621  equity $414.86  cash $397.81  open 3
  scanning chains + news...
  131 raw candidates across 4 chains, 160 headlines/posts
  2 passed gates | rejected: liquidity too thin x87, no h1 volume x30, too old x8, too new (bot war) x2, already discovered x2
  top: bill 0.61 | GTA 0.36
  tick bar 0.61 (top 10% of 2, floor 0.45)
  skip bill: solana concentration cap
  skip GTA: already held
  no entries this tick
  shadow: tracking 18, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
