# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T18:58:10+00:00`

## Equity

| | |
|---|---|
| Equity | **$397.98** |
| Return | **-20.40%** (start $500.00) |
| Cash | $375.67 |
| Deployed | $22.31 (5.6%) |
| Open positions | 5 / 8 |
| Closed trades | 28 (4W / 24L, WR 14%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $30.83 |
| Ticks run | 1833 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.50 | -30% | +17% | 19.7h |
| GTA | solana | $5.00 | $5.48 | +11% | +43% | 12.6h |
| BEAR | solana | $5.00 | $5.09 | +3% | +5% | 0.2h |
| WASTED | ethereum | $5.00 | $3.24 | +120% | +120% | 0.2h |
| JASON | ethereum | $5.00 | $1.96 | +0% | +0% | 0.0h |

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
  BUY[explore] BEAR       $5.00 @ $0.0001205  score 0.70  solana  liq $32,896
  BUY[explore] WASTED     $5.00 @ $0.0006616  score 0.72  ethereum  liq $67,520
  shadow: tracking 22, closed 4 this tick (3 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $399.60 (-20.08% since start)
tick #1823  equity $399.60  cash $380.67  open 4
exits-only pass. equity $396.10 (next scan in 10 min)
tick #1824  equity $396.10  cash $380.67  open 4
exits-only pass. equity $396.21 (next scan in 9 min)
tick #1825  equity $396.21  cash $380.67  open 4
exits-only pass. equity $396.16 (next scan in 8 min)
tick #1826  equity $396.16  cash $380.67  open 4
exits-only pass. equity $396.19 (next scan in 7 min)
tick #1827  equity $396.19  cash $380.67  open 4
exits-only pass. equity $396.55 (next scan in 6 min)
tick #1828  equity $396.55  cash $380.67  open 4
exits-only pass. equity $396.34 (next scan in 5 min)
tick #1829  equity $396.34  cash $380.67  open 4
exits-only pass. equity $397.40 (next scan in 4 min)
tick #1830  equity $397.40  cash $380.67  open 4
exits-only pass. equity $397.28 (next scan in 3 min)
tick #1831  equity $397.28  cash $380.67  open 4
  SELL WASTED     25% @ $0.001127  ->  $0.00   [take profit +50% (sold 25%)]
exits-only pass. equity $397.14 (next scan in 2 min)
tick #1832  equity $397.14  cash $380.67  open 4
exits-only pass. equity $397.71 (next scan in 1 min)
tick #1833  equity $397.71  cash $380.67  open 4
  scanning chains + news...
  164 raw candidates across 7 chains, 160 headlines/posts
  8 passed gates | rejected: liquidity too thin x85, no h1 volume x46, too old x15, already discovered x8, too new (bot war) x2
  top: WASTED 0.77 | JASON 0.74 | BEAR 0.54 | SWJ 0.54 | BFS 0.48
  tick bar 0.64 (top 10% of 8, floor 0.45)
  skip WASTED: already held
  BUY[explore] JASON      $5.00 @ $0.0006967  score 0.74  ethereum  liq $69,342
  shadow: tracking 25, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
