# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T12:01:53+00:00`

## Equity

| | |
|---|---|
| Equity | **$413.63** |
| Return | **-17.27%** (start $500.00) |
| Cash | $392.11 |
| Deployed | $21.52 (5.2%) |
| Open positions | 4 / 8 |
| Closed trades | 25 (3W / 22L, WR 12%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $12.61 |
| Ticks run | 1820 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $4.04 | -19% | +17% | 12.7h |
| GTA | solana | $5.00 | $5.65 | +14% | +43% | 5.6h |
| Socks | solana | $5.00 | $6.83 | +84% | +103% | 1.6h |
| LETSWIN | ethereum | $5.00 | $1.96 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| SWORDOPE | $-2.42 | -38% | 4.8h | stop loss -36% |
| REACHY | $-6.23 | -99% | 13.8h | stop loss -99% |

## Learned weights (v168)

_refit on 1797 observations (1695 shadow, 102 real), 492 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.149 |
| turnover | +0.126 |
| liq_quality | +0.089 |
| momentum_accel | +0.064 |
| buy_pressure | +0.061 |
| paid_boost | +0.035 |
| dip_in_uptrend | +0.031 |
| not_vertical | -0.029 |
| buzz | +0.020 |
| fdv_sanity | +0.011 |
| age_sweet | +0.007 |
| socials | -0.003 |

## Last run log
```
tick #1820  equity $416.20  cash $395.13  open 4
  SELL Macca      100% @ $1.77  ->  $1.97   [stop loss -59%]
  scanning chains + news...
  123 raw candidates across 7 chains, 160 headlines/posts
  4 passed gates | rejected: liquidity too thin x82, no h1 volume x27, too old x6, already discovered x3, too new (bot war) x1
  top: LETSWIN 0.64 | GETAJOB 0.64 | Macca 0.58 | Socks 0.25
  tick bar 0.62 (top 10% of 4, floor 0.45)
  BUY[exploit] LETSWIN    $5.00 @ $0.0009293  score 0.64  ethereum  liq $29,940
  skip Socks: already held
  shadow: tracking 20, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
