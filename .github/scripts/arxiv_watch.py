#!/usr/bin/env python3
"""Weekly arXiv triage for awesome-agentic-environment-evolving.

Fetches recent arXiv postings matching curated phrases, drops papers already
listed in README.md or docs/arxiv-watch.md, and appends the rest to the watch
file for human triage. Run by .github/workflows/arxiv-watch.yml (also works
locally: `python .github/scripts/arxiv_watch.py`).

No third-party dependencies: stdlib urllib + ElementTree only.
"""

import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
WATCH = ROOT / "docs" / "arxiv-watch.md"

# Phrases are matched against all metadata fields (title+abstract). Keep the
# list tight: this is a triage queue, not a final list -- noise costs review
# time. Prefer phrases that reliably appear in titles/abstracts of this field.
PHRASES = [
    "agent environment",
    "environment scaling",
    "synthetic environments",
    "verifiable environments",
    "environment synthesis",
    "agentic environment",
    "self-evolving environment",
    "environment curriculum",
    "world model agent training",
    "training environments for LLM",
]

DAYS = 30          # look back window (weekly cron + buffer)
MAX_RESULTS = 40   # per phrase
ATOM = "{http://www.w3.org/2005/Atom}"


def known_ids() -> set[str]:
    ids: set[str] = set()
    for path in (README, WATCH):
        if path.exists():
            text = path.read_text(encoding="utf-8")
            ids.update(re.findall(r"arXiv:(\d{4}\.\d{4,5})", text))
            ids.update(re.findall(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", text))
    return ids


def fetch(phrase: str) -> ET.Element:
    query = urllib.parse.quote(f'"{phrase}"')
    url = (
        "http://export.arxiv.org/api/query"
        f"?search_query=all:{query}"
        "&sortBy=submittedDate&sortOrder=descending"
        f"&max_results={MAX_RESULTS}"
    )
    with urllib.request.urlopen(url, timeout=60) as resp:
        return ET.fromstring(resp.read())


def main() -> None:
    cutoff = datetime.now(timezone.utc) - timedelta(days=DAYS)
    seen: set[str] = set()
    candidates: list[tuple[datetime.date, str, str]] = []

    for phrase in PHRASES:
        try:
            root = fetch(phrase)
        except Exception as exc:  # network hiccups shouldn't kill the run
            print(f"warn: query failed for {phrase!r}: {exc}", file=sys.stderr)
            continue
        for entry in root.findall(f"{ATOM}entry"):
            entry_id = entry.findtext(f"{ATOM}id") or ""
            match = re.search(r"abs/(\d{4}\.\d{4,5})", entry_id)
            if not match:
                continue
            paper_id = match.group(1)
            if paper_id in seen:
                continue
            seen.add(paper_id)
            published_raw = entry.findtext(f"{ATOM}published") or ""
            try:
                published = datetime.fromisoformat(published_raw.replace("Z", "+00:00"))
            except ValueError:
                continue
            if published < cutoff:
                continue
            title = " ".join((entry.findtext(f"{ATOM}title") or "").split())
            candidates.append((published.date(), paper_id, title))

    fresh = [c for c in candidates if c[1] not in known_ids()]
    if not fresh:
        print("no new candidates")
        return

    fresh.sort(reverse=True)
    today = datetime.now(timezone.utc).date()
    block = [f"\n## {today} (auto)\n"]
    for pub_date, paper_id, title in fresh:
        block.append(f"- [{pub_date}] [{title}](https://arxiv.org/abs/{paper_id}) `arXiv:{paper_id}`")

    WATCH.parent.mkdir(parents=True, exist_ok=True)
    if not WATCH.exists():
        WATCH.write_text(
            "# arXiv Watch (auto-generated triage queue)\n\n"
            "Candidates surfaced weekly by `.github/workflows/arxiv-watch.yml`.\n"
            "Triage into the README sections (add a one-liner + tags per CONTRIBUTING),\n"
            "then delete the line here. Out-of-scope lines are deleted without action.\n",
            encoding="utf-8",
        )
    with WATCH.open("a", encoding="utf-8") as fh:
        fh.write("\n".join(block) + "\n")
    print(f"added {len(fresh)} candidates to {WATCH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
