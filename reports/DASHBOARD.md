# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-09-24T00:31:48+00:00`

## Equity

| | |
|---|---|
| Equity | **$485.34** |
| Return | **-2.93%** (start $500.00) |
| Cash | $431.73 |
| Deployed | $53.61 (11.0%) |
| Open positions | 4 / 8 |
| Closed trades | 21 (8W / 13L, WR 38%) |
| Profit factor | 0.73 |
| Fees + slippage paid | $22.04 |
| Ticks run | 131 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| 蝴蝶家园 | bsc | $14.96 | $15.64 | +8% | +27% | 20.9h |
| GAYMF | solana | $10.06 | $7.73 | -22% | +0% | 0.4h |
| familiars | solana | $10.06 | $20.05 | +101% | +101% | 0.4h |
| UPTOBER | solana | $10.19 | $10.10 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| UPTOBER | $+2.38 | +16% | 13.4h | ratchet +25% (peak +71%) |
| GROKBOTIFY | $-7.28 | -100% | 0.3h | stop loss -98% |
| MSTOCK | $+2.04 | +13% | 2.3h | stop loss -74% |
| MOUSE | $-7.41 | -100% | 0.2h | stop loss -96% |
| LeoGuigna | $-15.38 | -100% | 0.8h | stop loss -99% |
| 币安的守护者 | $-4.02 | -52% | 1.5h | stop loss -44% |
| based | $-6.45 | -42% | 1.2h | stop loss -37% |
| DURIAN | $-5.02 | -64% | 0.5h | stop loss -57% |
| LeoGuigna | $+19.66 | +263% | 2.0h | trailing stop from +724% |
| BITCOINU | $+7.57 | +99% | 9.2h | trailing stop from +248% |
| based | $+1.95 | +26% | 2.0h | stop loss -38% |
| SHIELD | $-3.94 | -53% | 0.3h | stop loss -45% |
| ACAT | $-7.53 | -100% | 0.9h | stop loss -100% |
| MORE | $-6.18 | -40% | 1.2h | stop loss -35% |
| Archi | $+0.08 | +1% | 1.9h | stop loss -76% |

## Learned weights (v0)

_prior_

| Feature | Weight |
|---|---|
| liq_quality | +0.083 |
| turnover | +0.083 |
| buy_pressure | +0.083 |
| momentum_accel | +0.083 |
| not_vertical | +0.083 |
| age_sweet | +0.083 |
| socials | +0.083 |
| fdv_sanity | +0.083 |
| txn_depth | +0.083 |
| dip_in_uptrend | +0.083 |
| buzz | +0.083 |
| paid_boost | +0.083 |

## Last run log
```
tick #131  equity $479.14  cash $441.92  open 3
  scanning chains + news...
  87 raw candidates across 7 chains, 158 headlines/posts
  3 passed gates | rejected: liquidity too thin x43, no h1 volume x37, sell pressure x2, too new (bot war) x2
  top: UPTOBER 0.71 | JEANCOIN 0.60 | parafactual 0.45
  BUY[explore] UPTOBER    $10.19 @ $0.0001778  score 0.71  solana  liq $37,786
  shadow: tracking 30, closed 2 this tick (1 would have won)
    MISSED GENIUS     peak +1642%  (scored 0.61)
    MISSED ⠁⠏⠑        peak +741%  (scored 0.54)
    MISSED JEANPHIL   peak +284%  (scored 0.63)
```
