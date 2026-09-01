# Awesome Agentic Environment Evolving

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Environments as first-class citizens in LLM-agent research** — a curated list of research on how agent environments are **synthesized**, how they **evolve** with the agent, how their **quality is verified**, and how they are consumed as **data and services**.

> [中文导读（精简版）](README.zh-CN.md)

The field is converging on a paradigm shift: environments are no longer passive evaluation containers but the **producers of experiential data**. As argued in [*Agentic Environment Engineering*](https://arxiv.org/abs/2606.12191) (§2.2, "From Data Engineering to Environment Engineering") and [*Environment Scaling*](https://arxiv.org/abs/2511.09586), static datasets force the model to be a passive recipient of fixed-difficulty trajectories, while environments close the loop: every action changes state, and the task distribution can co-evolve with the learner. This list maps that emerging discipline — with **environment evolution mechanisms** as its spine, a dimension no existing list covers as its primary axis.

## Scope

**Include**
- Environment synthesis (programmatic, neural/world-model, compositional) — for agent training and evaluation.
- Environment evolution: difficulty-driven curricula, self-play & world-model co-evolution, scaling-driven expansion, agent–environment co-evolution, generator–verifier co-evolution.
- Environment quality: correctness, complexity calibration, diversity measurement, fidelity, reward & verifier design.
- Agentic data generation paradigms (forward/reverse) and the ACE quality lens.
- Domain training environments & strongly *environmental* benchmarks (interactive, stateful, executable).
- Agent-specific infrastructure: sandboxes, environment platforms/protocols, Environment-as-a-Service.

**Exclude**
- Pure video generation / game reconstruction world models not used for LLM/VLA agent training.
- Static QA-style benchmarks (no interaction, no state, no execution).
- General-purpose cloud-native infrastructure (Docker/K8s ecosystem) — see cloud-native lists instead.

## Contents

- [1. Surveys & Position Papers](#1-surveys--position-papers)
- [2. Formalization & Environment Attributes](#2-formalization--environment-attributes)
- [3. Environment & Data Synthesis](#3-environment--data-synthesis)
- [4. Environment Evolution Mechanisms](#4-environment-evolution-mechanisms-) ★
- [5. Quality, Verification & Reward](#5-quality-verification--reward)
- [6. Domain Environments & Benchmarks](#6-domain-environments--benchmarks)
- [7. Infrastructure & Environment-as-a-Service](#7-infrastructure--environment-as-a-service)
- [8. Training with Evolving Environments](#8-training-with-evolving-environments)
- [9. Scaling Evidence & Open Problems](#9-scaling-evidence--open-problems)

*Each category lists papers in a table. The **One-liner** column condenses what the source surveys say about the work; the **Tags** column records survey provenance and taxonomy labels (all keys optional). `src:` refs follow the surveys' own placement; taxonomy labels on rows the surveys do not classify are editorial assignments:*

- `src:` the source survey that lists the work — **AEE** = *Agentic Environment Engineering* ([2606.12191](https://arxiv.org/abs/2606.12191)) · **ES** = *Environment Scaling* ([2511.09586](https://arxiv.org/abs/2511.09586)) · **ACE** = *What Makes Good Agentic Data* ([2608.27260](https://arxiv.org/abs/2608.27260)), optionally with a table/section ref (e.g. `ACE-T1`). Works without `src:` were added by local curation (arXiv watch queue).
- `E:` environment construction source (ACE §3.2): `real` · `llm-synth` (LLM-generated symbolic specs) · `programmatic` (executable implementation) · `neural` (the transition function itself is a network, AEE §5.2)
- `route:` synthesis route (AEE §5.1): `task` (wrap real assets) · `real-world` (project real media) · `de-novo` (from scratch)
- `evolution:` evolution mechanism — `difficulty` · `neural` · `scaling` (AEE §7) · `co-evolve` (AEE §8.6) · `verifier` (ES survey's generator–verifier asymmetry)
- `paradigm:` data-generation paradigm (ACE §3): `forward` · `task-first` · `trajectory-first` · `structure-first` · `adaptive`
- `produces:` data factors output (ACE §2.4): subset of `E,q,τ,v`
- `quality:` quality dimension (AEE §5.3 + ACE lens): `correctness` · `complexity` · `diversity` · `fidelity` · `reward`

*Code links are being verified and added progressively — see [CONTRIBUTING](CONTRIBUTING.md).*

---

## 1. Surveys & Position Papers

### 1.1 Surveys

| Survey | Venue | One-liner | Link |
|---|---|---|---|
| **Agentic Environment Engineering for LLMs** | 2026 | The AEE survey this list's skeleton follows: 8 attribute pairs × 8 domains × 2 synthesis paradigms × 4 quality dimensions × agent & environment evolution (582 refs). | [arXiv:2606.12191](https://arxiv.org/abs/2606.12191) |
| **Environment Scaling for Interactive Agentic Experience Collection** | NeurIPS'25 SEA Workshop | Environments as producers of experiential data; the Generation–Execution–Feedback (GEF) loop; generator–verifier asymmetry. | [arXiv:2511.09586](https://arxiv.org/abs/2511.09586) · [companion list](https://github.com/lukahhcm/Awesome_Scaling_Environments) |
| **What Makes Good Agentic Data? An ACE Lens** | 2026 | Quality lens — Accuracy (admission condition) – Complexity (learner-relative calibration) – divErsity (behavioral coverage); data object d = (E, q, τ, v); forward vs. reverse generation. | [arXiv:2608.27260](https://arxiv.org/abs/2608.27260) |
| **A Survey of Self-Evolving Agents** | 2025 | Agent-centric view of self-evolution; the environment appears as one component (contrast with this list's environment-centric axis). | [list](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) |

### 1.2 Position Papers

| Paper | Venue | One-liner | Link |
|---|---|---|---|
| **Welcome to the Era of Experience** | Silver & Sutton, 2025 | The programmatic statement: agents must learn from their own interaction data, not static human corpora. | — |
| **AgentScaler** | ICLR 2026 | The manifesto-paper of environment scaling: 30k heterogeneous APIs turned into diverse environments by treating function calls as database reads/writes. | [arXiv:2509.13311](https://arxiv.org/abs/2509.13311) |
| **Scalable Environments Drive Generalizable Agents** | 2026 | Distinguishes trajectory scaling / task scaling / environment scaling; generalization requires scaling the distribution of executable rule sets. | [arXiv:2605.18181](https://arxiv.org/abs/2605.18181) |

## 2. Formalization & Environment Attributes

Two complementary cuts, plus the shared interaction formalism.

- **POMDP formalism** — both the AEE survey (§2.1, E = ⟨S, A, P, R, Ω, O, γ⟩ extended for tool-augmented, language-centered agents) and ACE (§2.1, interaction as partial observability) ground "agentic environment" in a POMDP.
- **Intra-environment decomposition (ACE §2.2)** — e = (D optional state carrier, F tool/action set, P_rule policies & constraints, Ω observation exposure, v optional success interface); E ranges from a *static interface specification* (tool schemas) to a *complete executable interaction substrate*. [arXiv:2608.27260](https://arxiv.org/abs/2608.27260)
- **Inter-environment attribute pairs (AEE survey §3)** — symbolic vs. neural · open- vs. closed-loop · online vs. offline · MDP vs. POMDP · deterministic vs. nondeterministic · discrete vs. continuous · uni- vs. multi-modal · single- vs. multi-agent. [arXiv:2606.12191](https://arxiv.org/abs/2606.12191)
- Terminology note: an **"LLM-synthesized environment"** (ACE) means LLMs generate *symbolic* tool specs/rules; a **"neural environment"** (AEE survey §3.1/§5.2) means the *transition function itself* is a network (world model). Different things — don't conflate.

## 3. Environment & Data Synthesis

Environment construction and agentic data generation are two views of one activity. In ACE's factorization, data is the object d = (E, q, τ, v) and generation means designing a joint distribution over its factors — so this chapter merges both views and organizes pipelines by **anchor** (ACE §3: which factor drives construction):

- **E-anchored (forward, E → q → τ)** — build the environment first; §3.1-3.4. Orthogonal tags: AEE's synthesis `route:` (what real material seeds the pipeline) × ACE's `E:` source (how the resulting artifact is implemented).
- **Reverse-anchored** — task, trajectory, or an intermediate structure drives construction; §3.5.
- **Adaptive** — the generation strategy itself is revised from accumulated experience; §3.6.

*The quality objective for which generated instances get accepted (ACE: Accuracy–Complexity–divErsity) is a separate question — see §5.*

### 3.1 E-Anchored Construction (Forward, E → q → τ)

**Task-driven** — wrap static real assets (repos, issues, real APIs, tasks) into environments (AEE §5.1.1).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **SWE-Gym** | ICML 2025 | 11 Python repos packaged as Docker environments with hybrid validators; trains both SWE agents and verifiers. | `src:AEE-5.1.1` `E:real` `route:task` `produces:E,τ,v` | [2412.21139](https://arxiv.org/abs/2412.21139) |
| **R2E-Gym** | COLM 2025 | Procedural SWE environments + hybrid test/LLM verification; 8,135 tasks. | `src:AEE-5.1.1,ES` `E:real` `route:task` `produces:E,q,v` | [2504.07164](https://arxiv.org/abs/2504.07164) |
| **SWE-smith** | NeurIPS 2025 | 50k synthesized SWE tasks from a single shared image via transient bug injection. | `src:AEE-5.1.1,ES` `E:real` `route:task` `produces:q` | [2504.21798](https://arxiv.org/abs/2504.21798) |
| **Scale-SWE** | 2026 | Environment Builder / Unittest Creator / Problem Writer agents immersed in the GitHub universe. | `src:AEE-5.1.1` `E:real` `route:task` | [2602.09892](https://arxiv.org/abs/2602.09892) |
| **SWE-Hub** | 2026 | System-level real-bug environments via Env Agent + Bug Agent. | `src:AEE-5.1.1` `E:real` `route:task` | [2603.00575](https://arxiv.org/abs/2603.00575) |
| **MEnvAgent** | 2026 | Incremental patching to *reuse* environments across tasks instead of rebuilding. | `src:AEE-5.1.1` `route:task` | [2601.22859](https://arxiv.org/abs/2601.22859) |
| **DockSmith** | 2026 | A *trained* model generates and repairs Dockerfiles for environment images. | `src:AEE-5.1.1` `route:task` | [2602.00592](https://arxiv.org/abs/2602.00592) |
| **SCALER** | 2026 | Competitive-programming data → verifiable environments with tunable difficulty for RL. | `src:AEE-5.1.1,7.2` `route:task` `evolution:difficulty` | [2601.04809](https://arxiv.org/abs/2601.04809) |
| **AgentFounder (Agentic CPT)** | 2025 | Wikipedia/CommonCrawl turned into interactive environments for continued pre-training. | `src:AEE-5.1.1` `route:task` | [2509.13310](https://arxiv.org/abs/2509.13310) |
| **daVinci-Env (OpenSWE)** | 2026 | 45,320 transparent Docker environments from 12.8k repos; the largest open SWE environment stack. | `E:real` `route:task` `produces:E,v` | [2603.13023](https://arxiv.org/abs/2603.13023) |
| **SWE-Universe** | 2026 | Million-scale real verifiable environments. | `src:AEE-5.1.2` `E:real` `route:real-world` | [2602.02361](https://arxiv.org/abs/2602.02361) |
| **ToolLLM** | ICLR 2024 | 16k+ real APIs; the founding large-scale tool dataset (tool-description prompting; teacher-guided rollouts). | `src:ACE-T1,T3` `E:real` `route:task` `paradigm:forward` `produces:q,τ` | — |
| **Gorilla** | NeurIPS 2024 | API-grounded instruction generation at scale. | `src:ACE-T1` `E:real` `route:task` `paradigm:forward` | — |
| **APIGen** | NeurIPS 2024 | Format check → execution → semantic review; the canonical three-layer verification pipeline. | `src:ACE-T1` `E:real` `route:task` `paradigm:forward` `verify:judge` | — |
| **ToolDial** | ICLR 2025 | Real API-graph-guided multi-turn dialogues. | `src:ACE-T1` `E:real` `route:task` `paradigm:forward` | — |
| **Close the Loop (InfTool)** | 2025 | Multi-agent role-play toward "infinite" tool-use data. | `src:ACE-T1` `E:real` `route:task` `paradigm:forward` | — |
| **TOUCAN** | 2025 | 1.5M tool-agent samples synthesized from real MCP environments. | `src:ACE-T1` `E:real` `route:task` `paradigm:forward` | — |

**Real-world-driven** — project real interaction media (web, OS, games, EHR) into simplified virtual environments (AEE §5.1.2).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **AgentSynth** | 2025 | Exploits information asymmetry: generating easy sub-tasks stepwise ≪ solving one hard long-horizon task; difficulty-controllable. | `src:AEE-5.1.2` `route:real-world` | [2506.14205](https://arxiv.org/abs/2506.14205) |
| **TaskCraft** | 2025 | Web-grounded, difficulty-tunable tool-call task synthesis (compositional scaling). | `src:AEE-5.1.2,ACE,ES` `route:real-world` `produces:q` | [2506.10055](https://arxiv.org/abs/2506.10055) |
| **VeriEnv** | 2026 | LMs as *environment creators*: clone real websites into executable, programmatically verifiable environments. | `src:AEE-5.1.2` `route:real-world` `produces:E,v` | [2603.10505](https://arxiv.org/abs/2603.10505) |
| **Training Needs Trustworthy Worlds** | 2026 | Verified synthetic web environments for agent learning. | `src:arxiv-watch` `route:real-world` | [2608.21898](https://arxiv.org/abs/2608.21898) |
| **AutoWebWorld** | 2026 | Websites as finite-state machines; systematic enumeration and verification ("infinite verifiable web environments"). | `src:AEE-5.1.2,7.3.1` `route:real-world` | [2602.14296](https://arxiv.org/abs/2602.14296) |
| **InfiniteWeb** | 2026 | Lightweight specs auto-expanded into functional websites + tasks + reward evaluators. | `src:AEE-5.1.3,7.3.1` `route:de-novo` `produces:E,q,v` | [2601.04126](https://arxiv.org/abs/2601.04126) |
| **V-GameGym** | 2025 | Visual-rendering feedback environments built on games. | `src:AEE-5.1.1` `route:task` | [2509.20136](https://arxiv.org/abs/2509.20136) |
| **MedMCP-Calc** | 2026 | MCP environments over real EHR stores + clinical guideline retrieval. | `src:AEE-5.1.2` `route:real-world` | [2601.23049](https://arxiv.org/abs/2601.23049) |

**De Novo** — synthesize from scratch with minimal seeds; the closest to "environment scaling as free expansion" (AEE §5.1.3). Covers both LLM-synthesized *symbolic* specs (`E:llm-synth`) and programmatic implementations (`E:programmatic`).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **AutoForge** | 2025 | Builds scalable state structures and a tool-call logic DAG before code generation; RL-stabilized. | `src:AEE-5.1.3,7.3.1,ACE-T1` `E:programmatic` `route:de-novo` `produces:E,q` | [2512.22857](https://arxiv.org/abs/2512.22857) |
| **Agent World Model** | ICML 2026 | "Infinity Synthetic Environments": code-driven, DB-backed fully synthetic pipeline reaching 1,000+ environments with execution-level self-correction. | `src:AEE-5.1.3,7.3.1,ACE-T1` `E:programmatic` `route:de-novo` | [2602.10090](https://arxiv.org/abs/2602.10090) |
| **ScaleEnv** | 2026 | From-scratch interactive environments + verifiable tasks; clean evidence that *domain count → generalization*. | `src:AEE-5.1.3,ACE-T1` `E:programmatic` `route:de-novo` | [2602.06820](https://arxiv.org/abs/2602.06820) |
| **EnvFactory** | 2026 | Automatic exploration/validation of stateful executable tool environments; a *few strongly verified environments can be more useful than a larger but unreliable set*. | `src:ACE-T1` `E:programmatic` `route:de-novo` | [2605.18703](https://arxiv.org/abs/2605.18703) |
| **EnvScaler** | ACL Findings 2026 | SkelBuilder (environment skeletons) + ScenGenerator (scenario instantiation + rule validators); 191 environments / ~7k scenarios. | `src:AEE-5.1.1,7.3.1,ACE-T1` `E:programmatic` `route:task` | [2601.05808](https://arxiv.org/abs/2601.05808) |
| **Agent-World** | 2026 | Self-evolving training arena: autonomous MCP/tool environment discovery + difficulty-controlled task synthesis. | `src:ACE-T1` `E:programmatic` `route:de-novo` `evolution:co-evolve` | [2604.18292](https://arxiv.org/abs/2604.18292) |
| **AutoEnv** | 2025 | Environments as factorizable distributions of transitions/observations/rewards; unified heterogeneous generation. | `src:AEE-5.1.3,7.3.2,ES` `E:programmatic` `route:de-novo` | [2511.19304](https://arxiv.org/abs/2511.19304) |
| **LOGIGEN** | 2026 | Logic-driven forward deduction; rules compiled into SQLite-backed physical environments. | `src:AEE-5.1.3,ACE` `E:programmatic` `route:de-novo` | [2603.00540](https://arxiv.org/abs/2603.00540) |
| **SWE-Playground** | 2025 | First fully synthetic SWE training pipeline, fully off GitHub. | `src:AEE-5.1.3` `E:programmatic` `route:de-novo` | [2512.12216](https://arxiv.org/abs/2512.12216) |
| **Endless Terminals** | 2026 | Samples file-operation/network-config dimensions into thousands of terminal environments. | `src:AEE-5.1.3` `E:programmatic` `route:de-novo` | [2601.16443](https://arxiv.org/abs/2601.16443) |
| **gg-bench** | 2025 | Randomly samples *brand-new* two-player games; contamination-proof by construction. | `src:AEE-5.1.3` `E:programmatic` `route:de-novo` | [2505.07215](https://arxiv.org/abs/2505.07215) |
| **RandomWorld** | EMNLP 2025 | Procedural environment generation for tool agents. | `src:ES` `E:programmatic` `route:de-novo` | [2506.11045](https://arxiv.org/abs/2506.11045) |
| **NL2Plan** | 2024 | Natural-language PDDL environment generation. | `src:AEE-5.1.3` `E:programmatic` `route:de-novo` | [2405.04215](https://arxiv.org/abs/2405.04215) |
| **Envs-FORGE** | 2026 | Frontier-optimized, reward-grounded environment synthesis for agent RL. | `src:arxiv-watch` `E:programmatic` `route:de-novo` `evolution:difficulty` | [2608.14312](https://arxiv.org/abs/2608.14312) |
| **AgentMercury** | 2026 | Agents synthesize verifiable business-scenario environments at scale. | `src:arxiv-watch` `E:programmatic` `route:de-novo` | [2608.20634](https://arxiv.org/abs/2608.20634) |
| **ToolACE** | ICLR 2025 | Self-evolving API pool + decision-tree retrieval. | `src:ACE-T1` `E:llm-synth` `route:de-novo` `paradigm:forward` | — |
| **ToolAlpaca** | 2023 | 3k simulated tool cases; the early demonstration. | `src:ACE-T1` `E:llm-synth` `route:de-novo` `paradigm:forward` | — |
| **Seal-Tools** | NLPCC 2024 | Self-instruct tool dataset. | `src:ACE-T1` `E:llm-synth` `route:de-novo` `paradigm:forward` | — |
| **SynthTools** | 2025 | Hierarchical, verifiable synthesis for scaling agent development. | `src:ACE-T1` `E:llm-synth` `route:de-novo` `paradigm:forward` | — |
| **ToolWeave** | 2026 | Synthetic tool graphs → complex multi-turn dialogues. | `src:ACE-T1` `E:llm-synth` `route:de-novo` `paradigm:forward` | — |
| **CodeGym** | ICLR 2026 | Synthetic code environments for end-to-end tool-use RL. | `src:ACE` `E:programmatic` `route:de-novo` `paradigm:forward` | [2509.17325](https://arxiv.org/abs/2509.17325) |
| **ToolVerse** | 2026 | Many environments + long-horizon tasks unlocking agentic RL. | `src:ACE` `E:programmatic` `route:de-novo` `paradigm:forward` | — |
| **SciDisco** | 2026 | Scientific-discovery environments scaled for turn-level RL. | `src:ACE-T3` `E:programmatic` `route:de-novo` `paradigm:forward` | — |
| **ASTRA** | 2026 | Auto-synthesized trajectory and RL arenas. | `src:ACE` `E:programmatic` `route:de-novo` `paradigm:forward` | — |

**Simulator / environment-free variants** — no persistent E is built; an LLM simulates environment responses (ACE).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **Simulating Environments with Reasoning Models** | 2025 | LLM simulators produce stateful responses from API specs. | `src:ACE` `E:llm-synth` `paradigm:forward` | — |
| **Environment-free Synthetic Data Generation for API Agents** | 2026 | Skip the environment entirely; generate interactions directly. | `src:ACE` `paradigm:forward` | — |
| **EnvACE** | 2026 | Internalizes environment dynamics via world-model rehearsal. | `src:ACE` `paradigm:forward` | — |

### 3.2 Neural Synthesis (World-Model-as-Environment)

The transition function P is parameterized by a network. Three abstraction levels (AEE §5.2).

**Pixel-level** — high fidelity, high redundancy.

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **DreamGen** | 2025 | Video world model (WAN2.1) generating synthetic robot trajectories from ~1000 videos. | `src:AEE-5.2.1` `E:neural` `produces:τ` | [2505.12705](https://arxiv.org/abs/2505.12705) |
| **GameNGen** | 2024 | A diffusion model as a real-time game engine (DOOM). | `src:AEE-5.2.1` `E:neural` | [2408.14837](https://arxiv.org/abs/2408.14837) |
| **Matrix-Game** | 2025 | Large-scale Minecraft data; key-mouse continuous input; sequel Matrix-Game 2.0 reaches minute-level stable interaction. | `src:AEE-5.2.1` `E:neural` | [2506.18701](https://arxiv.org/abs/2506.18701) |
| **NeuralOS** | 2025 | Hierarchical RNN maintains persistent OS state + diffusion rendering. | `src:AEE-5.2.1` `E:neural` | [2507.08800](https://arxiv.org/abs/2507.08800) |
| **DreamZero** | 2026 | "World Action Models are Zero-shot Policies." | `src:AEE-5.2.1` `E:neural` | [2602.15922](https://arxiv.org/abs/2602.15922) |
| **Pandora** | 2024 | World model with rule-controllable generation. | `src:AEE-5.2.1` `E:neural` | [2406.09455](https://arxiv.org/abs/2406.09455) |
| **Genie 3** | DeepMind 2025 | Real-time, long-horizon-consistent interactive world model (technical report). | `src:ES` `E:neural` | — |

**Token-level** — environments represented in language; cheap, abstract, planning-friendly (AEE §5.2.2).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **WebWorld** | 2026 | First large-scale open web world model, trained on 1M+ real open-web interactions; safe offline trajectory synthesis (+9.2 WebArena for Qwen3-14B). | `src:AEE-5.2.2` `E:neural` `produces:τ` | [2602.14721](https://arxiv.org/abs/2602.14721) |
| **WebDreamer** | TMLR 2025 | A strong LLM prompted *as* the web world model for model-predictive planning. | `src:AEE-5.2.2` `E:neural` | — |
| **Code2World** | 2026 | GUI states as renderable code; rendering-perception RL alignment. | `src:AEE-5.2.2,7.1` `E:neural` | [2602.09856](https://arxiv.org/abs/2602.09856) |
| **MobileDreamer** | 2026 | Structured text representation of GUI elements + rollout-imagination trees. | `src:AEE-5.2.2` `E:neural` | [2601.04035](https://arxiv.org/abs/2601.04035) |
| **UI-Simulator** | 2025 | LLM generates future UI states and guides rollouts for data synthesis. | `src:AEE-7.1.2` `E:neural` `evolution:neural` `produces:τ` | [2510.14969](https://arxiv.org/abs/2510.14969) |
| **gWorld** | 2026 | LLM-as-simulator for GUI environments. | `src:AEE-5.2.2` `E:neural` | [2602.01576](https://arxiv.org/abs/2602.01576) |
| **SWE-World** | 2026 | LLM-as-simulator for SWE environments. | `src:AEE-5.2.2` `E:neural` | [2602.03419](https://arxiv.org/abs/2602.03419) |
| **Simia** | 2025 | Reasoning models simulate environments to train agents (same work as *Simulating Environments with Reasoning Models*, §3.1). | `src:AEE-5.2.2` `E:neural` `produces:q,τ` | [2511.01824](https://arxiv.org/abs/2511.01824) |

**Latent-level** — compact learned representations (AEE §5.2.3).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **V-JEPA 2** | 2025 | 1M hours of video pre-training + 62h robot data → zero-shot robot planning. | `src:AEE-5.2.3` `E:neural` | [2506.09985](https://arxiv.org/abs/2506.09985) |
| **DINO-WM** | 2024 | World model on frozen DINOv2 features; zero-shot planning. | `src:AEE-5.2.3` `E:neural` | [2411.04983](https://arxiv.org/abs/2411.04983) |
| **IWM** | 2024 | "In-context" world models. | `src:AEE-5.2.3` `E:neural` | [2403.00504](https://arxiv.org/abs/2403.00504) |
| **AdaWorld** | ICML 2025 | Latent-action-conditioned, adaptable world models. | `src:AEE-5.2.1` `E:neural` | — |

### 3.3 Compositional Construction

Compose verifiable environments recursively rather than linearly expanding (task-level composition lives in §3.5 task-first).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **RACES** | 2026 | "Verifiable Environments Are LEGO Bricks": recursive composition (type matching + SEQUENTIAL/PARALLEL/SORT/SELECT operators); 50 composed environments ≈ 300 standalone ones. | `E:programmatic` `produces:E,v` | [2606.12373](https://arxiv.org/abs/2606.12373) |

### 3.4 Harnessing Static Environments (Reuse over Rebuild)

Re-activate existing static worlds instead of synthesizing new ones.

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **EnvHarness** | 2026 | Programmable plugin layer wraps static environments (preserving original validators) to reshape behavior; EnvRigger diagnoses policy defects from trajectories; up to +9.0 held-out. | `src:—` `produces:E,v` | [2608.19880](https://arxiv.org/abs/2608.19880) |
| **Environment Tuning** | 2025 | "Don't just fine-tune the agent, tune the environment": manual curricula + environment augmentation + progress feedback. | `src:AEE-7.2` `evolution:difficulty` | [2510.10197](https://arxiv.org/abs/2510.10197) |
| **CLI-Gym** | 2026 | "Environment reversal": deliberately corrupts environments to generate error-recovery training data. | `src:AEE-5.1.1` `route:task` `produces:τ` | [2602.10999](https://arxiv.org/abs/2602.10999) |

### 3.5 Reverse-Anchored Generation

Pipelines where the environment is *not* the anchor (ACE §3.3): a task, a trajectory, or an intermediate structure drives construction, and E is built or recovered afterwards.

**Task-first** (q → E → τ).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **AgentInstruct** | 2024 | Capability targets drive agentic-flow synthesis. | `src:ACE-T2` `paradigm:task-first` | — |
| **BUTTON** | ICLR 2025 | Composes atomic tasks into complex multi-turn requests before synthesizing functions and trajectories. | `src:ACE-T2` `paradigm:task-first` `produces:q,τ` | — |
| **Agentic Proposing** | 2026 | Problem-first compositional skill synthesis. | `src:ACE-T2` `paradigm:task-first` | — |
| **ToolBridge** | 2024 | Retrofit existing tasks with tools. | `src:ACE-T2` `paradigm:task-first` | — |
| **ToRA** | ICLR 2024 | Tool-integrated mathematical reasoning. | `src:ACE-T2` `paradigm:task-first` | — |
| **MathCoder** | ICLR 2024 | Code-assisted mathematical reasoning. | `src:ACE-T2` `paradigm:task-first` | — |
| **MARIO** | ACL Findings 2024 | Code-interpreter augmented reasoning. | `src:ACE-T2` `paradigm:task-first` | — |
| **AgentMath** | 2025 | Tool-augmented math reasoning. | `src:ACE-T2` `paradigm:task-first` | — |
| **ReTool** | ICLR 2026 | Strategic tool-use reasoning via RL. | `src:ACE-T2` `paradigm:task-first` | — |
| **ToRL** | 2025 | Tool-integrated RL at scale. | `src:ACE-T2` `paradigm:task-first` | — |
| **AutoSDT** | EMNLP 2025 | Scaling scientific-discovery tasks. | `src:ACE-T2,T3` `paradigm:task-first` | — |
| **Agentic-Ideation** | 2026 | Sample-efficient ideation trajectories from reference ideas. | `src:ACE-T2` `paradigm:task-first` | — |

**Trajectory-first** (τ → q; explore/mine behavior, then write the task).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **OS-Genesis** | ACL 2025 | Reverse task synthesis from GUI trajectories, avoiding manual curation. | `src:ACE-T2,AEE-6.3.1` `paradigm:trajectory-first` | — |
| **Learn-by-interact** | ICLR 2025 | Interaction-derived task synthesis for real environments. | `src:ACE-T2` `paradigm:trajectory-first` | — |
| **Trajectory2Task** | ACL 2026 | Executable trajectories → complex user intents. | `src:ACE-T2` `paradigm:trajectory-first` | — |
| **Unlocking Implicit Experience** | ACL 2026 | Mine implicit tool workflows from text. | `src:ACE-T2` `paradigm:trajectory-first` | — |
| **Explorer** | ACL Findings 2025 | Exploration-driven web trajectories. | `src:ACE-T2` `paradigm:trajectory-first` | — |
| **OpenMobile** | 2026 | Task+trajectory co-synthesis for mobile agents. | `src:ACE-T2,T3` `paradigm:trajectory-first` | — |
| **AgentTrek** | ICLR 2025 | Web tutorials → replayable trajectories. | `src:ACE` `paradigm:trajectory-first` | — |
| **Scaling Synthetic Task Generation via Exploration** | 2025 | Expand reachable states, then derive tasks. | `src:ACE` `paradigm:trajectory-first` | — |
| **WebExplorer** | 2025 | Explore-and-evolve for long-horizon web agents. | `src:ES,AEE-6.3` `paradigm:trajectory-first` | [2509.06501](https://arxiv.org/abs/2509.06501) |

**Structure-first** (generate an intermediate scaffold — tool graph, blueprint, plan — then realize E/q/τ; the scaffold is a construction device, not a fourth factor, ACE §3.3).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **APIGen-MT** | NeurIPS 2025 | Verified blueprints before dialogue realization. | `src:ACE-T2,ES` `paradigm:structure-first` | [2504.03601](https://arxiv.org/abs/2504.03601) |
| **Magnet** | ACL 2025 | Tool-graph → dialogue translation. | `src:ACE-T2` `paradigm:structure-first` | — |
| **ToolFlow** | NAACL 2025 | Tool-graph-guided coherent dialogues. | `src:ACE-T2` `paradigm:structure-first` | — |
| **ToolACE-MT** | ICLR 2026 | Non-autoregressive coarse-to-fine multi-turn generation. | `src:ACE-T2` `paradigm:structure-first` | — |
| **Execution-First** | 2026 | Execute tool traces first, then write tasks. | `src:ACE-T2` `paradigm:structure-first` | — |
| **Plan-and-Act** | ICML 2025 | Plan-first long-horizon planning. | `src:ACE` `paradigm:structure-first` | — |
| **Taskbench** | NeurIPS 2024 | Task-graph benchmark for task automation. | `src:ACE` `paradigm:structure-first` | — |
| **DeepPlanning** | ACL 2026 | Verifiable long-horizon planning benchmark. | `src:ACE` `paradigm:structure-first` | — |

### 3.6 Adaptive & Self-Evolving Generation

Cross-cutting (ACE-T2): the generation strategy itself is revised from accumulated experience, verified outcomes, and coverage gaps. For agent–environment *co-evolution as an evolution mechanism* (difficulty tracking, self-play), see §4.

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **AFlow** | ICLR 2025 | Searched agentic workflows. | `src:ACE-T2` `paradigm:adaptive` | [2410.10762](https://arxiv.org/abs/2410.10762) |
| **Chain-of-Agents** | 2025 | Distill multi-agent systems into one agent-foundation model. | `src:ACE-T2` `paradigm:adaptive` | — |
| **SESA** | 2026 | Self-play task posing + skill evolution. | `src:ACE-T2` `paradigm:adaptive` | — |
| **Socratic-SWE** | 2026 | Trace-derived skills for adaptive task generation. | `src:ACE-T2` `paradigm:adaptive` | — |
| **AgentGen** | KDD 2025 | Environment+task generation with bidirectional difficulty. | `src:ACE,ES` `paradigm:adaptive` | [2408.00764](https://arxiv.org/abs/2408.00764) |
| **From Failure to Mastery** | 2026 | Failure-driven hard-sample generation. | `src:ACE` `paradigm:adaptive` | — |
| **Recursive Synthesis** | 2026 | Recursive composition of long-horizon terminal tasks. | `src:ACE` `paradigm:adaptive` | — |

## 4. Environment Evolution Mechanisms ★

The core differentiator of this list: how environments *change over training time*. Five mechanisms (AEE survey §7 + extensions).

### 4.1 Difficulty-Driven Evolution (Curricula)

Environment adjusts task difficulty to the learner's current capability frontier (AEE §7.2).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **RLVE** | ICML 2026 | Adaptive verifiable environments: when pass-rate at the current upper-difficulty band exceeds a threshold, the distribution shifts harder. | `src:AEE-7.2,ES` `evolution:difficulty` | [2511.07317](https://arxiv.org/abs/2511.07317) |
| **GenEnv** | 2025 | α-Curriculum Reward drives task-generation success rate toward a target band; difficulty-aligned agent–environment co-evolution. | `src:AEE-7.2` `evolution:difficulty,co-evolve` | [2512.19682](https://arxiv.org/abs/2512.19682) |
| **DreamGym** | 2025 | Adaptive task generation favoring high reward-entropy tasks for online RL. | `src:AEE-7.2` `evolution:difficulty` | [2511.03773](https://arxiv.org/abs/2511.03773) |
| **AgentFrontier** | 2025 | Zone-of-Proximal-Development-guided synthesis that pushes the capability frontier as the model advances. | `src:AEE-6.3.3,ACE` `evolution:difficulty` `paradigm:adaptive` | [2510.24695](https://arxiv.org/abs/2510.24695) |
| **EvoEnv (Learning to Build the Environment)** | 2026 | A *single policy* is both environment generator and solver; verifiable Python environments from 10 seeds; fixed-data RLVR *degrades* while self-synthesized improves (72.4→74.8). | `src:—` `evolution:difficulty,co-evolve` `produces:E,v` | [2605.14392](https://arxiv.org/abs/2605.14392) |
| **ReSyn** | 2026 | Autonomously scales reasoning environments (instance generators + verifiers) to replace hand-written procedural ones for RLVR. | `evolution:difficulty` `produces:E,v` | [2602.20117](https://arxiv.org/abs/2602.20117) |
| **EnvGen** | 2024 | LLM adjusts game-environment configs targeting the agent's weaknesses. | `src:AEE-7.2,ES` `evolution:difficulty` | [2403.12014](https://arxiv.org/abs/2403.12014) |
| **Eurekaverse** | 2024 | LLM evolves parkour terrains from training statistics. | `src:AEE-7.2` `evolution:difficulty` | [2411.01775](https://arxiv.org/abs/2411.01775) |
| **Reasoning Core** | 2025 | Scalable symbolic reasoning environments with continuously controllable difficulty. | `src:AEE-7.2` `evolution:difficulty` | [2509.18083](https://arxiv.org/abs/2509.18083) |
| **EvoCurr** | 2025 | Behavior-code-generated curricula. | `src:ES` `evolution:difficulty` | [2508.09586](https://arxiv.org/abs/2508.09586) |
| **ADACTRL** | 2025 | Difficulty-aware budget allocation. | `src:ES` `evolution:difficulty` | [2505.18822](https://arxiv.org/abs/2505.18822) |
| **WebRL** | ICLR 2025 | Self-evolving online curriculum RL for web agents. | `src:AEE-6.4,ES` `evolution:difficulty` | — |
| **SCALER** | 2026 | Online difficulty controller keeps rollout accuracy inside a target band. | `src:AEE-7.2` `evolution:difficulty` | [2601.04809](https://arxiv.org/abs/2601.04809) |
| **CuES** | 2025 | Intrinsic-curiosity-driven exploration and task synthesis without predefined tasks. | `src:AEE-7.2` `evolution:difficulty` | [2512.01311](https://arxiv.org/abs/2512.01311) |
| **POET** | 2019 | Foundational paired open-ended environment–agent co-evolution: mutate + minimal-criterion filter + transfer. | `src:AEE-7.2` `evolution:difficulty,co-evolve` | [1901.01753](https://arxiv.org/abs/1901.01753) |
| **PAIRED** | NeurIPS 2021 | Adversarial regret-minimizing environment generators (UED). | `src:AEE-7.2` `evolution:difficulty` | [2012.02096](https://arxiv.org/abs/2012.02096) |
| **ACCEL** | ICML 2022 | Regret-based editing that preserves high-value environments against curriculum collapse (UED). | `src:AEE-7.2` `evolution:difficulty` | — |
| **MAESTRO / ReMiDi / DataEnvGym** | 2022-25 | Later UED lines: guided minimax regret; teacher-side data/environment generation driven by student errors (DataEnvGym, ICLR 2025). | `src:AEE-7.2` `evolution:difficulty` | — |

### 4.2 Neural-Driven Evolution (Self-Play & World Models)

The environment is instantiated by a learnable model — often the agent itself (AEE §7.1).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **Absolute Zero** | 2025 | One model is both proposer and solver; zero-data self-play reasoning. | `src:AEE-7.1,ES` `evolution:neural` | [2505.03335](https://arxiv.org/abs/2505.03335) |
| **R-Zero** | 2025 | Challenger–solver co-evolution from zero data. | `src:ES` `evolution:neural` | [2508.05004](https://arxiv.org/abs/2508.05004) |
| **Self-Challenging** | 2025 | The same model first challenges (synthesizes verifiable tasks) then executes (learns). | `src:AEE-7.1` `evolution:neural` | [2506.01716](https://arxiv.org/abs/2506.01716) |
| **SSR / SWE-RL** | 2025 | One model alternately injects and fixes bugs (self-play environment). | `src:AEE-7.1` `evolution:neural` | [2512.18552](https://arxiv.org/abs/2512.18552) |
| **Active Zero** | 2026 | Searcher/Questioner/Solver co-evolve to actively retrieve frontier samples. | `src:AEE-7.1` `evolution:neural` | [2602.11241](https://arxiv.org/abs/2602.11241) |
| **Vision-zero** | 2025 | Gamified visual-reasoning self-play. | `src:AEE-7.1` `evolution:neural` | [2509.25541](https://arxiv.org/abs/2509.25541) |
| **WebEvolver** | EMNLP 2025 | World model and agent policy jointly evolve (planning simulator + trajectory factory). | `src:AEE-7.1,ACE-T2` `evolution:neural,co-evolve` | — |
| **Agent2World** | 2025 | Agents learn a symbolic world model via multi-agent feedback (AEE: task-driven synthesis). | `src:AEE-5.1.1` | [2512.22336](https://arxiv.org/abs/2512.22336) |

### 4.3 Scaling-Driven Evolution

Expand the environment *distribution itself* rather than adjusting difficulty. Two granularities (AEE §7.3).

**Scenario-level** — more tasks/trajectories/websites/workflows within one interaction paradigm.

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **AgentScaler** | ICLR 2026 | 30k heterogeneous APIs; expands tool × user-intent × execution-path combinations (function calls as DB reads/writes). | `src:AEE-5.1.1,7.3.1,ES` `evolution:scaling` `E:real` | [2509.13311](https://arxiv.org/abs/2509.13311) |
| **EnvScaler** | ACL Findings 2026 | Skeleton → scenario instantiation pipeline. | `src:AEE-5.1.1,7.3.1,ACE-T1` `evolution:scaling` `E:programmatic` | [2601.05808](https://arxiv.org/abs/2601.05808) |
| **FTRL** | 2025 | Automated environment construction with feedback-driven tool-use improvement. | `src:AEE-7.3.1,ES` `evolution:scaling` | [2508.08791](https://arxiv.org/abs/2508.08791) |
| AutoForge · InfiniteWeb · WebWorld | — | Scenario-level scaling exemplars — see §3.1 / §3.2 for entries. | `evolution:scaling` | — |

**Environment-level** — heterogeneous, cross-domain environment expansion (AEE §7.3.2).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **ARE** | 2025 | "Scaling up agent environments and evaluations" (Meta): a general platform for constructing and orchestrating heterogeneous environments. | `src:AEE-7.3.2,ES` `evolution:scaling` | [2509.17158](https://arxiv.org/abs/2509.17158) |
| **AutoEnv** | 2025 | Factorized environment distributions for cross-environment generalization studies. | `src:AEE-7.3.2,ES` `evolution:scaling` | [2511.19304](https://arxiv.org/abs/2511.19304) |
| Agent World Model · Agent-World · ScaleEnv · EnvFactory · daVinci-Env | — | Environment-level scaling exemplars — see §3.1 for entries. | `evolution:scaling` | — |

### 4.4 Agent–Environment Co-Evolution

Bidirectional: the environment tracks the agent's weaknesses and new capabilities; both drift together (AEE §8.6).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **GenEnv** | 2025 | Difficulty-aligned co-evolution of environment simulator and agent. | `src:AEE-7.2,ACE` `evolution:co-evolve` | [2512.19682](https://arxiv.org/abs/2512.19682) |
| **EvoEnv** | 2026 | Single-policy generator+solver co-evolution. | `evolution:co-evolve` `produces:E,v` | [2605.14392](https://arxiv.org/abs/2605.14392) |
| **Agent-World** | 2026 | Environment and policy co-evolve in a training arena. | `src:ACE-T1` `evolution:co-evolve` | [2604.18292](https://arxiv.org/abs/2604.18292) |
| **Socratic-Zero** | 2025 | Data-free agent co-evolution via self-questioning. | `src:ES` `evolution:co-evolve` | [2509.24726](https://arxiv.org/abs/2509.24726) |
| **From Trainee to Trainer** | 2026 | LLMs design their own training environments (multi-agent reasoning). | `evolution:co-evolve` | [2606.17682](https://arxiv.org/abs/2606.17682) |
| **EigenData** | 2026 | Hierarchical multi-agent engine synthesizing tool dialogues with per-instance executable checkers; self-evolving loop + GRPO-style RL (τ²-bench Airline 73.0). | `src:ACE` `evolution:co-evolve` `produces:q,τ,v` | [2601.22607](https://arxiv.org/abs/2601.22607) |
| **Tool-R0** | 2026 | Zero-data self-evolving tool-learning agent. | `src:ACE` `evolution:co-evolve` `paradigm:adaptive` | — |
| **AgentEvolver** | 2025 | Self-questioning + experience-guided evolution. | `src:ACE-T2,AEE-6.3` `evolution:co-evolve` `paradigm:adaptive` | [2511.10395](https://arxiv.org/abs/2511.10395) |

### 4.5 Generator–Verifier Co-Evolution

Verifiers themselves are generated and refined alongside environments — the answer to generator–verifier asymmetry (ES survey §5.2 & App. A.2).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **Rubrics as Rewards** | 2025 | Fine-grained rubrics as scalable reward signals. | `src:ES` `evolution:verifier` `quality:reward` | [2507.17746](https://arxiv.org/abs/2507.17746) |
| **DR Tulu** | 2025 | Evolving rubrics for deep-research RL. | `src:ES` `evolution:verifier` | [2511.19399](https://arxiv.org/abs/2511.19399) |
| **Writing-zero** | 2025 | Verifiable-reward RL extended to creative writing. | `src:ES` `evolution:verifier` | [2506.00103](https://arxiv.org/abs/2506.00103) |
| **Generative Verifiers** | 2024 | Verifier LMs prompted to reason then judge. | `src:ES` `evolution:verifier` | [2408.15240](https://arxiv.org/abs/2408.15240) |
| **WebShepherd** | 2025 | Process reward model for web-agent rollouts. | `src:ES` `evolution:verifier` `verify:prm` | [2505.15277](https://arxiv.org/abs/2505.15277) |
| **CoPER** | 2025 | Policy and reward co-optimization. | `src:ES` `evolution:verifier` | [2508.05613](https://arxiv.org/abs/2508.05613) |
| **URPO** | 2025 | Unified reward-policy optimization. | `src:ES` `evolution:verifier` | [2507.17515](https://arxiv.org/abs/2507.17515) |
| **RLPR** | 2025 | Reference-free verifiers as reward source. | `src:ES` `evolution:verifier` | [2506.18254](https://arxiv.org/abs/2506.18254) |
| **Crossing the Reward Bridge** | 2025 | Verifier-model-free RL via judge co-training. | `src:ES` `evolution:verifier` | [2503.23829](https://arxiv.org/abs/2503.23829) |

## 5. Quality, Verification & Reward

What makes an environment *good*. This chapter is where the **ACE data objective** lives — the generation paradigm (how candidates are built, §3) is a separate question from which candidates get *accepted*: **Accuracy** (admission condition), **Complexity** (learner-relative placement), **divErsity** (batch-level coverage). Four quality dimensions (AEE §5.3) unified with that lens below.

### 5.1 Correctness

State transitions must be legal, tasks solvable, validators trustworthy — accuracy is the *admission condition*, not a tradeable metric (ACE §4). Mechanism groups: execution & unit tests (SWE-Gym, Scale-SWE, GameDevBench, V-GameGym, ScaleEnv, Endless Terminals — §3); gold-trajectory comparison (AutoForge, AgentSynth, SciAgentGym).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **MCP-Universe** | 2025 | Static + dynamic evaluators replacing unstable LLM judges for verifier reliability. | `src:AEE-5.3,ES` `quality:correctness` `verify:executable` | [2508.14704](https://arxiv.org/abs/2508.14704) |
| **InterCode** | 2023 | Gold-command-validated reward functions in interactive terminals. | `src:AEE-5.3,ES` `quality:correctness` `verify:executable` | [2306.14898](https://arxiv.org/abs/2306.14898) |
| **OSWorld-MCP** | 2025 | Execution validation + expert review for environment correctness. | `src:AEE-5.3` `quality:correctness` | [2510.24563](https://arxiv.org/abs/2510.24563) |
| **Anchor** | 2026 | Mitigates artifact drift when generating agent benchmarks via component-level validation. | `src:ACE` `quality:correctness` | — |
| **APIGen** | NeurIPS 2024 | The canonical layered check: format → execution → semantic review, at step and trajectory level (ACE §4 exemplar). | `src:ACE-T1` `quality:correctness` `verify:judge` | — |

*Correctness for neural environments is redefined as constraint satisfaction (AEE §5.3): DreamGen (VLM scoring), Matrix-Game (inverse-dynamics action consistency), Genie Envisioner (symmetric Hausdorff + NDTW), MobileDreamer (mIoU).*

### 5.2 Complexity & Learnability

Difficulty is learner- and configuration-relative (ACE §5): C_z(d) = 1 − Pr[v(d,τ)=1 | d, z] for model+scaffold+tools+budget z. Train in the "learnable band" near the capability frontier; keep harder tails for evaluation. Structural quantification exemplars: AutoForge (DAG depth), OSWorld-MCP (tool turns), LOGIGEN (permissions + irreversible transitions), NL2Plan (planner length); band-targeting: GenEnv (§4.1).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **AgentFrontier** | 2025 | ZPD-guided synthesis pushing the capability frontier as the model advances. | `src:ACE,AEE-6.3.3` `quality:complexity` | [2510.24695](https://arxiv.org/abs/2510.24695) |
| **Recursive Synthesis** | 2026 | Per-round pass-rate descent as *verified* difficulty growth. | `src:ACE` `quality:complexity` | — |
| **From Failure to Mastery** | 2026 | Failure-driven hard-sample generation. | `src:ACE` `quality:complexity` | — |
| **Learning with Challenges** | 2026 | Adaptive difficulty for mobile-GUI training. | `src:ACE` `quality:complexity` | — |
| **Tool-R0** | 2026 | Zero-data self-evolution keeps tasks at the learnable frontier. | `src:ACE` `quality:complexity` | — |
| **Breaking the Solver Bottleneck** | 2026 | Train task generators at the learnable frontier. | `src:ACE` `quality:complexity` | — |
| **ToolACE-R** | AAAI 2026 | Model-aware iterative training and adaptive refinement. | `src:ACE` `quality:complexity` | — |
| **Agent Psychometrics** | 2026 | Predicting per-task performance for difficulty targeting. | `src:ACE` `quality:complexity` | — |
| **gg-bench** | 2025 | Self-play win-rate-gap filtering calibrates difficulty. | `src:AEE-5.3` `quality:complexity` | [2505.07215](https://arxiv.org/abs/2505.07215) |
| **WRIT** | 2026 | Write/read-intensive trajectories: bidirectional calibration (simplify, don't only harden). | `src:ACE` `quality:complexity` | — |
| **HiL-Bench** | 2026 | Human-in-the-loop help-seeking benchmark. | `src:ACE` `quality:complexity` | — |

### 5.3 Diversity Measurement

Behavioral coverage / normalized entropy, conditional on accuracy + learnable complexity (ACE §6, Eq. 12–13). Grouped exemplars: embedding dedup (Agent World Model scenario-collapse prevention, EnvScaler t-SNE); structural coverage (AutoForge tool-DAG walks, MCP-Universe multi-server, TaskCraft multi-hop); neural output diversity (Genie Envisioner CLIP similarity, AdaWorld, I-JEPA multi-decode); perturbation & counterfactuals (Can Agents Generalize to the Open World?, 2026; domain randomization — see UED in §4.1).

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **Vendi Score** | 2023 | Practical batch-diversity metric adopted for agentic data. | `src:ACE` `quality:diversity` | [2309.00145](https://arxiv.org/abs/2309.00145) |
| **DIVE** | 2026 | Per-task toolset coverage improves OOD generalization. | `src:ACE,AEE` `quality:diversity` | — |
| **Beyond Quantity** | 2026 | *Trajectory diversity* scaling beats quantity scaling. | `src:ACE` `quality:diversity` | — |

### 5.4 Fidelity (Sim-to-Real)

The four sim-to-real gaps (AEE §8.5): correctness, difficulty, diversity, fidelity — e.g., LLM-generated pages can encode invalid transitions that teach pseudo-policies.

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **WorldScore** | 2025 | Unified evaluation of world generation & simulation. | `src:ES` `quality:fidelity` | [2504.00983](https://arxiv.org/abs/2504.00983) |
| **Web Turing Score** (WebWorld) | 2026 | Can an LLM distinguish real from simulated web environments? | `src:AEE-5.3` `quality:fidelity` | [2602.14721](https://arxiv.org/abs/2602.14721) |
| **WorldPrediction** | 2025 | Physical-commonsense evaluation for world models. | `src:ES` `quality:fidelity` | [2506.04363](https://arxiv.org/abs/2506.04363) |
| **GAIA-2** | 2025 | Keypoint-trajectory distance for video world models (FVD/LPIPS lines: DreamGen physics checks, EnerVerse continuity). | `src:AEE-5.3` `quality:fidelity` `E:neural` | [2503.20523](https://arxiv.org/abs/2503.20523) |
| **VeriEnv** | 2026 | Clones *real* websites as executable environments to attack the realism gap. | `src:AEE-5.1.2` `quality:fidelity` | [2603.10505](https://arxiv.org/abs/2603.10505) |

### 5.5 Reward Design & Reward-Hacking Defense

ACE's warning: optimizing against a *fixed* validator breeds validator-friendly shortcuts; "validator-accepted" ≠ "independently audited". See §4.5 for generator–verifier co-evolution.

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **Tulu 3 (RLVR)** | 2024 | Verifiable rewards in the post-training recipe. | `src:ES` `quality:reward` | [2411.15124](https://arxiv.org/abs/2411.15124) |
| **OTC-PO** | 2025 | Optimal Tool Calls (OTC): reward = correctness × tool-call efficiency. | `src:AEE-6.4` `quality:reward` | [2504.14870](https://arxiv.org/abs/2504.14870) |
| **Mock Worlds, Real Skills** | 2026 | Simulated tasks + rubric rewards replacing real-environment supervision. | `src:ACE` `quality:reward` `verify:rubric` | [2601.22511](https://arxiv.org/abs/2601.22511) |
| **WebShepherd** | 2025 | Process reward model for web-agent rollouts. | `src:ES` `quality:reward` `verify:prm` | [2505.15277](https://arxiv.org/abs/2505.15277) |
| **WebSTAR** | 2025 | Step-level filtering of computer-use trajectories. | `src:ACE` `quality:reward` `verify:judge` | — |
| **Search-p1** | 2026 | Path-centric reward shaping for search agents. | `src:ACE` `quality:reward` | — |
| **MONA** | 2025 | Multi-step-lookahead mitigation for long-horizon reward hacking. | `src:ES` `quality:reward` | — |
| **Hack-Verifiable Terminal Bench** | 2026 | Evaluates reward hacking in executable terminal environments. | `src:arxiv-watch` `quality:reward` | [2608.22103](https://arxiv.org/abs/2608.22103) |

## 6. Domain Environments & Benchmarks

Only *environmental* resources: interactive, stateful, executable. Static QA benchmarks are out of scope. (The AEE survey §4 carries exhaustive per-domain benchmark tables; here we keep the environment-defining works per domain.)

### 6.1 GUI / Web / OS

| Paper | Venue | One-liner | Tags | arXiv |
|---|---|---|---|---|
| **WebShop** | NeurIPS 2022 | Shoppable web environment; the founding web-agent benchmark. | `src:AEE-4.1,ES` | [2207.01206](https://arxiv.org/abs/2207.01206) |
| **Mind2Web** | NeurIPS 2023 | General web-agent benchmark (static snapshot; grounded tasks). | `src:AEE-4.1` | [2306.04570](https://arxiv.org/abs/2306.04570) |
| **WebArena** | ICLR 2024 | Self-hostable, reproducible interactive web environments. | `src:AEE-4.1,ES` | [2307.13854](https://arxiv.org/abs/2307.13854) |
| **VisualWebArena** | 2024 | Multimodal extension of WebArena. | `src:AEE-4.1,ES` | [2401.13649](https://arxiv.org/abs/2401.13649) |
| **WebVoyager** | 2024 | Live-web agent evaluation. | `src:AEE-4.1` | — |
| **WorkArena** | 2024 | Enterprise web (ServiceNow) realistic workflows. | `src:AEE-4.1` | — |
| **OSWorld** | NeurIPS 2024 | Real-OS interactive environments (cross-app, multimodal). | `src:AEE-4.1,ES` | [2404.07972](https://arxiv.org/abs/2404.07972) |
| **WindowsAgentArena** | 2024 | Windows-OS environments at scale. | `src:AEE-4.1` | — |
| **AgentStudio** | 2025 | Toolkit for building real-OS tasks. | `src:AEE-4.1` | — |
| **OSWorld-MCP** | 2025 | GUI + standard-protocol tool access combined. | `src:AEE-4.1,5.1.2,ES` | [2510.24563](https://arxiv.org/abs/2510.24563) |
| **AitW** | 2023 | Android-in-the-Wild trajectories. | `src:AEE-4.1` | [2307.10088](https://arxiv.org/abs/2307.10088) |
| **Mobile-Env** | 2023 | Multi-step Android interaction environments. | `src:AEE-4.1` | [2305.08144](https://arxiv.org/abs/2305.08144) |
| **AndroidWorld** | 2024 | Programmatic Android benchmark with 116 tasks. | `src:AEE-4.1,ES` | [2405.14573](https://arxiv.org/abs/2405.14573) |
| **AndroidControl** | 2024 | Hybrid human-collected control trajectories. | `src:AEE-4.1` | — |
| **Mobile-Bench** | 2024 | Mobile agent benchmark with saturated/unsaturated tasks. | `src:AEE-4.1` | — |
| **MobileAgentBench** | 2024 | Deterministic, reproducible mobile evaluation. | `src:AEE-4.1` | [2406.08184](https://arxiv.org/abs/2406.08184) |
| **MobileWorld** | 2025 | Controllable mobile environments (rewardable). | `src:AEE-4.1` | — |
| **OpenCUA** | 2025 | Open computer-use environment suite. | `src:ES` | [2508.09123](https://arxiv.org/abs/2508.09123) |

### 6.2 Tool / MCP

| Paper | Venue | One-liner | Tags | arXiv |
|---|---|---|---|---|
| **API-Bank** | 2023 | 73 APIs and 314 tool-invocation tasks. | `src:AEE-4.5` | — |
| **ToolBench / ToolLLM** | ICLR 2024 | 16k+ real APIs with instruction tuning. | `src:AEE-4.5,ACE-T1` | — |
| **BFCL** | ICML 2025 | Function-calling leaderboards (v3 adds multi-turn + agents). | `src:AEE-4.5` | — |
| **AppWorld** | ACL 2024 | 9 apps + 458 people; a controllable world of interlinked APIs. | `src:AEE-4.5,ES` | [2407.18901](https://arxiv.org/abs/2407.18901) |
| **ToolSandbox** | NAACL 2025 | Stateful, conversational, interactive tool evaluation. | `src:ACE` | — |
| **τ-bench** | 2024 | User-in-the-loop tool agent benchmark with policy compliance. | `src:AEE-4.5,ES` | [2406.12045](https://arxiv.org/abs/2406.12045) |
| **τ²-bench** | 2025 | Dual-control: agent controls tools AND the user simulator. | `src:AEE-4.5,ES` | [2506.07982](https://arxiv.org/abs/2506.07982) |
| **UserBench** | 2025 | Interactive environments with *imperfect* users. | `src:AEE-4.5` | [2507.22034](https://arxiv.org/abs/2507.22034) |
| **MCP-Universe** | 2025 | 151 tools over real MCP servers; dynamic+static evaluators. | `src:AEE-4.5,5.3` | [2508.14704](https://arxiv.org/abs/2508.14704) |
| **MCPVerse** | 2025 | MCP-server agent evaluation suite. | `src:AEE-4.5` | [2508.16260](https://arxiv.org/abs/2508.16260) |
| **MCP-Bench** | 2025 | 104 MCP tools across 17 domains with dynamic truth determination. | `src:AEE-4.5` | [2508.20453](https://arxiv.org/abs/2508.20453) |
| **MCPMark** | 2026 | Deep-operation tasks on real protocol servers (GitHub/Notion). | `src:AEE-5.1.2` | — |
| **ComplexMCP** | 2026 | Dynamic, interdependent, large-scale tool sandbox. | `src:ACE` | — |
| **M³-Bench** | 2026 | Multi-turn, multi-tool MCP benchmark. | `src:AEE-4.5` | — |

### 6.3 Coding / SWE / Terminal

| Paper | Venue | One-liner | Tags | arXiv |
|---|---|---|---|---|
| **SWE-bench** | ICLR 2024 | The canonical executable SWE benchmark (+ Pro / Multi / Multimodal / rebench variants). | `src:AEE-4.6` | — |
| **InterCode** | 2023 | Interactive terminal puzzles with execution feedback. | `src:AEE-4.6,ES` | [2306.14898](https://arxiv.org/abs/2306.14898) |
| **Terminal-Bench** | 2026 | Real terminal-agent tasks with verifiable end states. | `src:AEE-4.6` | [2601.11868](https://arxiv.org/abs/2601.11868) |
| **KernelBench** | 2025 | GPU-kernel synthesis with execution feedback. | `src:AEE-4.6` | [2502.10517](https://arxiv.org/abs/2502.10517) |
| **NL2Repo-bench** | 2025 | Repo-level code understanding. | `src:AEE-4.6` | — |
| **SWT-Bench / FEA-Bench** | 2024-25 | Agentic SWE task-trajectory benchmarks. | `src:AEE-4.6` | — |

### 6.4 Deep Research (agentic only)

| Paper | Venue | One-liner | Tags | arXiv |
|---|---|---|---|---|
| **GAIA** | ICLR 2024 | General assistant benchmark requiring tool use and multimodal grounding. | `src:AEE-4.2,ES` | — |
| **WebWalker** | ACL 2025 | Traversal-based web QA for agents. | `src:AEE-4.2` | — |
| **BrowseComp** | 2025 | Hard browsing-compensation tasks against live web. | `src:AEE-4.2` | [2504.12516](https://arxiv.org/abs/2504.12516) |
| **InfoDeepSeek** | 2025 | Agentic information seeking under explicit constraints. | `src:AEE-4.2` | [2505.15872](https://arxiv.org/abs/2505.15872) |
| **DeepResearch Bench** | 2025 | 100 PhD-level research tasks with tool+doc environments. | `src:AEE-4.2` | [2506.11763](https://arxiv.org/abs/2506.11763) |
| **DeepDive** | 2025 | KG-random-walk synthesis with obfuscated key clues. | `src:AEE-6.3` `paradigm:structure-first` | [2509.10446](https://arxiv.org/abs/2509.10446) |

### 6.5 Embodied & Game

| Paper | Venue | One-liner | Tags | arXiv |
|---|---|---|---|---|
| **ALFRED** | CVPR 2020 | Language instructions + household tasks. | `src:AEE-4.3` | — |
| **ALFWorld** | ICLR 2021 | Text-game embodied household environments. | `src:AEE-4.3,ES` | [2010.03768](https://arxiv.org/abs/2010.03768) |
| **TEACh** | AAAI 2022 | Dialogue-grounded household collaboration. | `src:AEE-4.3` | — |
| **Habitat** | ICCV 2019 | High-throughput 3D navigation simulation. | `src:AEE-4.3` | — |
| **RLBench** | RA-L 2020 | 100 manipulation tasks with demos. | `src:AEE-4.3` | — |
| **BEHAVIOR** | 2021 | Everyday activities with full activity definition. | `src:AEE-4.3` | — |
| **RoboCasa** | RSS 2024 | Large-scale kitchen manipulation generation. | `src:AEE-4.3,ACE-T3` | [2406.02523](https://arxiv.org/abs/2406.02523) |
| **EmbodiedBench** | ICML 2025 | Systematic embodied evaluation from planning to low-level control. | `src:AEE-4.3,5.1.2` | — |
| **MineDojo** | NeurIPS 2022 | Open-world Minecraft with internet-scaled knowledge. | `src:AEE-4.4` | — |
| **SmartPlay** | 2024 | Games as a probe of LLM capability dimensions. | `src:AEE-4.4` | [2310.01557](https://arxiv.org/abs/2310.01557) |
| **Baba Is AI** | 2024 | Rule-rewriting puzzles. | `src:AEE-4.4` | [2407.13729](https://arxiv.org/abs/2407.13729) |
| **BALROG** | 2024 | Game-based agentic evaluation (novel games, no contamination). | `src:AEE-4.4` | [2411.13543](https://arxiv.org/abs/2411.13543) |
| **AvalonBench** | 2023 | Hidden-role social deduction. | `src:AEE-4.4` | [2310.05036](https://arxiv.org/abs/2310.05036) |
| **TextArena** | 2025 | Unified competitive text-game arena. | `src:AEE-4.4` | [2504.11442](https://arxiv.org/abs/2504.11442) |
| **LMRL Gym** | 2023 | RL environments for language agents. | `src:AEE-4.4` | [2311.18232](https://arxiv.org/abs/2311.18232) |
| **GameArena** | 2024 | Strategic games as LLM evaluation. | `src:AEE-4.4` | [2412.06394](https://arxiv.org/abs/2412.06394) |
| **CivRealm** | 2024 | Civilization as open-ended strategy environment. | `src:AEE-4.4` | — |
| **Factorio Learning Environment** | 2025 | Open-ended factory-building with programmatic state. | `src:AEE-4.4` | [2503.09617](https://arxiv.org/abs/2503.09617) |

### 6.6 Science / Medical / Finance

| Paper | Venue | One-liner | Tags | arXiv |
|---|---|---|---|---|
| **ScienceWorld** | 2022 | 30 task types across 10 science topics. | `src:AEE-4.3` | — |
| **DiscoveryWorld** | 2024 | Scientific discovery in simulated worlds. | `src:AEE-4.7` | — |
| **ScienceAgentBench** | 2024 | Data-analysis scientific tasks. | `src:AEE-4.7` | — |
| **MLE-bench** | ICLR 2025 | ML engineering with real Kaggle competitions. | `src:AEE-4.7` | — |
| **MLE-Dojo** | 2025 | Interactive ML debugging environments. | `src:AEE-4.7` | — |
| **PaperArena** | 2025 | Cross-document literature analysis. | `src:AEE-4.7,5.1.1` | — |
| **MedAgentBench** | 2025 | 300 tool-oriented medical tasks. | `src:AEE-4.7` | [2501.14654](https://arxiv.org/abs/2501.14654) |
| **MedAgentGym** | 2025 | Trainable medical code-center environments (13k). | `src:AEE-4.7,5.1.1` | — |
| **TravelPlanner** | 2024 | Planning with commonsense constraints. | `src:AEE-4.7` | — |
| **CRMArena-Pro** | 2025 | Enterprise CRM operations. | `src:AEE-4.7` | — |
| **StockBench / FinDeepResearch** | 2025-26 | Financial reasoning environments. | `src:AEE-4.7` | — |

### 6.7 Multi-Agent Society

| Paper | Venue | One-liner | Tags | arXiv |
|---|---|---|---|---|
| **Generative Agents** | 2023 | 25 LLM agents in a simulated town; the founding social sandbox. | `src:AEE-3.8` | [2304.03442](https://arxiv.org/abs/2304.03442) |
| **SOTOPIA** | 2024 | Social-intelligence environments. | `src:ACE-T3` | [2310.11667](https://arxiv.org/abs/2310.11667) |
| **SOTOPIA-ToM** | 2025 | Theory-of-mind extension. | `src:ACE-T3` | — |
| **OASIS** | 2025 | Open agent-society simulation at million scale. | `src:ES` | [2411.11581](https://arxiv.org/abs/2411.11581) |
| **Melting Pot** | 2021 | Multi-agent evaluation substrates with cultural mixing. | `src:ACE-T3` | — |
| **Concordia** | 2023 | Social-simulation GM + agents. | `src:ACE-T3` | — |
| **AgentScope** | 2024 | Multi-agent platform with message exchange. | `src:ES` | [2402.14034](https://arxiv.org/abs/2402.14034) |

### 6.8 Cross-Domain Gyms

| Paper | Venue | One-liner | Tags | arXiv |
|---|---|---|---|---|
| **OpenAI Gym** | 2016 | The ancestral environment API. | — | — |
| **AgentBench** | 2023 | 8 environments, unified evaluation. | `src:AEE-4.8` | — |
| **AgentBoard** | 2024 | Analytic evaluation board with progress rate. | `src:AEE-4.8` | — |
| **AgentGym** | 2024 | 14 environments, unified *training*. | `src:AEE-4.8,ES` | [2406.04151](https://arxiv.org/abs/2406.04151) |
| **GEM** | 2025 | A gym for agentic LMs. | `src:AEE-4.8,ES` | [2510.01051](https://arxiv.org/abs/2510.01051) |
| **AgencyBench** | 2025 | Cross-domain agency evaluation. | `src:AEE-4.8` | — |
| **lmgame-Bench** | 2025 | Games wrapped in a Gymnasium API. | `src:AEE-5.1.2` | [2505.15146](https://arxiv.org/abs/2505.15146) |

## 7. Infrastructure & Environment-as-a-Service

Agent-specific infrastructure only.

### 7.1 Sandboxes & Runtimes

| Project | Type | One-liner | Link |
|---|---|---|---|
| **E2B** | sandbox | Code sandboxes for AI agents (agent-scoped standard). | [e2b.dev](https://e2b.dev) |
| **Modal** | sandbox/GPU | Cloud sandboxes widely used for parallel agent rollouts. | [modal.com](https://modal.com) |
| **Agent-oriented microVMs** | isolation | Firecracker-class VM isolation for parallel environment rollouts (see cloud-microVM ecosystems). | — |

### 7.2 Protocols & Platforms

| Paper / Project | Venue | One-liner | Tags | Link |
|---|---|---|---|---|
| **Model Context Protocol (MCP)** | 2024 | The de-facto tool/environment interface standard. | — | [modelcontextprotocol.io](https://modelcontextprotocol.io) |
| **ARE** | 2025 | Heterogeneous environment construction/orchestration platform (Meta). | `src:AEE-7.3.2,ES` `evolution:scaling` | [arXiv:2509.17158](https://arxiv.org/abs/2509.17158) |
| **GEM** | 2025 | "A gym for agentic LMs". | `src:AEE-4.8,ES` | [arXiv:2510.01051](https://arxiv.org/abs/2510.01051) |
| **AgentGym** | 2024 | 14 environments, unified training. | `src:AEE-4.8,ES` | [arXiv:2406.04151](https://arxiv.org/abs/2406.04151) |
| **SpeechGym** | 2026 | Audio-native gym for training voice agents via RL. | `src:arxiv-watch` | [arXiv:2608.26432](https://arxiv.org/abs/2608.26432) |
| **TextArena** | 2025 | Unified competitive text-game arena. | `src:AEE-4.4` | [arXiv:2504.11442](https://arxiv.org/abs/2504.11442) |

### 7.3 Environment-as-a-Service (EaaS)

Vision (AEE survey §8.1): unified API + cloud hosting decoupling agent development from environment deployment — live environments served on demand instead of shipped as containers. Early instances: managed agent runtime offerings from major cloud/LLM vendors.

## 8. Training with Evolving Environments

How environments are consumed; only entries tightly coupled to the environment loop.

### 8.1 Agentic RL

| Paper | Venue | One-liner | Tags | arXiv |
|---|---|---|---|---|
| **Search-R1** | 2025 | Search-integrated RL. | `src:ACE-T3` `focus:search` | [2503.09516](https://arxiv.org/abs/2503.09516) |
| **ReSearch** | 2025 | RL for search agents. | `src:AEE-6.4` `focus:search` | [2503.19470](https://arxiv.org/abs/2503.19470) |
| **DeepRetrieval** | 2025 | RL for retrieval. | `src:AEE-6.4` `focus:search` | [2503.00223](https://arxiv.org/abs/2503.00223) |
| **MaskSearch** | 2025 | Answer-masked multi-agent RL. | `src:AEE-6.3` `focus:search` | [2505.20285](https://arxiv.org/abs/2505.20285) |
| **ZeroSearch** | 2025 | An LLM simulates the search engine during RL. | `src:AEE-6.4` `focus:search` | [2505.04588](https://arxiv.org/abs/2505.04588) |
| **WebSailor** | 2025 | Uncertainty-driven web-agent RL. | `src:AEE-6.4,ES` `focus:search` | [2507.02592](https://arxiv.org/abs/2507.02592) |
| **ComputerRL** | 2025 | Alternating RL/SFT against entropy collapse in computer-use RL. | `src:AEE-6.4` `focus:gui` | [2508.14040](https://arxiv.org/abs/2508.14040) |
| **WebRL** | ICLR 2025 | Self-evolving online curricula for web agents. | `src:AEE-6.4,ES` `focus:gui` `evolution:difficulty` | — |
| **UI-S1** | 2025 | Semi-online RL for GUI agents. | `src:AEE-6.4` `focus:gui` | — |
| **GiGPO** | 2025 | Anchor-state grouped step-level credit assignment. | `src:AEE-6.4` `focus:credit` | [2505.10978](https://arxiv.org/abs/2505.10978) |
| **ARPO** | 2025 | Agentic RL with tool-integrated exploration. | `src:AEE-6.4` `focus:credit` | [2507.19849](https://arxiv.org/abs/2507.19849) |
| **RAGEN** | 2025 | Reward-variance-aware multi-turn RL. | `src:AEE-6.4` `focus:credit` | [2504.20073](https://arxiv.org/abs/2504.20073) |
| **AgentRL** | 2025 | Cross-policy sampling. | `src:AEE-6.4` `focus:credit` | [2510.04206](https://arxiv.org/abs/2510.04206) |
| **VAGEN** | 2025 | World-model rewards + bi-level GAE. | `src:AEE-6.4` `focus:credit` | [2510.16907](https://arxiv.org/abs/2510.16907) |
| **AEPO** | 2025 | Entropy-balanced agentic optimization. | `src:AEE-6.4` `focus:credit` | [2510.14545](https://arxiv.org/abs/2510.14545) |
| **AgentFold** | 2025 | Folding stale context for long-horizon RL. | `src:AEE-6.3` `focus:credit` | [2510.24699](https://arxiv.org/abs/2510.24699) |

### 8.2 Agentic SFT / Trajectory Synthesis

| Paper | Venue | One-liner | Tags | arXiv |
|---|---|---|---|---|
| **Agent-FLAN** | 2024 | ReAct-style data restructured into multi-turn format. | `src:AEE-6.3` | — |
| **AgentTuning** | 2023 | The founding agent-SFT mixture. | `src:AEE-6.3` | — |
| **Aguvis** | ICML 2025 | Automatic program generation + reasoning-trace augmentation. | `src:AEE-6.3` | — |
| **UI-TARS** | 2025 | Iterative collection + reflection for GUI agents. | `src:AEE-6.3` | — |
| **APIGen-MT** | NeurIPS 2025 | Verified blueprints → multi-turn dialogues. | `src:ACE-T2,ES` `paradigm:structure-first` | [2504.03601](https://arxiv.org/abs/2504.03601) |
| **Lingma SWE-GPT** | 2024 | Three-stage SWE workflow trajectories. | `src:AEE-6.3` | [2411.00622](https://arxiv.org/abs/2411.00622) |
| **ETO** | 2024 | Trajectory-collection-then-train loop. | `src:AEE-6.3` | [2403.02502](https://arxiv.org/abs/2403.02502) |
| **GUI-Reflection** | 2025 | First-error localization + retrospective correction. | `src:AEE-6.3` | — |
| **TopoCurate** | 2026 | Interaction-topology-based trajectory curation. | `src:AEE-6.3.3` | — |

### 8.3 Offline–Online Unification

- **On-Policy Distillation** · Thinking Machines, 2025 — an early bridge; multi-turn open problems remain (early errors change state → teacher supervision inconsistency).

## 9. Scaling Evidence & Open Problems

### 9.1 Environment-Scaling Evidence

What the empirical record says about scaling environments (the seed of "environment scaling laws").

| Paper | Venue | One-liner (survey-derived) | Tags | arXiv |
|---|---|---|---|---|
| **DIVE** | 2026 | Tool-pool coverage → OOD generalization. | `src:ACE` `quality:diversity` | — |
| **Beyond Quantity** | 2026 | Diversity scaling > quantity scaling. | `src:ACE` `quality:diversity` | — |
| **ScaleEnv** | 2026 | Domain count → held-out generalization. | `src:ACE-T1` | [2602.06820](https://arxiv.org/abs/2602.06820) |
| **EnvFactory** | 2026 | A few verified environments can be more useful than a larger unreliable set. | `src:ACE-T1` | [2605.18703](https://arxiv.org/abs/2605.18703) |
| **Skywork-SWE** | 2025 | SWE data scaling laws. | `src:ACE` | — |

*ACE's synthesis: the effective scaling variable is the **effective support** of the distribution (valid + learnable + non-redundant), not raw count; quantity scaling saturates as the learner grows.*

*The ES survey's own cross-work table (App. B, Table 2) shows the same pattern on SWE-bench Verified: SWE-Gym 2,438 tasks → 20.6, R2E-Gym 8,135 → 34.4, SWE-Smith 50,137 → 40.2 — more and more realistic environments correlate with higher solve rates.*

### 9.2 Open Directions

From the AEE survey (its §8), the ES survey's future-work discussion (§5.2–§6, App. A), and local curation; a research agenda rather than a paper list.

- **Environment scaling laws** — how do environment count / diversity / horizon / complexity quantitatively drive capability and generalization?
- **Environment learnability** — which environments produce stable learning signals (sparse rewards, huge state spaces, long horizons all fail)?
- **Environment–capability mapping** — which environments cultivate which meta-capabilities (memory, decomposition, world modeling, strategic planning)?
- **Closing the sim-to-real gap** — correctness, difficulty, diversity, and fidelity gaps between synthetic and real environments.
- **Generator–verifier asymmetry** — hard-to-verify domains are the biggest opportunity; can strong generators bootstrap verifiers?
- **Multi-agent environments** — non-stationarity, credit assignment, emergent behavior.
- **Long-horizon, open-ended, omni-modal environments**; **asynchronous** (non-ReAct-static) interaction.
- **EaaS standardization** (AEE §8.1) — unified observation/action/reward interfaces; reproducible deployment.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for scope rules, entry format, and PR guidelines.

## Acknowledgments

This list's taxonomy is built on three surveys — [*Agentic Environment Engineering*](https://arxiv.org/abs/2606.12191), [*Environment Scaling*](https://arxiv.org/abs/2511.09586), and the [*ACE Lens on agentic data*](https://arxiv.org/abs/2608.27260) — and complements [Awesome-Environment-Scaling](https://github.com/lukahhcm/Awesome_Scaling_Environments) (GEF-loop paper list) and [Awesome-Agent-Environments](https://github.com/ZackZikaiXiao/Awesome-Agent-Environments) (benchmark & infrastructure list).

## License

[MIT](LICENSE)
