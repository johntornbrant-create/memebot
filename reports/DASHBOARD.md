# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T08:35:30+00:00`

## Equity

| | |
|---|---|
| Equity | **$416.22** |
| Return | **-16.76%** (start $500.00) |
| Cash | $405.22 |
| Deployed | $10.99 (2.6%) |
| Open positions | 2 / 8 |
| Closed trades | 23 (3W / 20L, WR 13%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $9.24 |
| Ticks run | 1698 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $5.11 | +2% | +17% | 9.3h |
| GTA | solana | $5.00 | $5.88 | +19% | +19% | 2.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| KURUMI | $+5.28 | +58% | 6.0h | ratchet +65% (peak +136%) |
| MAYA | $-3.58 | -57% | 10.4h | ratchet +25% (peak +94%) |

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
  skip CLOCKED: solana concentration cap
  skip HOGE: solana concentration cap
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $416.28 (-16.74% since start)
tick #1688  equity $416.28  cash $400.13  open 3
exits-only pass. equity $416.26 (next scan in 10 min)
tick #1689  equity $416.26  cash $400.13  open 3
exits-only pass. equity $416.50 (next scan in 9 min)
tick #1690  equity $416.50  cash $400.13  open 3
exits-only pass. equity $416.34 (next scan in 8 min)
tick #1691  equity $416.34  cash $400.13  open 3
exits-only pass. equity $416.35 (next scan in 7 min)
tick #1692  equity $416.35  cash $400.13  open 3
exits-only pass. equity $416.42 (next scan in 6 min)
tick #1693  equity $416.42  cash $400.13  open 3
exits-only pass. equity $416.42 (next scan in 5 min)
tick #1694  equity $416.42  cash $400.13  open 3
exits-only pass. equity $416.48 (next scan in 4 min)
tick #1695  equity $416.48  cash $400.13  open 3
exits-only pass. equity $416.33 (next scan in 3 min)
tick #1696  equity $416.33  cash $400.13  open 3
  SELL SHIT       100% @ $0.000151  ->  $5.09   [ratchet +90% (peak +172%)]
exits-only pass. equity $416.04 (next scan in 2 min)
tick #1697  equity $416.04  cash $405.22  open 2
exits-only pass. equity $415.95 (next scan in 1 min)
tick #1698  equity $415.95  cash $405.22  open 2
  scanning chains + news...
  132 raw candidates across 6 chains, 160 headlines/posts
  3 passed gates | rejected: liquidity too thin x92, no h1 volume x31, too old x3, already discovered x3
  top: CLOCKED 0.38 | GTA 0.33 | HOGE 0.19
  tick bar 0.45 (top 10% of 3, floor 0.45)
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
