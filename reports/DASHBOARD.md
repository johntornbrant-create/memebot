# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T07:55:29+00:00`

## Equity

| | |
|---|---|
| Equity | **$363.45** |
| Return | **-27.31%** (start $500.00) |
| Cash | $352.36 |
| Deployed | $11.09 (3.1%) |
| Open positions | 2 / 8 |
| Closed trades | 71 (20W / 51L, WR 28%) |
| Profit factor | 0.52 |
| Fees + slippage paid | $60.89 |
| Ticks run | 942 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| STOCK | solana | $5.22 | $8.28 | +185% | +214% | 7.8h |
| WOOF | ethereum | $5.08 | $2.81 | +84% | +86% | 5.5h |

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
tick #942  equity $363.55  cash $352.36  open 2
  scanning chains + news...
  105 raw candidates across 5 chains, 156 headlines/posts
  10 passed gates | rejected: liquidity too thin x61, no h1 volume x28, too old x5, already discovered x1
  top: SNOWMOON 0.66 | GFB 0.56 | INUINK 0.52 | 久留美 0.41 | HOOKEDCAT 0.36
  tick bar 0.52 (top 30% of 10, floor 0.45)
  no entries this tick
  shadow: tracking 101, closed 1 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
  entries blocked: daily trade cap reached
```
