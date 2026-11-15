# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T19:09:58+00:00`

## Equity

| | |
|---|---|
| Equity | **$393.29** |
| Return | **-21.34%** (start $500.00) |
| Cash | $370.67 |
| Deployed | $22.62 (5.8%) |
| Open positions | 6 / 8 |
| Closed trades | 28 (4W / 24L, WR 14%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $33.87 |
| Ticks run | 1844 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.53 | -29% | +17% | 19.8h |
| GTA | solana | $5.00 | $5.60 | +13% | +43% | 12.8h |
| BEAR | solana | $5.00 | $4.62 | -7% | +5% | 0.4h |
| WASTED | ethereum | $5.00 | $2.56 | +74% | +120% | 0.4h |
| JASON | ethereum | $5.00 | $1.32 | -33% | +6% | 0.2h |
| GATO | ethereum | $5.00 | $1.96 | +0% | +0% | 0.0h |

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
  tick bar 0.64 (top 10% of 8, floor 0.45)
  skip WASTED: already held
  BUY[explore] JASON      $5.00 @ $0.0006967  score 0.74  ethereum  liq $69,342
  shadow: tracking 25, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $397.98 (-20.40% since start)
tick #1834  equity $397.98  cash $375.67  open 5
exits-only pass. equity $394.61 (next scan in 10 min)
tick #1835  equity $394.61  cash $375.67  open 5
exits-only pass. equity $394.75 (next scan in 9 min)
tick #1836  equity $394.75  cash $375.67  open 5
exits-only pass. equity $394.53 (next scan in 8 min)
tick #1837  equity $394.53  cash $375.67  open 5
exits-only pass. equity $394.00 (next scan in 7 min)
tick #1838  equity $394.00  cash $375.67  open 5
exits-only pass. equity $394.64 (next scan in 6 min)
tick #1839  equity $394.64  cash $375.67  open 5
exits-only pass. equity $394.70 (next scan in 5 min)
tick #1840  equity $394.70  cash $375.67  open 5
exits-only pass. equity $394.57 (next scan in 4 min)
tick #1841  equity $394.57  cash $375.67  open 5
exits-only pass. equity $394.57 (next scan in 3 min)
tick #1842  equity $394.57  cash $375.67  open 5
exits-only pass. equity $393.83 (next scan in 2 min)
tick #1843  equity $393.83  cash $375.67  open 5
exits-only pass. equity $394.08 (next scan in 1 min)
tick #1844  equity $394.08  cash $375.67  open 5
  scanning chains + news...
  170 raw candidates across 7 chains, 160 headlines/posts
  10 passed gates | rejected: liquidity too thin x101, no h1 volume x45, already discovered x7, too old x6, too new (bot war) x1
  top: GATO 0.88 | WASTED 0.75 | ANT 0.72 | Anthropig 0.70 | SWJ 0.52
  tick bar 0.64 (top 10% of 10, floor 0.45)
  BUY[exploit] GATO       $5.00 @ $0.0001115  score 0.88  ethereum  liq $26,682
  skip gtacoin: solana concentration cap
  shadow: tracking 28, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
