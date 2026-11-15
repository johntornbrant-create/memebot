# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T08:23:30+00:00`

## Equity

| | |
|---|---|
| Equity | **$416.28** |
| Return | **-16.74%** (start $500.00) |
| Cash | $400.13 |
| Deployed | $16.15 (3.9%) |
| Open positions | 3 / 8 |
| Closed trades | 22 (2W / 20L, WR 9%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $9.18 |
| Ticks run | 1687 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SHIT | solana | $5.00 | $5.78 | +108% | +172% | 14.4h |
| FOOD | solana | $5.05 | $5.05 | +1% | +17% | 9.1h |
| GTA | solana | $5.00 | $5.31 | +7% | +12% | 2.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| LUCIA | $-9.39 | -99% | 1.9h | stop loss -99% |

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
  tick bar 0.45 (top 10% of 2, floor 0.45)
  no entries this tick
  shadow: tracking 15, closed 4 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $417.27 (-16.55% since start)
tick #1677  equity $417.27  cash $400.13  open 3
exits-only pass. equity $417.09 (next scan in 10 min)
tick #1678  equity $417.09  cash $400.13  open 3
exits-only pass. equity $416.86 (next scan in 9 min)
tick #1679  equity $416.86  cash $400.13  open 3
exits-only pass. equity $416.91 (next scan in 8 min)
tick #1680  equity $416.91  cash $400.13  open 3
exits-only pass. equity $416.86 (next scan in 7 min)
tick #1681  equity $416.86  cash $400.13  open 3
exits-only pass. equity $416.82 (next scan in 6 min)
tick #1682  equity $416.82  cash $400.13  open 3
exits-only pass. equity $416.66 (next scan in 5 min)
tick #1683  equity $416.66  cash $400.13  open 3
exits-only pass. equity $416.71 (next scan in 4 min)
tick #1684  equity $416.71  cash $400.13  open 3
exits-only pass. equity $416.77 (next scan in 3 min)
tick #1685  equity $416.77  cash $400.13  open 3
exits-only pass. equity $416.63 (next scan in 2 min)
tick #1686  equity $416.63  cash $400.13  open 3
exits-only pass. equity $416.70 (next scan in 1 min)
tick #1687  equity $416.70  cash $400.13  open 3
  scanning chains + news...
  133 raw candidates across 6 chains, 160 headlines/posts
  3 passed gates | rejected: liquidity too thin x94, no h1 volume x30, too old x3, already discovered x3
  top: CLOCKED 0.51 | GTA 0.29 | HOGE 0.21
  tick bar 0.51 (top 10% of 3, floor 0.45)
  skip CLOCKED: solana concentration cap
  skip HOGE: solana concentration cap
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
