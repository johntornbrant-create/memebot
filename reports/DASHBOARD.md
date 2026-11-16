# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T00:25:00+00:00`

## Equity

| | |
|---|---|
| Equity | **$376.35** |
| Return | **-24.73%** (start $500.00) |
| Cash | $358.84 |
| Deployed | $17.51 (4.7%) |
| Open positions | 4 / 8 |
| Closed trades | 34 (4W / 30L, WR 12%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $52.24 |
| Ticks run | 2133 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.16 | +10% | +29% | 4.6h |
| GTAVI | solana | $5.00 | $4.99 | +1% | +6% | 0.2h |
| AI | solana | $5.00 | $5.35 | +8% | +11% | 0.2h |
| BUTTHOLE | solana | $5.00 | $4.94 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| J*B | $-4.19 | -84% | 3.8h | stop loss -83% |

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
  tick bar 0.53 (top 10% of 6, floor 0.45)
  BUY[explore] GTAVI      $5.00 @ $9.306e-05  score 0.53  solana  liq $27,189
  BUY[explore] AI         $5.00 @ $0.0001488  score 0.24  solana  liq $26,877
  shadow: tracking 45, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $375.96 (-24.81% since start)
tick #2123  equity $375.96  cash $363.84  open 3
exits-only pass. equity $376.02 (next scan in 10 min)
tick #2124  equity $376.02  cash $363.84  open 3
exits-only pass. equity $376.04 (next scan in 9 min)
tick #2125  equity $376.04  cash $363.84  open 3
exits-only pass. equity $375.69 (next scan in 8 min)
tick #2126  equity $375.69  cash $363.84  open 3
exits-only pass. equity $375.86 (next scan in 7 min)
tick #2127  equity $375.86  cash $363.84  open 3
exits-only pass. equity $375.92 (next scan in 6 min)
tick #2128  equity $375.92  cash $363.84  open 3
exits-only pass. equity $375.90 (next scan in 5 min)
tick #2129  equity $375.90  cash $363.84  open 3
exits-only pass. equity $375.63 (next scan in 4 min)
tick #2130  equity $375.63  cash $363.84  open 3
exits-only pass. equity $376.32 (next scan in 3 min)
tick #2131  equity $376.32  cash $363.84  open 3
exits-only pass. equity $376.06 (next scan in 2 min)
tick #2132  equity $376.06  cash $363.84  open 3
exits-only pass. equity $376.25 (next scan in 1 min)
tick #2133  equity $376.25  cash $363.84  open 3
  scanning chains + news...
  168 raw candidates across 8 chains, 160 headlines/posts
  6 passed gates | rejected: liquidity too thin x107, no h1 volume x34, too old x13, already discovered x6, unknown age x2
  top: GTAVI 0.49 | bill 0.45 | Socks 0.43 | BUTTHOLE 0.42 | AURA 0.37
  tick bar 0.49 (top 10% of 6, floor 0.45)
  skip AI: already held
  BUY[explore] BUTTHOLE   $5.00 @ $0.0005252  score 0.42  solana  liq $194,226
  shadow: tracking 45, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
