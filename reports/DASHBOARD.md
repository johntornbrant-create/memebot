# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-24T21:20:47+00:00`

## Equity

| | |
|---|---|
| Equity | **$478.23** |
| Return | **-4.35%** (start $500.00) |
| Cash | $459.11 |
| Deployed | $19.12 (4.0%) |
| Open positions | 2 / 8 |
| Closed trades | 4 (0W / 4L, WR 0%) |
| Profit factor | 0.45 |
| Fees + slippage paid | $0.62 |
| Ticks run | 1424 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| WRHND | solana | $9.56 | $9.47 | +0% | +0% | 0.0h |
| HCAT | solana | $9.56 | $9.47 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| TRUMP | $-6.53 | -67% | 0.3h | stop loss -67% |
| Leonida | $-6.82 | -99% | 0.5h | stop loss -99% |
| MI | $-3.37 | -48% | 1.0h | stop loss -47% |
| PRIVACY | $-5.06 | -72% | 1.0h | stop loss -71% |
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

## Learned weights (v102)

_refit on 1338 observations (1252 shadow, 86 real), 396 winners (30% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.132 |
| txn_depth | +0.106 |
| buy_pressure | +0.084 |
| not_vertical | -0.077 |
| momentum_accel | +0.067 |
| paid_boost | +0.060 |
| fdv_sanity | +0.031 |
| buzz | +0.027 |
| liq_quality | +0.020 |
| dip_in_uptrend | +0.017 |
| age_sweet | +0.013 |
| socials | +0.002 |

## Last run log
```
tick #1424  equity $478.23  cash $478.23  open 0
  scanning chains + news...
  116 raw candidates across 5 chains, 160 headlines/posts
  13 passed gates | rejected: liquidity too thin x69, too old x18, no h1 volume x14, already discovered x1, exit-liquidity trap (FDV/liq) x1
  top: WRHND 0.69 | HCAT 0.56 | swordcat 0.54 | MI 0.49 | BEARSTR 0.44
  tick bar 0.48 (top 30% of 13, floor 0.45)
  BUY[exploit] WRHND      $9.56 @ $0.001114  score 0.69  solana  liq $91,489
  BUY[exploit] HCAT       $9.56 @ $0.0003783  score 0.56  solana  liq $52,997
  shadow: tracking 44, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
