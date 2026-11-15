# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T19:22:09+00:00`

## Equity

| | |
|---|---|
| Equity | **$391.26** |
| Return | **-21.75%** (start $500.00) |
| Cash | $370.67 |
| Deployed | $20.60 (5.3%) |
| Open positions | 6 / 8 |
| Closed trades | 28 (4W / 24L, WR 14%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $33.87 |
| Ticks run | 1855 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.46 | -31% | +17% | 20.1h |
| GTA | solana | $5.00 | $5.74 | +16% | +43% | 13.0h |
| BEAR | solana | $5.00 | $4.83 | -2% | +5% | 0.6h |
| WASTED | ethereum | $5.00 | $3.36 | +128% | +146% | 0.6h |
| JASON | ethereum | $5.00 | $1.56 | -21% | +6% | 0.4h |
| GATO | ethereum | $5.00 | $1.65 | -16% | +0% | 0.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| CATTLEAXE | $-2.39 | -38% | 7.9h | stop loss -37% |

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
  BUY[exploit] GATO       $5.00 @ $0.0001115  score 0.88  ethereum  liq $26,682
  skip gtacoin: solana concentration cap
  shadow: tracking 28, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $393.29 (-21.34% since start)
tick #1845  equity $393.29  cash $370.67  open 6
exits-only pass. equity $389.96 (next scan in 10 min)
tick #1846  equity $389.96  cash $370.67  open 6
exits-only pass. equity $390.31 (next scan in 9 min)
tick #1847  equity $390.31  cash $370.67  open 6
exits-only pass. equity $390.65 (next scan in 8 min)
tick #1848  equity $390.65  cash $370.67  open 6
exits-only pass. equity $390.49 (next scan in 7 min)
tick #1849  equity $390.49  cash $370.67  open 6
exits-only pass. equity $391.19 (next scan in 6 min)
tick #1850  equity $391.19  cash $370.67  open 6
exits-only pass. equity $390.54 (next scan in 5 min)
tick #1851  equity $390.54  cash $370.67  open 6
exits-only pass. equity $390.85 (next scan in 4 min)
tick #1852  equity $390.85  cash $370.67  open 6
exits-only pass. equity $391.38 (next scan in 3 min)
tick #1853  equity $391.38  cash $370.67  open 6
exits-only pass. equity $391.12 (next scan in 2 min)
tick #1854  equity $391.12  cash $370.67  open 6
exits-only pass. equity $390.73 (next scan in 1 min)
tick #1855  equity $390.73  cash $370.67  open 6
  scanning chains + news...
  163 raw candidates across 6 chains, 160 headlines/posts
  8 passed gates | rejected: liquidity too thin x102, no h1 volume x35, already discovered x7, too old x6, too new (bot war) x2
  top: Anthropig 0.78 | GATO 0.75 | WASTED 0.74 | ANT 0.70 | Macca 0.44
  tick bar 0.64 (top 10% of 8, floor 0.45)
  skip Anthropig: solana concentration cap
  skip WASTED: already held
  no entries this tick
  shadow: tracking 28, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
