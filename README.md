# 🏭 BP-Factory

> **AI-Powered Business Plan Foundry — 为腾讯 WorkBuddy 量身锻造的智能 BP 流水线。**
>
> 从原始数据到投资人-ready 的专业商业计划书，一行命令，全自动流水线。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![WorkBuddy](https://img.shields.io/badge/Tencent-WorkBuddy-blueviolet.svg)](https://workbuddy.qq.com)
[![Skills](https://img.shields.io/badge/Skills-13-orange.svg)](#-技能全景图)

---

## 💡 为什么叫 BP-Factory？

**BP** = Business Plan，商业计划书。**Factory** = 工厂、流水线。

就像现代化工厂将原材料加工为成品，BP-Factory 通过 **6 人专家团队并行协作 + 3 级代码强制检查点 + 13 个技能无缝编排**，将原始想法和数据"生产"为经得起投资人审视的专业商业计划书。

不是模板填充，不是 AI 随机输出 —— 是 **标准化的智能生产线**。

---

## 🔥 核心亮点

### 代码强制，不是纸上谈兵

```
❌ 传统方案：SKILL.md 里写"请确保字数达标" → AI 可能忽略
✅ BP-Factory：master_check.py 代码强制校验 → 不达标就拒绝输出
```

**约束流程，不约束内容。** Harness 管"怎么做"的合规性，AI 自主决定"写什么"。

### 6 人专家团队并行协作

| 角色 | 职责 |
|------|------|
| 🦅 **Claw（项目总监）** | 数据收集、清洗、流程编排、最终交付 |
| 🔬 **行业研究员** | 行业趋势分析、竞争格局、市场规模测算 |
| 💰 **财务分析师** | 三大报表分析、DCF 估值、盈利预测 |
| 🎯 **战略分析师** | SWOT 分析、商业模式画布、投资建议 |
| 🛡️ **流程监管专家** | Harness 检查点触发、全流程合规监督 |
| ✅ **质量审核官** | 4 层质量关口检查、一票否决权 |

### 3 级强制检查点

| 检查点 | 时机 | 校验内容 | 失败后果 |
|--------|------|---------|---------|
| 🔒 **pre-flight** | Agent 启动前 | Agent 配额 = 6、项目目录初始化 | 流程硬性停止 |
| 🔒 **pre-merge** | 章节合并前 | 章节去重（>75% 相似度拦截）、8 章完整性 | 打回重写 |
| 🔒 **pre-deliver** | 最终交付前 | 字数实测（≥20000）、图表存在性验证、10 项技能调用完整性 | 拒绝输出 |

---

## 📦 技能全景图（13 个技能）

### 🏗️ 第一层：核心引擎（3 个）

| 技能 | 版本 | 能力 |
|------|------|------|
| **[business-plan-creator](skills/business-plan-creator/SKILL.md)** | `v5.0.1` | 主引擎：6 人团队调度 + Harness 约束引擎 + skill_trace 追踪 |
| **[markdown-to-word](skills/markdown-to-word/SKILL.md)** | `v2.0.0` | 文档转换器：4 套企业级模板（深蓝标题 / 三线表 / 条纹行）|
| **[markdown-processor](skills/markdown-processor/SKILL.md)** | `v1.0.0` | 文档处理引擎：多文件合并、标题修复、格式统一 |

### 🔧 第二层：支撑组件（7 个）

| 技能 | 用途 |
|------|------|
| **data-cleaner** | 多源数据清洗引擎：去重、可信度评级、结构化输出（质量评分 ≥ 80）|
| **business-writer** | 商业写作专家：三层论述结构 + 主旨标题 + 去除 AI 味 |
| **humanizer** | 文本人性化：自动检测并消除 AI 生成痕迹 |
| **assistant** | WorkBuddy 核心整合：自我提升 + 记忆管理 + 知识图谱 |
| **self-improving-agent** | Agent 自我反思与持续学习框架 |
| **ontology** | 结构化知识图谱引擎 |
| **find-skills** | 技能发现与安装助手 |

### 🚀 第三层：领域整合包（3 个）🆕

| 整合包 | 内容 | 与 BP-Factory 的关系 |
|--------|------|-------------------|
| **[scientist](skills/scientist/SKILL.md)** | 7 合 1 科研全流程：头脑风暴→文献→EDA→可视化→论文→PPT→示意图 | 提供 data-visualization（期刊级图表生成）能力 |
| **[NeoData金融搜索服务](skills/NeoData金融搜索服务/SKILL.md)** | 自然语言金融数据搜索：A股/港股/美股/基金/宏观/外汇 7 大类 | 提供 finance-data-retrieval（实时金融数据获取）能力 |
| **[金融财务分析整合包](skills/金融财务分析整合包/SKILL.md)** | 全链路金融分析：数据获取→财务分析→交易决策→报表生成→可视化 | 补充三大报表分析 + 投资决策引擎 |

> **13 个技能协同工作**：business-plan-creator 运行时自动联动 data-cleaner（清洗）→ business-writer（写作）→ markdown-processor（合并）→ markdown-to-word（输出），scientist 和金融包提供底层数据能力支撑。

---

## 🏗️ 架构：智能锻造流水线

```
                        BP-Factory Pipeline
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Raw Data    ┌──────────┐   ┌──────────┐   ┌──────────┐   📄   │
│  ──────────▶ │ 数据清洗  │──▶│ 专家写作  │──▶│ 文档整合  │──▶ 输出 │
│              │data-cleaner│   │6 Agents  │   │md-processor│      │
│              └──────────┘   └──────────┘   └──────────┘        │
│                    │              │              │               │
│              ┌─────▼─────┐ ┌────▼────┐  ┌─────▼─────┐          │
│              │ NeoData   │ │Scientist│  │markdown-   │          │
│              │ 金融数据   │ │可视化   │  │to-word     │          │
│              └───────────┘ └─────────┘  └───────────┘          │
│                                                                 │
│    🔒 pre-flight          🔒 pre-merge        🔒 pre-deliver    │
│    Agent配额=6            章节去重+完整性      字数+图表+技能追踪  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎯 markdown-to-word 转换器

### 四套设计模板

| 模板 | 适用场景 | 特色 |
|------|---------|------|
| **user_default** | 自定义（推荐）| 深蓝标题层次 + 专业三线表 + 微软雅黑正文 |
| **corporate** | 商业计划书、投资分析报告 | 28pt 深蓝标题 + 蓝色表头 |
| **academic** | 学术论文、研究报告 | 双倍行距 + 首行缩进 |
| **default** | 通用文档 | 简洁通用 |

### v2.0.0 关键修复

- 🔥 修复颜色 Fallback Bug：从全局黑色 → 专业蓝色背景表头
- 🔥 字号层次优化：H1/H2/H3 从几乎一样 → 22pt/16pt/13pt 清晰三层
- 🔥 表格样式全面升级：三线表 + 蓝色表头（#2B579A）+ 浅蓝灰条纹行（#E8EEF4）

---

## 🚦 快速开始

### 前置要求

```bash
pip install markdown python-docx beautifulsoup4
```

### 在 WorkBuddy 中使用

```markdown
# 一键生成商业计划书
@skill:business-plan-creator
主题：分析 XX 公司的投资价值与发展战略

# Markdown 转 Word
@skill:markdown-to-word
输入文件：my_plan.md
模板：user_default
```

### 命令行使用

```bash
# 商业计划书生成
cd skills/business-plan-creator
python scripts/bp_orchestrator.py --topic "你的公司或项目"

# Markdown 转 Word
cd skills/markdown-to-word
python scripts/markdown_to_word_pro.py input.md -o output.docx -t user_default

# Markdown 文档处理
cd skills/markdown-processor
python scripts/process.py input.md --output clean.md

# 金融数据查询
cd skills/NeoData金融搜索服务
python scripts/query.py "腾讯最新财报营收"
```

---

## 📁 项目结构

```
BP-Factory/
├── skills/
│   ├── business-plan-creator/      # 🏗️ 商业计划书主引擎 (v5.0.1)
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── harness/            # Harness 约束引擎
│   │   │   │   ├── master_check.py # 主检查器（3 级检查点）
│   │   │   │   ├── chapter_dedup.py# 章节去重
│   │   │   │   ├── chart_existence.py # 图表验证
│   │   │   │   ├── skill_trace.py  # 技能追踪（v5.0.1 新增）
│   │   │   │   └── word_count.py   # 字数实测
│   │   │   └── bp_orchestrator.py  # 流程编排器
│   │   └── references/             # 专家职责 + 质量清单
│   │
│   ├── markdown-to-word/           # 📄 Markdown → Word (v2.0.0)
│   │   ├── scripts/markdown_to_word_pro.py
│   │   └── assets/styles/          # 4 套设计模板 XML
│   │
│   ├── markdown-processor/         # 🔧 文档处理引擎 (v1.0.0)
│   │   └── scripts/
│   │       ├── merge.py            # 多文件合并
│   │       ├── process.py          # 标题修复 + 格式统一
│   │       ├── check_headings.py   # 标题检查
│   │       └── fix_headings.py     # 标题修复
│   │
│   ├── scientist/                  # 🔬 科研全流程整合包 (7合1)
│   ├── NeoData金融搜索服务/        # 📊 自然语言金融数据搜索
│   ├── 金融财务分析整合包/          # 💹 全链路金融分析
│   │
│   ├── data-cleaner/               # 🧹 数据清洗引擎
│   ├── business-writer/            # ✍️ 商业写作专家
│   ├── humanizer/                  # 🎭 文本人性化
│   ├── assistant/                  # 🧠 WorkBuddy 核心整合
│   ├── self-improving-agent/       # 🔄 自我学习框架
│   ├── ontology/                   # 📚 知识图谱引擎
│   └── find-skills/                # 🔍 技能发现助手
│
├── LICENSE                         # MIT License
└── README.md
```

---

## 💡 设计哲学

### 三个"绝不"

1. **绝不套模板** — 内容写作 100% AI 自主，Harness 只约束流程不约束内容
2. **绝不跳步骤** — 代码级强制校验，约束写在代码里，不是写在纸上
3. **绝不硬编码** — 所有转换、清洗、生成全部通过技能脚本执行，有技能必须用技能

### 自主 vs 约束的边界

| Harness 管什么 | AI 自主什么 |
|----------------|------------|
| Agent 数量、章节去重、图表验证 | 分析角度、论证方式、案例选择 |
| 字数实测、技能调用完整性 | 写作风格、表达策略、商业判断 |
| 交付格式合规 | 数据解读、投资逻辑、风险判断 |

---

## 📄 许可证

本项目采用 **MIT License** 开源协议。自由使用、修改、分发。

---

## 🙏 致谢

- 由 [Elong-svg](https://github.com/Elong-svg) 创建并维护
- 专为 **腾讯 WorkBuddy AI 编程助手** 设计开发
- 技能编排、Agent 协作、约束引擎均深度适配 WorkBuddy 工作流体系

---

> *"约束写在纸上没有代码强制执行 = 没有约束。约束写在代码里，才是真正的执行力。"*
>
> *— BP-Factory Harness Engine, v5.0.1*
