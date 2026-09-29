# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T13:32:36+00:00`

## Equity

| | |
|---|---|
| Equity | **$363.01** |
| Return | **-27.40%** (start $500.00) |
| Cash | $358.41 |
| Deployed | $4.60 (1.3%) |
| Open positions | 1 / 8 |
| Closed trades | 72 (21W / 51L, WR 29%) |
| Profit factor | 0.54 |
| Fees + slippage paid | $63.96 |
| Ticks run | 978 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| WOOF | ethereum | $5.08 | $4.60 | +300% | +360% | 11.1h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| STOCK | $+5.89 | +113% | 9.5h | ratchet +120% (peak +214%) |
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
tick #978  equity $363.15  cash $358.41  open 1
  scanning chains + news...
  61 raw candidates across 4 chains, 160 headlines/posts
  7 passed gates | rejected: liquidity too thin x37, no h1 volume x11, already discovered x4, too new (bot war) x1, too old x1
  top: THESIS 0.58 | STOCK 0.58 | inu 0.49 | INUINK 0.49 | HOOKEDCAT 0.38
  tick bar 0.58 (top 30% of 7, floor 0.45)
  no entries this tick
  shadow: tracking 102, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
  entries blocked: daily trade cap reached
```
