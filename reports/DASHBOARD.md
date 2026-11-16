# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T06:09:41+00:00`

## Equity

| | |
|---|---|
| Equity | **$369.76** |
| Return | **-26.05%** (start $500.00) |
| Cash | $353.34 |
| Deployed | $16.42 (4.4%) |
| Open positions | 4 / 8 |
| Closed trades | 36 (4W / 32L, WR 11%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $52.43 |
| Ticks run | 2002 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.23 | +13% | +29% | 10.4h |
| WISHMAS | solana | $5.00 | $4.53 | -8% | +5% | 5.6h |
| Anthropig | solana | $5.00 | $4.66 | -6% | +0% | 4.2h |
| Marvin | solana | $5.00 | $4.94 | +0% | +0% | 0.0h |

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
tick #2002  equity $372.60  cash $355.28  open 4
  SELL Neil       100% @ $9.309e-05  ->  $3.06   [stop loss -37%]
  scanning chains + news...
  101 raw candidates across 4 chains, 160 headlines/posts
  5 passed gates | rejected: liquidity too thin x61, no h1 volume x28, already discovered x4, too old x3
  top: GTA 0.59 | 6STAR 0.59 | Marvin 0.41 | Anthropig 0.37 | WISHMAS 0.24
  tick bar 0.59 (top 10% of 5, floor 0.45)
  BUY[explore] Marvin     $5.00 @ $0.000642  score 0.41  solana  liq $75,165
  skip WISHMAS: already held
  shadow: tracking 47, closed 2 this tick (2 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
