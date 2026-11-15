# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T19:33:56+00:00`

## Equity

| | |
|---|---|
| Equity | **$388.54** |
| Return | **-22.29%** (start $500.00) |
| Cash | $370.67 |
| Deployed | $17.88 (4.6%) |
| Open positions | 5 / 8 |
| Closed trades | 29 (4W / 25L, WR 14%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $39.88 |
| Ticks run | 1866 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.55 | -29% | +17% | 20.2h |
| GTA | solana | $5.00 | $5.46 | +10% | +43% | 13.2h |
| BEAR | solana | $5.00 | $4.77 | -3% | +5% | 0.8h |
| WASTED | ethereum | $5.00 | $2.39 | +117% | +159% | 0.8h |
| GATO | ethereum | $5.00 | $1.70 | -13% | +9% | 0.4h |

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
  shadow: tracking 28, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $391.26 (-21.75% since start)
tick #1856  equity $391.26  cash $370.67  open 6
exits-only pass. equity $391.25 (next scan in 10 min)
tick #1857  equity $391.25  cash $370.67  open 6
exits-only pass. equity $391.06 (next scan in 9 min)
tick #1858  equity $391.06  cash $370.67  open 6
exits-only pass. equity $391.27 (next scan in 8 min)
tick #1859  equity $391.27  cash $370.67  open 6
  SELL WASTED     25% @ $0.001713  ->  $0.00   [take profit +150% (sold 25%)]
exits-only pass. equity $390.44 (next scan in 7 min)
tick #1860  equity $390.44  cash $370.67  open 6
exits-only pass. equity $390.03 (next scan in 6 min)
tick #1861  equity $390.03  cash $370.67  open 6
exits-only pass. equity $389.91 (next scan in 5 min)
tick #1862  equity $389.91  cash $370.67  open 6
exits-only pass. equity $390.18 (next scan in 4 min)
tick #1863  equity $390.18  cash $370.67  open 6
exits-only pass. equity $390.22 (next scan in 3 min)
tick #1864  equity $390.22  cash $370.67  open 6
exits-only pass. equity $389.58 (next scan in 2 min)
tick #1865  equity $389.58  cash $370.67  open 6
  SELL JASON      100% @ $0.0004097  ->  $0.00   [stop loss -41%]
exits-only pass. equity $388.51 (next scan in 1 min)
tick #1866  equity $388.51  cash $370.67  open 5
  scanning chains + news...
  161 raw candidates across 9 chains, 160 headlines/posts
  11 passed gates | rejected: liquidity too thin x84, no h1 volume x48, too old x8, already discovered x7, sell pressure x1
  top: GATO 0.78 | WISHMAS 0.77 | Anthropig 0.75 | ANT 0.68 | WASTED 0.67
  tick bar 0.64 (top 10% of 11, floor 0.45)
  skip gtacoin: solana concentration cap
  skip SWJ: solana concentration cap
  no entries this tick
  shadow: tracking 31, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
