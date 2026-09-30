# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-30T04:28:10+00:00`

## Equity

| | |
|---|---|
| Equity | **$347.38** |
| Return | **-30.52%** (start $500.00) |
| Cash | $340.76 |
| Deployed | $6.61 (1.9%) |
| Open positions | 1 / 8 |
| Closed trades | 76 (21W / 55L, WR 28%) |
| Profit factor | 0.51 |
| Fees + slippage paid | $67.40 |
| Ticks run | 1078 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SS | solana | $7.12 | $6.61 | -6% | +10% | 3.9h |

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
tick #1078  equity $347.63  cash $340.76  open 1
  scanning chains + news...
  161 raw candidates across 5 chains, 156 headlines/posts
  13 passed gates | rejected: liquidity too thin x91, no h1 volume x30, too old x15, already discovered x8, sell pressure x2
  top: NUTFLEX 0.83 | AIRPAD 0.65 | SI 0.60 | BEE 0.44 | RESI 0.40
  tick bar 0.60 (top 30% of 13, floor 0.45)
  no entries this tick
  shadow: tracking 112, closed 0 this tick (0 would have won)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
    MISSED Moon       peak +2942%  (scored 0.86)
  entries blocked: 7d loss -16.3% <= -15%
```
