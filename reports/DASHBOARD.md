# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T03:42:07+00:00`

## Equity

| | |
|---|---|
| Equity | **$359.12** |
| Return | **-28.18%** (start $500.00) |
| Cash | $345.10 |
| Deployed | $14.02 (3.9%) |
| Open positions | 3 / 8 |
| Closed trades | 70 (20W / 50L, WR 29%) |
| Profit factor | 0.53 |
| Fees + slippage paid | $57.79 |
| Ticks run | 915 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| STOCK | solana | $5.22 | $6.51 | +68% | +68% | 3.6h |
| WOOF | ethereum | $5.08 | $2.22 | +9% | +16% | 1.3h |
| SNOWBALL | solana | $7.25 | $5.29 | -26% | +11% | 0.8h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| x/acc | $-7.90 | -99% | 0.2h | stop loss -98% |

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
tick #915  equity $358.76  cash $345.10  open 3
  scanning chains + news...
  142 raw candidates across 5 chains, 156 headlines/posts
  10 passed gates | rejected: liquidity too thin x82, no h1 volume x23, too old x19, already discovered x6, exit-liquidity trap (FDV/liq) x1
  top: BAU 0.92 | DUCKYOU 0.67 | BNBuilder 0.54 | INUINK 0.46 | SITRUMP 0.37
  tick bar 0.54 (top 30% of 10, floor 0.45)
  no entries this tick
  shadow: tracking 103, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
  entries blocked: daily trade cap reached
```
