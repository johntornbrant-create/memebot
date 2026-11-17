# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-17T11:20:33+00:00`

## Equity

| | |
|---|---|
| Equity | **$330.34** |
| Return | **-33.93%** (start $500.00) |
| Cash | $313.14 |
| Deployed | $17.20 (5.2%) |
| Open positions | 4 / 8 |
| Closed trades | 51 (5W / 46L, WR 10%) |
| Profit factor | 0.34 |
| Fees + slippage paid | $89.85 |
| Ticks run | 2640 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| TE | base | $5.00 | $3.60 | -27% | +10% | 13.0h |
| GTA | solana | $5.00 | $5.29 | +7% | +10% | 10.0h |
| LEOSTAR | solana | $5.00 | $5.90 | +19% | +36% | 3.6h |
| GTA6 | ethereum | $5.00 | $2.41 | +23% | +39% | 1.6h |

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
  skip BLG Champion: already held
  no entries this tick
  shadow: tracking 38, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $332.22 (-33.56% since start)
tick #2630  equity $332.22  cash $310.07  open 5
exits-only pass. equity $330.73 (next scan in 10 min)
tick #2631  equity $330.73  cash $310.07  open 5
  SELL BLG Champion 100% @ $2.75  ->  $3.07   [stop loss -36%]
exits-only pass. equity $329.69 (next scan in 9 min)
tick #2632  equity $329.69  cash $313.14  open 4
exits-only pass. equity $329.99 (next scan in 8 min)
tick #2633  equity $329.99  cash $313.14  open 4
exits-only pass. equity $330.16 (next scan in 7 min)
tick #2634  equity $330.16  cash $313.14  open 4
exits-only pass. equity $330.04 (next scan in 6 min)
tick #2635  equity $330.04  cash $313.14  open 4
exits-only pass. equity $330.15 (next scan in 5 min)
tick #2636  equity $330.15  cash $313.14  open 4
exits-only pass. equity $330.36 (next scan in 4 min)
tick #2637  equity $330.36  cash $313.14  open 4
exits-only pass. equity $330.37 (next scan in 3 min)
tick #2638  equity $330.37  cash $313.14  open 4
exits-only pass. equity $330.41 (next scan in 2 min)
tick #2639  equity $330.41  cash $313.14  open 4
exits-only pass. equity $330.21 (next scan in 1 min)
tick #2640  equity $330.21  cash $313.14  open 4
  scanning chains + news...
  122 raw candidates across 7 chains, 159 headlines/posts
  8 passed gates | rejected: liquidity too thin x73, no h1 volume x24, too old x13, already discovered x4
  top: BLG Champion 0.58 | GTA 0.53 | BAWSAQ 0.45 | BAWSAQ 0.45 | ETF 0.35
  tick bar 0.58 (top 10% of 8, floor 0.45)
  skip BLG Champion: blacklisted (previously stopped out)
  no entries this tick
  shadow: tracking 38, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
