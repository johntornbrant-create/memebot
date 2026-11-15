# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T19:46:10+00:00`

## Equity

| | |
|---|---|
| Equity | **$388.62** |
| Return | **-22.28%** (start $500.00) |
| Cash | $365.67 |
| Deployed | $22.95 (5.9%) |
| Open positions | 6 / 8 |
| Closed trades | 29 (4W / 25L, WR 14%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $42.92 |
| Ticks run | 1877 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.71 | -26% | +17% | 20.5h |
| GTA | solana | $5.00 | $5.08 | +3% | +43% | 13.4h |
| BEAR | solana | $5.00 | $3.96 | -20% | +5% | 1.0h |
| WASTED | ethereum | $5.00 | $3.15 | +185% | +217% | 1.0h |
| GATO | ethereum | $5.00 | $2.05 | +5% | +19% | 0.6h |
| Macca | ethereum | $5.00 | $1.96 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| JASON | $-5.00 | -100% | 0.6h | stop loss -41% |
| GTA | $-5.00 | -100% | 1.1h | stop loss -99% |
| LETSWIN | $-5.00 | -100% | 5.6h | stop loss -83% |
| Socks | $+0.41 | +8% | 7.2h | ratchet +42% (peak +103%) |
| Macca | $-3.03 | -61% | 1.2h | stop loss -59% |
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

## Learned weights (v169)

_refit on 1806 observations (1699 shadow, 107 real), 494 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.152 |
| turnover | +0.127 |
| liq_quality | +0.096 |
| momentum_accel | +0.065 |
| buy_pressure | +0.062 |
| paid_boost | +0.034 |
| fdv_sanity | +0.030 |
| not_vertical | -0.029 |
| dip_in_uptrend | +0.025 |
| buzz | +0.019 |
| age_sweet | +0.009 |
| socials | -0.004 |

## Last run log
```
  skip gtacoin: solana concentration cap
  skip SWJ: solana concentration cap
  no entries this tick
  shadow: tracking 31, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $388.54 (-22.29% since start)
tick #1867  equity $388.54  cash $370.67  open 5
exits-only pass. equity $388.22 (next scan in 10 min)
tick #1868  equity $388.22  cash $370.67  open 5
exits-only pass. equity $388.62 (next scan in 9 min)
tick #1869  equity $388.62  cash $370.67  open 5
exits-only pass. equity $389.01 (next scan in 8 min)
tick #1870  equity $389.01  cash $370.67  open 5
exits-only pass. equity $389.28 (next scan in 7 min)
tick #1871  equity $389.28  cash $370.67  open 5
exits-only pass. equity $389.66 (next scan in 6 min)
tick #1872  equity $389.66  cash $370.67  open 5
exits-only pass. equity $389.71 (next scan in 5 min)
tick #1873  equity $389.71  cash $370.67  open 5
exits-only pass. equity $390.07 (next scan in 4 min)
tick #1874  equity $390.07  cash $370.67  open 5
exits-only pass. equity $389.37 (next scan in 3 min)
tick #1875  equity $389.37  cash $370.67  open 5
exits-only pass. equity $389.25 (next scan in 2 min)
tick #1876  equity $389.25  cash $370.67  open 5
exits-only pass. equity $389.01 (next scan in 1 min)
tick #1877  equity $389.01  cash $370.67  open 5
  scanning chains + news...
  164 raw candidates across 7 chains, 160 headlines/posts
  11 passed gates | rejected: liquidity too thin x101, no h1 volume x38, already discovered x7, too old x6, unknown age x1
  top: GATO 0.79 | WISHMAS 0.76 | WASTED 0.76 | Anthropig 0.67 | ANT 0.66
  tick bar 0.64 (top 10% of 11, floor 0.45)
  skip Anthropig: solana concentration cap
  BUY[explore] Macca      $5.00 @ $0.01483  score 0.51  ethereum  liq $327,382
  shadow: tracking 31, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
