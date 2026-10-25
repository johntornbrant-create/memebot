# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-25T11:54:44+00:00`

## Equity

| | |
|---|---|
| Equity | **$457.71** |
| Return | **-8.46%** (start $500.00) |
| Cash | $421.51 |
| Deployed | $36.19 (7.9%) |
| Open positions | 4 / 8 |
| Closed trades | 9 (0W / 9L, WR 0%) |
| Profit factor | 0.41 |
| Fees + slippage paid | $7.40 |
| Ticks run | 1432 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| REACHY | solana | $6.27 | $7.43 | +20% | +31% | 10.5h |
| KURUMI | solana | $9.11 | $15.95 | +136% | +136% | 5.4h |
| SWORDOPE | solana | $6.41 | $6.34 | +0% | +0% | 0.0h |
| 币安AiPro | bsc | $6.41 | $6.31 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| MAYA | $-3.58 | -57% | 10.4h | ratchet +25% (peak +94%) |
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

## Learned weights (v104)

_refit on 1356 observations (1266 shadow, 90 real), 398 winners (29% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.142 |
| txn_depth | +0.108 |
| not_vertical | -0.077 |
| buy_pressure | +0.074 |
| momentum_accel | +0.066 |
| paid_boost | +0.058 |
| buzz | +0.028 |
| fdv_sanity | +0.026 |
| dip_in_uptrend | +0.025 |
| liq_quality | +0.018 |
| age_sweet | +0.011 |
| socials | +0.001 |

## Last run log
```
tick #1432  equity $456.28  cash $429.07  open 3
  SELL MAYA       100% @ $2.438e-06  ->  $0.00   [ratchet +25% (peak +94%)]
  SELL KURUMI     25% @ $0.0006813  ->  $5.26   [take profit +50% (sold 25%)]
  scanning chains + news...
  102 raw candidates across 8 chains, 160 headlines/posts
  8 passed gates | rejected: liquidity too thin x58, no h1 volume x32, too old x2, sell pressure x1, already discovered x1
  top: SOL 0.60 | SWORDOPE 0.51 | KURUMI 0.40 | NAVA 0.39 | 币安AiPro 0.34
  tick bar 0.46 (top 30% of 8, floor 0.45)
  BUY[explore] SWORDOPE   $6.41 @ $0.001394  score 0.51  solana  liq $109,710
  BUY[explore] 币安AiPro    $6.41 @ $6.268e-05  score 0.34  bsc  liq $50,586
  shadow: tracking 39, closed 6 this tick (2 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
