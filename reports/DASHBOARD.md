# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T02:44:42+00:00`

## Equity

| | |
|---|---|
| Equity | **$350.34** |
| Return | **-29.93%** (start $500.00) |
| Cash | $332.65 |
| Deployed | $17.69 (5.1%) |
| Open positions | 4 / 8 |
| Closed trades | 44 (5W / 39L, WR 11%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $62.21 |
| Ticks run | 2445 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| GTA | solana | $5.00 | $5.27 | +7% | +39% | 19.6h |
| TE | base | $5.00 | $3.69 | -25% | +10% | 4.4h |
| ETF | solana | $5.00 | $4.61 | -7% | +19% | 2.0h |
| GTA | solana | $5.00 | $4.13 | -16% | +1% | 1.4h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| 现货不怕 | $-1.95 | -39% | 1.5h | stop loss -37% |
| LEOSTAR | $+1.63 | +33% | 1.8h | ratchet +25% (peak +77%) |
| WISHMAS | $-1.36 | -27% | 24.0h | time stop 24h, only -25% |
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
  no entries this tick
  shadow: tracking 32, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $350.92 (-29.82% since start)
tick #2435  equity $350.92  cash $329.60  open 5
exits-only pass. equity $350.74 (next scan in 10 min)
tick #2436  equity $350.74  cash $329.60  open 5
exits-only pass. equity $350.81 (next scan in 9 min)
tick #2437  equity $350.81  cash $329.60  open 5
exits-only pass. equity $350.45 (next scan in 8 min)
tick #2438  equity $350.45  cash $329.60  open 5
exits-only pass. equity $350.61 (next scan in 7 min)
tick #2439  equity $350.61  cash $329.60  open 5
  SELL 现货不怕       100% @ $0.0001001  ->  $3.05   [stop loss -37%]
exits-only pass. equity $350.93 (next scan in 6 min)
tick #2440  equity $350.93  cash $332.65  open 4
exits-only pass. equity $350.92 (next scan in 5 min)
tick #2441  equity $350.92  cash $332.65  open 4
exits-only pass. equity $350.66 (next scan in 4 min)
tick #2442  equity $350.66  cash $332.65  open 4
exits-only pass. equity $350.96 (next scan in 3 min)
tick #2443  equity $350.96  cash $332.65  open 4
exits-only pass. equity $350.90 (next scan in 2 min)
tick #2444  equity $350.90  cash $332.65  open 4
exits-only pass. equity $350.76 (next scan in 1 min)
tick #2445  equity $350.76  cash $332.65  open 4
  scanning chains + news...
  124 raw candidates across 8 chains, 159 headlines/posts
  6 passed gates | rejected: liquidity too thin x78, no h1 volume x27, too old x11, already discovered x2
  top: HOGE 0.83 | BAWSAQ 0.67 | ETF 0.57 | GTA 0.47 | LEOSTAR 0.44
  tick bar 0.66 (top 10% of 6, floor 0.45)
  skip GTA: already held
  skip HOGE: blacklisted (previously stopped out)
  no entries this tick
  shadow: tracking 32, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
