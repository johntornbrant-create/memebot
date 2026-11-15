# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T07:23:30+00:00`

## Equity

| | |
|---|---|
| Equity | **$415.11** |
| Return | **-16.98%** (start $500.00) |
| Cash | $397.81 |
| Deployed | $17.29 (4.2%) |
| Open positions | 3 / 8 |
| Closed trades | 22 (2W / 20L, WR 9%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $9.15 |
| Ticks run | 1632 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SHIT | solana | $5.00 | $7.41 | +100% | +144% | 13.4h |
| FOOD | solana | $5.05 | $4.99 | -0% | +17% | 8.1h |
| GTA | solana | $5.00 | $4.89 | -1% | +4% | 1.0h |

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
  skip GTA: already held
  no entries this tick
  shadow: tracking 18, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $414.93 (-17.01% since start)
tick #1622  equity $414.93  cash $397.81  open 3
exits-only pass. equity $414.96 (next scan in 10 min)
tick #1623  equity $414.96  cash $397.81  open 3
exits-only pass. equity $414.97 (next scan in 9 min)
tick #1624  equity $414.97  cash $397.81  open 3
exits-only pass. equity $414.86 (next scan in 8 min)
tick #1625  equity $414.86  cash $397.81  open 3
exits-only pass. equity $414.93 (next scan in 7 min)
tick #1626  equity $414.93  cash $397.81  open 3
exits-only pass. equity $414.95 (next scan in 6 min)
tick #1627  equity $414.95  cash $397.81  open 3
exits-only pass. equity $415.06 (next scan in 5 min)
tick #1628  equity $415.06  cash $397.81  open 3
exits-only pass. equity $414.89 (next scan in 4 min)
tick #1629  equity $414.89  cash $397.81  open 3
exits-only pass. equity $415.02 (next scan in 3 min)
tick #1630  equity $415.02  cash $397.81  open 3
exits-only pass. equity $415.10 (next scan in 2 min)
tick #1631  equity $415.10  cash $397.81  open 3
exits-only pass. equity $415.20 (next scan in 1 min)
tick #1632  equity $415.20  cash $397.81  open 3
  scanning chains + news...
  133 raw candidates across 4 chains, 160 headlines/posts
  3 passed gates | rejected: liquidity too thin x90, no h1 volume x32, too old x6, already discovered x2
  top: bill 0.60 | HOGE 0.41 | GTA 0.28
  tick bar 0.60 (top 10% of 3, floor 0.45)
  skip bill: solana concentration cap
  no entries this tick
  shadow: tracking 19, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
