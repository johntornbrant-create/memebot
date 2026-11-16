# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-16T11:59:49+00:00`

## Equity

| | |
|---|---|
| Equity | **$368.04** |
| Return | **-26.39%** (start $500.00) |
| Cash | $346.30 |
| Deployed | $21.74 (5.9%) |
| Open positions | 5 / 8 |
| Closed trades | 37 (4W / 33L, WR 11%) |
| Profit factor | 0.37 |
| Fees + slippage paid | $55.56 |
| Ticks run | 2179 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| Macca | ethereum | $5.00 | $2.20 | +12% | +29% | 16.2h |
| WISHMAS | solana | $5.00 | $4.37 | -12% | +5% | 11.4h |
| Anthropig | solana | $5.00 | $3.28 | -34% | +13% | 10.0h |
| GTA | solana | $5.00 | $6.89 | +39% | +39% | 4.8h |
| 1.0 | ethereum | $5.00 | $1.96 | +0% | +0% | 0.0h |

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
tick #2179  equity $367.71  cash $351.30  open 4
  scanning chains + news...
  144 raw candidates across 7 chains, 160 headlines/posts
  6 passed gates | rejected: liquidity too thin x81, no h1 volume x48, too old x3, already discovered x3, unknown age x2
  top: 1.0 0.81 | mihao 0.77 | Anthropig 0.56 | gtacoin 0.36 | GTA 0.33
  tick bar 0.64 (top 10% of 6, floor 0.45)
  BUY[exploit] 1.0        $5.00 @ $0.0001392  score 0.81  ethereum  liq $29,950
  skip 1.0: solana concentration cap
  shadow: tracking 46, closed 2 this tick (1 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
