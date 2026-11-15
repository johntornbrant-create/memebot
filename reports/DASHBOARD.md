# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T17:36:48+00:00`

## Equity

| | |
|---|---|
| Equity | **$404.93** |
| Return | **-19.01%** (start $500.00) |
| Cash | $390.67 |
| Deployed | $14.26 (3.5%) |
| Open positions | 3 / 8 |
| Closed trades | 27 (4W / 23L, WR 15%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $18.70 |
| Ticks run | 1821 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.29 | -34% | +17% | 18.3h |
| GTA | solana | $5.00 | $5.97 | +21% | +43% | 11.2h |
| GTA | ethereum | $5.00 | $1.96 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| LETSWIN | $-5.00 | -100% | 5.6h | stop loss -83% |
| Socks | $+0.41 | +8% | 7.2h | ratchet +42% (peak +103%) |
| Macca | $-3.03 | -61% | 1.2h | stop loss -59% |
| HOGE | $-1.94 | -39% | 0.2h | stop loss -37% |
| SHIT | $+4.56 | +91% | 14.6h | ratchet +90% (peak +172%) |
| worth | $-1.96 | -39% | 3.0h | stop loss -37% |
| 牛逼 | $+3.99 | +80% | 12.2h | ratchet +88% (peak +168%) |
| J*B | $-4.19 | -84% | 3.8h | stop loss -83% |
| FLAPAI | $-6.90 | -79% | 6.7h | stop loss -78% |
| GTA | $-5.00 | -57% | 6.7h | stop loss -56% |
| GTA | $-2.64 | -43% | 11.7h | ratchet +65% (peak +135%) |
| TIT | $-7.07 | -80% | 4.9h | stop loss -79% |
| 币安AiPro | $-1.62 | -25% | 18.2h | ratchet +47% (peak +109%) |
| CATTLEAXE | $-2.39 | -38% | 7.9h | stop loss -37% |
| BTC | $-2.59 | -42% | 4.0h | stop loss -40% |

## Learned weights (v169)

_refit on 1806 observations (1699 shadow, 107 real), 494 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.152 |
| turnover | +0.127 |
| liq_quality | +0.096 |
| momentum_accel | +0.065 |
| buy_pressure | +0.062 |
| paid_boost | +0.034 |
| fdv_sanity | +0.030 |
| not_vertical | -0.029 |
| dip_in_uptrend | +0.025 |
| buzz | +0.019 |
| age_sweet | +0.009 |
| socials | -0.004 |

## Last run log
```
tick #1821  equity $413.63  cash $392.11  open 4
  SELL Socks      100% @ $0.0001691  ->  $3.56   [ratchet +42% (peak +103%)]
  SELL LETSWIN    100% @ $0.0001546  ->  $0.00   [stop loss -83%]
  scanning chains + news...
  82 raw candidates across 7 chains, 160 headlines/posts
  3 passed gates | rejected: liquidity too thin x54, no h1 volume x20, too old x2, too new (bot war) x1, already discovered x1
  top: GTA 0.63 | Jacket 0.55 | gtacoin 0.44
  tick bar 0.63 (top 10% of 3, floor 0.45)
  BUY[exploit] GTA        $5.00 @ $0.0001574  score 0.63  ethereum  liq $31,977
  shadow: tracking 21, closed 1 this tick (1 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
