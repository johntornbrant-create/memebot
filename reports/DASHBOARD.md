# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-29T02:52:36+00:00`

## Equity

| | |
|---|---|
| Equity | **$362.59** |
| Return | **-27.48%** (start $500.00) |
| Cash | $338.20 |
| Deployed | $24.40 (6.7%) |
| Open positions | 4 / 8 |
| Closed trades | 69 (19W / 50L, WR 28%) |
| Profit factor | 0.52 |
| Fees + slippage paid | $57.70 |
| Ticks run | 909 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| STOCK | solana | $5.22 | $6.90 | +34% | +41% | 2.7h |
| WOOF | ethereum | $5.08 | $2.36 | +16% | +16% | 0.5h |
| INKCHAN | solana | $7.24 | $7.88 | +47% | +69% | 0.2h |
| SNOWBALL | solana | $7.25 | $7.18 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| CATSTR | $-4.68 | -56% | 1.1h | stop loss -55% |

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
tick #909  equity $364.24  cash $338.54  open 4
  SELL SNOWBALL   100% @ $0.0003326  ->  $6.90   [ratchet +78% (peak +154%)]
  scanning chains + news...
  85 raw candidates across 5 chains, 156 headlines/posts
  7 passed gates | rejected: liquidity too thin x45, no h1 volume x29, too old x2, too new (bot war) x1, already discovered x1
  top: INKCHAN 0.85 | SNOWBALL 0.56 | INUINK 0.46 | SITRUMP 0.36 | HOOKEDCAT 0.19
  tick bar 0.56 (top 30% of 7, floor 0.45)
  BUY[exploit] SNOWBALL   $7.25 @ $0.0003326  score 0.56  solana  liq $55,056
  shadow: tracking 100, closed 1 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
```
