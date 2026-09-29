# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T05:54:29+00:00`

## Equity

| | |
|---|---|
| Equity | **$360.27** |
| Return | **-27.95%** (start $500.00) |
| Cash | $349.36 |
| Deployed | $10.90 (3.0%) |
| Open positions | 2 / 8 |
| Closed trades | 71 (20W / 51L, WR 28%) |
| Profit factor | 0.52 |
| Fees + slippage paid | $57.84 |
| Ticks run | 930 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| STOCK | solana | $5.22 | $8.70 | +125% | +139% | 5.8h |
| WOOF | ethereum | $5.08 | $2.21 | +8% | +20% | 3.5h |

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

## Learned weights (v12)

_refit on 417 observations (357 shadow, 60 real), 151 winners (36% base rate)_

| Feature | Weight |
|---|---|
| buy_pressure | +0.094 |
| not_vertical | -0.084 |
| momentum_accel | +0.073 |
| turnover | +0.054 |
| fdv_sanity | +0.048 |
| dip_in_uptrend | +0.025 |
| paid_boost | -0.025 |
| buzz | -0.021 |
| liq_quality | +0.017 |
| socials | +0.010 |
| age_sweet | +0.007 |
| txn_depth | +0.007 |

## Last run log
```
tick #930  equity $359.96  cash $349.36  open 2
  scanning chains + news...
  104 raw candidates across 7 chains, 116 headlines/posts
  5 passed gates | rejected: liquidity too thin x56, no h1 volume x37, too old x3, already discovered x2, too new (bot war) x1
  top: DOTS 0.83 | INUINK 0.76 | HOOKEDCAT 0.32 | CWC 0.28 | Mamesuke 0.13
  tick bar 0.76 (top 30% of 5, floor 0.45)
  no entries this tick
  shadow: tracking 93, closed 4 this tick (2 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
  entries blocked: daily trade cap reached
```
