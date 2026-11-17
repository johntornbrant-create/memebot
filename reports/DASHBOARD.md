# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T11:56:36+00:00`

## Equity

| | |
|---|---|
| Equity | **$329.36** |
| Return | **-34.13%** (start $500.00) |
| Cash | $308.14 |
| Deployed | $21.21 (6.4%) |
| Open positions | 5 / 8 |
| Closed trades | 51 (5W / 46L, WR 10%) |
| Profit factor | 0.34 |
| Fees + slippage paid | $92.89 |
| Ticks run | 2673 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $3.60 | -27% | +10% | 13.6h |
| GTA | solana | $5.00 | $5.18 | +5% | +17% | 10.6h |
| LEOSTAR | solana | $5.00 | $5.23 | +6% | +36% | 4.2h |
| GTA6 | ethereum | $5.00 | $2.20 | +12% | +39% | 2.2h |
| POPO | ethereum | $5.00 | $1.96 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| BLG Champion | $-1.93 | -39% | 0.2h | stop loss -36% |
| ETF | $-2.06 | -41% | 10.2h | stop loss -40% |
| BLG Champion | $-0.20 | -4% | 1.0h | ratchet +0% (peak +44%) |
| GTAPEPE | $-5.00 | -100% | 1.6h | ratchet +85% (peak +164%) |
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
  top: BLG Champion 0.60 | GROKIA 0.57 | GTA 0.53 | BAWSAQ 0.49 | LEOSTAR 0.42
  tick bar 0.60 (top 10% of 8, floor 0.45)
  skip BLG Champion: blacklisted (previously stopped out)
  no entries this tick
  shadow: tracking 39, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $330.11 (-33.98% since start)
tick #2663  equity $330.11  cash $313.14  open 4
exits-only pass. equity $330.22 (next scan in 10 min)
tick #2664  equity $330.22  cash $313.14  open 4
exits-only pass. equity $330.32 (next scan in 9 min)
tick #2665  equity $330.32  cash $313.14  open 4
exits-only pass. equity $330.12 (next scan in 8 min)
tick #2666  equity $330.12  cash $313.14  open 4
exits-only pass. equity $329.98 (next scan in 7 min)
tick #2667  equity $329.98  cash $313.14  open 4
exits-only pass. equity $330.16 (next scan in 6 min)
tick #2668  equity $330.16  cash $313.14  open 4
exits-only pass. equity $330.07 (next scan in 5 min)
tick #2669  equity $330.07  cash $313.14  open 4
exits-only pass. equity $330.09 (next scan in 4 min)
tick #2670  equity $330.09  cash $313.14  open 4
exits-only pass. equity $329.90 (next scan in 3 min)
tick #2671  equity $329.90  cash $313.14  open 4
exits-only pass. equity $329.91 (next scan in 2 min)
tick #2672  equity $329.91  cash $313.14  open 4
exits-only pass. equity $329.64 (next scan in 1 min)
tick #2673  equity $329.64  cash $313.14  open 4
  scanning chains + news...
  114 raw candidates across 7 chains, 159 headlines/posts
  9 passed gates | rejected: liquidity too thin x71, no h1 volume x19, too old x11, already discovered x4
  top: POPO 0.88 | BLG Champion 0.61 | BAWSAQ 0.48 | GTA 0.46 | LEOSTAR 0.44
  tick bar 0.66 (top 10% of 9, floor 0.45)
  BUY[exploit] POPO       $5.00 @ $0.0001002  score 0.88  ethereum  liq $25,196
  shadow: tracking 40, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
