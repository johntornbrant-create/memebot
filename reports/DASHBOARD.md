# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T12:20:37+00:00`

## Equity

| | |
|---|---|
| Equity | **$326.55** |
| Return | **-34.69%** (start $500.00) |
| Cash | $303.14 |
| Deployed | $23.41 (7.2%) |
| Open positions | 6 / 8 |
| Closed trades | 51 (5W / 46L, WR 10%) |
| Profit factor | 0.34 |
| Fees + slippage paid | $92.94 |
| Ticks run | 2695 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $3.60 | -27% | +10% | 14.0h |
| GTA | solana | $5.00 | $5.30 | +7% | +17% | 11.0h |
| LEOSTAR | solana | $5.00 | $5.84 | +18% | +36% | 4.6h |
| GTA6 | ethereum | $5.00 | $2.25 | +15% | +39% | 2.6h |
| POPO | ethereum | $5.00 | $1.43 | -27% | +17% | 0.4h |
| BAWSAQ | solana | $5.00 | $4.94 | +0% | +0% | 0.0h |

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
  top: POPO 0.73 | BLG Champion 0.61 | BAWSAQ 0.43 | CHAR 0.42 | GROKIA 0.37
  tick bar 0.66 (top 10% of 6, floor 0.45)
  skip POPO: already held
  no entries this tick
  shadow: tracking 37, closed 3 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $327.82 (-34.44% since start)
tick #2685  equity $327.82  cash $308.14  open 5
exits-only pass. equity $327.26 (next scan in 10 min)
tick #2686  equity $327.26  cash $308.14  open 5
exits-only pass. equity $327.00 (next scan in 9 min)
tick #2687  equity $327.00  cash $308.14  open 5
exits-only pass. equity $327.06 (next scan in 8 min)
tick #2688  equity $327.06  cash $308.14  open 5
exits-only pass. equity $326.88 (next scan in 7 min)
tick #2689  equity $326.88  cash $308.14  open 5
exits-only pass. equity $326.89 (next scan in 6 min)
tick #2690  equity $326.89  cash $308.14  open 5
exits-only pass. equity $326.95 (next scan in 5 min)
tick #2691  equity $326.95  cash $308.14  open 5
exits-only pass. equity $326.90 (next scan in 4 min)
tick #2692  equity $326.90  cash $308.14  open 5
exits-only pass. equity $326.66 (next scan in 3 min)
tick #2693  equity $326.66  cash $308.14  open 5
exits-only pass. equity $326.82 (next scan in 2 min)
tick #2694  equity $326.82  cash $308.14  open 5
exits-only pass. equity $326.65 (next scan in 1 min)
tick #2695  equity $326.65  cash $308.14  open 5
  scanning chains + news...
  104 raw candidates across 9 chains, 159 headlines/posts
  4 passed gates | rejected: liquidity too thin x66, no h1 volume x28, too old x5, sell pressure x1
  top: BAWSAQ 0.66 | CHAR 0.46 | GROKIA 0.33 | LEOSTAR 0.33
  tick bar 0.66 (top 10% of 4, floor 0.45)
  BUY[exploit] BAWSAQ     $5.00 @ $0.001763  score 0.66  solana  liq $101,604
  shadow: tracking 37, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
