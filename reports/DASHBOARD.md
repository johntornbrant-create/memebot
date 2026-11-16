# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T23:44:29+00:00`

## Equity

| | |
|---|---|
| Equity | **$356.51** |
| Return | **-28.70%** (start $500.00) |
| Cash | $336.41 |
| Deployed | $20.10 (5.6%) |
| Open positions | 4 / 8 |
| Closed trades | 41 (4W / 37L, WR 10%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $61.85 |
| Ticks run | 2280 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| WISHMAS | solana | $5.00 | $3.40 | -31% | +5% | 23.1h |
| GTA | solana | $5.00 | $6.59 | +33% | +39% | 16.6h |
| TE | base | $5.00 | $5.04 | +2% | +10% | 1.4h |
| LEOSTAR | solana | $5.00 | $5.08 | +37% | +77% | 0.2h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| Trader | $-1.97 | -39% | 3.6h | stop loss -38% |
| Macca | $-5.00 | -100% | 26.6h | time stop 27h, only +10% |
| 1.0 | $-5.00 | -100% | 7.8h | stop loss -99% |
| Anthropig | $-5.00 | -100% | 17.8h | stop loss -100% |
| Marvin | $-2.04 | -41% | 0.8h | stop loss -39% |
| Neil | $-1.94 | -39% | 4.2h | stop loss -37% |
| GTAVI | $-3.57 | -71% | 1.4h | stop loss -70% |
| GATO | $-5.00 | -100% | 2.3h | ratchet +55% (peak +121%) |
| FOOD | $-1.85 | -37% | 21.4h | stop loss -35% |
| WASTED | $-5.00 | -100% | 1.6h | ratchet +190% (peak +314%) |
| BEAR | $-4.85 | -97% | 1.1h | stop loss -97% |
| GTA | $-0.17 | -3% | 13.4h | ratchet +0% (peak +43%) |
| JASON | $-5.00 | -100% | 0.6h | stop loss -41% |
| GTA | $-5.00 | -100% | 1.1h | stop loss -99% |
| LETSWIN | $-5.00 | -100% | 5.6h | stop loss -83% |

## Learned weights (v171)

_refit on 1836 observations (1717 shadow, 119 real), 503 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.143 |
| turnover | +0.120 |
| liq_quality | +0.104 |
| momentum_accel | +0.070 |
| buy_pressure | +0.061 |
| paid_boost | +0.028 |
| not_vertical | -0.028 |
| dip_in_uptrend | +0.027 |
| fdv_sanity | +0.024 |
| buzz | +0.023 |
| age_sweet | +0.013 |
| socials | -0.006 |

## Last run log
```
  BUY[exploit] LEOSTAR    $5.00 @ $0.0007127  score 0.71  solana  liq $60,159
  shadow: tracking 32, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $353.34 (-29.33% since start)
tick #2270  equity $353.34  cash $334.33  open 4
exits-only pass. equity $354.30 (next scan in 10 min)
tick #2271  equity $354.30  cash $334.33  open 4
exits-only pass. equity $354.88 (next scan in 9 min)
tick #2272  equity $354.88  cash $334.33  open 4
exits-only pass. equity $355.05 (next scan in 8 min)
tick #2273  equity $355.05  cash $334.33  open 4
exits-only pass. equity $355.44 (next scan in 7 min)
tick #2274  equity $355.44  cash $334.33  open 4
  SELL LEOSTAR    25% @ $0.001219  ->  $2.08   [take profit +50% (sold 25%)]
exits-only pass. equity $357.22 (next scan in 6 min)
tick #2275  equity $357.22  cash $336.41  open 4
exits-only pass. equity $357.91 (next scan in 5 min)
tick #2276  equity $357.91  cash $336.41  open 4
exits-only pass. equity $356.76 (next scan in 4 min)
tick #2277  equity $356.76  cash $336.41  open 4
exits-only pass. equity $356.64 (next scan in 3 min)
tick #2278  equity $356.64  cash $336.41  open 4
exits-only pass. equity $356.51 (next scan in 2 min)
tick #2279  equity $356.51  cash $336.41  open 4
exits-only pass. equity $356.41 (next scan in 1 min)
tick #2280  equity $356.41  cash $336.41  open 4
  scanning chains + news...
  178 raw candidates across 9 chains, 159 headlines/posts
  5 passed gates | rejected: liquidity too thin x109, no h1 volume x50, too old x9, already discovered x5
  top: MEOWL 0.80 | GTA 0.72 | LEOSTAR 0.65 | BAWSAQ 0.44 | COGE 0.40
  tick bar 0.66 (top 10% of 5, floor 0.45)
  skip MEOWL: solana concentration cap
  skip GTA: solana concentration cap
  no entries this tick
  shadow: tracking 33, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
