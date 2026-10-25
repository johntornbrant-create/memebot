# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-25T06:28:07+00:00`

## Equity

| | |
|---|---|
| Equity | **$455.26** |
| Return | **-8.95%** (start $500.00) |
| Cash | $429.07 |
| Deployed | $26.19 (5.8%) |
| Open positions | 3 / 8 |
| Closed trades | 8 (0W / 8L, WR 0%) |
| Profit factor | 0.41 |
| Fees + slippage paid | $7.16 |
| Ticks run | 1430 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| REACHY | solana | $6.27 | $8.11 | +31% | +31% | 5.0h |
| MAYA | solana | $6.27 | $8.97 | +93% | +93% | 5.0h |
| KURUMI | solana | $9.11 | $9.02 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| LUCIA | $-9.39 | -99% | 1.9h | stop loss -99% |
| ODIE | $-9.47 | -100% | 1.9h | stop loss -100% |
| WRHND | $-1.81 | -19% | 4.1h | ratchet +25% (peak +93%) |
| HCAT | $-9.53 | -100% | 2.1h | stop loss -99% |
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

## Learned weights (v103)

_refit on 1353 observations (1263 shadow, 90 real), 397 winners (29% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.141 |
| txn_depth | +0.110 |
| not_vertical | -0.078 |
| buy_pressure | +0.075 |
| momentum_accel | +0.065 |
| paid_boost | +0.060 |
| buzz | +0.031 |
| dip_in_uptrend | +0.026 |
| fdv_sanity | +0.025 |
| liq_quality | +0.016 |
| age_sweet | +0.008 |
| socials | +0.006 |

## Last run log
```
tick #1430  equity $451.84  cash $438.18  open 2
  scanning chains + news...
  130 raw candidates across 7 chains, 160 headlines/posts
  11 passed gates | rejected: liquidity too thin x79, no h1 volume x31, too old x7, already discovered x2
  top: KURUMI 0.48 | Chunkee 0.45 | ███ 0.37 | WRHND 0.31 | REACHY 0.30
  tick bar 0.45 (top 30% of 11, floor 0.45)
  BUY[exploit] KURUMI     $9.11 @ $0.0002891  score 0.48  solana  liq $45,129
  shadow: tracking 41, closed 3 this tick (1 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
