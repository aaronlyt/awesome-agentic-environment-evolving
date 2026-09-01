# awesome-agentic-environment-evolving 调研提案

> 调研时间：2026-09-01
> 状态：提案（待评审），仓库尚未初始化
> 源综述：① Agentic Environment Engineering for LLMs（人大/中科院，582 refs）② What Makes Good Agentic Data: An ACE Lens（arXiv 2608.27260，华为/上交）③ Environment Scaling for Interactive Agentic Experience Collection（arXiv 2511.09586，HKUST/阿里，NeurIPS'25 SEA Workshop）

---

## 1. 背景与动机

三篇综述从不同角度论证了同一件事：**环境正在从"评测容器"变成"经验数据的生产者和一等公民"**，且这个方向 2025-2026 年处于爆发期。

| 综述 | 核心框架 | 对本列表的最大贡献 |
|---|---|---|
| Agentic Environment Engineering（环境工程综述） | 环境生命周期：建模(8属性对)→领域(8域)→合成(符号3路线/神经3层级)→质量(4维)→智能体演化(4路径)→**环境演化(3范式)**→未来(EaaS/scaling laws) | **分类学骨架**：最完整、582 篇参考文献即条目池 |
| ACE Lens（好数据三要素） | 数据对象 d=(E,q,τ,v)；环境参数化 e=(D,F,P_rule,Ω,v)；Accuracy(准入)-Complexity(校准)-divErsity(覆盖)；正向/逆向生成范式 | **质量与验证维度** + **数据生成范式章节** + **环境形式化分解**（注意：ACE 不使用"environment as data"表述，见 §4.6 归属备注） |
| Environment Scaling（环境扩展综述） | GEF 循环（Generation-Execution-Feedback）；生成-验证不对称 | **演化机制的阶段切分**（任务生成/执行/反馈三阶段的扩展轴） |

三者互补：环境工程综述给"环境的完整生命周期"，ACE 给"数据质量的三维目标"，GEF 给"训练管线视角的扩展轴"。本列表以**演化（evolving）为主线**融合三者——这正是每篇综述各自的核心但没有任何现有 awesome 列表覆盖的角度。

## 2. 竞品分析

### 2.1 现有列表格局

| 列表 | Stars | 组织轴 | 条目数 | 主要盲区 |
|---|---|---|---|---|
| [Awesome-Environment-Scaling](https://github.com/lukahhcm/Awesome_Scaling_Environments)（2511.09586 官方配套） | 73 | GEF 三阶段（生成/执行/反馈） | ~110，纯论文 | 无基础设施、无代码资源、无质量度量专题、无按域索引 |
| [Awesome-Agent-Environments](https://github.com/ZackZikaiXiao/Awesome-Agent-Environments) | 18 | 三层（任务层基准/构造层生成/执行层沙箱） | ~125-130 | 生成与演化仅一节；无具身/游戏域；无奖励与验证专题 |
| [Awesome-Self-Evolving-Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) | — | 以 agent 为中心的自我进化 | — | 环境只是其中一小节 |
| Awesome-Long-Horizon-Agents（RUC-NLPIR）等 | — | 长程任务 | — | 交叉引用少量环境扩展论文 |

### 2.2 空隙（本列表的立足点）

1. **没有列表以"环境演化机制"为主分类轴**：课程/自博弈/规模扩展/agent-环境共进化/世界模型共演化分散在各列表的角落，而这恰是三篇综述共同的 climax（环境工程综述 Sec 7 专章"环境演化"）。
2. **没有列表做"环境质量控制"专题**：正确性/复杂度校准/多样性度量/保真度（ACE 三维 + 环境工程综述 5.3），竞品全部缺失——而这恰是从"堆环境"到"好环境"的关键，2026 年论文已在集中回答。
3. **没有列表把基础设施与"环境即数据"连接起来**：沙箱/运行时/编排/EaaS 与环境合成、scaling laws 属于同一生命周期的上下游，但散落在不同列表。
4. **时机**：概念命名刚爆发（environment scaling / env-as-data / agentic environment engineering / era of experience），NeurIPS'25 已有 SEA Workshop，社区需要统一地图；竞品 star 都不高（<100），先发优势窗口存在。

### 2.3 可行性结论

**可行，时机好。**

- 内容供给：三篇综述合计可提取 **500+ 不重复条目**（环境工程综述 582 refs；ACE 三张大表全部标注开源链接；GEF 列表 110 条），本地已精读 6 篇代表作（RLVE、AgentScaler、Agent World Model、EnvHarness、EvoEnv 等）+ 2026 Top-15 追踪清单。
- 持续供给：2026 年 1-8 月每月新增 2-5 篇环境合成/演化论文（见本地 env-as-data-2026-papers.md），方向不会枯竭。
- 制作经验：已有 awesome-agent-trace-and-evidence-attribution 制作经验与论文库工作流。

**风险与对策**

| 风险 | 对策 |
|---|---|
| 与竞品条目大量重叠 | 靠分类学差异（演化轴）+ 条目元数据（见 §5）取胜，重叠不回避，重叠条目按我们的轴重新归位 |
| 维护成本（月增 2-5 篇） | GitHub Action 定期抓 arXiv 关键词（environment scaling / agent environment / world model + RL）生成候选清单，人工归档 |
| 范围过大（具身/游戏世界模型极易失控） | MVP 阶段以数字智能体环境为主，具身/游戏只收录"与 LLM agent 训练相关"的条目并设独立小节，明确收录边界写进 CONTRIBUTING |
| 命名 | `awesome-agentic-environment-evolving` 语法上略怪但"evolving"正是差异点；可接受；备选 awesome-agent-environment-evolution / awesome-env-as-data（后者概念最准但 SEO 弱）。建议保留现名，README 首句即定义 "agentic environment evolving = 合成、演化、验证与服务化 agent 环境" |

## 3. 定位与侧重点

**一句话定位**：以**环境为中心的演化生命周期**为主线的资源列表——环境如何被**合成**、如何随智能体**演化**、如何被**质量管控**、如何作为**数据/服务被消费**。

**三个差异点**（相对所有竞品）：

1. **演化机制为一级目录**：难度驱动（课程）、神经驱动（自博弈/世界模型）、规模驱动、agent-环境共进化、存量环境再激活——五个机制子类是本列表的核心章节，竞品最多各有一节。
2. **ACE 元数据贯穿所有条目**：每个条目标注它生产什么（环境 E / 任务 q / 轨迹 τ / 验证器 v）、验证方式（可执行/单测/金轨迹/rubric/LLM-judge）、难度是否模型相对校准、多样性度量——把"好数据三要素"从论文变成可检索的列表维度。
3. **基础设施与科学问题并重**：沙箱/运行时/编排/协议（MCP）/EaaS 收进来，同时收录 environment scaling laws、可学习性、环境-能力映射等开放问题——分别对应"让环境跑起来"和"让环境科学化"两端。

**目标读者**：做 agentic RL、训练环境构建、智能体数据合成的研究者与工程师。

**语言**：英文为主（面向国际社区 + star 增长），README 可附中文导读（结合现有公众号渠道）。

## 4. 分类体系提案（主目录）

设计原则：以环境工程综述的生命周期为骨架，嵌入 ACE 的质量维度与 GEF 的管线视角。★ 标注核心差异章节。

```
awesome-agentic-environment-evolving

1. Surveys & Position Papers                        # 三篇核心综述 + 宣言类
   ├─ Surveys: 环境工程综述 / Environment Scaling(2511.09586) / ACE(2608.27260) / Self-Evolving Agents
   └─ Position: Era of Experience(Silver&Sutton) / AgentScaler / Scalable Environments Drive
      Generalizable Agents(2605.18181) / 从数据工程到环境工程

2. Formalization & Environment Attributes          # 轻量章：两个互补切法
   ├─ POMDP 交互形式化（环境工程综述 Sec 2.1 与 ACE Sec 2.1 共用）
   ├─ 环境内部分解（ACE §2.2）: e = (D 状态载体, F 工具动作集, P_rule 规则权限, Ω 观测接口,
   │   v 成功接口)；关键谱系论断：E 从"静态接口规范"到"完整可执行交互基底"
   └─ 环境间差异维度（环境工程综述 Sec 3，8 属性对）: 符号vs神经 · 开环vs闭环 · 在线vs离线 ·
       MDP vs POMDP · 确定vs非确定 · 离散vs连续 · 单vs多模态 · 单vs多智能体

3. Environment Synthesis（环境怎么来）
   # 双标签组织：环境工程综述的"合成路线"（用什么真实材料启动）× ACE 的"E 来源"
   # （产物 E 的性质：真实精选 / LLM 合成规范 / 程序化可执行）——两个正交切法。
   # 注意区分：ACE 的 "LLM-Synthesized" 指 LLM 生成符号工具规范（产物仍是符号）；
   # 环境工程综述的 "Neural" 指转移函数由神经网络参数化（世界模型）。术语易混，README 需澄清。
   3.1 Symbolic / Programmatic（符号合成）
       ├─ Task-driven（真实资产封装）: SWE-Gym, R2E-Gym, SWE-smith, SWE-rebench, MEnvAgent,
       │   DockSmith, Scale-SWE, SWE-Hub, AgentFounder, MedAgentGym, SCALER
       ├─ Real-world-driven（真实世界投影）: AgentSynth, TaskCraft, OS-Genesis, VeriEnv,
       │   AutoWebWorld, MCPMark, InfiniteWeb, V-GameGym, EmbodiedBench
       └─ De Novo（从零合成）: AutoForge, ScaleEnv, Agent World Model, LOGIGEN, AutoEnv,
           SWE-Playground, Endless Terminals, gg-bench, RandomWorld, daVinci-Env(45k Docker),
           Agent-World, EnvFactory, EnvScaler
   3.2 Neural / World-Model-as-Environment（神经合成）
       ├─ Pixel-level: DreamGen, GameNGen, DIAMOND, Matrix-Game, NeuralOS, DreamZero
       ├─ Token-level: WebDreamer, WebWorld, Code2World, MobileDreamer, UI-Simulator, gWorld
       └─ Latent-level: V-JEPA 2, DINO-WM, AdaWorld, IWM
   3.3 Compositional Synthesis（组合合成）: RACES(递归组合), BUTTON, TaskCraft, Skill-Graph 系
   3.4 Harnessing Static Environments（存量环境再激活）★: EnvHarness, Environment Tuning, CLI-Gym(环境反转)

4. Environment Evolution Mechanisms ★★（核心差异章：环境怎么进化）
   4.1 Difficulty-driven（难度/课程驱动）
       RLVE, GenEnv, SCALER, EnvGen, Eurekaverse, DreamGym, AgentFrontier(ZPD),
       EvoEnv, Reasoning Core, WebRL, UED 经典系(PAIRED/ACCEL/MAESTRO/ReMiDi), CuES
   4.2 Neural-driven（神经驱动：自博弈与世界模型共演化）
       Absolute Zero, R-Zero, Self-Challenging, Vision-zero, SSR/SWE-RL(注入-修复),
       WebEvolver, Agent2World, Active Zero, Simia
   4.3 Scaling-driven（规模驱动）
       ├─ Scenario-level: AgentScaler, EnvScaler, AutoForge, InfiniteWeb, FTRL, WebWorld
       └─ Environment-level: ARE, AutoEnv, Agent World Model, Agent-World, ScaleEnv, EnvFactory
   4.4 Agent-Environment Co-evolution（共进化）
       GenEnv, EvoEnv(单策略双角色), Agent-World, Socratic-Zero, From Trainee to Trainer,
       Tool-R0, AgentEvolver, Breaking the Solver Bottleneck
   4.5 Generator-Verifier Co-evolution（生成-验证器共进化）
       Rubrics as Rewards, DR Tulu, Writing-zero, CoPER, URPO, Generative Verifiers,
       EigenData(逐实例可执行 checker)

5. Quality, Verification & Reward ★（竞品空白：什么是好环境/好数据）
   5.1 Correctness: 执行与单测, 金轨迹比对, 验证器自身可靠性(MCP-Universe 动静态评估器)
   5.2 Complexity & Learnability: 模型相对难度校准, 可学习带, 失败驱动筛选
   5.3 Diversity Measurement: 行为覆盖/归一化熵, Vendi Score, 嵌入去重, ACE 条件化覆盖
   5.4 Fidelity: Web Turing Score, FVD/LPIPS, 物理合理性, sim-to-real 四差距
   5.6 Reward Design for Environments: RLVR, rubric, PRM(WebShepherd), reward hacking 防御(MONA)

6. Agentic Data Generation（数据生成范式与质量目标）★
   6.1 命题引子: "环境取代数据的角色"——出自环境工程综述 Sec 2.2（From Data Engineering to
       Environment Engineering）与环境扩展综述（环境=经验数据的生产者）。
       ⚠ 归属备注：ACE 论文不使用 "environment as data" 表述；其立场是环境仅为数据对象
       d=(E,q,τ,v) 的四因子之一。"环境即数据"作为仓库世界观应放 README 引言并引用上述两篇，
       不可归于 ACE。
   6.2 ACE 质量目标: Accuracy(准入条件)-Complexity(模型相对校准)-divErsity(行为覆盖)；
       生成范式（如何构造）≠ 数据目标（如何选择/接纳）——ACE 刻意分离的两个问题
   6.3 Forward Generation(E→q→τ, ACE §3.2, 按 E 来源三分): Real/Curated(ToolLLM, TOUCAN,
       APIGen, SWE-Gym), LLM-Synthesized(ToolACE, ToolAlpaca), Programmatic/Executable
       (EnvScaler, Agent-World, EnvFactory, ScaleEnv)
   6.4 Reverse Generation(ACE §3.3): Task-first(AgentInstruct, BUTTON, Agentic Proposing),
       Trajectory-first(OS-Genesis, Trajectory2Task, Learn-by-interact, WebExplorer),
       Structure-first(APIGen-MT, Magnet, ToolFlow, ToolACE-MT),
       Adaptive/Self-evolving 横切(AFlow, SESA, Socratic-SWE, From Failure to Mastery)
   6.5 Scaling Evidence（环境扩展的实证与 scaling laws）: DIVE, Beyond Quantity, Skywork-SWE,
       ScaleEnv(域数→泛化), EnvFactory(少量强验证>海量冗余)

7. Domain Environments & Benchmarks（按域的现成环境，紧凑收录）
   GUI/Web/OS · Deep Research · Tool & MCP · Coding/SWE · Terminal · Embodied & Game ·
   Science/Medical/Finance · Multi-agent Society（Generative Agents, OASIS, SOTOPIA, τ²-bench）
   ——每域只收"被用于训练/演化"的环境型基准，纯评测基准克制收录，避免与
   Awesome-Agent-Environments 重复造表

8. Infrastructure（基础设施：让环境跑起来）
   ├─ Sandboxes & Runtime: E2B, Firecracker, gVisor, Kata, WASI, Modal, Docker 系
   ├─ Orchestration & Protocols: MCP, Kubernetes 系, 环境编排
   ├─ Environment Platforms: ARE, GEM, AgentGym, AgentGym-RL, TextArena, OpenAI Gym 系
   └─ Environment-as-a-Service (EaaS) ★: 论文愿景 + 现有云服务(Claude Managed Agents 等)

9. Training with Evolving Environments（训练栈：环境怎么被消费）
   ├─ Agentic RL: Search-R1, WebSailor, ComputerRL, GiGPO, ARPO, DAPO/GRPO 要点文
   ├─ Agentic SFT / Trajectory Synthesis: Agent-FLAN, AgentTuning, UI-TARS, APIGen-MT
   └─ Offline-Online Unification: On-Policy Distillation, EvolveSearch

10. Open Problems & Science ★
    environment scaling laws · 环境可学习性 · 环境-能力映射 · 多智能体环境 ·
    长程/开放式/全模态环境 · sim-to-real · 验证器-生成者不对称 · 离线-在线统一
```

### 分类来源对照（设计依据）

| 章节 | 主要依据 |
|---|---|
| 2 | 环境工程综述 Sec 3（环境间 8 属性对）+ ACE §2.2（环境内分解 e=(D,F,P_rule,Ω,v) 与"静态规范→可执行基底"谱系），两种切法互补 |
| 3.1 三路线 / 3.2 三层级 | 环境工程综述 Sec 5.1 / 5.2（合成路线轴）× ACE §3.2（E 来源轴：real/curated · LLM-synthesized · programmatic），双标签正交标注 |
| 3.3 / 3.4 | RACES 论文（2026 Top-15 #10）/ EnvHarness（2026 Top-15 #13，"存量再利用"独立角度） |
| 4.1-4.3 | 环境工程综述 Sec 7 三范式的直接采用 |
| 4.4 | 环境工程综述 Sec 8.6 + ACE 自演化横切类 |
| 4.5 | Environment Scaling 综述反馈章 + 生成-验证不对称论断 |
| 5 | 环境工程综述 Sec 5.3 四维 + ACE 三维的合并 |
| 6 | 6.1 命题出自环境工程综述 Sec 2.2 + 环境扩展综述（ACE 无此表述）；6.2-6.4 出自 ACE §3-§4 的质量目标与正向/逆向生成范式；6.5 来自 2026 实证论文群 |
| 7 | 环境工程综述 Sec 4 八域压缩 |
| 8 | Awesome-Agent-Environments 执行层 + 环境工程综述 Sec 8.1 EaaS |
| 9 | 环境工程综述 Sec 6 压缩（只保留"与环境耦合"的要点） |
| 10 | 环境工程综述 Sec 8 + Environment Scaling 未来方向 |

## 5. 条目格式提案

比竞品多做一层元数据（这是可检索性的来源，也是工作量大头，建议 MVP 就带上）：

```markdown
- **AgentScaler** — Towards General Agentic Intelligence via Environment Scaling
  ![ICLR 2026](badge) | Synthesis: symbolic / scenario-scaling | Evolution: scaling-driven |
  Produces: E+q | Verify: executable | Code: [GitHub](...) | [arXiv:2509.13311](...)
```

字段：录用/年份徽章、合成范式、演化机制（多选）、产出物（E/q/τ/v）、验证方式、开源链接。可用脚本从本地论文库自动生成初稿。

## 6. 落地计划

- **Phase 1（MVP，先跑通）**：README 骨架 + 第 1/3/4 章先填满（差异化最強），条目 ~150；三篇综述的表全部转入。
- **Phase 2**：补 5/6/7 章（质量/数据/领域），条目 ~300；加 awesome 徽章与自动 arXiv 追踪 Action。
- **Phase 3**：8/9/10 章 + 中文导读 + 与公众号联动；考虑每半年 release 一版 changelog。

## 7. 范围决策（已拍板，2026-09-01）

1. **具身/游戏世界模型**：只收"用于 LLM/VLA agent 训练"的；纯视频生成、游戏重建类不收。
2. **评测基准门槛**：训练型环境全收；评测型只收"环境性强的"（可交互、有状态、可执行）；静态 QA 类基准不收。
3. **基础设施深度**：只列 agent 场景专用（E2B、Modal、面向 agent 的 microVM 等）；通用云原生设施（Docker/K8s 全家桶）不收。
4. **仓库语言**：英文 README 为主 + `README.zh-CN.md` 精简镜像。
5. **papers 库引用**：不同步建（本地精读笔记不进仓库）。

---

## 附记：结构演进（2026-09-01 v2）

初版十章中的 §3（环境合成，AEE 的"构造轴"）与 §6（Agentic Data Generation，ACE 的"正向/逆向生成轴"）存在结构性重复——同一批论文（EnvScaler、Agent World Model、TaskCraft、OS-Genesis 等）在两章各出现一次。v2 合并为单一章 **§3 Environment & Data Synthesis**，按 ACE 的"锚点"概念组织：

- **E 锚定**（正向 E→q→τ）：§3.1 四组（任务驱动/真实世界驱动/从零/免环境模拟器），`route:`×`E:` 双标签正交标注；§3.2 神经合成；§3.3 组合；§3.4 存量再利用
- **逆向锚定**（任务/轨迹/结构优先）：§3.5
- **自适应生成**：§3.6（与 §4 演化机制以交叉引用衔接）

由此：ACE 质量目标（原 6.1）归入 §5（质量章引言），scaling 实证（原 6.4）归入 §9.1（与新 §9"Scaling Evidence & Open Problems"合并）。全列表从十章缩为九章（领域环境→§6、基础设施→§7、训练栈→§8）。

---

## 附记：事实核查 pass（2026-09-01 v2.1）

用三个只读 subagent 分别把 README 全部 `src:` 标注（324 行表格、~250 个带来源标注的条目）逐条对回三篇源综述原文，发现并修复 40 处偏差：

- **章节/表引用错位（17 处）**：多数是把同一篇论文放进了综述的另一节（如 Agent2World 实为 AEE §5.1.1 任务驱动表、UI-Simulator 实为 §7.1.2 神经演化、AgentFrontier 实为 §6.3.3 轨迹精炼、ScienceWorld 实为 §4.3 具身域表）；ACE 侧 8 个 `ACE-T1/T2` 实际只出现在正文而非表中（CodeGym、ToolVerse、ASTRA、AgentTrek、Plan-and-Act、Taskbench、Tool-R0×2），降为裸 `src:ACE`。
- **虚构来源（3 处）**：SOTOPIA/Melting Pot 的 AEE 标注、Generative Agents 的 ACE-T3、TopoCurate 的 ACE 均不在对应综述中——已改为真实出处（TopoCurate 实为 AEE §6.3.3）。
- **route 标签与综述自身分类冲突（4 处）**：V-GameGym、EnvScaler、InfiniteWeb、SWE-Universe 的 route 改回 AEE 表格的原始归类。
- **结构归属修正（图例）**：`evolution:` 五值中只有 difficulty/neural/scaling 出自 AEE §7，co-evolve 是 §8.6，verifier 来自 ES——图例已逐值标注；并注明无 `src:` 章节号的行为编辑性分类。
- **ES 归属收紧**：§9.2 开放方向中 EaaS/learnability 并非 ES future-work 原文，归属句改为"AEE §8 + ES §5.2–§6/App. A + 本地策展"；§4.5 引用改为 ES §5.2 & App. A.2；§9.1 补 ES App. B Table 2 的实证数据（SWE-Gym 2,438→20.6 / R2E-Gym 8,135→34.4 / SWE-Smith 50,137→40.2）。
- **小的表述精度**：ACE 的 e=(D,v) 均为 optional；难度公式 C_z 无误；多样性条件化是 Eq. 12（coverage/entropy 是 Eq. 13）；OTC=Optimal Tool Calls；AndroidWorld 116 tasks；API-Bank 73 APIs/314 tasks；Matrix-Game 的"minute-level"属 2.0 代；Simia 与 Simulating Environments with Reasoning Models 为同工双列，已互注。
- **意外收获**：AgentEvolver 的真实 arXiv ID（2511.10395）从 AEE 参考文献补入。

未发现公式、符号或章节级的结构性错误——ACE 的 e/d 形式化、三分类、五范式，AEE 的三路线×质量四维，ES 的 GEF 循环与生成-验证不对称均与原文一致。
