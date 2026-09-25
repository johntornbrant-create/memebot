"""All knobs in one place. Paper trading only - no keys, no real orders, ever."""

# ---------- bankroll ----------
START_EQUITY      = 500.00      # USD, fake
CURRENCY          = "USD"

# ---------- risk (the part that matters) ----------
# Prior evidence: 58% of copied memecoin positions went to zero (copytrade sim 2026-08-19).
# So every position is assumed to be a potential -100%. Sizing is built around that.
MAX_POS_PCT       = 0.020       # 2.0% of equity -> $10 on $500. Cut from 3% while the
                                # strategy is unprofitable at this polling rate: extends runway
                                # so the shadow book keeps collecting the data that matters.
MIN_POS_USD       = 5.00        # 2% of $425 is $8.50 and this floor was $8.00 - one bad
                                # week and every trade would fall below the minimum and the
                                # bot would silently stop trading. Gas is now ~$0.02 on
                                # Solana, so $5 is fine (~1% round trip).
MAX_CONCURRENT    = 8           # 8 x 3% = 24% max exposure at any instant
MAX_DEPLOYED_PCT  = 0.35        # never more than 35% of equity out of cash
MAX_PER_CHAIN     = 3           # 20 chains - do not pile into one
MAX_NEW_PER_TICK  = 2           # never chase a whole burst at once (sim died from this)

# circuit breakers
DAILY_LOSS_HALT   = -0.06       # -6% on the day -> no new entries for 24h
WEEKLY_LOSS_HALT  = -0.15       # -15% on the week -> no new entries for 7d
KILL_SWITCH_EQ    = 0.65        # equity < 65% of start ($325) -> hard halt, manual reset only
MAX_TRADES_DAY    = 12          # activity cap

# ---------- exits ----------
STOP_LOSS         = -0.35       # memecoin noise eats tight stops

# RATCHET: once a gain has been earned, it is never fully given back. Measured need -
# day 1 had a position peak at +59% and still close at -100%, and three more peak above
# +110% and close near zero. Selection was finding runners; the exit handed them back.
# (peak gain reached, stop floor from then on). Monotonic, never loosens.
RATCHET           = [(0.40, 0.00), (0.70, 0.25), (1.00, 0.40)]

# TAKE-PROFIT LADDER - restored, and it was a mistake to remove it.
# At 15-minute polling a stop is unenforceable: JEANCOIN peaked +1139%, its ratchet floor
# was +767%, and it closed at -84%. $149 was lost gapping THROUGH ratchet floors in 24h.
# Selling into strength is the only exit that does not need the price to come back to us.
# Grid-searched over all 44 real closed trades; this was the best of 13 configurations
# (-$42.19 vs -$73.65 actual). Every other config, including flat targets, did worse.
TP_LADDER         = [(0.50, 0.25), (1.50, 0.25), (4.00, 0.25), (9.00, 0.25)]
TRAIL_AFTER       = 1.00        # start trailing at +100%: winners peaked at +724%
                                # and +248% then gapped down between 15-min checks
TRAIL_PCT         = 0.30
TIME_STOP_H       = 24          # flat in 24h if not up >10%
TIME_STOP_MIN_GAIN= 0.10
MAX_HOLD_H        = 96          # nothing lives past 4 days

# ---------- execution realism ----------
DEX_FEE           = 0.0030      # 0.30% swap fee

# Per-side gas/priority cost, by chain. A flat $0.35 was wrong by ~20x on Solana - where
# ~85% of trades land - and it alone accounted for 85% of the first day's drawdown while
# gross PnL was roughly flat. Fees must match the chain or the bot learns from fiction.
PRIORITY_FEE_BY_CHAIN = {
    "solana": 0.02, "base": 0.03, "arbitrum": 0.03, "optimism": 0.03, "blast": 0.03,
    "linea": 0.03, "mantle": 0.03, "unichain": 0.03, "sonic": 0.03, "abstract": 0.03,
    "berachain": 0.03, "hyperliquid": 0.03, "bsc": 0.05, "polygon": 0.04,
    "avalanche": 0.05, "cronos": 0.05, "sui": 0.04, "ton": 0.05, "tron": 0.05,
    "ethereum": 3.00,
}
PRIORITY_FEE_DEFAULT = 0.10
SLIPPAGE_K        = 0.9         # slippage = K * (size / liquidity), both sides
EXTRA_SLIP_FLOOR  = 0.004       # 0.4% minimum slippage - you never get the quote

# ---------- candidate filters (hard gates, applied before scoring) ----------
MIN_LIQUIDITY_USD = 25_000      # thinner than this = cannot exit
MAX_LIQUIDITY_USD = 3_000_000   # already discovered
MIN_VOL_H1_USD    = 15_000
MIN_AGE_MIN       = 20          # skip the first 20min - that is the bot war, we lose it
MAX_AGE_H         = 72
MIN_TXNS_H1       = 40
MIN_BUYERS_RATIO  = 0.45        # buys / (buys+sells) in h1
MAX_FDV_LIQ_RATIO = 60          # FDV 60x liquidity = exit liquidity trap
CHAINS = ["solana", "base", "ethereum", "bsc", "arbitrum", "polygon", "avalanche",
          "sui", "ton", "tron", "blast", "optimism", "hyperliquid", "abstract",
          "berachain", "sonic", "unichain", "linea", "mantle", "cronos"]

# ---------- scoring ----------
ENTRY_THRESHOLD   = 0.70        # walk-forward tested: 0.70 held up out-of-sample
                                # (+24.6%/trade), 0.79 collapsed to +1.4%. In-sample said
                                # 0.85 was best - that was overfitting. Cap the adaptive
                                # threshold near here.
THRESHOLD_MAX     = 0.74
LEARN_MIN_TRADES  = 60          # do not refit weights on less than this
LEARN_BLEND       = 0.50        # new weights = 50% fitted + 50% prior (anti-overfit)

# ---------- sources ----------
GT_CHAINS_PER_TICK = 8          # rotate GeckoTerminal deep-scan; DexScreener covers all
HTTP_TIMEOUT      = 20
USER_AGENT        = "memebot-paper/1.0 (research; no trading)"
NEWS_FEEDS = [
    "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "https://cointelegraph.com/rss",
    "https://decrypt.co/feed",
    "https://feeds.foxnews.com/foxnews/latest",
    "https://news.google.com/rss/search?q=memecoin+OR+solana+OR+crypto&hl=en-US&gl=US&ceid=US:en",
]
REDDIT_SUBS = ["CryptoCurrency", "solana", "CryptoMoonShots", "SatoshiStreetBets", "wallstreetbets"]


# ---------- self-learning: explore vs exploit ----------
# A bot that only buys what it already believes never finds out what it was wrong about.
# A share of every tick is spent exploring: random picks among candidates that pass the
# SAFETY gates, score ignored entirely.
EXPLORE_RATE_COLD = 0.60        # before it has data, mostly explore
EXPLORE_RATE_WARM = 0.20        # forever after - never stop learning
COLD_TRADES       = 40          # we now have 140 labelled observations - stop burning
                                # 60% of entries on random picks, drop to the 20% warm rate

# ---------- shadow book: learning from what it did NOT buy ----------
# Every gate-passing candidate is tracked for 24h whether or not we bought it.
# This is how it learns from misses, not only from its own losers.
SHADOW_ENABLED    = True
SHADOW_TRACK_H    = 24
SHADOW_MAX_OPEN   = 240
SHADOW_WIN_MOVE   = 0.50        # +50% peak in the window = "that was a good buy"
