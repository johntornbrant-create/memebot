# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T11:47:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$408.82** |
| Return | **-18.24%** (start $500.00) |
| Cash | $394.84 |
| Deployed | $13.97 (3.4%) |
| Open positions | 3 / 8 |
| Closed trades | 27 (4W / 23L, WR 15%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $18.78 |
| Ticks run | 1874 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $4.39 | -12% | +17% | 12.5h |
| GTA | solana | $5.00 | $5.33 | +8% | +43% | 5.4h |
| Socks | solana | $5.00 | $4.26 | +15% | +60% | 0.8h |

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
  skip Socks: already held
  no entries this tick
  shadow: tracking 20, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $409.07 (-18.19% since start)
tick #1864  equity $409.07  cash $394.84  open 3
exits-only pass. equity $409.84 (next scan in 10 min)
tick #1865  equity $409.84  cash $394.84  open 3
exits-only pass. equity $410.39 (next scan in 9 min)
tick #1866  equity $410.39  cash $394.84  open 3
exits-only pass. equity $410.17 (next scan in 8 min)
tick #1867  equity $410.17  cash $394.84  open 3
exits-only pass. equity $410.17 (next scan in 7 min)
tick #1868  equity $410.17  cash $394.84  open 3
exits-only pass. equity $409.81 (next scan in 6 min)
tick #1869  equity $409.81  cash $394.84  open 3
exits-only pass. equity $409.67 (next scan in 5 min)
tick #1870  equity $409.67  cash $394.84  open 3
exits-only pass. equity $409.51 (next scan in 4 min)
tick #1871  equity $409.51  cash $394.84  open 3
exits-only pass. equity $408.89 (next scan in 3 min)
tick #1872  equity $408.89  cash $394.84  open 3
exits-only pass. equity $408.94 (next scan in 2 min)
tick #1873  equity $408.94  cash $394.84  open 3
exits-only pass. equity $408.74 (next scan in 1 min)
tick #1874  equity $408.74  cash $394.84  open 3
  scanning chains + news...
  101 raw candidates across 5 chains, 160 headlines/posts
  3 passed gates | rejected: liquidity too thin x58, no h1 volume x23, too old x11, already discovered x6
  top: GETAJOB 0.67 | Macca 0.59 | Socks 0.25
  tick bar 0.62 (top 10% of 3, floor 0.45)
  skip GETAJOB: solana concentration cap
  skip Macca: blacklisted (previously stopped out)
  no entries this tick
  shadow: tracking 20, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
