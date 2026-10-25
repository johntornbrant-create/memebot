# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-25T01:27:10+00:00`

## Equity

| | |
|---|---|
| Equity | **$448.04** |
| Return | **-10.39%** (start $500.00) |
| Cash | $435.49 |
| Deployed | $12.55 (2.8%) |
| Open positions | 2 / 8 |
| Closed trades | 8 (0W / 8L, WR 0%) |
| Profit factor | 0.41 |
| Fees + slippage paid | $7.04 |
| Ticks run | 1428 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| REACHY | solana | $6.27 | $6.21 | +0% | +0% | 0.0h |
| MAYA | solana | $6.27 | $6.21 | +0% | +0% | 0.0h |

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
tick #1428  equity $470.57  cash $444.72  open 3
  SELL WRHND      100% @ $0.0005145  ->  $3.24   [ratchet +25% (peak +93%)]
  SELL ODIE       100% @ $1.521e-10  ->  $0.00   [stop loss -100%]
  SELL LUCIA      100% @ $1.923e-06  ->  $0.08   [stop loss -99%]
  scanning chains + news...
  132 raw candidates across 7 chains, 160 headlines/posts
  10 passed gates | rejected: liquidity too thin x89, no h1 volume x18, too old x12, already discovered x2, exit-liquidity trap (FDV/liq) x1
  top: MAYA 0.65 | BTC 0.56 | WRHND 0.45 | REACHY 0.44 | SWORDOPE 0.42
  tick bar 0.45 (top 30% of 10, floor 0.45)
  BUY[explore] REACHY     $6.27 @ $0.0001925  score 0.44  solana  liq $36,084
  BUY[explore] MAYA       $6.27 @ $0.0008188  score 0.65  solana  liq $78,287
  shadow: tracking 41, closed 5 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
