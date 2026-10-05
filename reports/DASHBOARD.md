# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-05T20:56:53+00:00`

## Equity

| | |
|---|---|
| Equity | **$332.79** |
| Return | **-33.44%** (start $500.00) |
| Cash | $326.13 |
| Deployed | $6.66 (2.0%) |
| Open positions | 1 / 8 |
| Closed trades | 80 (22W / 58L, WR 28%) |
| Profit factor | 0.49 |
| Fees + slippage paid | $67.87 |
| Ticks run | 1214 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| MINTRO | solana | $6.66 | $6.59 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| TIT | $-5.47 | -81% | 8.3h | stop loss -80% |
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

## Learned weights (v33)

_refit on 867 observations (788 shadow, 79 real), 296 winners (34% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.104 |
| buy_pressure | +0.085 |
| not_vertical | -0.068 |
| momentum_accel | +0.048 |
| txn_depth | +0.042 |
| buzz | -0.034 |
| dip_in_uptrend | +0.026 |
| fdv_sanity | +0.022 |
| socials | +0.019 |
| liq_quality | -0.009 |
| paid_boost | -0.009 |
| age_sweet | -0.000 |

## Last run log
```
tick #1214  equity $337.99  cash $331.49  open 1
  SELL TIT        100% @ $3.744e-05  ->  $1.30   [stop loss -80%]
  scanning chains + news...
  125 raw candidates across 6 chains, 160 headlines/posts
  8 passed gates | rejected: liquidity too thin x80, no h1 volume x31, too old x2, already discovered x2, too new (bot war) x1
  top: MINTRO 0.70 | USEFUL 0.65 | sizeinu 0.46 | AGENTCAT 0.45 | INCOGNITO 0.38
  tick bar 0.53 (top 30% of 8, floor 0.45)
  BUY[exploit] MINTRO     $6.66 @ $0.001045  score 0.70  solana  liq $96,389
  shadow: tracking 25, closed 11 this tick (3 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
