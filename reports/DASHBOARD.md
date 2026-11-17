# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T09:20:37+00:00`

## Equity

| | |
|---|---|
| Equity | **$337.14** |
| Return | **-32.57%** (start $500.00) |
| Cash | $312.32 |
| Deployed | $24.82 (7.4%) |
| Open positions | 6 / 8 |
| Closed trades | 47 (5W / 42L, WR 11%) |
| Profit factor | 0.35 |
| Fees + slippage paid | $77.52 |
| Ticks run | 2530 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $3.64 | -26% | +10% | 11.0h |
| ETF | solana | $5.00 | $4.06 | -18% | +19% | 8.6h |
| GTA | solana | $5.00 | $5.20 | +5% | +10% | 8.0h |
| LEOSTAR | solana | $5.00 | $4.41 | -11% | +3% | 1.6h |
| GTAPEPE | ethereum | $5.00 | $2.52 | +28% | +31% | 0.6h |
| BLG Champion | bsc | $5.00 | $4.91 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| KATIA | $-5.00 | -100% | 1.0h | stop loss -79% |
| BAWSAQ | $-5.00 | -100% | 3.9h | stop loss -99% |
| GTA | $-0.33 | -7% | 24.6h | time stop 25h, only -4% |
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
  skip GTAPEPE: already held
  skip Macca: blacklisted (previously stopped out)
  no entries this tick
  shadow: tracking 36, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $339.49 (-32.10% since start)
tick #2520  equity $339.49  cash $317.32  open 6
  SELL KATIA      100% @ $3.414e-05  ->  $0.00   [stop loss -79%]
exits-only pass. equity $337.38 (next scan in 10 min)
tick #2521  equity $337.38  cash $317.32  open 5
exits-only pass. equity $337.16 (next scan in 9 min)
tick #2522  equity $337.16  cash $317.32  open 5
exits-only pass. equity $337.06 (next scan in 8 min)
tick #2523  equity $337.06  cash $317.32  open 5
exits-only pass. equity $337.02 (next scan in 7 min)
tick #2524  equity $337.02  cash $317.32  open 5
exits-only pass. equity $336.99 (next scan in 6 min)
tick #2525  equity $336.99  cash $317.32  open 5
exits-only pass. equity $336.87 (next scan in 5 min)
tick #2526  equity $336.87  cash $317.32  open 5
exits-only pass. equity $337.10 (next scan in 4 min)
tick #2527  equity $337.10  cash $317.32  open 5
exits-only pass. equity $337.26 (next scan in 3 min)
tick #2528  equity $337.26  cash $317.32  open 5
exits-only pass. equity $337.18 (next scan in 2 min)
tick #2529  equity $337.18  cash $317.32  open 5
exits-only pass. equity $337.20 (next scan in 1 min)
tick #2530  equity $337.20  cash $317.32  open 5
  scanning chains + news...
  150 raw candidates across 7 chains, 159 headlines/posts
  8 passed gates | rejected: liquidity too thin x89, no h1 volume x32, too old x12, already discovered x9
  top: BLG Champion 0.67 | GTAPEPE 0.64 | KATIA 0.63 | GTA 0.60 | Rocco 0.51
  tick bar 0.66 (top 10% of 8, floor 0.45)
  BUY[exploit] BLG Champion $5.00 @ $7.1  score 0.67  bsc  liq $720,665
  shadow: tracking 36, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
