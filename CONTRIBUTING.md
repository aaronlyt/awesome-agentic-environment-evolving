# Contributing

Thanks for improving this list! Please read the scope rules and format below before opening a PR.

## Scope Rules (what gets accepted)

The list is about **environments as first-class citizens in LLM-agent research**. Acceptance criteria:

1. **In**: environment synthesis, environment evolution mechanisms, environment quality/verification/reward, agentic data generation paradigms, domain training environments, agent-specific infrastructure (sandboxes, platforms, protocols, EaaS).
2. **Embodied / game world models**: only if used for **LLM/VLA agent training or evaluation**. Pure video generation and game reconstruction papers are out.
3. **Benchmarks**: training-oriented environments are always in. Evaluation benchmarks must be **strongly environmental** — interactive, stateful, executable. Static QA-style benchmarks are out.
4. **Infrastructure**: only agent-specific tooling (e.g., agent sandboxes, environment platforms). General cloud-native projects (Docker/K8s ecosystem) belong in cloud-native lists.
5. **Recency preference**: 2024+ by default; pre-2024 only for foundational works (UED classics, ALFWorld, etc.).

If your entry doesn't fit an existing subsection, open an issue first — we can add subsections, but the ten-section spine (formalization → synthesis → evolution → quality → data → domains → infrastructure → training → open problems) is stable.

## Entry Format

Add one **table row** in the correct subsection:

```markdown
| **Name** | Venue Year | One-line summary of the mechanism (condense the source survey's description when available). | `src:AEE-5.1.1` `route:de-novo` `E:programmatic` `produces:E,q` | [XXXX.XXXXX](https://arxiv.org/abs/XXXX.XXXXX) |
```

The tag vocabulary is defined in the README legend (`src:` survey provenance, `E:` construction source, `route:` synthesis route, `evolution:` mechanism, `paradigm:` data-generation paradigm, `produces:` output factors, `quality:` quality dimension, `verify:` verification type). Use the subset that applies. Rules:

- Keep the one-liner factual and mechanism-focused (what it does), not marketing (what it claims). When the work appears in a source survey (AEE / ES / ACE), prefer condensing the survey's own description and record it via `src:`.
- Prefer linking **arXiv abs pages**; use OpenReview/ACL Anthology when that's the canonical source. Leave the arXiv cell as `—` rather than guessing an ID.
- **Code links must be verified** — do not add a code link unless you have confirmed the repo exists and matches the paper. Unverified links are worse than no links.
- Venue cells use the major-venue abbreviation + year (e.g., `ICML 2026`). Preprints: just the year.
- Escape `|` inside cells — use `·` or `/` instead.

## Where to place an entry

Quick decision guide:

- Does the paper **build** new environments or generate agentic data? → §3, organized by **anchor**: E-anchored construction (route decides the group: task-driven wraps real assets · real-world-driven projects real media · de novo from scratch · simulator/environment-free, §3.1; neural §3.2; compositional §3.3; static-world reuse §3.4), reverse-anchored (task-/trajectory-/structure-first, §3.5), or adaptive generation (§3.6).
- Does the environment **change during training** (curriculum, self-play, scaling, co-evolution)? → §4.
- Is it about **measuring or ensuring environment/data quality** (correctness/difficulty/diversity/fidelity/rewards — the ACE objective)? → §5.
- Is it a **ready-to-use environment/benchmark** in a domain? → §6.
- Is it **infrastructure** (sandbox, protocol, platform, serving)? → §7.
- Is it a **training algorithm** tightly coupled to environments? → §8.
- Is it **empirical scaling evidence or an open research question**? → §9.

Cross-cutting papers may appear in two sections; the canonical (most detailed) entry should live in the closest section, others can cross-reference it ("see §3.1").

## Process

1. Fork → branch → edit `README.md` (and `README.zh-CN.md` if the section's representative table changes).
2. Add your entry in the correct subsection, following the format above.
3. PR with a one-line rationale. New-subsection PRs should explain why existing ones don't fit.

## Notes

- arXiv links in the initial import were extracted from three surveys' reference lists; a few pre-2024 and venue-only entries intentionally lack links. Corrections are very welcome.
