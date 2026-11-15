# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T20:10:00+00:00`

## Equity

| | |
|---|---|
| Equity | **$382.55** |
| Return | **-23.49%** (start $500.00) |
| Cash | $370.64 |
| Deployed | $11.91 (3.1%) |
| Open positions | 4 / 8 |
| Closed trades | 31 (4W / 27L, WR 13%) |
| Profit factor | 0.38 |
| Fees + slippage paid | $42.99 |
| Ticks run | 1899 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.72 | -26% | +17% | 20.8h |
| WASTED | ethereum | $5.00 | $3.60 | +226% | +255% | 1.4h |
| GATO | ethereum | $5.00 | $2.46 | +25% | +44% | 1.0h |
| Macca | ethereum | $5.00 | $2.13 | +8% | +8% | 0.4h |

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
  tick bar 0.64 (top 10% of 12, floor 0.45)
  no entries this tick
  shadow: tracking 32, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
done. equity $381.91 (-23.62% since start)
tick #1889  equity $381.91  cash $370.64  open 4
exits-only pass. equity $381.59 (next scan in 10 min)
tick #1890  equity $381.59  cash $370.64  open 4
exits-only pass. equity $381.79 (next scan in 9 min)
tick #1891  equity $381.79  cash $370.64  open 4
exits-only pass. equity $382.12 (next scan in 8 min)
tick #1892  equity $382.12  cash $370.64  open 4
exits-only pass. equity $382.03 (next scan in 7 min)
tick #1893  equity $382.03  cash $370.64  open 4
exits-only pass. equity $382.13 (next scan in 6 min)
tick #1894  equity $382.13  cash $370.64  open 4
exits-only pass. equity $382.25 (next scan in 5 min)
tick #1895  equity $382.25  cash $370.64  open 4
exits-only pass. equity $382.30 (next scan in 4 min)
tick #1896  equity $382.30  cash $370.64  open 4
exits-only pass. equity $382.37 (next scan in 3 min)
tick #1897  equity $382.37  cash $370.64  open 4
exits-only pass. equity $382.78 (next scan in 2 min)
tick #1898  equity $382.78  cash $370.64  open 4
exits-only pass. equity $383.17 (next scan in 1 min)
tick #1899  equity $383.17  cash $370.64  open 4
  scanning chains + news...
  184 raw candidates across 9 chains, 160 headlines/posts
  13 passed gates | rejected: liquidity too thin x100, no h1 volume x47, too old x14, already discovered x8, exit-liquidity trap (FDV/liq) x1
  top: GATO 0.78 | WASTED 0.72 | bill 0.63 | Anthropig 0.57 | Socks 0.57
  tick bar 0.64 (top 10% of 13, floor 0.45)
  no entries this tick
  shadow: tracking 34, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
```
