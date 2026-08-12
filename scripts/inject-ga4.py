#!/usr/bin/env python3
"""Ensure the GA4 gtag.js snippet is present immediately after <head> on every
HTML page in the site.

Run with no arguments to inject the snippet into any page that is missing it:

    python3 scripts/inject-ga4.py

Run with --check to only report missing/misplaced pages and exit non-zero if
any are found (used by CI to fail fast without modifying files):

    python3 scripts/inject-ga4.py --check

Keeping the GA4 measurement ID in one place means new pages get tracking
automatically via the CI workflow (.github/workflows/ga4-tracking.yml).
"""
import glob
import re
import sys

GA4_ID = "G-N19Q4DQ28B"

SNIPPET = f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', '{GA4_ID}');
</script>"""


# Google Search Console verification files must contain only their token line,
# so they are never touched.
EXCLUDE_RE = re.compile(r"(^|/)google[0-9a-f]+\.html$", flags=re.IGNORECASE)


def html_files():
    return [
        f
        for f in glob.glob("**/*.html", recursive=True)
        if not f.startswith(".git") and not EXCLUDE_RE.search(f)
    ]


def process(check_only):
    missing = []
    changed = []
    for f in html_files():
        with open(f, encoding="utf-8") as fh:
            content = fh.read()

        if GA4_ID in content:
            continue

        missing.append(f)
        if check_only:
            continue

        # Insert the snippet on its own line right after the opening <head> tag.
        m = re.search(r"<head\b[^>]*>", content, flags=re.IGNORECASE)
        if not m:
            print(f"WARNING: no <head> tag found in {f}, skipping", file=sys.stderr)
            continue
        pos = m.end()
        content = content[:pos] + "\n" + SNIPPET + content[pos:]
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(content)
        changed.append(f)

    return missing, changed


def main():
    check_only = "--check" in sys.argv[1:]
    missing, changed = process(check_only)

    if check_only:
        if missing:
            print("Pages missing the GA4 snippet:")
            for f in missing:
                print(f"  - {f}")
            print(
                "\nRun `python3 scripts/inject-ga4.py` to fix, "
                "or let the ga4-tracking workflow do it on push."
            )
            return 1
        print("All HTML pages have the GA4 snippet.")
        return 0

    if changed:
        print(f"Injected GA4 snippet into {len(changed)} page(s):")
        for f in changed:
            print(f"  - {f}")
    else:
        print("No changes needed; all HTML pages already have the GA4 snippet.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
