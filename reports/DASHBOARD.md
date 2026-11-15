# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T10:35:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$417.70** |
| Return | **-16.46%** (start $500.00) |
| Cash | $400.13 |
| Deployed | $17.57 (4.2%) |
| Open positions | 3 / 8 |
| Closed trades | 24 (3W / 21L, WR 12%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $9.43 |
| Ticks run | 1808 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $4.48 | -10% | +17% | 11.3h |
| GTA | solana | $5.00 | $6.41 | +30% | +43% | 4.2h |
| Socks | solana | $5.00 | $6.67 | +80% | +103% | 0.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| KURUMI | $+5.28 | +58% | 6.0h | ratchet +65% (peak +136%) |

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
  tick bar 0.45 (top 10% of 1, floor 0.45)
  BUY[explore] Socks      $5.00 @ $0.0001739  score 0.39  solana  liq $29,573
  shadow: tracking 17, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $414.42 (-17.12% since start)
tick #1798  equity $414.42  cash $398.29  open 3
exits-only pass. equity $416.57 (next scan in 10 min)
tick #1799  equity $416.57  cash $398.29  open 3
  SELL Socks      25% @ $0.0002644  ->  $1.85   [take profit +50% (sold 25%)]
exits-only pass. equity $416.68 (next scan in 9 min)
tick #1800  equity $416.68  cash $400.13  open 3
exits-only pass. equity $416.83 (next scan in 8 min)
tick #1801  equity $416.83  cash $400.13  open 3
exits-only pass. equity $416.68 (next scan in 7 min)
tick #1802  equity $416.68  cash $400.13  open 3
exits-only pass. equity $415.80 (next scan in 6 min)
tick #1803  equity $415.80  cash $400.13  open 3
exits-only pass. equity $415.99 (next scan in 5 min)
tick #1804  equity $415.99  cash $400.13  open 3
exits-only pass. equity $418.46 (next scan in 4 min)
tick #1805  equity $418.46  cash $400.13  open 3
exits-only pass. equity $417.63 (next scan in 3 min)
tick #1806  equity $417.63  cash $400.13  open 3
exits-only pass. equity $417.51 (next scan in 2 min)
tick #1807  equity $417.51  cash $400.13  open 3
exits-only pass. equity $417.41 (next scan in 1 min)
tick #1808  equity $417.41  cash $400.13  open 3
  scanning chains + news...
  141 raw candidates across 7 chains, 160 headlines/posts
  1 passed gates | rejected: liquidity too thin x105, no h1 volume x24, already discovered x7, too old x4
  top: Socks 0.44
  tick bar 0.45 (top 10% of 1, floor 0.45)
  skip Socks: already held
  no entries this tick
  shadow: tracking 17, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
