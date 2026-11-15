# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T11:23:29+00:00`

## Equity

| | |
|---|---|
| Equity | **$412.00** |
| Return | **-17.60%** (start $500.00) |
| Cash | $391.76 |
| Deployed | $20.24 (4.9%) |
| Open positions | 4 / 8 |
| Closed trades | 26 (4W / 22L, WR 15%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $18.71 |
| Ticks run | 1852 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.91 | -22% | +17% | 12.1h |
| GTA | solana | $5.00 | $6.33 | +28% | +43% | 5.0h |
| Macca | bsc | $5.00 | $4.65 | -5% | +14% | 0.6h |
| Socks | solana | $5.00 | $5.35 | +44% | +53% | 0.4h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| LETSWIN | $-5.00 | -100% | 0.2h | ratchet +0% (peak +64%) |
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
  shadow: tracking 20, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $415.50 (-16.90% since start)
tick #1842  equity $415.50  cash $389.90  open 5
exits-only pass. equity $412.50 (next scan in 10 min)
tick #1843  equity $412.50  cash $389.90  open 5
exits-only pass. equity $413.19 (next scan in 9 min)
tick #1844  equity $413.19  cash $389.90  open 5
  SELL LETSWIN    25% @ $0.001597  ->  $0.00   [take profit +50% (sold 25%)]
exits-only pass. equity $411.73 (next scan in 8 min)
tick #1845  equity $411.73  cash $389.90  open 5
exits-only pass. equity $411.97 (next scan in 7 min)
tick #1846  equity $411.97  cash $389.90  open 5
exits-only pass. equity $412.79 (next scan in 6 min)
tick #1847  equity $412.79  cash $389.90  open 5
exits-only pass. equity $412.51 (next scan in 5 min)
tick #1848  equity $412.51  cash $389.90  open 5
exits-only pass. equity $412.54 (next scan in 4 min)
tick #1849  equity $412.54  cash $389.90  open 5
exits-only pass. equity $413.36 (next scan in 3 min)
tick #1850  equity $413.36  cash $389.90  open 5
  SELL Socks      25% @ $0.0004783  ->  $1.86   [take profit +50% (sold 25%)]
exits-only pass. equity $414.01 (next scan in 2 min)
tick #1851  equity $414.01  cash $391.76  open 5
  SELL LETSWIN    100% @ $0.0008371  ->  $0.00   [ratchet +0% (peak +64%)]
exits-only pass. equity $412.35 (next scan in 1 min)
tick #1852  equity $412.35  cash $391.76  open 4
  scanning chains + news...
  102 raw candidates across 5 chains, 160 headlines/posts
  4 passed gates | rejected: liquidity too thin x58, no h1 volume x23, too old x11, already discovered x6
  top: LETSWIN 0.86 | Macca 0.61 | GETAJOB 0.56 | Socks 0.29
  tick bar 0.62 (top 10% of 4, floor 0.45)
  skip LETSWIN: blacklisted (previously stopped out)
  no entries this tick
  shadow: tracking 20, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
