# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-10-06T01:31:08+00:00`

## Equity

| | |
|---|---|
| Equity | **$332.84** |
| Return | **-33.43%** (start $500.00) |
| Cash | $326.18 |
| Deployed | $6.66 (2.0%) |
| Open positions | 1 / 8 |
| Closed trades | 80 (22W / 58L, WR 28%) |
| Profit factor | 0.49 |
| Fees + slippage paid | $67.87 |
| Ticks run | 1215 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| SWAP | solana | $6.66 | $6.59 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| TIT | $-5.43 | -80% | 8.5h | stop loss -80% |
| XMAN | $-6.88 | -100% | 7.1h | stop loss -99% |
| SS | $+1.46 | +21% | 9.3h | ratchet +25% (peak +95%) |
| NUTFLEX | $-4.20 | -59% | 1.1h | stop loss -58% |
| FKCANCER | $-2.88 | -41% | 0.8h | stop loss -39% |
| SAI | $-3.50 | -49% | 1.5h | stop loss -48% |
| ARTHUR | $-4.77 | -66% | 0.3h | stop loss -66% |
| WOOF | $-4.47 | -88% | 12.8h | ratchet +222% (peak +360%) |
| STOCK | $+5.89 | +113% | 9.5h | ratchet +120% (peak +214%) |
| SNOWBALL | $-2.98 | -41% | 1.1h | stop loss -40% |
| INKCHAN | $+0.60 | +8% | 1.0h | ratchet +0% (peak +69%) |
| SNOWBALL | $+7.23 | +101% | 0.8h | ratchet +78% (peak +154%) |
| 鹅次元 | $+3.43 | +48% | 0.9h | ratchet +88% (peak +168%) |
| SITRUMP | $-3.03 | -42% | 1.1h | stop loss -41% |
| Adventures | $-3.57 | -50% | 0.2h | stop loss -49% |

## Learned weights (v34)

_refit on 868 observations (788 shadow, 80 real), 296 winners (34% base rate)_

| Feature | Weight |
|---|---|
| turnover | +0.103 |
| buy_pressure | +0.087 |
| not_vertical | -0.069 |
| momentum_accel | +0.049 |
| txn_depth | +0.044 |
| buzz | -0.034 |
| dip_in_uptrend | +0.026 |
| socials | +0.026 |
| fdv_sanity | +0.021 |
| paid_boost | -0.011 |
| liq_quality | -0.010 |
| age_sweet | +0.001 |

## Last run log
```
tick #1215  equity $332.84  cash $332.84  open 0
  scanning chains + news...
  128 raw candidates across 7 chains, 160 headlines/posts
  7 passed gates | rejected: liquidity too thin x97, no h1 volume x17, too old x4, too new (bot war) x1, sell pressure x1
  top: SWAP 0.51 | MINTRO 0.39 | sizeinu 0.39 | blast 0.37 | ZKBNB 0.31
  tick bar 0.45 (top 30% of 7, floor 0.45)
  BUY[exploit] SWAP       $6.66 @ $0.0003564  score 0.51  solana  liq $58,857
  shadow: tracking 19, closed 18 this tick (5 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED e/acc      peak +5180%  (scored 0.58)
    MISSED BABYCALI   peak +4979%  (scored 0.93)
```
