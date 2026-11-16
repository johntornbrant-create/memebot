# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T10:45:30+00:00`

## Equity

| | |
|---|---|
| Equity | **$367.11** |
| Return | **-26.58%** (start $500.00) |
| Cash | $351.21 |
| Deployed | $15.90 (4.3%) |
| Open positions | 4 / 8 |
| Closed trades | 38 (4W / 34L, WR 11%) |
| Profit factor | 0.36 |
| Fees + slippage paid | $52.71 |
| Ticks run | 2255 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.39 | +22% | +29% | 15.0h |
| WISHMAS | solana | $5.00 | $4.52 | -9% | +5% | 10.2h |
| Anthropig | solana | $5.00 | $3.41 | -31% | +13% | 8.8h |
| GTA | solana | $5.00 | $5.58 | +51% | +51% | 3.6h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| mihao | $-1.92 | -38% | 1.1h | stop loss -36% |
| Marvin | $-2.04 | -41% | 0.8h | stop loss -39% |
| Neil | $-1.94 | -39% | 4.2h | stop loss -37% |
| GTAVI | $-3.57 | -71% | 1.4h | stop loss -70% |
| GATO | $-5.00 | -100% | 2.3h | ratchet +55% (peak +121%) |
| FOOD | $-1.85 | -37% | 21.4h | stop loss -35% |
| WASTED | $-5.00 | -100% | 1.6h | ratchet +190% (peak +314%) |
| BEAR | $-4.85 | -97% | 1.1h | stop loss -97% |
| GTA | $-0.17 | -3% | 13.4h | ratchet +0% (peak +43%) |
| JASON | $-5.00 | -100% | 0.6h | stop loss -41% |
| GTA | $-5.00 | -100% | 1.1h | stop loss -99% |
| LETSWIN | $-5.00 | -100% | 5.6h | stop loss -83% |
| Socks | $+0.41 | +8% | 7.2h | ratchet +42% (peak +103%) |
| Macca | $-3.03 | -61% | 1.2h | stop loss -59% |
| HOGE | $-1.94 | -39% | 0.2h | stop loss -37% |

## Learned weights (v170)

_refit on 1825 observations (1708 shadow, 117 real), 498 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.145 |
| turnover | +0.117 |
| liq_quality | +0.105 |
| momentum_accel | +0.066 |
| buy_pressure | +0.060 |
| not_vertical | -0.033 |
| paid_boost | +0.029 |
| dip_in_uptrend | +0.029 |
| fdv_sanity | +0.023 |
| buzz | +0.019 |
| age_sweet | +0.018 |
| socials | -0.009 |

## Last run log
```
  shadow: tracking 45, closed 1 this tick (1 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $368.29 (-26.34% since start)
tick #2245  equity $368.29  cash $346.30  open 5
exits-only pass. equity $367.01 (next scan in 10 min)
tick #2246  equity $367.01  cash $346.30  open 5
exits-only pass. equity $366.81 (next scan in 9 min)
tick #2247  equity $366.81  cash $346.30  open 5
exits-only pass. equity $366.82 (next scan in 8 min)
tick #2248  equity $366.82  cash $346.30  open 5
  SELL mihao      100% @ $0.009709  ->  $3.08   [stop loss -36%]
exits-only pass. equity $366.49 (next scan in 7 min)
tick #2249  equity $366.49  cash $349.38  open 4
exits-only pass. equity $366.66 (next scan in 6 min)
tick #2250  equity $366.66  cash $349.38  open 4
exits-only pass. equity $366.71 (next scan in 5 min)
tick #2251  equity $366.71  cash $349.38  open 4
exits-only pass. equity $366.51 (next scan in 4 min)
tick #2252  equity $366.51  cash $349.38  open 4
exits-only pass. equity $366.96 (next scan in 3 min)
tick #2253  equity $366.96  cash $349.38  open 4
exits-only pass. equity $367.18 (next scan in 2 min)
tick #2254  equity $367.18  cash $349.38  open 4
exits-only pass. equity $366.99 (next scan in 1 min)
tick #2255  equity $366.99  cash $349.38  open 4
  SELL GTA        25% @ $0.0002027  ->  $1.83   [take profit +50% (sold 25%)]
  scanning chains + news...
  135 raw candidates across 6 chains, 160 headlines/posts
  4 passed gates | rejected: liquidity too thin x90, no h1 volume x33, already discovered x4, too old x2, too new (bot war) x1
  top: mihao 0.76 | GTA 0.50 | gtacoin 0.49 | Anthropig 0.35
  tick bar 0.64 (top 10% of 4, floor 0.45)
  skip mihao: blacklisted (previously stopped out)
  skip gtacoin: solana concentration cap
  no entries this tick
  shadow: tracking 45, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
