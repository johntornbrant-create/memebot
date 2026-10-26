# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-26T01:11:07+00:00`

## Equity

| | |
|---|---|
| Equity | **$442.41** |
| Return | **-11.52%** (start $500.00) |
| Cash | $417.77 |
| Deployed | $24.64 (5.6%) |
| Open positions | 3 / 8 |
| Closed trades | 14 (1W / 13L, WR 7%) |
| Profit factor | 0.41 |
| Fees + slippage paid | $8.00 |
| Ticks run | 1442 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| 币安AiPro | bsc | $6.41 | $9.59 | +103% | +103% | 13.3h |
| TIT | solana | $8.85 | $8.77 | +0% | +0% | 0.0h |
| GTA | solana | $6.19 | $6.13 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| CATTLEAXE | $-2.39 | -38% | 7.9h | stop loss -37% |
| BTC | $-2.59 | -42% | 4.0h | stop loss -40% |
| SWORDOPE | $-2.42 | -38% | 4.8h | stop loss -36% |
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

## Learned weights (v106)

_refit on 1380 observations (1285 shadow, 95 real), 401 winners (29% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.142 |
| txn_depth | +0.105 |
| momentum_accel | +0.077 |
| buy_pressure | +0.074 |
| not_vertical | -0.070 |
| paid_boost | +0.040 |
| age_sweet | +0.028 |
| dip_in_uptrend | +0.021 |
| liq_quality | +0.019 |
| buzz | +0.018 |
| fdv_sanity | +0.015 |
| socials | -0.004 |

## Last run log
```
tick #1442  equity $438.80  cash $429.69  open 1
  SELL 币安AiPro    25% @ $0.000127  ->  $3.12   [take profit +50% (sold 25%)]
  scanning chains + news...
  130 raw candidates across 6 chains, 160 headlines/posts
  8 passed gates | rejected: liquidity too thin x102, no h1 volume x19, already discovered x1
  top: TIT 0.66 | GTA 0.59 | LAUNCH 0.55 | DANIELLA 0.54 | GTA 0.53
  tick bar 0.50 (top 30% of 8, floor 0.45)
  BUY[exploit] TIT        $8.85 @ $0.00117  score 0.66  solana  liq $92,848
  BUY[explore] GTA        $6.19 @ $0.0005852  score 0.59  solana  liq $64,522
  shadow: tracking 30, closed 3 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
