#!/usr/bin/env python3
"""Record which functions have a Microsoft Learn page, for the cards to link to.

  python lab/shared-export/learn_links.py exports/learn-links.json

Asks https://learn.microsoft.com/en-us/powerquery-m/<card file> for every function in the
catalogue and keeps those that answer 200 after redirects. sync_shared.py links only those:
a card never carries a link nobody checked. The result is input to the sync, like the
#shared exports, so it lives in exports/ and is rerun when the catalogue changes.
"""
import json
import os
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "scripts"))
import m_blocks  # noqa: E402

BASE = "https://learn.microsoft.com/en-us/powerquery-m/"


def status(file, tries=6):
    """200 or 404, or None when Learn would not say. A 429 (rate limit) is waited out,
    never read as "no page"."""
    request = urllib.request.Request(BASE + file, method="HEAD",
                                     headers={"User-Agent": "powerquery-m-for-agents link check"})
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return file, response.status
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return file, 404
            if e.code != 429 and e.code < 500:
                return file, None
        except OSError:
            pass
        time.sleep(min(60, 5 * 2 ** attempt))
    return file, None


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print(__doc__, file=sys.stderr)
        return 2
    files = sorted({r["file"] for r in m_blocks.load_catalog()["functions"]})
    results = {}
    for file in files:
        results[file] = status(file)[1]
        time.sleep(0.5)
    unknown = sorted(f for f, s in results.items() if s is None)
    if unknown:
        print(f"{len(unknown)} page(s) gave no answer; rerun: {', '.join(unknown[:5])}", file=sys.stderr)
        return 1
    found = sorted(f for f, s in results.items() if s == 200)
    with open(argv[0], "w", encoding="utf-8", newline="\n") as f:
        json.dump({"base": BASE, "files": found}, f, indent=1)
        f.write("\n")
    print(f"{len(found)} of {len(files)} functions have a Learn page -> {argv[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
