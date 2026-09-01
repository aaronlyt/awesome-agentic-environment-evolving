# Awesome Agentic Environment Evolving（中文导读）

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 本文件是 [English README](README.md) 的精简中文导读；完整条目（arXiv 链接、逐条说明）以英文版为准。

**主线：让环境成为 LLM 智能体的一等公民，并且是会演化的** —— 收录环境如何被**合成**、如何随智能体**演化**、质量如何被**验证**、以及如何作为**数据/服务**被消费。

## 核心命题

环境正在从"评测容器"变成"经验数据的生产者"：静态数据集让模型被动接收固定难度的轨迹，而环境让每一步动作都改变状态、任务分布可以随学习者共同演化（《Agentic Environment Engineering》§2.2 "From Data Engineering to Environment Engineering"、《Environment Scaling》）。本列表以**环境演化机制**为脊柱组织该领域 —— 这是现有列表均未作为主轴的维度。

## 收录边界

- ✅ 收：环境合成（程序化/世界模型/组合式）、环境演化（课程/自博弈/规模/共进化）、质量控制（正确性/复杂度/多样性/保真度/奖励）、agentic 数据生成范式、训练型环境与"环境性强"的基准（可交互、有状态、可执行）、agent 专用基础设施（沙箱/平台/协议/EaaS）。
- ❌ 不收：与 LLM/VLA agent 训练无关的纯视频生成、游戏重建世界模型；静态 QA 型基准；通用云原生设施。

## 十章结构

| 章 | 内容 | 代表工作 |
|---|---|---|
| 1. 综述与立场 | 三篇核心综述 + 宣言 | 环境工程综述 (2606.12191) · Environment Scaling (2511.09586) · ACE (2608.27260) · Era of Experience · AgentScaler |
| 2. 形式化与属性 | POMDP 形式化；环境**内部分解** e=(D,F,P_rule,Ω,v)（ACE）；环境**间差异** 8 属性对（环境工程综述） | — |
| 3. 环境合成 | 符号合成三路线（任务驱动/真实世界驱动/从零）· 神经合成三层级（像素/词/潜空间）· 组合合成 · **存量环境再激活** | SWE-Gym · Agent World Model · ScaleEnv · EnvFactory · WebWorld · EnvHarness |
| 4. 环境演化机制 ★ | 难度驱动（课程）· 神经驱动（自博弈/世界模型）· 规模驱动 · agent-环境共进化 · 生成-验证器共进化 | RLVE · Absolute Zero · AgentScaler · ARE · GenEnv · EvoEnv · Rubrics as Rewards |
| 5. 质量/验证/奖励 | 正确性 · 复杂度与可学习性 · 多样性度量 · 保真度 · 奖励设计 | MCP-Universe · Vendi Score · Web Turing Score |
| 6. Agentic 数据生成 | ACE 质量目标；正向生成（E→q→τ，按 E 来源三分）；逆向生成（任务/轨迹/结构优先 + 自演化横切）；scaling 实证 | ToolLLM · APIGen · ToolACE · OS-Genesis · APIGen-MT |
| 7. 领域环境 | GUI/Web · Tool/MCP · SWE/Terminal · Deep Research · 具身/游戏 · 多智能体社会 | WebArena · OSWorld · τ²-bench · TextArena |
| 8. 基础设施 | 沙箱/运行时 · 协议与平台（MCP、ARE、GEM）· EaaS 愿景 | E2B · Modal · MCP |
| 9. 训练栈 | Agentic RL · 轨迹合成 SFT · 离线-在线统一 | Search-R1 · WebSailor · ComputerRL · On-Policy Distillation |
| 10. 开放问题 | environment scaling laws · 可学习性 · 环境-能力映射 · sim-to-real · 生成-验证不对称 · 多智能体环境 · EaaS 标准化 | — |

## 术语提醒

- ACE 的 **"LLM-Synthesized Environment"** 指 LLM 生成*符号*工具规范（产物仍是符号的）；环境工程综述的 **"Neural 合成"** 指转移函数由神经网络参数化（世界模型）。二者不是一个概念。
- "Environment as Data / 环境取代数据"的命题出自环境工程综述与环境扩展综述；ACE 论文不使用该表述，其立场是环境为数据对象 d=(E,q,τ,v) 的四因子之一。

## 贡献

收录规则与条目格式见 [CONTRIBUTING.md](CONTRIBUTING.md)。
