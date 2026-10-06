# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-06T07:58:52+00:00`

## Equity

| | |
|---|---|
| Equity | **$326.28** |
| Return | **-34.74%** (start $500.00) |
| Cash | $319.75 |
| Deployed | $6.53 (2.0%) |
| Open positions | 1 / 8 |
| Closed trades | 81 (22W / 59L, WR 27%) |
| Profit factor | 0.48 |
| Fees + slippage paid | $67.96 |
| Ticks run | 1217 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| APU | solana | $6.53 | $6.46 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| SITRUMP | $-3.03 | -42% | 1.1h | stop loss -41% |

## Learned weights (v35)

_refit on 886 observations (806 shadow, 80 real), 301 winners (34% base rate)_

| Feature | Weight |
|---|---|
| buy_pressure | +0.096 |
| turnover | +0.095 |
| not_vertical | -0.080 |
| txn_depth | +0.052 |
| momentum_accel | +0.043 |
| dip_in_uptrend | +0.030 |
| buzz | -0.024 |
| socials | +0.018 |
| fdv_sanity | +0.012 |
| liq_quality | -0.009 |
| paid_boost | +0.005 |
| age_sweet | +0.001 |

## Last run log
```
tick #1217  equity $332.74  cash $326.18  open 1
  SELL SWAP       100% @ $6.914e-06  ->  $0.11   [stop loss -98%]
  scanning chains + news...
  180 raw candidates across 10 chains, 160 headlines/posts
  4 passed gates | rejected: liquidity too thin x98, no h1 volume x65, already discovered x7, too old x5, sell pressure x1
  top: APU 0.65 | Contagion 0.23 | MINTRO 0.22 | VACAT 0.21
  tick bar 0.48 (top 30% of 4, floor 0.45)
  BUY[exploit] APU        $6.53 @ $0.0002506  score 0.65  solana  liq $42,877
  shadow: tracking 12, closed 10 this tick (4 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
