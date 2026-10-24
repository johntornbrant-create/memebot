# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-24T23:30:07+00:00`

## Equity

| | |
|---|---|
| Equity | **$473.61** |
| Return | **-5.28%** (start $500.00) |
| Cash | $444.72 |
| Deployed | $28.89 (6.1%) |
| Open positions | 3 / 8 |
| Closed trades | 5 (0W / 5L, WR 0%) |
| Profit factor | 0.44 |
| Fees + slippage paid | $3.85 |
| Ticks run | 1426 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| WRHND | solana | $9.56 | $9.95 | +40% | +93% | 2.2h |
| ODIE | ethereum | $9.47 | $6.40 | +0% | +0% | 0.0h |
| LUCIA | solana | $9.47 | $9.38 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| SAI | $-3.50 | -49% | 1.5h | stop loss -48% |
| ARTHUR | $-4.77 | -66% | 0.3h | stop loss -66% |
| WOOF | $-4.47 | -88% | 12.8h | ratchet +222% (peak +360%) |

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
tick #1426  equity $485.50  cash $463.63  open 2
  SELL HCAT       100% @ $2.182e-06  ->  $0.03   [stop loss -99%]
  scanning chains + news...
  160 raw candidates across 5 chains, 160 headlines/posts
  9 passed gates | rejected: liquidity too thin x106, no h1 volume x18, too old x15, already discovered x6, unknown age x4
  top: ODIE 0.74 | LUCIA 0.55 | SWORDOPE 0.54 | GDC 0.39 | REMUS 0.38
  tick bar 0.48 (top 30% of 9, floor 0.45)
  BUY[exploit] ODIE       $9.47 @ $0.0005455  score 0.74  ethereum  liq $50,475
  BUY[exploit] LUCIA      $9.47 @ $0.000182  score 0.55  solana  liq $34,825
  shadow: tracking 41, closed 6 this tick (1 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
