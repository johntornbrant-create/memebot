# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T19:58:09+00:00`

## Equity

| | |
|---|---|
| Equity | **$381.91** |
| Return | **-23.62%** (start $500.00) |
| Cash | $370.64 |
| Deployed | $11.27 (3.0%) |
| Open positions | 4 / 8 |
| Closed trades | 31 (4W / 27L, WR 13%) |
| Profit factor | 0.38 |
| Fees + slippage paid | $42.99 |
| Ticks run | 1888 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.79 | -24% | +17% | 20.7h |
| WASTED | ethereum | $5.00 | $3.00 | +171% | +220% | 1.2h |
| GATO | ethereum | $5.00 | $2.36 | +20% | +20% | 0.8h |
| Macca | ethereum | $5.00 | $2.12 | +8% | +8% | 0.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| BEAR | $-4.85 | -97% | 1.1h | stop loss -97% |
| GTA | $-0.17 | -3% | 13.4h | ratchet +0% (peak +43%) |
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
  BUY[explore] Macca      $5.00 @ $0.01483  score 0.51  ethereum  liq $327,382
  shadow: tracking 31, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $388.62 (-22.28% since start)
tick #1878  equity $388.62  cash $365.67  open 6
exits-only pass. equity $385.58 (next scan in 10 min)
tick #1879  equity $385.58  cash $365.67  open 6
exits-only pass. equity $385.36 (next scan in 9 min)
tick #1880  equity $385.36  cash $365.67  open 6
  SELL GTA        100% @ $8.825e-05  ->  $4.83   [ratchet +0% (peak +43%)]
exits-only pass. equity $385.49 (next scan in 8 min)
tick #1881  equity $385.49  cash $370.50  open 5
  SELL BEAR       100% @ $4.059e-06  ->  $0.15   [stop loss -97%]
exits-only pass. equity $381.89 (next scan in 7 min)
tick #1882  equity $381.89  cash $370.64  open 4
exits-only pass. equity $381.92 (next scan in 6 min)
tick #1883  equity $381.92  cash $370.64  open 4
exits-only pass. equity $381.93 (next scan in 5 min)
tick #1884  equity $381.93  cash $370.64  open 4
exits-only pass. equity $382.06 (next scan in 4 min)
tick #1885  equity $382.06  cash $370.64  open 4
exits-only pass. equity $382.08 (next scan in 3 min)
tick #1886  equity $382.08  cash $370.64  open 4
exits-only pass. equity $381.93 (next scan in 2 min)
tick #1887  equity $381.93  cash $370.64  open 4
exits-only pass. equity $382.04 (next scan in 1 min)
tick #1888  equity $382.04  cash $370.64  open 4
  scanning chains + news...
  157 raw candidates across 7 chains, 160 headlines/posts
  12 passed gates | rejected: liquidity too thin x93, no h1 volume x35, too old x8, already discovered x8, unknown age x1
  top: GATO 0.79 | WISHMAS 0.76 | WASTED 0.72 | ANT 0.65 | Anthropig 0.59
  tick bar 0.64 (top 10% of 12, floor 0.45)
  no entries this tick
  shadow: tracking 32, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
```
