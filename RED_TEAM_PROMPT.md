# Paste this into ChatGPT / Gemini / Grok, along with the repo link or the files

You are red-teaming a PAPER-TRADING memecoin bot. Fake money ($500), no wallet, no keys,
no real orders. Your job is to find where it loses money or breaks, NOT to praise it.

Files that matter: bot/risk.py, bot/portfolio.py, bot/features.py, bot/config.py, bot/run.py

Answer ONLY these six questions. Be specific, cite line numbers, no compliments.

1. RISK HOLES. Give a concrete sequence of market events that drops equity more than 35%
   before the kill switch (equity < $325) can fire. Ticks are 15 minutes apart and the bot
   only prices positions once per tick.

2. FILL REALISM. `_friction()` in portfolio.py models cost as
   slippage = 0.9 * (size/liquidity) + 0.004, plus a 0.30% DEX fee and $0.35 priority fee.
   For a $15 position in a $50k pool on a token moving 40%/hour, is this optimistic?
   By how much? Give a number, not an adjective.

3. SURVIVORSHIP / DEAD TOKENS. Positions that cannot be priced are marked to ZERO. Is that
   right, or does it understate losses in some cases and overstate them in others? What
   breaks if DexScreener simply 404s for 20 minutes on a token that is actually fine?

4. LEARNING TRAP. bot/learn.py refits 12 weights on closed trades, labels a win as +15%,
   requires 60 trades, blends 50/50 with a prior. Name the specific overfitting or
   selection-bias failure this will hit first. Note that the bot only ever observes
   outcomes for tokens it CHOSE to buy — it never sees what the rejected ones did.

5. THE EXIT-FIRST BUG CLASS. exit_rules() returns at most ONE action per tick and the
   take-profit ladder marks each rung as hit permanently. Find the scenario where this
   leaves the bot holding something it should have sold.

6. WHAT WOULD YOU DELETE? Which of the 12 features is most likely pure noise, and what is
   your reasoning? Do not suggest adding features. Suggest removing one.

Finish with: the single highest-expected-value change, in one sentence.
