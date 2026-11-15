# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T10:59:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$415.31** |
| Return | **-16.94%** (start $500.00) |
| Cash | $394.90 |
| Deployed | $20.41 (4.9%) |
| Open positions | 4 / 8 |
| Closed trades | 25 (4W / 21L, WR 16%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $9.62 |
| Ticks run | 1830 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.76 | -25% | +17% | 11.7h |
| GTA | solana | $5.00 | $6.27 | +27% | +43% | 4.6h |
| Macca | bsc | $5.00 | $5.39 | +10% | +14% | 0.2h |
| Socks | solana | $5.00 | $4.94 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| Socks | $+1.61 | +32% | 0.4h | ratchet +42% (peak +103%) |
| HOGE | $-1.94 | -39% | 0.2h | stop loss -37% |
| SHIT | $+4.56 | +91% | 14.6h | ratchet +90% (peak +172%) |
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
  BUY[exploit] Macca      $5.00 @ $4.27  score 0.51  bsc  liq $795,832
  skip Socks: already held
  shadow: tracking 18, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $416.20 (-16.76% since start)
tick #1820  equity $416.20  cash $395.13  open 4
  SELL Socks      100% @ $0.000226  ->  $4.76   [ratchet +42% (peak +103%)]
exits-only pass. equity $415.02 (next scan in 10 min)
tick #1821  equity $415.02  cash $399.90  open 3
exits-only pass. equity $415.41 (next scan in 9 min)
tick #1822  equity $415.41  cash $399.90  open 3
exits-only pass. equity $415.03 (next scan in 8 min)
tick #1823  equity $415.03  cash $399.90  open 3
exits-only pass. equity $414.74 (next scan in 7 min)
tick #1824  equity $414.74  cash $399.90  open 3
exits-only pass. equity $415.10 (next scan in 6 min)
tick #1825  equity $415.10  cash $399.90  open 3
exits-only pass. equity $415.30 (next scan in 5 min)
tick #1826  equity $415.30  cash $399.90  open 3
exits-only pass. equity $415.69 (next scan in 4 min)
tick #1827  equity $415.69  cash $399.90  open 3
exits-only pass. equity $415.47 (next scan in 3 min)
tick #1828  equity $415.47  cash $399.90  open 3
exits-only pass. equity $415.09 (next scan in 2 min)
tick #1829  equity $415.09  cash $399.90  open 3
exits-only pass. equity $414.95 (next scan in 1 min)
tick #1830  equity $414.95  cash $399.90  open 3
  scanning chains + news...
  145 raw candidates across 7 chains, 160 headlines/posts
  2 passed gates | rejected: liquidity too thin x110, no h1 volume x24, already discovered x7, too old x2
  top: Macca 0.59 | Socks 0.45
  tick bar 0.59 (top 10% of 2, floor 0.45)
  skip Macca: already held
  BUY[explore] Socks      $5.00 @ $0.0003123  score 0.45  solana  liq $41,399
  shadow: tracking 18, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
