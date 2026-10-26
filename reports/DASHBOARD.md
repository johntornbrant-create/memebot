# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-26T06:09:02+00:00`

## Equity

| | |
|---|---|
| Equity | **$435.58** |
| Return | **-12.88%** (start $500.00) |
| Cash | $407.35 |
| Deployed | $28.23 (6.5%) |
| Open positions | 3 / 8 |
| Closed trades | 16 (1W / 15L, WR 6%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $8.33 |
| Ticks run | 1444 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| GTA | solana | $6.19 | $10.81 | +135% | +135% | 5.0h |
| GTA | solana | $8.71 | $8.63 | +0% | +0% | 0.0h |
| FLAPAI | bsc | $8.71 | $8.60 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| TIT | $-7.07 | -80% | 4.9h | stop loss -79% |
| 币安AiPro | $-1.62 | -25% | 18.2h | ratchet +47% (peak +109%) |
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

## Learned weights (v107)

_refit on 1395 observations (1299 shadow, 96 real), 406 winners (29% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.141 |
| txn_depth | +0.110 |
| buy_pressure | +0.075 |
| momentum_accel | +0.071 |
| not_vertical | -0.070 |
| paid_boost | +0.035 |
| dip_in_uptrend | +0.030 |
| liq_quality | +0.023 |
| age_sweet | +0.023 |
| fdv_sanity | +0.017 |
| buzz | +0.013 |
| socials | -0.009 |

## Last run log
```
tick #1444  equity $446.65  cash $417.77  open 3
  SELL 币安AiPro    100% @ $2.279e-05  ->  $1.66   [ratchet +47% (peak +109%)]
  SELL TIT        100% @ $0.0002416  ->  $1.78   [stop loss -79%]
  SELL GTA        25% @ $0.001376  ->  $3.56   [take profit +50% (sold 25%)]
  scanning chains + news...
  130 raw candidates across 8 chains, 160 headlines/posts
  14 passed gates | rejected: liquidity too thin x72, no h1 volume x37, too old x5, sell pressure x1, already discovered x1
  top: GTA 0.77 | FLAPAI 0.69 | Chop 0.65 | 4AGENT 0.46 | Bow 0.45
  tick bar 0.46 (top 30% of 14, floor 0.45)
  BUY[exploit] GTA        $8.71 @ $0.0002961  score 0.77  solana  liq $47,863
  BUY[exploit] FLAPAI     $8.71 @ $7.961e-05  score 0.69  bsc  liq $28,476
  shadow: tracking 34, closed 5 this tick (3 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
