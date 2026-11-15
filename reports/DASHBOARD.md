# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T11:59:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$407.85** |
| Return | **-18.43%** (start $500.00) |
| Cash | $398.44 |
| Deployed | $9.42 (2.3%) |
| Open positions | 2 / 8 |
| Closed trades | 28 (5W / 23L, WR 18%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $18.82 |
| Ticks run | 1885 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.99 | -20% | +17% | 12.7h |
| GTA | solana | $5.00 | $5.43 | +10% | +43% | 5.6h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| Socks | $+0.46 | +9% | 0.8h | ratchet +0% (peak +60%) |
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
done. equity $408.82 (-18.24% since start)
tick #1875  equity $408.82  cash $394.84  open 3
  SELL Socks      100% @ $0.0003068  ->  $3.60   [ratchet +0% (peak +60%)]
exits-only pass. equity $407.90 (next scan in 10 min)
tick #1876  equity $407.90  cash $398.44  open 2
exits-only pass. equity $407.99 (next scan in 9 min)
tick #1877  equity $407.99  cash $398.44  open 2
exits-only pass. equity $407.91 (next scan in 8 min)
tick #1878  equity $407.91  cash $398.44  open 2
exits-only pass. equity $407.74 (next scan in 7 min)
tick #1879  equity $407.74  cash $398.44  open 2
exits-only pass. equity $407.64 (next scan in 6 min)
tick #1880  equity $407.64  cash $398.44  open 2
exits-only pass. equity $407.86 (next scan in 5 min)
tick #1881  equity $407.86  cash $398.44  open 2
exits-only pass. equity $407.79 (next scan in 4 min)
tick #1882  equity $407.79  cash $398.44  open 2
exits-only pass. equity $407.72 (next scan in 3 min)
tick #1883  equity $407.72  cash $398.44  open 2
exits-only pass. equity $408.00 (next scan in 2 min)
tick #1884  equity $408.00  cash $398.44  open 2
exits-only pass. equity $407.93 (next scan in 1 min)
tick #1885  equity $407.93  cash $398.44  open 2
  scanning chains + news...
  99 raw candidates across 5 chains, 160 headlines/posts
  4 passed gates | rejected: liquidity too thin x55, no h1 volume x23, too old x11, already discovered x6
  top: LETSWIN 0.68 | GETAJOB 0.66 | Macca 0.59 | Socks 0.22
  tick bar 0.62 (top 10% of 4, floor 0.45)
  skip Macca: blacklisted (previously stopped out)
  skip LETSWIN: blacklisted (previously stopped out)
  no entries this tick
  shadow: tracking 20, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
