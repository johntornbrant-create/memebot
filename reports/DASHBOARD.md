# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T20:21:56+00:00`

## Equity

| | |
|---|---|
| Equity | **$382.83** |
| Return | **-23.43%** (start $500.00) |
| Cash | $370.64 |
| Deployed | $12.18 (3.2%) |
| Open positions | 4 / 8 |
| Closed trades | 31 (4W / 27L, WR 13%) |
| Profit factor | 0.38 |
| Fees + slippage paid | $42.99 |
| Ticks run | 1910 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.59 | -28% | +17% | 21.0h |
| WASTED | ethereum | $5.00 | $4.09 | +270% | +314% | 1.6h |
| GATO | ethereum | $5.00 | $2.23 | +14% | +44% | 1.2h |
| Macca | ethereum | $5.00 | $2.27 | +15% | +16% | 0.6h |

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
  tick bar 0.64 (top 10% of 13, floor 0.45)
  no entries this tick
  shadow: tracking 34, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
done. equity $382.55 (-23.49% since start)
tick #1900  equity $382.55  cash $370.64  open 4
exits-only pass. equity $382.98 (next scan in 10 min)
tick #1901  equity $382.98  cash $370.64  open 4
exits-only pass. equity $382.92 (next scan in 9 min)
tick #1902  equity $382.92  cash $370.64  open 4
exits-only pass. equity $382.75 (next scan in 8 min)
tick #1903  equity $382.75  cash $370.64  open 4
exits-only pass. equity $382.43 (next scan in 7 min)
tick #1904  equity $382.43  cash $370.64  open 4
exits-only pass. equity $382.69 (next scan in 6 min)
tick #1905  equity $382.69  cash $370.64  open 4
exits-only pass. equity $383.01 (next scan in 5 min)
tick #1906  equity $383.01  cash $370.64  open 4
exits-only pass. equity $382.96 (next scan in 4 min)
tick #1907  equity $382.96  cash $370.64  open 4
exits-only pass. equity $383.00 (next scan in 3 min)
tick #1908  equity $383.00  cash $370.64  open 4
exits-only pass. equity $382.68 (next scan in 2 min)
tick #1909  equity $382.68  cash $370.64  open 4
exits-only pass. equity $382.62 (next scan in 1 min)
tick #1910  equity $382.62  cash $370.64  open 4
  scanning chains + news...
  159 raw candidates across 9 chains, 160 headlines/posts
  12 passed gates | rejected: liquidity too thin x84, no h1 volume x39, too old x14, already discovered x7, too new (bot war) x1
  top: GATO 0.77 | WASTED 0.73 | bill 0.61 | ANT 0.55 | Anthropig 0.55
  tick bar 0.64 (top 10% of 12, floor 0.45)
  no entries this tick
  shadow: tracking 34, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
  entries blocked: daily trade cap reached
```
