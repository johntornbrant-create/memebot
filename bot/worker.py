"""Long-running worker: real sub-minute polling inside GitHub Actions.

Why this exists. Measured over 200 runs, GitHub delivers only 2-6% of a */5 or */15 cron
on free runners - about one run every four hours - while a 6-hourly cron delivers 95%.
Frequency is what gets throttled, not duration. A job may run up to 6 hours.

So: ask for one run every 6 hours (reliable), and have that run stay alive the whole time,
checking positions every POLL_SECONDS. That converts 4-hour stop resolution into ~1-minute
resolution, free, with no server and no account.

State is committed every COMMIT_EVERY_MIN so nothing is lost if the runner is killed.
"""
import os, subprocess, sys, time, traceback
from datetime import datetime, timezone

from . import config, portfolio as pf_mod
from .run import tick

RUN_MINUTES      = int(os.environ.get("RUN_MINUTES", "330"))   # stop well before the 6h cap
POLL_SECONDS     = int(os.environ.get("POLL_SECONDS", "60"))   # position check cadence
COMMIT_EVERY_MIN = 5
ROOT = os.path.join(os.path.dirname(__file__), "..")


def log(m):
    print(f"[{datetime.now(timezone.utc):%H:%M:%S}] {m}", flush=True)


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def commit_state(label):
    git("config", "user.name", "memebot")
    git("config", "user.email", "memebot@users.noreply.github.com")
    for _ in range(4):
        git("fetch", "-q", "origin", "master")
        git("reset", "-q", "--soft", "origin/master")
        git("add", "-A", "state", "reports")
        if git("diff", "--staged", "--quiet").returncode == 0:
            return False
        git("commit", "-q", "-m", f"{label} {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}")
        if git("push", "-q", "origin", "HEAD:master").returncode == 0:
            return True
        time.sleep(4)
    log("WARNING: could not push state")
    return False


def main():
    started = time.time()
    deadline = started + RUN_MINUTES * 60
    last_commit = 0.0
    polls = 0
    log(f"worker up: polling every {POLL_SECONDS}s for {RUN_MINUTES} min "
        f"(full scan every {config.SCAN_EVERY_MIN} min)")

    while time.time() < deadline:
        polls += 1
        try:
            tick()                      # tick() itself decides whether a full scan is due
        except Exception:
            log("tick failed:\n" + traceback.format_exc())

        if (time.time() - last_commit) / 60 >= COMMIT_EVERY_MIN:
            if commit_state("worker"):
                log(f"state pushed (poll {polls})")
            last_commit = time.time()

        try:
            pf = pf_mod.load()
            if pf.get("halted"):
                log(f"HALTED: {pf.get('halt_reason','')} - exits still run, no new entries")
        except Exception:
            pass

        sleep = POLL_SECONDS - ((time.time() - started) % POLL_SECONDS)
        time.sleep(max(5, min(sleep, POLL_SECONDS)))

    commit_state("worker final")
    mins = (time.time() - started) / 60
    log(f"worker done: {polls} polls over {mins:.0f} min "
        f"(~1 position check every {mins*60/max(polls,1):.0f}s)")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
