# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-30T00:07:38+00:00`

## Equity

| | |
|---|---|
| Equity | **$359.02** |
| Return | **-28.20%** (start $500.00) |
| Cash | $344.66 |
| Deployed | $14.36 (4.0%) |
| Open positions | 2 / 8 |
| Closed trades | 73 (21W / 52L, WR 29%) |
| Profit factor | 0.53 |
| Fees + slippage paid | $67.13 |
| Ticks run | 1049 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SAI | solana | $7.18 | $7.11 | +0% | +0% | 0.0h |
| ARTHUR | solana | $7.18 | $7.11 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| WOOF | $-4.47 | -88% | 12.8h | ratchet +222% (peak +360%) |
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
tick #1049  equity $359.02  cash $359.02  open 0
  scanning chains + news...
  194 raw candidates across 9 chains, 156 headlines/posts
  8 passed gates | rejected: liquidity too thin x96, no h1 volume x63, too old x17, already discovered x6, sell pressure x2
  top: SAI 0.75 | ARTHUR 0.65 | SS 0.59 | BEE 0.50 | PARASITE 0.37
  tick bar 0.65 (top 30% of 8, floor 0.45)
  BUY[exploit] SAI        $7.18 @ $0.0002899  score 0.75  solana  liq $48,605
  BUY[exploit] ARTHUR     $7.18 @ $0.0007469  score 0.65  solana  liq $84,027
  shadow: tracking 110, closed 1 this tick (1 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
```
