# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T21:56:35+00:00`

## Equity

| | |
|---|---|
| Equity | **$360.29** |
| Return | **-27.94%** (start $500.00) |
| Cash | $341.30 |
| Deployed | $18.99 (5.3%) |
| Open positions | 4 / 8 |
| Closed trades | 39 (4W / 35L, WR 10%) |
| Profit factor | 0.36 |
| Fees + slippage paid | $58.63 |
| Ticks run | 2181 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.18 | +11% | +29% | 26.2h |
| WISHMAS | solana | $5.00 | $3.71 | -25% | +5% | 21.3h |
| GTA | solana | $5.00 | $6.35 | +29% | +39% | 14.8h |
| Trader | solana | $5.00 | $6.75 | +36% | +36% | 2.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| 1.0 | $-5.00 | -100% | 7.8h | stop loss -99% |
| Anthropig | $-5.00 | -100% | 17.8h | stop loss -100% |
| Marvin | $-2.04 | -41% | 0.8h | stop loss -39% |
| Neil | $-1.94 | -39% | 4.2h | stop loss -37% |
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

## Learned weights (v171)

_refit on 1836 observations (1717 shadow, 119 real), 503 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.143 |
| turnover | +0.120 |
| liq_quality | +0.104 |
| momentum_accel | +0.070 |
| buy_pressure | +0.061 |
| paid_boost | +0.028 |
| not_vertical | -0.028 |
| dip_in_uptrend | +0.027 |
| fdv_sanity | +0.024 |
| buzz | +0.023 |
| age_sweet | +0.013 |
| socials | -0.006 |

## Last run log
```
tick #2181  equity $358.60  cash $341.30  open 4
  scanning chains + news...
  210 raw candidates across 11 chains, 159 headlines/posts
  7 passed gates | rejected: liquidity too thin x120, no h1 volume x60, too old x16, already discovered x5, too new (bot war) x1
  top: CHOP 0.67 | rockstar 0.60 | BAWSAQ 0.52 | HOGE 0.48 | WIGGLES 0.47
  tick bar 0.66 (top 10% of 7, floor 0.45)
  skip WIGGLES: solana concentration cap
  skip CHOP: solana concentration cap
  no entries this tick
  shadow: tracking 28, closed 14 this tick (2 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
