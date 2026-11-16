# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T07:33:29+00:00`

## Equity

| | |
|---|---|
| Equity | **$368.30** |
| Return | **-26.34%** (start $500.00) |
| Cash | $351.30 |
| Deployed | $17.00 (4.6%) |
| Open positions | 4 / 8 |
| Closed trades | 37 (4W / 33L, WR 11%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $52.52 |
| Ticks run | 2079 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.44 | +24% | +29% | 11.8h |
| WISHMAS | solana | $5.00 | $4.38 | -11% | +5% | 7.0h |
| Anthropig | solana | $5.00 | $5.21 | +5% | +11% | 5.6h |
| GTA | solana | $5.00 | $4.97 | +0% | +8% | 0.4h |

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
  skip GTA: already held
  skip Marvin: blacklisted (previously stopped out)
  no entries this tick
  shadow: tracking 45, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $367.60 (-26.48% since start)
tick #2069  equity $367.60  cash $351.30  open 4
exits-only pass. equity $367.31 (next scan in 10 min)
tick #2070  equity $367.31  cash $351.30  open 4
exits-only pass. equity $367.31 (next scan in 9 min)
tick #2071  equity $367.31  cash $351.30  open 4
exits-only pass. equity $368.10 (next scan in 8 min)
tick #2072  equity $368.10  cash $351.30  open 4
exits-only pass. equity $368.44 (next scan in 7 min)
tick #2073  equity $368.44  cash $351.30  open 4
exits-only pass. equity $368.18 (next scan in 6 min)
tick #2074  equity $368.18  cash $351.30  open 4
exits-only pass. equity $368.27 (next scan in 5 min)
tick #2075  equity $368.27  cash $351.30  open 4
exits-only pass. equity $368.65 (next scan in 4 min)
tick #2076  equity $368.65  cash $351.30  open 4
exits-only pass. equity $368.52 (next scan in 3 min)
tick #2077  equity $368.52  cash $351.30  open 4
exits-only pass. equity $368.67 (next scan in 2 min)
tick #2078  equity $368.67  cash $351.30  open 4
exits-only pass. equity $368.58 (next scan in 1 min)
tick #2079  equity $368.58  cash $351.30  open 4
  scanning chains + news...
  103 raw candidates across 5 chains, 160 headlines/posts
  2 passed gates | rejected: liquidity too thin x56, no h1 volume x27, too old x14, already discovered x4
  top: Anthropig 0.48 | GTA 0.26
  tick bar 0.48 (top 10% of 2, floor 0.45)
  skip Anthropig: already held
  no entries this tick
  shadow: tracking 44, closed 1 this tick (1 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
