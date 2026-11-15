# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T11:11:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$415.50** |
| Return | **-16.90%** (start $500.00) |
| Cash | $389.90 |
| Deployed | $25.60 (6.2%) |
| Open positions | 5 / 8 |
| Closed trades | 25 (4W / 21L, WR 16%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $12.66 |
| Ticks run | 1841 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.69 | -26% | +17% | 11.9h |
| GTA | solana | $5.00 | $6.19 | +25% | +43% | 4.8h |
| Macca | bsc | $5.00 | $4.87 | -1% | +14% | 0.4h |
| Socks | solana | $5.00 | $5.85 | +18% | +18% | 0.2h |
| LETSWIN | ethereum | $5.00 | $1.96 | +0% | +0% | 0.0h |

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
  tick bar 0.59 (top 10% of 2, floor 0.45)
  skip Macca: already held
  BUY[explore] Socks      $5.00 @ $0.0003123  score 0.45  solana  liq $41,399
  shadow: tracking 18, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $415.31 (-16.94% since start)
tick #1831  equity $415.31  cash $394.90  open 4
exits-only pass. equity $414.65 (next scan in 10 min)
tick #1832  equity $414.65  cash $394.90  open 4
exits-only pass. equity $414.74 (next scan in 9 min)
tick #1833  equity $414.74  cash $394.90  open 4
exits-only pass. equity $414.64 (next scan in 8 min)
tick #1834  equity $414.64  cash $394.90  open 4
exits-only pass. equity $414.42 (next scan in 7 min)
tick #1835  equity $414.42  cash $394.90  open 4
exits-only pass. equity $413.94 (next scan in 6 min)
tick #1836  equity $413.94  cash $394.90  open 4
exits-only pass. equity $414.71 (next scan in 5 min)
tick #1837  equity $414.71  cash $394.90  open 4
exits-only pass. equity $414.88 (next scan in 4 min)
tick #1838  equity $414.88  cash $394.90  open 4
exits-only pass. equity $415.18 (next scan in 3 min)
tick #1839  equity $415.18  cash $394.90  open 4
exits-only pass. equity $414.52 (next scan in 2 min)
tick #1840  equity $414.52  cash $394.90  open 4
exits-only pass. equity $414.50 (next scan in 1 min)
tick #1841  equity $414.50  cash $394.90  open 4
  scanning chains + news...
  102 raw candidates across 5 chains, 160 headlines/posts
  4 passed gates | rejected: liquidity too thin x58, no h1 volume x22, too old x12, already discovered x6
  top: LETSWIN 0.79 | Macca 0.60 | GETAJOB 0.55 | Socks 0.47
  tick bar 0.62 (top 10% of 4, floor 0.45)
  BUY[exploit] LETSWIN    $5.00 @ $0.001031  score 0.79  ethereum  liq $31,350
  skip Macca: already held
  shadow: tracking 20, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
