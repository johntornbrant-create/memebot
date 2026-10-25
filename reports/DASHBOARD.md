# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-25T15:17:56+00:00`

## Equity

| | |
|---|---|
| Equity | **$444.37** |
| Return | **-11.13%** (start $500.00) |
| Cash | $418.25 |
| Deployed | $26.13 (5.9%) |
| Open positions | 4 / 8 |
| Closed trades | 11 (1W / 10L, WR 9%) |
| Profit factor | 0.42 |
| Fees + slippage paid | $7.64 |
| Ticks run | 1434 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SWORDOPE | solana | $6.41 | $5.30 | -16% | +0% | 3.4h |
| 币安AiPro | bsc | $6.41 | $8.39 | +33% | +33% | 3.4h |
| BTC | solana | $6.22 | $6.16 | +0% | +0% | 0.0h |
| CATTLEAXE | solana | $6.22 | $6.16 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| REACHY | $-6.23 | -99% | 13.8h | stop loss -99% |
| KURUMI | $+5.28 | +58% | 6.0h | ratchet +65% (peak +136%) |
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
tick #1434  equity $451.89  cash $430.64  open 3
  SELL REACHY     100% @ $2.079e-06  ->  $0.05   [stop loss -99%]
  scanning chains + news...
  114 raw candidates across 5 chains, 160 headlines/posts
  7 passed gates | rejected: liquidity too thin x55, no h1 volume x25, too old x15, already discovered x8, unknown age x2
  top: ASSETS 0.64 | TTC 0.62 | PumpkinBot 0.57 | BTC 0.46 | CATTLEAXE 0.39
  tick bar 0.46 (top 30% of 7, floor 0.45)
  BUY[explore] BTC        $6.22 @ $0.0001156  score 0.46  solana  liq $29,382
  BUY[explore] CATTLEAXE  $6.22 @ $0.001664  score 0.39  solana  liq $121,017
  shadow: tracking 39, closed 4 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
