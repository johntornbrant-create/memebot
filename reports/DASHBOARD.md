# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T06:57:29+00:00`

## Equity

| | |
|---|---|
| Equity | **$368.16** |
| Return | **-26.37%** (start $500.00) |
| Cash | $353.34 |
| Deployed | $14.82 (4.0%) |
| Open positions | 4 / 8 |
| Closed trades | 36 (4W / 32L, WR 11%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $52.43 |
| Ticks run | 2046 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.28 | +16% | +29% | 11.2h |
| WISHMAS | solana | $5.00 | $4.30 | -13% | +5% | 6.4h |
| Anthropig | solana | $5.00 | $4.89 | -1% | +0% | 5.0h |
| Marvin | solana | $5.00 | $3.35 | -32% | +10% | 0.8h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| SHIT | $+4.56 | +91% | 14.6h | ratchet +90% (peak +172%) |
| worth | $-1.96 | -39% | 3.0h | stop loss -37% |

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
  skip Anthropig: already held
  no entries this tick
  shadow: tracking 46, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $367.49 (-26.50% since start)
tick #2036  equity $367.49  cash $353.34  open 4
exits-only pass. equity $367.83 (next scan in 10 min)
tick #2037  equity $367.83  cash $353.34  open 4
exits-only pass. equity $367.85 (next scan in 9 min)
tick #2038  equity $367.85  cash $353.34  open 4
exits-only pass. equity $367.97 (next scan in 8 min)
tick #2039  equity $367.97  cash $353.34  open 4
exits-only pass. equity $367.83 (next scan in 7 min)
tick #2040  equity $367.83  cash $353.34  open 4
exits-only pass. equity $367.78 (next scan in 6 min)
tick #2041  equity $367.78  cash $353.34  open 4
exits-only pass. equity $367.89 (next scan in 5 min)
tick #2042  equity $367.89  cash $353.34  open 4
exits-only pass. equity $367.80 (next scan in 4 min)
tick #2043  equity $367.80  cash $353.34  open 4
exits-only pass. equity $367.87 (next scan in 3 min)
tick #2044  equity $367.87  cash $353.34  open 4
exits-only pass. equity $368.09 (next scan in 2 min)
tick #2045  equity $368.09  cash $353.34  open 4
exits-only pass. equity $368.20 (next scan in 1 min)
tick #2046  equity $368.20  cash $353.34  open 4
  scanning chains + news...
  89 raw candidates across 4 chains, 160 headlines/posts
  5 passed gates | rejected: liquidity too thin x50, no h1 volume x26, too old x4, already discovered x4
  top: BUTTHOLE 0.51 | Anthropig 0.50 | Marvin 0.45 | 6STAR 0.37 | GTA 0.29
  tick bar 0.51 (top 10% of 5, floor 0.45)
  skip Marvin: already held
  skip BUTTHOLE: solana concentration cap
  no entries this tick
  shadow: tracking 45, closed 1 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
