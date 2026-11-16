# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T06:45:29+00:00`

## Equity

| | |
|---|---|
| Equity | **$367.49** |
| Return | **-26.50%** (start $500.00) |
| Cash | $353.34 |
| Deployed | $14.16 (3.9%) |
| Open positions | 4 / 8 |
| Closed trades | 36 (4W / 32L, WR 11%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $52.43 |
| Ticks run | 2035 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.22 | +13% | +29% | 11.0h |
| WISHMAS | solana | $5.00 | $3.94 | -20% | +5% | 6.2h |
| Anthropig | solana | $5.00 | $4.56 | -8% | +0% | 4.8h |
| Marvin | solana | $5.00 | $3.43 | -31% | +10% | 0.6h |

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
  skip BUTTHOLE: solana concentration cap
  no entries this tick
  shadow: tracking 46, closed 1 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $368.64 (-26.27% since start)
tick #2025  equity $368.64  cash $353.34  open 4
exits-only pass. equity $368.62 (next scan in 10 min)
tick #2026  equity $368.62  cash $353.34  open 4
exits-only pass. equity $368.60 (next scan in 9 min)
tick #2027  equity $368.60  cash $353.34  open 4
exits-only pass. equity $368.05 (next scan in 8 min)
tick #2028  equity $368.05  cash $353.34  open 4
exits-only pass. equity $367.90 (next scan in 7 min)
tick #2029  equity $367.90  cash $353.34  open 4
exits-only pass. equity $368.07 (next scan in 6 min)
tick #2030  equity $368.07  cash $353.34  open 4
exits-only pass. equity $367.85 (next scan in 5 min)
tick #2031  equity $367.85  cash $353.34  open 4
exits-only pass. equity $367.65 (next scan in 4 min)
tick #2032  equity $367.65  cash $353.34  open 4
exits-only pass. equity $368.49 (next scan in 3 min)
tick #2033  equity $368.49  cash $353.34  open 4
exits-only pass. equity $367.54 (next scan in 2 min)
tick #2034  equity $367.54  cash $353.34  open 4
exits-only pass. equity $367.71 (next scan in 1 min)
tick #2035  equity $367.71  cash $353.34  open 4
  scanning chains + news...
  91 raw candidates across 4 chains, 160 headlines/posts
  6 passed gates | rejected: liquidity too thin x52, no h1 volume x25, too old x4, already discovered x4
  top: BUTTHOLE 0.50 | Anthropig 0.49 | Marvin 0.41 | 6STAR 0.40 | GTA 0.32
  tick bar 0.50 (top 10% of 6, floor 0.45)
  skip GTA: solana concentration cap
  skip Anthropig: already held
  no entries this tick
  shadow: tracking 46, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
