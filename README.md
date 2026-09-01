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
- [3. Environment Synthesis](#3-environment-synthesis)
- [4. Environment Evolution Mechanisms](#4-environment-evolution-mechanisms) ★
- [5. Quality, Verification & Reward](#5-quality-verification--reward)
- [6. Agentic Data Generation](#6-agentic-data-generation)
- [7. Domain Environments & Benchmarks](#7-domain-environments--benchmarks)
- [8. Infrastructure & Environment-as-a-Service](#8-infrastructure--environment-as-a-service)
- [9. Training with Evolving Environments](#9-training-with-evolving-environments)
- [10. Open Problems & Science of Environments](#10-open-problems--science-of-environments)

*Entry format: **Name** · venue/year — one-liner. `E-source` tags use the ACE taxonomy of environment construction (real/curated · LLM-synthesized · programmatic/executable, [ACE §3.2](https://arxiv.org/abs/2608.27260)); `produces` lists which data factors are output (E environment, q task, τ trajectory, v verifier). Code links are being verified and added progressively — see [CONTRIBUTING](CONTRIBUTING.md).*

---

## 1. Surveys & Position Papers

### 1.1 Surveys

- **Agentic Environment Engineering for LLMs: A Survey of Environment Modeling, Synthesis, Evaluation, and Application** · 2026 — the lifecycle survey this list's skeleton follows: 8 attribute pairs × 8 domains × 2 synthesis paradigms × 4 quality dimensions × agent & environment evolution. [arXiv:2606.12191](https://arxiv.org/abs/2606.12191)
- **Environment Scaling for Interactive Agentic Experience Collection: A Survey** · NeurIPS'25 SEA Workshop — environments as producers of experiential data; the Generation–Execution–Feedback (GEF) loop; generator–verifier asymmetry. [arXiv:2511.09586](https://arxiv.org/abs/2511.09586) · [companion list](https://github.com/lukahhcm/Awesome_Scaling_Environments)
- **What Makes Good Agentic Data? An ACE Lens on Data Generation for LLM Agents** · 2026 — quality lens for agentic data: Accuracy (admission condition) – Complexity (learner-relative calibration) – divErsity (behavioral coverage); data object d = (E, q, τ, v); forward vs. reverse generation. [arXiv:2608.27260](https://arxiv.org/abs/2608.27260)
- **A Survey of Self-Evolving Agents** · 2025 — agent-centric view of self-evolution; environment appears as one component. [list](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents)

### 1.2 Position Papers

- **Welcome to the Era of Experience** · Silver & Sutton, 2025 — the programmatic statement that agents must learn from their own interaction data, not human-static corpora.
- **AgentScaler: Towards General Agentic Intelligence via Environment Scaling** · ICLR 2026 — the manifesto-paper for environment scaling: 30k heterogeneous APIs turned into diverse environments by treating function calls as database reads/writes. [arXiv:2509.13311](https://arxiv.org/abs/2509.13311)
- **Scalable Environments Drive Generalizable Agents** · 2026 — distinguishes trajectory scaling / task scaling / **environment scaling**; argues generalization requires scaling the distribution of executable rule sets; contrasts procedural generators vs. generative world models. [arXiv:2605.18181](https://arxiv.org/abs/2605.18181)

## 2. Formalization & Environment Attributes

Two complementary cuts, plus the shared interaction formalism.

- **POMDP formalism** — both the lifecycle survey (§2.1, E = ⟨S, A, P, R, Ω, O, γ⟩ extended for tool-augmented, language-centered agents) and ACE (§2.1, interaction as partial observability) ground "agentic environment" in a POMDP.
- **Intra-environment decomposition (ACE §2.2)** — e = (D state carrier, F tool/action set, P_rule policies & constraints, Ω observation exposure, v success interface); E ranges from a *static interface specification* (tool schemas) to a *complete executable interaction substrate*. [arXiv:2608.27260](https://arxiv.org/abs/2608.27260)
- **Inter-environment attribute pairs (lifecycle survey §3)** — symbolic vs. neural · open- vs. closed-loop · online vs. offline · MDP vs. POMDP · deterministic vs. stochastic · discrete vs. continuous · uni- vs. multi-modal · single- vs. multi-agent. [arXiv:2606.12191](https://arxiv.org/abs/2606.12191)
- Terminology note: an **"LLM-synthesized environment"** (ACE) means LLMs generate *symbolic* tool specs/rules; a **"neural environment"** (lifecycle survey §3.1/§5.2) means the *transition function itself* is a network (world model). Different things — don't conflate.

## 3. Environment Synthesis

Dual-label organization: the lifecycle survey's **synthesis route** (what real material seeds the pipeline) × ACE's **E-source** (how the resulting E is implemented).

### 3.1 Symbolic / Programmatic Synthesis

**Task-driven** — wrap static real assets (repos, issues, tasks) into executable environments.

- **SWE-Gym** · ICML 2025 — 11 Python repos packaged as Docker environments with hybrid validators; trains both SWE agents and verifiers. [arXiv:2412.21139](https://arxiv.org/abs/2412.21139)
- **R2E-Gym** · COLM 2025 — procedural SWE environments + hybrid (test & LLM) verification; 8,135 tasks. [arXiv:2504.07164](https://arxiv.org/abs/2504.07164)
- **SWE-smith** · NeurIPS 2025 — 50k synthesized SWE tasks from a single shared image via transient bug injection. [arXiv:2504.21798](https://arxiv.org/abs/2504.21798)
- **Scale-SWE** · 2026 — three-agent collaboration (Environment Builder / Unittest Creator / Problem Writer) immersed in the GitHub universe. [arXiv:2602.09892](https://arxiv.org/abs/2602.09892)
- **SWE-Hub** · 2026 — system-level real-bug environments via Env Agent + Bug Agent. [arXiv:2603.00575](https://arxiv.org/abs/2603.00575)
- **MEnvAgent** · 2026 — incremental patching to *reuse* environments across tasks instead of rebuilding. [arXiv:2601.22859](https://arxiv.org/abs/2601.22859)
- **DockSmith** · 2026 — a *trained* model that generates and repairs Dockerfiles for environment images. [arXiv:2602.00592](https://arxiv.org/abs/2602.00592)
- **SCALER** · 2026 — competitive-programming data synthesized into verifiable environments with tunable difficulty for RL. [arXiv:2601.04809](https://arxiv.org/abs/2601.04809)
- **AgentFounder / Agentic CPT** · 2025 — turns unstructured corpora (Wikipedia/CommonCrawl) into interactive environments for continued pre-training. [arXiv:2509.13310](https://arxiv.org/abs/2509.13310)
- **daVinci-Env (OpenSWE)** · 2026 — 45,320 fully transparent executable Docker environments from 12.8k repos; the largest open SWE environment synthesis stack. [arXiv:2603.13023](https://arxiv.org/abs/2603.13023)

**Real-world-driven** — project real interaction media (web, OS, games, tools) into simplified virtual environments.

- **AgentSynth** · 2025 — exploits information asymmetry: generating easy sub-tasks stepwise is far cheaper than solving one long-horizon task; difficulty-controllable. [arXiv:2506.14205](https://arxiv.org/abs/2506.14205)
- **TaskCraft** · 2025 — web-grounded, difficulty-tunable tool-call task synthesis (compositional scaling). [arXiv:2506.10055](https://arxiv.org/abs/2506.10055)
- **OS-Genesis** · ACL 2025 — reverse task synthesis from GUI trajectories, avoiding manual curation. [paper](https://aclanthology.org/) *(trajectory-first; see also §6.4)*
- **VeriEnv** · 2026 — LMs as *environment creators*: clone real websites into executable, programmatically verifiable synthetic environments. [arXiv:2603.10505](https://arxiv.org/abs/2603.10505)
- **Training Needs Trustworthy Worlds** · 2026 — verified synthetic web environments for agent learning. [arXiv:2608.21898](https://arxiv.org/abs/2608.21898)
- **AutoWebWorld** · 2026 — websites as finite-state machines; systematic enumeration and verification of web environments ("infinite verifiable web environments"). [arXiv:2602.14296](https://arxiv.org/abs/2602.14296)
- **InfiniteWeb** · 2026 — lightweight specs auto-expanded into functional websites + tasks + reward evaluators. [arXiv:2601.04126](https://arxiv.org/abs/2601.04126)
- **V-GameGym** · 2025 — visual-rendering feedback environments built on games. [arXiv:2509.20136](https://arxiv.org/abs/2509.20136)
- **MedMCP-Calc** · 2026 — MCP environments over real EHR stores + clinical guideline retrieval. [arXiv:2601.23049](https://arxiv.org/abs/2601.23049)
- **SWE-Universe** · 2026 — million-scale real verifiable environments. [arXiv:2602.02361](https://arxiv.org/abs/2602.02361)

**De Novo** — synthesize environments from scratch with minimal seeds; the closest to "environment scaling as free expansion."

- **AutoForge** · 2025 — builds scalable state structures and a tool-call logic DAG before code generation; RL-stabilized. [arXiv:2512.22857](https://arxiv.org/abs/2512.22857)
- **Agent World Model** · ICML 2026 — "Infinity Synthetic Environments for Agentic RL": code-driven, DB-backed fully synthetic pipeline reaching 1,000+ environments with execution-level self-correction. [arXiv:2602.10090](https://arxiv.org/abs/2602.10090)
- **ScaleEnv** · 2026 — from-scratch fully interactive environments + verifiable tasks; clean evidence that *domain count → generalization* on unseen benchmarks. [arXiv:2602.06820](https://arxiv.org/abs/2602.06820)
- **EnvFactory** · 2026 — automatic exploration/validation of stateful executable tool environments (85 envs, 7 domains); shows a *few strongly verified environments beat masses of redundant ones*. [arXiv:2605.18703](https://arxiv.org/abs/2605.18703)
- **EnvScaler** · ACL Findings 2026 — SkelBuilder (environment skeletons) + ScenGenerator (scenario instantiation + rule validators); 191 environments / ~7k scenarios. [arXiv:2601.05808](https://arxiv.org/abs/2601.05808)
- **Agent-World** · 2026 — self-evolving training arena: autonomous discovery of MCP/tool environments + controllable-difficulty task synthesis; environment and policy co-evolve. [arXiv:2604.18292](https://arxiv.org/abs/2604.18292)
- **AutoEnv** · 2025 — environments as factorizable distributions of transitions/observations/rewards; unified generation of heterogeneous environments for cross-environment learning. [arXiv:2511.19304](https://arxiv.org/abs/2511.19304)
- **LOGIGEN** · 2026 — logic-driven forward deduction; rules compiled into SQLite-backed physical environments. [arXiv:2603.00540](https://arxiv.org/abs/2603.00540)
- **SWE-Playground** · 2025 — first fully synthetic SWE training pipeline, fully off GitHub. [arXiv:2512.12216](https://arxiv.org/abs/2512.12216)
- **Endless Terminals** · 2026 — samples file-operation/network-config dimensions to synthesize thousands of terminal environments. [arXiv:2601.16443](https://arxiv.org/abs/2601.16443)
- **gg-bench** · 2025 — randomly samples *brand-new* two-player games; contamination-proof by construction. [arXiv:2505.07215](https://arxiv.org/abs/2505.07215)
- **RandomWorld** · EMNLP 2025 — procedural environment generation for tool agents. [arXiv:2506.11045](https://arxiv.org/abs/2506.11045)
- **NL2Plan** · 2024 — natural-language PDDL environment generation. [arXiv:2405.04215](https://arxiv.org/abs/2405.04215)
- **Envs-FORGE** · 2026 — frontier-optimized, reward-grounded environment synthesis for agent RL. [arXiv:2608.14312](https://arxiv.org/abs/2608.14312)
- **AgentMercury** · 2026 — agents synthesize verifiable business-scenario environments at scale. [arXiv:2608.20634](https://arxiv.org/abs/2608.20634)

### 3.2 Neural Synthesis (World-Model-as-Environment)

The transition function P is parameterized by a network. Three abstraction levels (lifecycle survey §5.2).

**Pixel-level** — high fidelity, high redundancy.

- **DreamGen** · 2025 — video world model (WAN2.1) generating synthetic robot trajectories from ~1000 videos. [arXiv:2505.12705](https://arxiv.org/abs/2505.12705)
- **GameNGen** · 2024 — a diffusion model as a real-time game engine (DOOM). [arXiv:2408.14837](https://arxiv.org/abs/2408.14837)
- **Matrix-Game** · 2025 — large-scale Minecraft data, key-mouse continuous input, minute-level stable interaction. [arXiv:2506.18701](https://arxiv.org/abs/2506.18701)
- **NeuralOS** · 2025 — hierarchical RNN maintains persistent OS state + diffusion rendering. [arXiv:2507.08800](https://arxiv.org/abs/2507.08800)
- **DreamZero** · 2026 — "World Action Models are Zero-shot Policies". [arXiv:2602.15922](https://arxiv.org/abs/2602.15922)
- **Pandora** · 2024 — world-model with rule-controllable generation. [arXiv:2406.09455](https://arxiv.org/abs/2406.09455)
- **Genie 3** · DeepMind 2025 — real-time, long-horizon-consistent interactive world model (technical report).

**Token-level** — environments represented in language; cheap, abstract, planning-friendly.

- **WebWorld** · 2026 — first large-scale open web world model, trained on 1M+ real open-web interactions; safe offline synthesis of web-agent trajectories (+9.2 WebArena for Qwen3-14B). [arXiv:2602.14721](https://arxiv.org/abs/2602.14721)
- **WebDreamer** · TMLR 2025 — a strong LLM prompted *as* the web world model for model-predictive planning.
- **Code2World** · 2026 — GUI states as renderable code; rendering-perception RL alignment. [arXiv:2602.09856](https://arxiv.org/abs/2602.09856)
- **MobileDreamer** · 2026 — structured text representation of GUI elements + rollout-imagination trees. [arXiv:2601.04035](https://arxiv.org/abs/2601.04035)
- **UI-Simulator** · 2025 — LLM generates future UI states and guides rollouts for data synthesis. [arXiv:2510.14969](https://arxiv.org/abs/2510.14969)
- **gWorld / SWE-World / Simia** · 2025-26 — LLM-as-simulator lines for GUI, SWE, and general environments. [arXiv:2602.01576](https://arxiv.org/abs/2602.01576) · [arXiv:2602.03419](https://arxiv.org/abs/2602.03419) · [arXiv:2511.01824](https://arxiv.org/abs/2511.01824)

**Latent-level** — compact learned representations.

- **V-JEPA 2** · 2025 — 1M hours of video pre-training + 62h robot data → zero-shot robot planning. [arXiv:2506.09985](https://arxiv.org/abs/2506.09985)
- **DINO-WM** · 2024 — world model on frozen DINOv2 features; zero-shot planning. [arXiv:2411.04983](https://arxiv.org/abs/2411.04983)
- **IWM** · 2024 — "in-context" world models. [arXiv:2403.00504](https://arxiv.org/abs/2403.00504)
- **AdaWorld** · ICML 2025 — latent-action-conditioned, adaptable world models.

### 3.3 Compositional Synthesis

Compose verifiable environments/tasks recursively rather than linearly expanding.

- **RACES** · 2026 — "Verifiable Environments Are LEGO Bricks": recursive composition (type matching + SEQUENTIAL/PARALLEL/SORT/SELECT operators); 50 composed environments ≈ 300 standalone ones. [arXiv:2606.12373](https://arxiv.org/abs/2606.12373)
- **BUTTON** · ICLR 2025 — composes atomic tasks into complex multi-turn requests before synthesizing functions and trajectories. *(see also §6.4)*

### 3.4 Harnessing Static Environments (Reuse over Rebuild)

Re-activate existing static worlds instead of synthesizing new ones.

- **EnvHarness** · 2026 — programmable plugin layer wrapping static environments (preserving original validators) to reshape behavior; EnvRigger diagnoses policy defects from trajectories and synthesizes harnesses; up to +9.0 held-out. [arXiv:2608.19880](https://arxiv.org/abs/2608.19880)
- **Environment Tuning** · 2025 — "Don't just fine-tune the agent, tune the environment": manual curricula + environment augmentation + progress feedback. [arXiv:2510.10197](https://arxiv.org/abs/2510.10197)
- **CLI-Gym** · 2026 — "environment reversal": deliberately corrupts environments to generate error-recovery training data. [arXiv:2602.10999](https://arxiv.org/abs/2602.10999)

## 4. Environment Evolution Mechanisms ★

The core differentiator of this list: how environments *change over training time*. Five mechanisms (lifecycle survey §7 + extensions).

### 4.1 Difficulty-Driven Evolution (Curricula)

Environment adjusts task difficulty to the learner's current capability frontier.

- **RLVE** · ICML 2026 — adaptive verifiable environments: when pass-rate at the current upper-difficulty band exceeds a threshold, the distribution shifts harder. [arXiv:2511.07317](https://arxiv.org/abs/2511.07317)
- **GenEnv** · 2025 — α-Curriculum Reward drives task-generation success rate toward a target band; difficulty-aligned agent–environment co-evolution. [arXiv:2512.19682](https://arxiv.org/abs/2512.19682)
- **DreamGym** · 2025 — adaptive task generation favoring high reward-entropy tasks for online RL. [arXiv:2511.03773](https://arxiv.org/abs/2511.03773)
- **AgentFrontier** · 2025 — Zone-of-Proximal-Development-guided data synthesis that pushes the capability frontier as the model advances. [arXiv:2510.24695](https://arxiv.org/abs/2510.24695)
- **EvoEnv (Learning to Build the Environment)** · 2026 — a *single policy* is both environment generator and solver; verifiable Python environments from 10 seeds with staged checks, difficulty calibration, novelty checks; fixed-data RLVR *degrades* while self-synthesized improves (72.4→74.8). [arXiv:2605.14392](https://arxiv.org/abs/2605.14392)
- **ReSyn** · 2026 — autonomously scales reasoning environments (instance generators + verifiers) to replace hand-written procedural ones for RLVR. [arXiv:2602.20117](https://arxiv.org/abs/2602.20117)
- **EnvGen** · 2024 — LLM adjusts game-environment configs targeting the agent's weaknesses. [arXiv:2403.12014](https://arxiv.org/abs/2403.12014)
- **Eurekaverse** · 2024 — LLM evolves parkour terrains from training statistics. [arXiv:2411.01775](https://arxiv.org/abs/2411.01775)
- **Reasoning Core** · 2025 — scalable symbolic reasoning environments with continuously controllable difficulty. [arXiv:2509.18083](https://arxiv.org/abs/2509.18083)
- **EvoCurr** · 2025 — behavior-code-generated curricula. [arXiv:2508.09586](https://arxiv.org/abs/2508.09586)
- **ADACTRL** · 2025 — difficulty-aware budget allocation. [arXiv:2505.18822](https://arxiv.org/abs/2505.18822)
- **WebRL** · ICLR 2025 — self-evolving online curriculum RL for web agents.
- **SCALER** · 2026 — online difficulty controller keeps rollout accuracy inside a target band. [arXiv:2601.04809](https://arxiv.org/abs/2601.04809)
- **CuES** · 2025 — intrinsic-curiosity-driven exploration and task synthesis without predefined tasks. [arXiv:2512.01311](https://arxiv.org/abs/2512.01311)
- **UED classics** · 2019-24 — Unsupervised Environment Design: **PAIRED** [arXiv:2012.02096](https://arxiv.org/abs/2012.02096), adversarial regret-minimizing environment generators; ACCEL, MAESTRO, ReMiDi, DataEnvGym (teacher-side generation driven by student errors).

### 4.2 Neural-Driven Evolution (Self-Play & World Models)

The environment is instantiated by a learnable model — often the agent itself.

- **Absolute Zero** · 2025 — one model is both proposer and solver; zero-data self-play reasoning. [arXiv:2505.03335](https://arxiv.org/abs/2505.03335)
- **R-Zero** · 2025 — challenger–solver co-evolution from zero data. [arXiv:2508.05004](https://arxiv.org/abs/2508.05004)
- **Self-Challenging** · 2025 — the same model first challenges (synthesizes verifiable tasks) then executes (learns). [arXiv:2506.01716](https://arxiv.org/abs/2506.01716)
- **SSR / SWE-RL** · 2025 — one model alternately injects and fixes bugs (self-play environment). [arXiv:2512.18552](https://arxiv.org/abs/2512.18552)
- **Active Zero** · 2026 — Searcher/Questioner/Solver co-evolve to actively retrieve frontier samples. [arXiv:2602.11241](https://arxiv.org/abs/2602.11241)
- **Vision-zero** · 2025 — gamified visual-reasoning self-play. [arXiv:2509.25541](https://arxiv.org/abs/2509.25541)
- **WebEvolver** · EMNLP 2025 — world model and agent policy jointly evolve (planning simulator + trajectory factory).
- **Agent2World** · 2025 — agents learn a symbolic world model from multi-agent feedback. [arXiv:2512.22336](https://arxiv.org/abs/2512.22336)

### 4.3 Scaling-Driven Evolution

Expand the environment *distribution itself* rather than adjusting difficulty. Two granularities (lifecycle survey §7.3).

**Scenario-level** — more tasks/trajectories/websites/workflows within one interaction paradigm.

- **AgentScaler** · ICLR 2026 — 30k heterogeneous APIs; expands tool × user-intent × execution-path combinations. [arXiv:2509.13311](https://arxiv.org/abs/2509.13311)
- **EnvScaler** · ACL Findings 2026 — skeleton → scenario instantiation pipeline. [arXiv:2601.05808](https://arxiv.org/abs/2601.05808)
- **FTRL** · 2025 — automated environment construction with feedback-driven tool-use improvement. [arXiv:2508.08791](https://arxiv.org/abs/2508.08791)
- Also: AutoForge, InfiniteWeb, WebWorld (§3).

**Environment-level** — heterogeneous, cross-domain environment expansion.

- **ARE** · 2025 — "Scaling up agent environments and evaluations" (Meta): general platform for constructing and orchestrating heterogeneous environments. [arXiv:2509.17158](https://arxiv.org/abs/2509.17158)
- **AutoEnv** · 2025 — factorized environment distributions for cross-environment generalization studies. [arXiv:2511.19304](https://arxiv.org/abs/2511.19304)
- Also: Agent World Model, Agent-World, ScaleEnv, EnvFactory, daVinci-Env (§3.1).

### 4.4 Agent–Environment Co-Evolution

Bidirectional: the environment tracks the agent's weaknesses and new capabilities; both drift together.

- **GenEnv** · 2025 — difficulty-aligned co-evolution of environment simulator and agent. [arXiv:2512.19682](https://arxiv.org/abs/2512.19682)
- **EvoEnv** · 2026 — single-policy generator+solver co-evolution. [arXiv:2605.14392](https://arxiv.org/abs/2605.14392)
- **Agent-World** · 2026 — environment and policy co-evolve in a training arena. [arXiv:2604.18292](https://arxiv.org/abs/2604.18292)
- **Socratic-Zero** · 2025 — data-free agent co-evolution via self-questioning. [arXiv:2509.24726](https://arxiv.org/abs/2509.24726)
- **From Trainee to Trainer** · 2026 — LLMs design their own training environments (multi-agent reasoning). [arXiv:2606.17682](https://arxiv.org/abs/2606.17682)
- **EigenData** · 2026 — hierarchical multi-agent engine synthesizing tool dialogues with per-instance executable checkers; self-evolving loop + GRPO-style RL (τ²-bench Airline 73.0). [arXiv:2601.22607](https://arxiv.org/abs/2601.22607)
- **Tool-R0** · 2026 — zero-data self-evolving tool-learning agent.
- **AgentEvolver** · 2025 — self-questioning + experience-guided evolution.

### 4.5 Generator–Verifier Co-Evolution

Verifiers themselves are generated and refined alongside environments — the answer to generator–verifier asymmetry (Environment Scaling survey §Feedback).

- **Rubrics as Rewards** · 2025 — fine-grained rubrics as scalable reward signals. [arXiv:2507.17746](https://arxiv.org/abs/2507.17746)
- **DR Tulu** · 2025 — evolving rubrics for deep-research RL. [arXiv:2511.19399](https://arxiv.org/abs/2511.19399)
- **Writing-zero** · 2025 — verifiable-reward RL extended to creative writing. [arXiv:2506.00103](https://arxiv.org/abs/2506.00103)
- **Generative Verifiers** · 2024 — verifier LMs prompted to reason then judge. [arXiv:2408.15240](https://arxiv.org/abs/2408.15240)
- **WebShepherd** · 2025 — process reward model for web-agent rollouts. [arXiv:2505.15277](https://arxiv.org/abs/2505.15277)
- **CoPER** · 2025 — policy and reward co-optimization. [arXiv:2508.05613](https://arxiv.org/abs/2508.05613)
- **URPO** · 2025 — unified reward-policy optimization. [arXiv:2507.17515](https://arxiv.org/abs/2507.17515)
- **RLPR** · 2025 — reward from preference / reference-free verifiers. [arXiv:2506.18254](https://arxiv.org/abs/2506.18254)
- **Crossing the Reward Bridge** · 2025 — verifier-model-free RL via judge co-training. [arXiv:2503.23829](https://arxiv.org/abs/2503.23829)

## 5. Quality, Verification & Reward

What makes an environment *good* — four dimensions (lifecycle survey §5.3) unified with the ACE lens (Accuracy admission / Complexity calibration / divErsity coverage).

### 5.1 Correctness

State transitions must be legal, tasks solvable, validators trustworthy — accuracy is the *admission condition*, not a tradeable metric (ACE §4).

- Execution & unit tests as ground truth: SWE-Gym, Scale-SWE, GameDevBench (Godot test harness), V-GameGym (sandbox auto-repair), ScaleEnv (programmatic tests), Endless Terminals (container build + init/completion tests) — see §3.
- Gold-trajectory / terminal-state comparison: AutoForge (gold tool sequences), AgentSynth (stepwise verifier), SciAgentGym.
- **Verifier reliability itself**: **MCP-Universe** · 2025 — static+dynamic evaluators replacing unstable LLM judges. [arXiv:2508.14704](https://arxiv.org/abs/2508.14704) · **InterCode** · 2023 — gold-command-validated reward functions. [arXiv:2306.14898](https://arxiv.org/abs/2306.14898) · **OSWorld-MCP** · 2025 — execution validation + expert review. [arXiv:2510.24563](https://arxiv.org/abs/2510.24563)
- Correctness for *neural* environments, redefined as constraint satisfaction: DreamGen (VLM scoring), Matrix-Game (inverse-dynamics action consistency), Genie Envisioner (symmetric Hausdorff + NDTW), MobileDreamer (mIoU box overlap).
- **Anchor** · 2026 — mitigates artifact drift when generating agent benchmarks via component-level validation.
- Layered rule–model–human checking (ACE §4): format → execution → semantic, at step and trajectory level — APIGen is the canonical example.

### 5.2 Complexity & Learnability

Difficulty is learner- and configuration-relative (ACE §5): C_z(d) = 1 − Pr[v(d,τ)=1 | d, z] for model+scaffold+tools+budget z. Train in the "learnable band" near the capability frontier; keep harder tails for evaluation.

- Structural quantification: AutoForge (DAG depth), OSWorld-MCP (tool-turn counts), LOGIGEN (multi-variable + role permissions + irreversible transitions), NL2Plan (optimal-plan-length binning).
- Calibration against strong models / humans: gg-bench (self-play win-rate-gap filtering), AI Gamestore (expert cognitive ratings).
- Failure-driven, model-aware filtering: **AgentFrontier** · 2025 — ZPD-guided frontier pushing. [arXiv:2510.24695](https://arxiv.org/abs/2510.24695) · **GenEnv** · 2025 — success rate steered to a target band. [arXiv:2512.19682](https://arxiv.org/abs/2512.19682) · **Recursive Synthesis** · 2026 — per-round pass-rate descent as verified difficulty growth · **From Failure to Mastery** · 2026 — failure-driven hard-sample generation · **Learning with Challenges** · 2026 — adaptive mobile-GUI difficulty · **Tool-R0** · 2026 · **Breaking the Solver Bottleneck** · 2026 — train generators at the learnable frontier · **ToolACE-R** · AAAI 2026 — model-aware iterative refinement · **Agent Psychometrics** · 2026 — per-task performance prediction.
- Bidirectional calibration (simplify, don't only harden): WRIT · 2026 — write/read-intensive trajectories · **HiL-Bench** · 2026 — human-in-the-loop help-seeking · scaffolding changes the execution config z itself (ACE §5.7).

### 5.3 Diversity Measurement

- **Vendi Score** · 2023 — practical batch-diversity metric. [arXiv:2309.00145](https://arxiv.org/abs/2309.00145)
- Behavioral coverage / normalized entropy, conditional on accuracy + learnable complexity (ACE §6, Eq. 13); action-graph and dependency-path fingerprints for redundancy.
- Embedding dedup: Agent World Model (scenario-collapse prevention), EnvScaler (embedding similarity + t-SNE checks).
- Structural coverage: AutoForge (tool-DAG random walks), MCP-Universe (multi-server tool combinations), TaskCraft (multi-hop).
- Output-distribution diversity for neural environments: Genie Envisioner (CLIP pairwise similarity), AdaWorld (cross-context transfer), I-JEPA (multi-sample decoding).
- Coverage-guided scaling: **DIVE** · 2026 — per-task toolset coverage improves OOD generalization · **Beyond Quantity** · 2026 — *trajectory diversity* scaling beats quantity scaling.
- Perturbation & counterfactual variation: **Can Agents Generalize to the Open World?** · 2026 · domain-randomization classics (see also UED in §4.1).

### 5.4 Fidelity (Sim-to-Real)

- **WorldScore** · 2025 — unified evaluation of world generation & simulation. [arXiv:2504.00983](https://arxiv.org/abs/2504.00983)
- **Web Turing Score** (WebWorld) · 2026 — can an LLM distinguish real from simulated web environments? [arXiv:2602.14721](https://arxiv.org/abs/2602.14721)
- **WorldPrediction** · 2025 — physical-commonsense evaluation for world models. [arXiv:2506.04363](https://arxiv.org/abs/2506.04363)
- Physics & motion metrics: DreamGen (rigid-body motion checks), GAIA-2 (keypoint-trajectory distance) [arXiv:2503.20523](https://arxiv.org/abs/2503.20523), EnerVerse (expert-judged continuity).
- The four sim-to-real gaps (lifecycle survey §8.5): correctness, difficulty, diversity, fidelity — e.g., LLM-generated pages can encode invalid transitions that teach pseudo-policies.
- **VeriEnv** · 2026 — clones *real* websites as executable environments to attack the realism gap. [arXiv:2603.10505](https://arxiv.org/abs/2603.10505)

### 5.5 Reward Design & Reward-Hacking Defense

- **Tulu 3 (RLVR)** · 2024 — verifiable rewards in the post-training recipe. [arXiv:2411.15124](https://arxiv.org/abs/2411.15124)
- **OTC-PO** · 2025 — over-trust correction: reward × tool-call efficiency. [arXiv:2504.14870](https://arxiv.org/abs/2504.14870)
- **Mock Worlds, Real Skills** · 2026 — simulated tasks + rubric rewards replacing real-environment supervision. [arXiv:2601.22511](https://arxiv.org/abs/2601.22511)
- Process/step-level rewards: **WebShepherd** · 2025 — web-agent process reward model. [arXiv:2505.15277](https://arxiv.org/abs/2505.15277) · **WebSTAR** · 2025 — step-level filtering · **Search-p1** · 2026 — path-centric reward shaping.
- **MONA** · 2025 — multi-step-lookahead mitigation for long-horizon reward hacking.
- **Hack-Verifiable Terminal Bench** · 2026 — evaluates reward hacking in executable terminal environments. [arXiv:2608.22103](https://arxiv.org/abs/2608.22103)
- ACE's warning: optimizing against a *fixed* validator breeds validator-friendly shortcuts; "validator-accepted" ≠ "independently audited". See §4.5 for generator–verifier co-evolution.

## 6. Agentic Data Generation

Data-generation paradigms and quality objectives for agents (ACE §3). The environment is one *factor* of the data object d = (E, q, τ, v); the "environments replace data" thesis itself belongs to the surveys in §1. Two questions are kept separate throughout: the generation *paradigm* (how candidates are built) and the data *objective* (which get accepted — the ACE lens, §5).

### 6.1 The ACE Objective

Accuracy (admission condition) – Complexity (learner-relative placement) – divErsity (batch-level coverage). [arXiv:2608.27260](https://arxiv.org/abs/2608.27260)

### 6.2 Forward Generation (E → q → τ)

**Real / curated environments**

- **ToolLLM** · ICLR 2024 — 16k+ real APIs; the founding large-scale tool dataset.
- **Gorilla** · NeurIPS 2024 — API-grounded instruction generation at scale.
- **APIGen** · NeurIPS 2024 — format check → execution → semantic review; the canonical three-layer verification pipeline.
- **ToolDial** · ICLR 2025 — real API-graph-guided multi-turn dialogues.
- **Close the Loop (InfTool)** · 2025 — multi-agent role-play toward "infinite" tool-use data.
- **TOUCAN** · 2025 — 1.5M tool-agent samples synthesized from real MCP environments.
- SWE pipelines from real repos: SWE-Gym, R2E-Gym, SWE-smith, SWE-rebench (§3.1).

**LLM-synthesized (symbolic) environments**

- **ToolACE** · ICLR 2025 — self-evolving API pool + decision-tree retrieval.
- **ToolAlpaca** · 2023 — 3k simulated tool cases; the early demonstration.
- **Seal-Tools** · NLPCC 2024 — self-instruct tool dataset.
- **SynthTools** · 2025 — hierarchical, verifiable synthesis for scaling agent development.
- **ToolWeave** · 2026 — synthetic tool graphs → complex multi-turn dialogues.

**Programmatic / executable environments**

- EnvScaler, Agent-World, EnvFactory, ScaleEnv, Agent World Model, LOGIGEN (§3.1).
- **CodeGym** · ICLR 2026 — synthetic code environments for end-to-end tool-use RL. [arXiv:2509.17325](https://arxiv.org/abs/2509.17325)
- **ToolVerse** · 2026 — many environments + long-horizon tasks unlocking agentic RL.
- **SciDisco** · 2026 — scientific-discovery environments scaled for turn-level RL.
- **ASTRA** · 2026 — auto-synthesized trajectory and RL arenas.

**Simulator / environment-free variants**

- **Simulating Environments with Reasoning Models** · 2025 — LLM simulators produce stateful responses from API specs.
- **Environment-free Synthetic Data Generation for API Agents** · 2026.
- **EnvACE** · 2026 — internalizes environment dynamics via world-model rehearsal.

### 6.3 Reverse Generation

**Task-first**

- **AgentInstruct** · 2024 — capability targets drive agentic-flow synthesis.
- **BUTTON** · ICLR 2025 — compose atomic tasks into complex multi-turn requests.
- **Agentic Proposing** · 2026 — problem-first compositional skill synthesis.
- **ToolBridge** · 2024 — retrofit existing tasks with tools.
- Tool-integrated math: **ToRA** · ICLR 2024 · **MathCoder** · ICLR 2024 · **MARIO** · ACL Findings 2024 · **AgentMath** · 2025 · **ReTool** · ICLR 2026 · **ToRL** · 2025.
- Science: **AutoSDT** · EMNLP 2025 — scaling scientific-discovery tasks · **Agentic-Ideation** · 2026 — sample-efficient ideation trajectories.

**Trajectory-first**

- **OS-Genesis** · ACL 2025 — reverse GUI trajectory → task.
- **Learn-by-interact** · ICLR 2025 — interaction-derived task synthesis for real environments.
- **Trajectory2Task** · ACL 2026 — executable trajectories → complex user intents.
- **Unlocking Implicit Experience** · ACL 2026 — mine implicit tool workflows from text.
- **Explorer** · ACL Findings 2025 — exploration-driven web trajectories.
- **OpenMobile** · 2026 — task+trajectory co-synthesis for mobile agents.
- **AgentTrek** · ICLR 2025 — web tutorials → replayable trajectories.
- **Scaling Synthetic Task Generation via Exploration** · 2025 — expand reachable states, then derive tasks.
- **WebExplorer** · 2025 — explore-and-evolve for long-horizon web agents. [arXiv:2509.06501](https://arxiv.org/abs/2509.06501)

**Structure-first**

- **APIGen-MT** · NeurIPS 2025 — verified blueprints before dialogue realization. [arXiv:2504.03601](https://arxiv.org/abs/2504.03601)
- **Magnet** · ACL 2025 — tool-graph → dialogue translation.
- **ToolFlow** · NAACL 2025 — tool-graph-guided coherent dialogues.
- **ToolACE-MT** · ICLR 2026 — non-autoregressive coarse-to-fine multi-turn generation.
- **Execution-First** · 2026 — execute tool traces first, then write tasks.
- **Plan-and-Act** · ICML 2025 — plan-first long-horizon planning.
- **TaskCraft** · 2025 — scalable agentic-task generation with tunable complexity. [arXiv:2506.10055](https://arxiv.org/abs/2506.10055)
- **Taskbench** · NeurIPS 2024 · **DeepPlanning** · ACL 2026 — verifiable long-horizon planning benchmark.

**Adaptive / self-evolving (cross-cutting)**

- **AFlow** · ICLR 2025 — searched agentic workflows. [arXiv:2410.10762](https://arxiv.org/abs/2410.10762)
- **Chain-of-Agents** · 2025 — distill multi-agent systems into one agent-foundation model.
- **AgentEvolver** · 2025 — self-questioning + experience-guided evolution.
- **WebEvolver** · EMNLP 2025 — self-improvement with a co-evolving world model.
- **SESA** · 2026 — self-play task posing + skill evolution.
- **Socratic-SWE** · 2026 — trace-derived skills for adaptive task generation.
- **AgentGen** · KDD 2025 — environment+task generation with bidirectional difficulty. [arXiv:2408.00764](https://arxiv.org/abs/2408.00764)
- **Tool-R0** · 2026 — zero-data self-evolving tool learning.
- **From Failure to Mastery** · 2026 — failure-driven hard-sample generation.
- **Recursive Synthesis** · 2026 — recursive composition of long-horizon terminal tasks.

### 6.4 Scaling Evidence

- **DIVE** · 2026 — tool-pool coverage → OOD generalization.
- **Beyond Quantity** · 2026 — diversity scaling > quantity scaling.
- **ScaleEnv** · 2026 — domain count → held-out generalization. [arXiv:2602.06820](https://arxiv.org/abs/2602.06820)
- **EnvFactory** · 2026 — few strongly-verified environments > masses of redundant ones. [arXiv:2605.18703](https://arxiv.org/abs/2605.18703)
- **Skywork-SWE** · 2025 — SWE data scaling laws.
- ACE's synthesis: the effective scaling variable is the *effective support* of the distribution (valid + learnable + non-redundant), not raw count; quantity scaling saturates as the learner grows.

## 7. Domain Environments & Benchmarks

Only *environmental* resources: interactive, stateful, executable. Static QA benchmarks are out of scope. (The lifecycle survey §4 carries exhaustive per-domain benchmark tables; here we keep the environment-defining works per domain.)

### 7.1 GUI / Web / OS

- **WebShop** · NeurIPS 2022 — [arXiv:2207.01206](https://arxiv.org/abs/2207.01206) · **Mind2Web** · NeurIPS 2023 — [arXiv:2306.04570](https://arxiv.org/abs/2306.04570) · **WebArena** · ICLR 2024 — [arXiv:2307.13854](https://arxiv.org/abs/2307.13854) · **VisualWebArena** · 2024 — [arXiv:2401.13649](https://arxiv.org/abs/2401.13649) · **WebVoyager** · 2024 · **WorkArena** · 2024.
- **OSWorld** · NeurIPS 2024 — [arXiv:2404.07972](https://arxiv.org/abs/2404.07972) · **WindowsAgentArena** · 2024 · **AgentStudio** · 2025 · **OSWorld-MCP** · 2025 — [arXiv:2510.24563](https://arxiv.org/abs/2510.24563).
- **AitW** · 2023 — [arXiv:2307.10088](https://arxiv.org/abs/2307.10088) · **Mobile-Env** · 2023 — [arXiv:2305.08144](https://arxiv.org/abs/2305.08144) · **AndroidWorld** · 2024 — [arXiv:2405.14573](https://arxiv.org/abs/2405.14573) · **AndroidControl** · 2024 · **Mobile-Bench** · 2024 · **MobileAgentBench** · 2024 — [arXiv:2406.08184](https://arxiv.org/abs/2406.08184) · **MobileWorld** · 2025 · **OpenCUA** · 2025 — [arXiv:2508.09123](https://arxiv.org/abs/2508.09123).

### 7.2 Tool / MCP

- **API-Bank** · 2023 · **ToolBench/ToolLLM** · ICLR 2024 · **BFCL** · ICML 2025 · **AppWorld** · ACL 2024 — [arXiv:2407.18901](https://arxiv.org/abs/2407.18901) · **ToolSandbox** · NAACL 2025 — stateful, conversational tool evaluation.
- **τ-bench** · 2024 — [arXiv:2406.12045](https://arxiv.org/abs/2406.12045) · **τ²-bench** · 2025 — dual-control environments — [arXiv:2506.07982](https://arxiv.org/abs/2506.07982) · **UserBench** · 2025 — [arXiv:2507.22034](https://arxiv.org/abs/2507.22034).
- **MCP-Universe** · 2025 — [arXiv:2508.14704](https://arxiv.org/abs/2508.14704) · **MCPVerse** · 2025 — [arXiv:2508.16260](https://arxiv.org/abs/2508.16260) · **MCP-Bench** · 2025 — [arXiv:2508.20453](https://arxiv.org/abs/2508.20453) · **MCPMark** · 2026 — deep-operation tasks on real protocol servers · **ComplexMCP** · 2026 — dynamic, interdependent tool sandbox · **M³-Bench** · 2026.

### 7.3 Coding / SWE / Terminal

- **SWE-bench** · ICLR 2024 — the canonical executable SWE benchmark; variants: SWE-bench Pro, Multi-SWE-bench, SWE-bench Multimodal, SWE-rebench. Training environments: §3.1.
- **InterCode** · 2023 — interactive terminal puzzles — [arXiv:2306.14898](https://arxiv.org/abs/2306.14898).
- **Terminal-Bench** · 2026 — [arXiv:2601.11868](https://arxiv.org/abs/2601.11868).
- **KernelBench** · 2025 — GPU-kernel synthesis with execution feedback — [arXiv:2502.10517](https://arxiv.org/abs/2502.10517).
- **NL2Repo-bench** · 2025 — repo-level code understanding · **SWT-Bench / FEA-Bench** · 2024-25 — agentic SWE task trajectories.

### 7.4 Deep Research (agentic only)

- **GAIA** · ICLR 2024 · **WebWalker** · ACL 2025 · **BrowseComp** · 2025 — [arXiv:2504.12516](https://arxiv.org/abs/2504.12516).
- **InfoDeepSeek** · 2025 — agentic information seeking — [arXiv:2505.15872](https://arxiv.org/abs/2505.15872).
- **DeepResearch Bench** · 2025 — [arXiv:2506.11763](https://arxiv.org/abs/2506.11763).
- **DeepDive** · 2025 — KG-random-walk synthesis with obfuscated key clues — [arXiv:2509.10446](https://arxiv.org/abs/2509.10446).

### 7.5 Embodied & Game

- Embodied: **ALFRED** · CVPR 2020 · **ALFWorld** · ICLR 2021 — [arXiv:2010.03768](https://arxiv.org/abs/2010.03768) · **TEACh** · AAAI 2022 · **Habitat** · ICCV 2019 · **RLBench** · RA-L 2020 · **BEHAVIOR** · 2021 · **RoboCasa** · RSS 2024 — [arXiv:2406.02523](https://arxiv.org/abs/2406.02523) · **EmbodiedBench** · ICML 2025.
- Game: **MineDojo** · NeurIPS 2022 · **SmartPlay** · 2024 — [arXiv:2310.01557](https://arxiv.org/abs/2310.01557) · **Baba Is AI** · 2024 — rule-rewriting puzzles — [arXiv:2407.13729](https://arxiv.org/abs/2407.13729) · **BALROG** · 2024 — [arXiv:2411.13543](https://arxiv.org/abs/2411.13543) · **AvalonBench** · 2023 — hidden-role social deduction — [arXiv:2310.05036](https://arxiv.org/abs/2310.05036) · **TextArena** · 2025 — [arXiv:2504.11442](https://arxiv.org/abs/2504.11442) · **LMRL Gym** · 2023 — [arXiv:2311.18232](https://arxiv.org/abs/2311.18232) · **GameArena** · 2024 — [arXiv:2412.06394](https://arxiv.org/abs/2412.06394) · **CivRealm** · 2024 · **Factorio Learning Environment** · 2025 — [arXiv:2503.09617](https://arxiv.org/abs/2503.09617).

### 7.6 Science / Medical / Finance

- **ScienceWorld** · 2022 · **DiscoveryWorld** · 2024 · **ScienceAgentBench** · 2024 · **MLE-bench** · ICLR 2025 · **MLE-Dojo** · 2025 · **PaperArena** · 2025.
- **MedAgentBench** · 2025 — [arXiv:2501.14654](https://arxiv.org/abs/2501.14654) · **MedAgentGym** · 2025 — trainable medical tool environments.
- **TravelPlanner** · 2024 · **CRMArena-Pro** · 2025 · **StockBench / FinDeepResearch** · 2025-26.

### 7.7 Multi-Agent Society

- **Generative Agents** · 2023 — 25 LLM agents in a simulated town — [arXiv:2304.03442](https://arxiv.org/abs/2304.03442).
- **SOTOPIA** · 2024 — social-intelligence environments — [arXiv:2310.11667](https://arxiv.org/abs/2310.11667) · **SOTOPIA-ToM** · 2025.
- **OASIS** · 2025 — open agent-society simulation at million scale — [arXiv:2411.11581](https://arxiv.org/abs/2411.11581).
- **Melting Pot** · 2021 — multi-agent evaluation substrates · **Concordia** · 2023 — social-simulation GM + agents · **AgentScope** · 2024 — [arXiv:2402.14034](https://arxiv.org/abs/2402.14034).

### 7.8 Cross-Domain Gyms

- **OpenAI Gym** · 2016 — the ancestral API.
- **AgentBench** · 2023 · **AgentBoard** · 2024 · **AgentGym** · 2024 — 14 environments, unified training — [arXiv:2406.04151](https://arxiv.org/abs/2406.04151) · **GEM** · 2025 — a gym for agentic LMs — [arXiv:2510.01051](https://arxiv.org/abs/2510.01051) · **AgencyBench** · 2025 · **lmgame-Bench** · 2025 — games wrapped in a Gymnasium API — [arXiv:2505.15146](https://arxiv.org/abs/2505.15146).

## 8. Infrastructure & Environment-as-a-Service

Agent-specific infrastructure only.

### 8.1 Sandboxes & Runtimes

- **E2B** — code sandboxes for AI agents. · **Modal** — cloud sandboxes/GPUs popular for agent rollouts. · Agent-oriented microVM stacks (Firecracker-class isolation for parallel environment rollouts).

### 8.2 Protocols & Platforms

- **Model Context Protocol (MCP)** — the de-facto tool/environment interface standard. [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **ARE** · 2025 — heterogeneous environment construction/orchestration platform. [arXiv:2509.17158](https://arxiv.org/abs/2509.17158)
- **GEM** · 2025 — "a gym for agentic LMs". [arXiv:2510.01051](https://arxiv.org/abs/2510.01051)
- **SpeechGym** · 2026 — audio-native gym for training voice agents via RL. [arXiv:2608.26432](https://arxiv.org/abs/2608.26432)
- **AgentGym** · 2024 — 14 environments, unified training. [arXiv:2406.04151](https://arxiv.org/abs/2406.04151)
- **TextArena** · 2025 — unified competitive text-game arena. [arXiv:2504.11442](https://arxiv.org/abs/2504.11442)

### 8.3 Environment-as-a-Service (EaaS)

Vision (lifecycle survey §8.1): unified API + cloud hosting decoupling agent development from environment deployment — live environments served on demand instead of shipped as containers. Early instances: managed agent runtime offerings from major cloud/LLM vendors.

## 9. Training with Evolving Environments

How environments are consumed; only entries tightly coupled to the environment loop.

### 9.1 Agentic RL

Search & tool-integrated RL:

- **Search-R1** · 2025 — search-integrated RL. [arXiv:2503.09516](https://arxiv.org/abs/2503.09516) · **ReSearch** · 2025 — [arXiv:2503.19470](https://arxiv.org/abs/2503.19470) · **DeepRetrieval** · 2025 — [arXiv:2503.00223](https://arxiv.org/abs/2503.00223) · **MaskSearch** · 2025 — answer-masked multi-agent RL. [arXiv:2505.20285](https://arxiv.org/abs/2505.20285)
- **ZeroSearch** · 2025 — an LLM simulates the search engine during RL. [arXiv:2505.04588](https://arxiv.org/abs/2505.04588)
- **WebSailor** · 2025 — uncertainty-driven web-agent RL. [arXiv:2507.02592](https://arxiv.org/abs/2507.02592)

Computer-use & GUI RL:

- **ComputerRL** · 2025 — alternating RL/SFT against entropy collapse. [arXiv:2508.14040](https://arxiv.org/abs/2508.14040) · **WebRL** · ICLR 2025 — self-evolving online curricula · **UI-S1** · 2025 — semi-online RL.

Credit assignment, sampling, and stability:

- **GiGPO** · 2025 — anchor-state grouped step-level credit assignment. [arXiv:2505.10978](https://arxiv.org/abs/2505.10978) · **ARPO** · 2025 — tool-integrated exploration. [arXiv:2507.19849](https://arxiv.org/abs/2507.19849) · **RAGEN** · 2025 — reward-variance-aware multi-turn RL. [arXiv:2504.20073](https://arxiv.org/abs/2504.20073) · **AgentRL** · 2025 — cross-policy sampling. [arXiv:2510.04206](https://arxiv.org/abs/2510.04206) · **VAGEN** · 2025 — world-model rewards + bi-level GAE. [arXiv:2510.16907](https://arxiv.org/abs/2510.16907) · **AEPO** · 2025 — entropy-balanced agentic optimization. [arXiv:2510.14545](https://arxiv.org/abs/2510.14545) · **AgentFold** · 2025 — folding stale context for long-horizon RL. [arXiv:2510.24699](https://arxiv.org/abs/2510.24699)

### 9.2 Agentic SFT / Trajectory Synthesis

- **Agent-FLAN** · 2024 — ReAct-style data restructured into multi-turn format · **AgentTuning** · 2023 — the founding agent-SFT mixture · **Aguvis** · ICML 2025 — automatic program generation + reasoning-trace augmentation · **UI-TARS** · 2025 — iterative collection + reflection · **APIGen-MT** · NeurIPS 2025 — [arXiv:2504.03601](https://arxiv.org/abs/2504.03601) · **Lingma SWE-GPT** · 2024 — three-stage SWE workflow trajectories. [arXiv:2411.00622](https://arxiv.org/abs/2411.00622)
- Trajectory refinement: **ETO** · 2024 — trajectory-collection-then-train loop. [arXiv:2403.02502](https://arxiv.org/abs/2403.02502) · **GUI-Reflection** · 2025 — first-error localization + retrospective correction · **TopoCurate** · 2026 — interaction-topology-based curation.

### 9.3 Offline–Online Unification

- **On-Policy Distillation** · Thinking Machines, 2025 — an early bridge; multi-turn open problems remain (early errors change state → teacher supervision inconsistency).

## 10. Open Problems & Science of Environments

From the lifecycle survey (§8) and Environment Scaling survey future-work; a research agenda rather than a paper list.

- **Environment scaling laws** — how do environment count / diversity / horizon / complexity quantitatively drive capability and generalization?
- **Environment learnability** — which environments produce stable learning signals (sparse rewards, huge state spaces, long horizons all fail)?
- **Environment–capability mapping** — which environments cultivate which meta-capabilities (memory, decomposition, world modeling, strategic planning)?
- **Closing the sim-to-real gap** — correctness, difficulty, diversity, and fidelity gaps between synthetic and real environments.
- **Generator–verifier asymmetry** — hard-to-verify domains are the biggest opportunity; can strong generators bootstrap verifiers?
- **Multi-agent environments** — non-stationarity, credit assignment, emergent behavior.
- **Long-horizon, open-ended, omni-modal environments**; **asynchronous** (non-ReAct-static) interaction.
- **EaaS standardization** — unified observation/action/reward interfaces; reproducible deployment.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for scope rules, entry format, and PR guidelines.

## Acknowledgments

This list's taxonomy is built on three surveys — [*Agentic Environment Engineering*](https://arxiv.org/abs/2606.12191), [*Environment Scaling*](https://arxiv.org/abs/2511.09586), and the [*ACE Lens on agentic data*](https://arxiv.org/abs/2608.27260) — and complements [Awesome-Environment-Scaling](https://github.com/lukahhcm/Awesome_Scaling_Environments) (GEF-loop paper list) and [Awesome-Agent-Environments](https://github.com/ZackZikaiXiao/Awesome-Agent-Environments) (benchmark & infrastructure list).

## License

[MIT](LICENSE)
