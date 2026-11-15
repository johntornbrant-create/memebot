# MEMEBOT — paper trading dashboard

_Fake money. No broker, no keys, no real orders._  
Updated `2026-11-15T10:23:31+00:00`

## Equity

| | |
|---|---|
| Equity | **$414.42** |
| Return | **-17.12%** (start $500.00) |
| Cash | $398.29 |
| Deployed | $16.13 (3.9%) |
| Open positions | 3 / 8 |
| Closed trades | 24 (3W / 21L, WR 12%) |
| Profit factor | 0.40 |
| Fees + slippage paid | $9.40 |
| Ticks run | 1797 |

## Open positions

| Token | Chain | Cost | Now | P&L | Peak | Held |
|---|---|---|---|---|---|---|
| FOOD | solana | $5.05 | $4.44 | -11% | +17% | 11.1h |
| GTA | solana | $5.00 | $6.69 | +35% | +43% | 4.0h |
| Socks | solana | $5.00 | $4.94 | +0% | +0% | 0.0h |

## Last closed trades

| Token | P&L | % | Held | Exit reason |
|---|---|---|---|---|
| HOGE | $-1.94 | -39% | 0.2h | stop loss -37% |
| SHIT | $+4.56 | +91% | 14.6h | ratchet +90% (peak +172%) |
| worth | $-1.96 | -39% | 3.0h | stop loss -37% |
| 牛逼 | $+3.99 | +80% | 12.2h | ratchet +88% (peak +168%) |
| J*B | $-4.19 | -84% | 3.8h | stop loss -83% |
| FLAPAI | $-6.90 | -79% | 6.7h | stop loss -78% |
| GTA | $-5.00 | -57% | 6.7h | stop loss -56% |
| GTA | $-2.64 | -43% | 11.7h | ratchet +65% (peak +135%) |
| TIT | $-7.07 | -80% | 4.9h | stop loss -79% |
| 币安AiPro | $-1.62 | -25% | 18.2h | ratchet +47% (peak +109%) |
| CATTLEAXE | $-2.39 | -38% | 7.9h | stop loss -37% |
| BTC | $-2.59 | -42% | 4.0h | stop loss -40% |
| SWORDOPE | $-2.42 | -38% | 4.8h | stop loss -36% |
| REACHY | $-6.23 | -99% | 13.8h | stop loss -99% |
| KURUMI | $+5.28 | +58% | 6.0h | ratchet +65% (peak +136%) |

## Learned weights (v168)

_refit on 1797 observations (1695 shadow, 102 real), 492 winners (27% base rate)_

| Feature | Weight |
|---|---|
| txn_depth | +0.149 |
| turnover | +0.126 |
| liq_quality | +0.089 |
| momentum_accel | +0.064 |
| buy_pressure | +0.061 |
| paid_boost | +0.035 |
| dip_in_uptrend | +0.031 |
| not_vertical | -0.029 |
| buzz | +0.020 |
| fdv_sanity | +0.011 |
| age_sweet | +0.007 |
| socials | -0.003 |

## Last run log
```
  scanning chains + news...
  142 raw candidates across 7 chains, 160 headlines/posts
  0 passed gates | rejected: liquidity too thin x106, no h1 volume x26, already discovered x6, too old x4
  no entries this tick
  shadow: tracking 16, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
done. equity $414.18 (-17.16% since start)
tick #1787  equity $414.18  cash $403.29  open 2
exits-only pass. equity $414.30 (next scan in 10 min)
tick #1788  equity $414.30  cash $403.29  open 2
exits-only pass. equity $414.15 (next scan in 9 min)
tick #1789  equity $414.15  cash $403.29  open 2
exits-only pass. equity $414.30 (next scan in 8 min)
tick #1790  equity $414.30  cash $403.29  open 2
exits-only pass. equity $414.17 (next scan in 7 min)
tick #1791  equity $414.17  cash $403.29  open 2
exits-only pass. equity $414.49 (next scan in 6 min)
tick #1792  equity $414.49  cash $403.29  open 2
exits-only pass. equity $414.88 (next scan in 5 min)
tick #1793  equity $414.88  cash $403.29  open 2
exits-only pass. equity $414.45 (next scan in 4 min)
tick #1794  equity $414.45  cash $403.29  open 2
exits-only pass. equity $414.57 (next scan in 3 min)
tick #1795  equity $414.57  cash $403.29  open 2
exits-only pass. equity $414.64 (next scan in 2 min)
tick #1796  equity $414.64  cash $403.29  open 2
exits-only pass. equity $414.54 (next scan in 1 min)
tick #1797  equity $414.54  cash $403.29  open 2
  scanning chains + news...
  141 raw candidates across 7 chains, 160 headlines/posts
  1 passed gates | rejected: liquidity too thin x106, no h1 volume x25, already discovered x5, too old x4
  top: Socks 0.39
  tick bar 0.45 (top 10% of 1, floor 0.45)
  BUY[explore] Socks      $5.00 @ $0.0001739  score 0.39  solana  liq $29,573
  shadow: tracking 17, closed 0 this tick (0 would have won)
    MISSED NI         peak +277296%  (scored 0.21)
    MISSED GTAX       peak +11365%  (scored 0.25)
    MISSED e/acc      peak +5180%  (scored 0.58)
```
