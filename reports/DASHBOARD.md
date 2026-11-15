# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T11:35:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$409.07** |
| Return | **-18.19%** (start $500.00) |
| Cash | $394.84 |
| Deployed | $14.23 (3.5%) |
| Open positions | 3 / 8 |
| Closed trades | 27 (4W / 23L, WR 15%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $18.78 |
| Ticks run | 1863 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $4.28 | -14% | +17% | 12.3h |
| GTA | solana | $5.00 | $6.05 | +22% | +43% | 5.2h |
| Socks | solana | $5.00 | $3.91 | +5% | +60% | 0.6h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| Macca | $-1.92 | -38% | 0.8h | stop loss -36% |
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
  no entries this tick
  shadow: tracking 20, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $412.00 (-17.60% since start)
tick #1853  equity $412.00  cash $391.76  open 4
exits-only pass. equity $411.47 (next scan in 10 min)
tick #1854  equity $411.47  cash $391.76  open 4
exits-only pass. equity $411.83 (next scan in 9 min)
tick #1855  equity $411.83  cash $391.76  open 4
exits-only pass. equity $412.31 (next scan in 8 min)
tick #1856  equity $412.31  cash $391.76  open 4
exits-only pass. equity $412.31 (next scan in 7 min)
tick #1857  equity $412.31  cash $391.76  open 4
exits-only pass. equity $411.53 (next scan in 6 min)
tick #1858  equity $411.53  cash $391.76  open 4
exits-only pass. equity $410.16 (next scan in 5 min)
tick #1859  equity $410.16  cash $391.76  open 4
exits-only pass. equity $410.22 (next scan in 4 min)
tick #1860  equity $410.22  cash $391.76  open 4
exits-only pass. equity $410.46 (next scan in 3 min)
tick #1861  equity $410.46  cash $391.76  open 4
exits-only pass. equity $409.49 (next scan in 2 min)
tick #1862  equity $409.49  cash $391.76  open 4
  SELL Macca      100% @ $2.74  ->  $3.08   [stop loss -36%]
exits-only pass. equity $409.14 (next scan in 1 min)
tick #1863  equity $409.14  cash $394.84  open 3
  scanning chains + news...
  101 raw candidates across 5 chains, 160 headlines/posts
  4 passed gates | rejected: liquidity too thin x57, no h1 volume x23, too old x11, already discovered x6
  top: LETSWIN 0.81 | Macca 0.61 | GETAJOB 0.52 | Socks 0.25
  tick bar 0.62 (top 10% of 4, floor 0.45)
  skip LETSWIN: blacklisted (previously stopped out)
  skip Socks: already held
  no entries this tick
  shadow: tracking 20, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
