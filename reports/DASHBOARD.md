# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T01:58:16+00:00`

## Equity

| | |
|---|---|
| Equity | **$372.60** |
| Return | **-25.48%** (start $500.00) |
| Cash | $355.28 |
| Deployed | $17.32 (4.6%) |
| Open positions | 4 / 8 |
| Closed trades | 35 (4W / 31L, WR 11%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $52.33 |
| Ticks run | 2001 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.15 | +9% | +29% | 6.2h |
| WISHMAS | solana | $5.00 | $5.18 | +5% | +5% | 1.4h |
| Anthropig | solana | $5.00 | $4.94 | +0% | +0% | 0.0h |
| Neil | solana | $5.00 | $4.94 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| GTAVI | $-3.57 | -71% | 1.4h | stop loss -70% |
| GATO | $-5.00 | -100% | 2.3h | ratchet +55% (peak +121%) |
| FOOD | $-1.85 | -37% | 21.4h | stop loss -35% |
| WASTED | $-5.00 | -100% | 1.6h | ratchet +190% (peak +314%) |
| BEAR | $-4.85 | -97% | 1.1h | stop loss -97% |
| GTA | $-0.17 | -3% | 13.4h | ratchet +0% (peak +43%) |
| JASON | $-5.00 | -100% | 0.6h | stop loss -41% |
| GTA | $-5.00 | -100% | 1.1h | stop loss -99% |
| LETSWIN | $-5.00 | -100% | 5.6h | stop loss -83% |
| Socks | $+0.41 | +8% | 7.2h | ratchet +42% (peak +103%) |
| Macca | $-3.03 | -61% | 1.2h | stop loss -59% |
| HOGE | $-1.94 | -39% | 0.2h | stop loss -37% |
| SHIT | $+4.56 | +91% | 14.6h | ratchet +90% (peak +172%) |
| worth | $-1.96 | -39% | 3.0h | stop loss -37% |
| 牛逼 | $+3.99 | +80% | 12.2h | ratchet +88% (peak +168%) |

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
tick #2001  equity $376.08  cash $363.84  open 3
  SELL GTAVI      100% @ $3.006e-05  ->  $1.43   [stop loss -70%]
  scanning chains + news...
  60 raw candidates across 2 chains, 160 headlines/posts
  6 passed gates | rejected: liquidity too thin x44, no h1 volume x8, too old x2
  top: BUTTHOLE 0.53 | BAWSAQ 0.51 | CYBERDACITY 0.48 | Neil 0.47 | FiveM 0.43
  tick bar 0.53 (top 10% of 6, floor 0.45)
  BUY[explore] Anthropig  $5.00 @ $0.001124  score 0.42  solana  liq $76,800
  BUY[explore] Neil       $5.00 @ $0.0001484  score 0.47  solana  liq $28,904
  shadow: tracking 47, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
