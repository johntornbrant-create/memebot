# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T20:34:02+00:00`

## Equity

| | |
|---|---|
| Equity | **$378.80** |
| Return | **-24.24%** (start $500.00) |
| Cash | $370.64 |
| Deployed | $8.16 (2.2%) |
| Open positions | 3 / 8 |
| Closed trades | 32 (4W / 28L, WR 12%) |
| Profit factor | 0.38 |
| Fees + slippage paid | $46.01 |
| Ticks run | 1921 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.38 | -32% | +17% | 21.2h |
| GATO | ethereum | $5.00 | $2.67 | +36% | +44% | 1.4h |
| Macca | ethereum | $5.00 | $2.11 | +7% | +16% | 0.8h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| WASTED | $-5.00 | -100% | 1.6h | ratchet +190% (peak +314%) |
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
  no entries this tick
  shadow: tracking 34, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
done. equity $382.83 (-23.43% since start)
tick #1911  equity $382.83  cash $370.64  open 4
exits-only pass. equity $382.15 (next scan in 10 min)
tick #1912  equity $382.15  cash $370.64  open 4
exits-only pass. equity $382.23 (next scan in 9 min)
tick #1913  equity $382.23  cash $370.64  open 4
  SELL WASTED     100% @ $0.00176  ->  $0.00   [ratchet +190% (peak +314%)]
exits-only pass. equity $378.65 (next scan in 8 min)
tick #1914  equity $378.65  cash $370.64  open 3
exits-only pass. equity $378.54 (next scan in 7 min)
tick #1915  equity $378.54  cash $370.64  open 3
exits-only pass. equity $378.59 (next scan in 6 min)
tick #1916  equity $378.59  cash $370.64  open 3
exits-only pass. equity $378.78 (next scan in 5 min)
tick #1917  equity $378.78  cash $370.64  open 3
exits-only pass. equity $378.63 (next scan in 4 min)
tick #1918  equity $378.63  cash $370.64  open 3
exits-only pass. equity $378.68 (next scan in 3 min)
tick #1919  equity $378.68  cash $370.64  open 3
exits-only pass. equity $378.57 (next scan in 2 min)
tick #1920  equity $378.57  cash $370.64  open 3
exits-only pass. equity $378.70 (next scan in 1 min)
tick #1921  equity $378.70  cash $370.64  open 3
  scanning chains + news...
  137 raw candidates across 8 chains, 160 headlines/posts
  12 passed gates | rejected: liquidity too thin x80, no h1 volume x29, already discovered x7, too old x6, too new (bot war) x1
  top: GATO 0.78 | WASTED 0.73 | BUTTHOLE 0.62 | gtacoin 0.61 | TAIL 0.60
  tick bar 0.64 (top 10% of 12, floor 0.45)
  no entries this tick
  shadow: tracking 36, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
```
