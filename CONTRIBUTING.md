# Contributing

Thanks for improving this list! Please read the scope rules and format below before opening a PR.

## Scope Rules (what gets accepted)

The list is about **environments as first-class, evolving citizens of LLM agents**. Acceptance criteria:

1. **In**: environment synthesis, environment evolution mechanisms, environment quality/verification/reward, agentic data generation paradigms, domain training environments, agent-specific infrastructure (sandboxes, platforms, protocols, EaaS).
2. **Embodied / game world models**: only if used for **LLM/VLA agent training or evaluation**. Pure video generation and game reconstruction papers are out.
3. **Benchmarks**: training-oriented environments are always in. Evaluation benchmarks must be **strongly environmental** — interactive, stateful, executable. Static QA-style benchmarks are out.
4. **Infrastructure**: only agent-specific tooling (e.g., agent sandboxes, environment platforms). General cloud-native projects (Docker/K8s ecosystem) belong in cloud-native lists.
5. **Recency preference**: 2024+ by default; pre-2024 only for foundational works (UED classics, ALFWorld, etc.).

If your entry doesn't fit an existing subsection, open an issue first — we can add subsections, but the ten-section spine (formalization → synthesis → evolution → quality → data → domains → infrastructure → training → open problems) is stable.

## Entry Format

```markdown
- **Name** · venue/year — one-line description of what it does and why it matters.
  `E-source: real|llm-synth|programmatic` `produces: E,q,τ,v` [arXiv:XXXX.XXXXX](https://arxiv.org/abs/XXXX.XXXXX) · [Code](https://github.com/...)
```

Rules:

- One line per entry; keep descriptions factual and mechanism-focused (what it does), not marketing (what it claims).
- Prefer linking **arXiv abs pages**; use OpenReview/ACL Anthology when that's the canonical source.
- **Code links must be verified** — do not add a code link unless you have confirmed the repo exists and matches the paper. Unverified links are worse than no links.
- Tag entries with ACE `E-source` (environment construction source) and `produces` (which data factors it outputs) when it aids classification; optional for domain benchmarks.
- Venue tags use the major-venue abbreviation + year (e.g., `ICML 2026`). Preprints: just the year.

## Where to place an entry

Quick decision guide:

- Does the paper **build** new environments? → §3 (route decides the subsection: task-driven wraps real assets · real-world-driven projects real media · de novo synthesizes from scratch · §3.4 reuses static worlds).
- Does the environment **change during training** (curriculum, self-play, scaling, co-evolution)? → §4.
- Is it about **measuring or ensuring environment quality** (correctness/difficulty/diversity/fidelity/rewards)? → §5.
- Is it a **data-generation pipeline** whose primary product is training data (SFT trajectories, tasks)? → §6.
- Is it a **ready-to-use environment/benchmark** in a domain? → §7.
- Is it **infrastructure** (sandbox, protocol, platform, serving)? → §8.
- Is it a **training algorithm** tightly coupled to environments? → §9.

Cross-cutting papers may appear in two sections; the canonical (most detailed) entry should live in the closest section, others can cross-reference it ("see §3.1").

## Process

1. Fork → branch → edit `README.md` (and `README.zh-CN.md` if the section's representative table changes).
2. Add your entry in the correct subsection, following the format above.
3. PR with a one-line rationale. New-subsection PRs should explain why existing ones don't fit.

## Notes

- arXiv links in the initial import were extracted from three surveys' reference lists; a few pre-2024 and venue-only entries intentionally lack links. Corrections are very welcome.
