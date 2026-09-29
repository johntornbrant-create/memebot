# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T06:32:07+00:00`

## Equity

| | |
|---|---|
| Equity | **$364.22** |
| Return | **-27.16%** (start $500.00) |
| Cash | $352.36 |
| Deployed | $11.86 (3.3%) |
| Open positions | 2 / 8 |
| Closed trades | 71 (20W / 51L, WR 28%) |
| Profit factor | 0.52 |
| Fees + slippage paid | $57.89 |
| Ticks run | 932 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| STOCK | solana | $5.22 | $9.12 | +214% | +214% | 6.4h |
| WOOF | ethereum | $5.08 | $2.74 | +34% | +39% | 4.1h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| SNOWBALL | $-2.98 | -41% | 1.1h | stop loss -40% |
| INKCHAN | $+0.60 | +8% | 1.0h | ratchet +0% (peak +69%) |
| SNOWBALL | $+7.23 | +101% | 0.8h | ratchet +78% (peak +154%) |
| 鹅次元 | $+3.43 | +48% | 0.9h | ratchet +88% (peak +168%) |
| SITRUMP | $-3.03 | -42% | 1.1h | stop loss -41% |
| Adventures | $-3.57 | -50% | 0.2h | stop loss -49% |
| Murphy | $-3.60 | -50% | 0.2h | stop loss -49% |
| PAIDINK | $-3.09 | -60% | 0.6h | ratchet +0% (peak +61%) |
| GAVCOIN | $-7.41 | -100% | 0.4h | stop loss -48% |
| INUINK | $-2.90 | -56% | 0.4h | stop loss -54% |
| Q4 | $-0.65 | -11% | 13.7h | ratchet +0% (peak +48%) |
| ZC | $-7.98 | -100% | 6.0h | stop loss -44% |
| XPAD | $+5.34 | +68% | 2.2h | ratchet +74% (peak +149%) |
| e/acc | $-7.96 | -99% | 2.8h | stop loss -98% |
| QPEPE | $-7.87 | -99% | 0.2h | stop loss -37% |

## Learned weights (v13)

_refit on 515 observations (444 shadow, 71 real), 185 winners (36% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.072 |
| buy_pressure | +0.068 |
| not_vertical | -0.067 |
| buzz | -0.066 |
| momentum_accel | +0.066 |
| fdv_sanity | +0.047 |
| paid_boost | -0.037 |
| age_sweet | +0.026 |
| txn_depth | +0.023 |
| dip_in_uptrend | +0.021 |
| liq_quality | +0.015 |
| socials | +0.006 |

## Last run log
```
tick #932  equity $361.60  cash $349.36  open 2
  SELL STOCK      25% @ $0.0007497  ->  $3.00   [take profit +150% (sold 25%)]
  scanning chains + news...
  114 raw candidates across 5 chains, 156 headlines/posts
  11 passed gates | rejected: liquidity too thin x50, no h1 volume x24, too old x21, already discovered x7, too new (bot war) x1
  top: DOTS 0.84 | WOOF 0.66 | 企鹅 0.63 | INUINK 0.53 | MI 0.47
  tick bar 0.63 (top 30% of 11, floor 0.45)
  no entries this tick
  shadow: tracking 96, closed 1 this tick (1 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
  entries blocked: daily trade cap reached
```
