# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-30T01:41:03+00:00`

## Equity

| | |
|---|---|
| Equity | **$348.04** |
| Return | **-30.39%** (start $500.00) |
| Cash | $336.57 |
| Deployed | $11.47 (3.3%) |
| Open positions | 2 / 8 |
| Closed trades | 75 (21W / 54L, WR 28%) |
| Profit factor | 0.52 |
| Fees + slippage paid | $67.35 |
| Ticks run | 1058 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SS | solana | $7.12 | $6.56 | -7% | +7% | 1.1h |
| FKCANCER | solana | $7.07 | $4.91 | -30% | +0% | 0.7h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| SAI | $-3.50 | -49% | 1.5h | stop loss -48% |
| ARTHUR | $-4.77 | -66% | 0.3h | stop loss -66% |
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

## Learned weights (v14)

_refit on 590 observations (517 shadow, 73 real), 210 winners (36% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.089 |
| buy_pressure | +0.074 |
| not_vertical | -0.071 |
| momentum_accel | +0.061 |
| fdv_sanity | +0.053 |
| buzz | -0.048 |
| paid_boost | -0.038 |
| txn_depth | +0.032 |
| liq_quality | +0.021 |
| age_sweet | +0.021 |
| socials | +0.015 |
| dip_in_uptrend | +0.012 |

## Last run log
```
tick #1058  equity $352.65  cash $332.88  open 3
  SELL SAI        100% @ $0.0001521  ->  $3.68   [stop loss -48%]
  scanning chains + news...
  97 raw candidates across 8 chains, 160 headlines/posts
  12 passed gates | rejected: liquidity too thin x45, no h1 volume x36, already discovered x3, sell pressure x1
  top: DAD 0.83 | tok 0.78 | BEE 0.63 | RESI 0.52 | 犇犇 0.49
  tick bar 0.63 (top 30% of 12, floor 0.45)
  no entries this tick
  shadow: tracking 107, closed 2 this tick (1 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
  entries blocked: 7d loss -16.2% <= -15%
```
