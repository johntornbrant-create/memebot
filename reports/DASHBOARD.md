# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T18:46:26+00:00`

## Equity

| | |
|---|---|
| Equity | **$399.60** |
| Return | **-20.08%** (start $500.00) |
| Cash | $380.67 |
| Deployed | $18.93 (4.7%) |
| Open positions | 4 / 8 |
| Closed trades | 28 (4W / 24L, WR 14%) |
| Profit factor | 0.39 |
| Fees + slippage paid | $24.79 |
| Ticks run | 1822 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $3.48 | -30% | +17% | 19.5h |
| GTA | solana | $5.00 | $5.45 | +10% | +43% | 12.4h |
| BEAR | solana | $5.00 | $4.94 | +0% | +0% | 0.0h |
| WASTED | ethereum | $5.00 | $1.96 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| GTA | $-5.00 | -100% | 1.1h | stop loss -99% |
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
tick #1822  equity $404.93  cash $390.67  open 3
  SELL GTA        100% @ $1.834e-06  ->  $0.00   [stop loss -99%]
  scanning chains + news...
  133 raw candidates across 7 chains, 160 headlines/posts
  6 passed gates | rejected: liquidity too thin x71, no h1 volume x34, too old x16, already discovered x5, too new (bot war) x1
  top: WASTED 0.72 | BEAR 0.70 | SWJ 0.64 | Macca 0.44 | gtacoin 0.43
  tick bar 0.64 (top 10% of 6, floor 0.45)
  BUY[explore] BEAR       $5.00 @ $0.0001205  score 0.70  solana  liq $32,896
  BUY[explore] WASTED     $5.00 @ $0.0006616  score 0.72  ethereum  liq $67,520
  shadow: tracking 22, closed 4 this tick (3 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
