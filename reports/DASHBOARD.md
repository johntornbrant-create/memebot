# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-24T15:24:41+00:00`

## Equity

| | |
|---|---|
| Equity | **$500.00** |
| Return | **+0.00%** (start $500.00) |
| Cash | $486.00 |
| Deployed | $14.00 (2.8%) |
| Open positions | 2 / 8 |
| Closed trades | 0 (0W / 0L, WR 0%) |
| Profit factor | 0.48 |
| Fees + slippage paid | $0.14 |
| Ticks run | 1419 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| PRIVACY | solana | $7.00 | $6.93 | +0% | +0% | 0.0h |
| MI | solana | $7.00 | $6.93 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| APU | $-3.72 | -57% | 6.8h | stop loss -56% |
| SWAP | $-6.55 | -98% | 6.4h | stop loss -98% |
| TIT | $-5.43 | -80% | 8.5h | stop loss -80% |
| XMAN | $-6.88 | -100% | 7.1h | stop loss -99% |
| SS | $+1.46 | +21% | 9.3h | ratchet +25% (peak +95%) |
| NUTFLEX | $-4.20 | -59% | 1.1h | stop loss -58% |
| FKCANCER | $-2.88 | -41% | 0.8h | stop loss -39% |
| SAI | $-3.50 | -49% | 1.5h | stop loss -48% |
| ARTHUR | $-4.77 | -66% | 0.3h | stop loss -66% |
| WOOF | $-4.47 | -88% | 12.8h | ratchet +222% (peak +360%) |
| STOCK | $+5.89 | +113% | 9.5h | ratchet +120% (peak +214%) |
| SNOWBALL | $-2.98 | -41% | 1.1h | stop loss -40% |
| INKCHAN | $+0.60 | +8% | 1.0h | ratchet +0% (peak +69%) |
| SNOWBALL | $+7.23 | +101% | 0.8h | ratchet +78% (peak +154%) |
| 鹅次元 | $+3.43 | +48% | 0.9h | ratchet +88% (peak +168%) |

## Learned weights (v101)

_refit on 1321 observations (1239 shadow, 82 real), 391 winners (30% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.139 |
| txn_depth | +0.098 |
| buy_pressure | +0.091 |
| not_vertical | -0.086 |
| momentum_accel | +0.070 |
| paid_boost | +0.049 |
| buzz | +0.037 |
| fdv_sanity | +0.031 |
| liq_quality | +0.024 |
| dip_in_uptrend | +0.017 |
| age_sweet | +0.011 |
| socials | -0.003 |

## Last run log
```
tick #1419  equity $500.00  cash $500.00  open 0
  scanning chains + news...
  76 raw candidates across 5 chains, 160 headlines/posts
  10 passed gates | rejected: liquidity too thin x45, no h1 volume x14, too old x7
  top: DOGETRUMP 0.68 | VIRTUAL 0.60 | PRIVACY 0.51 | MI 0.50 | GDC 0.42
  tick bar 0.47 (top 30% of 10, floor 0.45)
  BUY[explore] PRIVACY    $7.00 @ $0.001532  score 0.51  solana  liq $107,500
  BUY[explore] MI         $7.00 @ $0.00129  score 0.50  solana  liq $95,490
  shadow: tracking 34, closed 9 this tick (4 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
