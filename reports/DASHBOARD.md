# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T19:47:07+00:00`

## Equity

| | |
|---|---|
| Equity | **$358.60** |
| Return | **-28.28%** (start $500.00) |
| Cash | $341.30 |
| Deployed | $17.30 (4.8%) |
| Open positions | 4 / 8 |
| Closed trades | 39 (4W / 35L, WR 10%) |
| Profit factor | 0.36 |
| Fees + slippage paid | $58.63 |
| Ticks run | 2180 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.29 | +17% | +29% | 24.0h |
| WISHMAS | solana | $5.00 | $4.28 | -13% | +5% | 19.2h |
| GTA | solana | $5.00 | $5.73 | +16% | +39% | 12.6h |
| Trader | solana | $5.00 | $4.94 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| 1.0 | $-5.00 | -100% | 7.8h | stop loss -99% |
| Anthropig | $-5.00 | -100% | 17.8h | stop loss -100% |
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

## Learned weights (v171)

_refit on 1836 observations (1717 shadow, 119 real), 503 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.143 |
| turnover | +0.120 |
| liq_quality | +0.104 |
| momentum_accel | +0.070 |
| buy_pressure | +0.061 |
| paid_boost | +0.028 |
| not_vertical | -0.028 |
| dip_in_uptrend | +0.027 |
| fdv_sanity | +0.024 |
| buzz | +0.023 |
| age_sweet | +0.013 |
| socials | -0.006 |

## Last run log
```
tick #2180  equity $368.04  cash $346.30  open 5
  SELL Anthropig  100% @ $2.505e-06  ->  $0.00   [stop loss -100%]
  SELL 1.0        100% @ $1.827e-06  ->  $0.00   [stop loss -99%]
  scanning chains + news...
  121 raw candidates across 7 chains, 159 headlines/posts
  9 passed gates | rejected: liquidity too thin x76, no h1 volume x26, too old x5, already discovered x5
  top: VICEDORD 0.72 | GTA 0.67 | GTA 0.65 | ROCCO 0.62 | VICECAT 0.57
  tick bar 0.66 (top 10% of 9, floor 0.45)
  BUY[explore] Trader     $5.00 @ $0.0002047  score 0.52  solana  liq $34,269
  skip GTA: solana concentration cap
  shadow: tracking 37, closed 18 this tick (7 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
