# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-25T21:08:48+00:00`

## Equity

| | |
|---|---|
| Equity | **$439.55** |
| Return | **-12.09%** (start $500.00) |
| Cash | $425.86 |
| Deployed | $13.68 (3.1%) |
| Open positions | 2 / 8 |
| Closed trades | 13 (1W / 12L, WR 8%) |
| Profit factor | 0.41 |
| Fees + slippage paid | $7.73 |
| Ticks run | 1438 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| 币安AiPro | bsc | $6.41 | $9.05 | +43% | +43% | 9.2h |
| CATTLEAXE | solana | $6.22 | $4.63 | -25% | +3% | 5.8h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| SWAP | $-6.55 | -98% | 6.4h | stop loss -98% |

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
tick #1438  equity $439.99  cash $425.86  open 2
  scanning chains + news...
  102 raw candidates across 6 chains, 160 headlines/posts
  6 passed gates | rejected: liquidity too thin x74, no h1 volume x18, too old x2, too new (bot war) x1, already discovered x1
  top: NMS 0.79 | Chop 0.62 | GTA 0.55 | LAUNCH 0.40 | CATTLEAXE 0.25
  tick bar 0.50 (top 30% of 6, floor 0.45)
  no entries this tick
  shadow: tracking 38, closed 2 this tick (1 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
  entries blocked: daily loss -6.6% <= -6%
```
