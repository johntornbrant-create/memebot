# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-30T06:32:28+00:00`

## Equity

| | |
|---|---|
| Equity | **$348.16** |
| Return | **-30.37%** (start $500.00) |
| Cash | $336.31 |
| Deployed | $11.85 (3.4%) |
| Open positions | 2 / 8 |
| Closed trades | 76 (21W / 55L, WR 28%) |
| Profit factor | 0.51 |
| Fees + slippage paid | $67.51 |
| Ticks run | 1092 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SS | solana | $7.12 | $7.25 | +37% | +95% | 6.0h |
| NUTFLEX | solana | $7.07 | $4.59 | -34% | +0% | 0.9h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| FKCANCER | $-2.88 | -41% | 0.8h | stop loss -39% |
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

## Learned weights (v15)

_refit on 613 observations (537 shadow, 76 real), 219 winners (36% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.097 |
| buy_pressure | +0.078 |
| not_vertical | -0.077 |
| paid_boost | -0.060 |
| momentum_accel | +0.053 |
| fdv_sanity | +0.041 |
| txn_depth | +0.038 |
| buzz | -0.035 |
| age_sweet | +0.026 |
| dip_in_uptrend | +0.023 |
| socials | +0.013 |
| liq_quality | +0.008 |

## Last run log
```
tick #1092  equity $348.70  cash $336.31  open 2
  scanning chains + news...
  74 raw candidates across 6 chains, 156 headlines/posts
  7 passed gates | rejected: liquidity too thin x37, no h1 volume x24, too old x3, too new (bot war) x2, already discovered x1
  top: SS 0.36 | PARASITE 0.28 | RESI 0.26 | SI 0.18 | AIRPAD 0.15
  tick bar 0.45 (top 30% of 7, floor 0.45)
  no entries this tick
  shadow: tracking 107, closed 4 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
  entries blocked: 7d loss -16.2% <= -15%
```
