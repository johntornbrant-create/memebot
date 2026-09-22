"""All knobs in one place. Paper trading only - no keys, no real orders, ever."""

# ---------- bankroll ----------
START_EQUITY      = 500.00      # USD, fake
CURRENCY          = "USD"

# ---------- risk (the part that matters) ----------
# Prior evidence: 58% of copied memecoin positions went to zero (copytrade sim 2026-08-19).
# So every position is assumed to be a potential -100%. Sizing is built around that.
MAX_POS_PCT       = 0.030       # 3.0% of equity per position  -> $15 on $500
MIN_POS_USD       = 5.00        # below this, fees/slippage eat the trade
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
TP_LADDER         = [(0.80, 0.50), (2.00, 0.25)]   # (+gain, fraction sold)
TRAIL_AFTER       = 2.00        # after +200%, trail the runner
TRAIL_PCT         = 0.40
TIME_STOP_H       = 24          # flat in 24h if not up >10%
TIME_STOP_MIN_GAIN= 0.10
MAX_HOLD_H        = 96          # nothing lives past 4 days

# ---------- execution realism ----------
DEX_FEE           = 0.0030      # 0.30% swap fee
PRIORITY_FEE_USD  = 0.35        # priority fee + gas, per side
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
ENTRY_THRESHOLD   = 0.62        # score must clear this to trade
LEARN_MIN_TRADES  = 60          # do not refit weights on less than this
LEARN_BLEND       = 0.50        # new weights = 50% fitted + 50% prior (anti-overfit)

# ---------- sources ----------
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
COLD_TRADES       = 80          # closed trades before switching to warm

# ---------- shadow book: learning from what it did NOT buy ----------
# Every gate-passing candidate is tracked for 24h whether or not we bought it.
# This is how it learns from misses, not only from its own losers.
SHADOW_ENABLED    = True
SHADOW_TRACK_H    = 24
SHADOW_MAX_OPEN   = 240
SHADOW_WIN_MOVE   = 0.50        # +50% peak in the window = "that was a good buy"
