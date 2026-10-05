# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-05T12:38:44+00:00`

## Equity

| | |
|---|---|
| Equity | **$338.26** |
| Return | **-32.35%** (start $500.00) |
| Cash | $331.49 |
| Deployed | $6.77 (2.0%) |
| Open positions | 1 / 8 |
| Closed trades | 79 (22W / 57L, WR 28%) |
| Profit factor | 0.50 |
| Fees + slippage paid | $67.77 |
| Ticks run | 1212 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TIT | solana | $6.77 | $6.70 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| Adventures | $-3.57 | -50% | 0.2h | stop loss -49% |
| Murphy | $-3.60 | -50% | 0.2h | stop loss -49% |

## Learned weights (v32)

_refit on 854 observations (776 shadow, 78 real), 293 winners (34% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.101 |
| buy_pressure | +0.087 |
| not_vertical | -0.077 |
| momentum_accel | +0.043 |
| txn_depth | +0.043 |
| buzz | -0.036 |
| dip_in_uptrend | +0.032 |
| fdv_sanity | +0.023 |
| socials | +0.021 |
| liq_quality | -0.015 |
| paid_boost | -0.004 |
| age_sweet | -0.002 |

## Last run log
```
tick #1212  equity $346.98  cash $338.24  open 1
  SELL XMAN       100% @ $2.741e-06  ->  $0.02   [stop loss -99%]
  scanning chains + news...
  129 raw candidates across 6 chains, 160 headlines/posts
  9 passed gates | rejected: liquidity too thin x67, no h1 volume x36, too old x8, already discovered x7, too new (bot war) x1
  top: TIT 0.60 | GOMO 0.54 | BATONROGUE 0.46 | AGENTCAT 0.41 | Sacabambaspis 0.39
  tick bar 0.48 (top 30% of 9, floor 0.45)
  BUY[exploit] TIT        $6.77 @ $0.0001894  score 0.60  solana  liq $36,920
  shadow: tracking 31, closed 7 this tick (2 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
