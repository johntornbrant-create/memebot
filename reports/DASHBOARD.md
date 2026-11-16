# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T07:09:28+00:00`

## Equity

| | |
|---|---|
| Equity | **$367.74** |
| Return | **-26.45%** (start $500.00) |
| Cash | $351.30 |
| Deployed | $16.44 (4.5%) |
| Open positions | 4 / 8 |
| Closed trades | 37 (4W / 33L, WR 11%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $52.52 |
| Ticks run | 2057 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.27 | +16% | +29% | 11.4h |
| WISHMAS | solana | $5.00 | $4.10 | -17% | +5% | 6.6h |
| Anthropig | solana | $5.00 | $5.06 | +2% | +5% | 5.2h |
| GTA | solana | $5.00 | $4.94 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
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
| Socks | $+0.41 | +8% | 7.2h | ratchet +42% (peak +103%) |
| Macca | $-3.03 | -61% | 1.2h | stop loss -59% |
| HOGE | $-1.94 | -39% | 0.2h | stop loss -37% |
| SHIT | $+4.56 | +91% | 14.6h | ratchet +90% (peak +172%) |

## Learned weights (v170)

_refit on 1825 observations (1708 shadow, 117 real), 498 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.145 |
| turnover | +0.117 |
| liq_quality | +0.105 |
| momentum_accel | +0.066 |
| buy_pressure | +0.060 |
| not_vertical | -0.033 |
| paid_boost | +0.029 |
| dip_in_uptrend | +0.029 |
| fdv_sanity | +0.023 |
| buzz | +0.019 |
| age_sweet | +0.018 |
| socials | -0.009 |

## Last run log
```
  skip BUTTHOLE: solana concentration cap
  no entries this tick
  shadow: tracking 45, closed 1 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $368.16 (-26.37% since start)
tick #2047  equity $368.16  cash $353.34  open 4
exits-only pass. equity $368.03 (next scan in 10 min)
tick #2048  equity $368.03  cash $353.34  open 4
exits-only pass. equity $367.57 (next scan in 9 min)
tick #2049  equity $367.57  cash $353.34  open 4
  SELL Marvin     100% @ $0.00039  ->  $2.96   [stop loss -39%]
exits-only pass. equity $367.32 (next scan in 8 min)
tick #2050  equity $367.32  cash $356.30  open 3
exits-only pass. equity $367.38 (next scan in 7 min)
tick #2051  equity $367.38  cash $356.30  open 3
exits-only pass. equity $367.61 (next scan in 6 min)
tick #2052  equity $367.61  cash $356.30  open 3
exits-only pass. equity $367.52 (next scan in 5 min)
tick #2053  equity $367.52  cash $356.30  open 3
exits-only pass. equity $367.53 (next scan in 4 min)
tick #2054  equity $367.53  cash $356.30  open 3
exits-only pass. equity $367.53 (next scan in 3 min)
tick #2055  equity $367.53  cash $356.30  open 3
exits-only pass. equity $367.67 (next scan in 2 min)
tick #2056  equity $367.67  cash $356.30  open 3
exits-only pass. equity $367.97 (next scan in 1 min)
tick #2057  equity $367.97  cash $356.30  open 3
  scanning chains + news...
  106 raw candidates across 5 chains, 160 headlines/posts
  4 passed gates | rejected: liquidity too thin x57, no h1 volume x27, too old x14, already discovered x4
  top: BUTTHOLE 0.51 | Marvin 0.50 | Anthropig 0.47 | GTA 0.29
  tick bar 0.51 (top 10% of 4, floor 0.45)
  BUY[explore] GTA        $5.00 @ $0.0001346  score 0.29  solana  liq $35,257
  skip BUTTHOLE: solana concentration cap
  shadow: tracking 45, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
