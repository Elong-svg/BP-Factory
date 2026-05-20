# 🦅 Oh My BP

> **专为腾讯 WorkBuddy 设计的 AI 商业计划书生成工具集。**  
> 一行命令，从原始数据到专业级商业计划书 —— 不套模板、不走捷径、不牺牲质量。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![WorkBuddy](https://img.shields.io/badge/Tencent-WorkBuddy-blueviolet.svg)](https://workbuddy.qq.com)

---

## 💡 是什么？

**Oh My BP** 是一套为 **腾讯 WorkBuddy AI 编程助手** 量身打造的商业计划书生成工具集。

它不是一堆 Markdown 模板的简单堆砌，而是一个深度适配 WorkBuddy 工作流体系的 **智能 Agent 协作引擎** —— 具备 Harness 代码级约束、多 Agent 并行协作、数据清洗到可视化图表生成的完整能力。

### 为什么叫 "Oh My"？

灵感来源于开源社区经典的 "Oh My" 系列（如 Oh My Zsh、Oh My CodeBuddy），代表 **开箱即用、一键启动、无需折腾** 的开发体验。

---

## 🚀 为什么选择 Oh My BP？

### WorkBuddy 深度集成

| 特性 | 说明 |
|------|------|
| **多 Agent 协作体系** | 深度适配 WorkBuddy 的 Agent 调度框架，6 个领域专家（行业分析师、财务专家、竞争分析师等）并行写作 |
| **Harness 约束引擎** | 专为 WorkBuddy Agent 循环设计的 3 级检查点系统，代码级强制校验 |
| **技能生态联动** | 与 WorkBuddy 内置的 data-cleaner、business-writer、markdown-to-word 等技能无缝衔接 |
| **记忆系统集成** | 自动对接 WorkBuddy 的记忆层（MEMORY.md + .learnings/），持续优化输出质量 |

### 核心能力

- 📊 **数据驱动** —— 从原始 CSV/JSON 数据自动清洗、分析到可视化图表
- 🤖 **多 Agent 协作** —— 6 个领域专家并行写作，Harness 自动协调
- 🔒 **代码级约束引擎** —— 字数实测、章节去重、图表渲染验证、技能调用追踪，全部强制执行
- 📝 **专业文档输出** —— Markdown → Word 一键转换，深蓝标题层次 + 专业三线表 + 企业级排版

---

## 📦 包含哪些技能？

### 核心技能

| 技能 | 版本 | 说明 |
|------|------|------|
| **[business-plan-creator](skills/business-plan-creator/SKILL.md)** | v5.0.1 | 🏗️ 主引擎：Harness 约束引擎 + 3 级检查点 + 技能追踪 |
| **[markdown-to-word](skills/markdown-to-word/SKILL.md)** | v2.0.0 | 📄 Markdown → Word 转换器：4 套设计模板，企业级排版 |

### 辅助技能

| 技能 | 说明 |
|------|------|
| **data-cleaner** | 🧹 多源数据清洗与结构化引擎 |
| **business-writer** | ✍️ 商业写作专家，生成专业商业论述 |
| **humanizer** | 🎭 去除 AI 味，让内容读起来像人写的 |
| **assistant** | 🧠 WorkBuddy 核心能力整合：自我提升 + 记忆管理 + 知识图谱 |
| **self-improving-agent** | 🔄 Agent 自我反思与持续学习框架 |
| **ontology** | 📚 结构化知识图谱引擎 |
| **find-skills** | 🔍 技能发现与安装助手 |

---

## 🏗️ Harness 约束引擎（核心亮点）

### 传统 vs Oh My BP

```
❌ 传统方案：SKILL.md 里写"请确保字数达标" → AI 可能忽略
✅ Oh My BP：master_check.py 代码强制校验 → 不达标就拒绝输出
```

### 三级检查点

| 检查点 | 时机 | 校验内容 |
|--------|------|---------|
| **pre-flight** | Agent 启动前 | Agent 数量配额、任务分配、资源校验 |
| **pre-merge** | 章节合并前 | 章节编号冲突检测（>75% 相似度自动拦截） |
| **pre-deliver** | 最终交付前 | 字数实测、图表渲染验证、10 项技能调用完整性 |

### 技能追踪系统

```
AI 每调用一个必需技能 → 写入 skill_trace.json → Harness 验证 10/10 完整 → 放行
```

> **约束流程，不约束内容** —— Harness 管流程合规，AI 自主决定写什么、怎么写。

---

## 📊 markdown-to-word 转换器

### 四套设计模板

| 模板 | 适用场景 | 特色 |
|------|---------|------|
| **user_default** | 自定义（推荐） | 深蓝标题层次 + 专业三线表 + 微软雅黑正文 |
| **corporate** | 商业计划书、投资分析报告 | 28pt 深蓝标题 + 蓝色表头 |
| **academic** | 学术论文、研究报告 | 双倍行距 + 首行缩进 |
| **default** | 通用文档 | 简洁通用 |

### v2.0 关键修复

- 🔥 修复颜色 Fallback Bug：表头全黑 → 专业蓝色背景
- 🔥 字号层次优化：H1/H2/H3 从几乎一样 → 22pt/16pt/13pt 清晰层次
- 🔥 表格样式全面升级：三线表 + 蓝色表头 + 条纹行

---

## 🚦 快速开始

### 前置要求

```bash
pip install markdown python-docx beautifulsoup4 python-docx-template
```

### 在 WorkBuddy 中使用

```markdown
# 直接通过 WorkBuddy 技能调用
@skill:business-plan-creator
主题：分析 XX 公司的投资价值

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
```

---

## 📁 项目结构

```
oh-my-bp/
├── skills/
│   ├── business-plan-creator/      # 商业计划书主引擎
│   │   ├── SKILL.md                # 技能文档（v5.0.1）
│   │   ├── scripts/
│   │   │   ├── harness/            # Harness 约束引擎
│   │   │   │   ├── master_check.py # 主检查器
│   │   │   │   ├── chapter_dedup.py# 章节去重
│   │   │   │   ├── chart_existence.py # 图表验证
│   │   │   │   ├── skill_trace.py  # 技能追踪
│   │   │   │   └── word_count.py   # 字数实测
│   │   │   └── bp_orchestrator.py  # 流程编排器
│   │   └── templates/              # 商业计划书模板
│   ├── markdown-to-word/           # Markdown 转 Word
│   │   ├── scripts/markdown_to_word_pro.py
│   │   └── assets/styles/          # 4 套设计模板
│   ├── data-cleaner/               # 数据清洗
│   ├── business-writer/            # 商业写作
│   └── ...                         # 其他辅助技能
└── README.md
```

---

## 💡 设计理念

### 三个"绝不"

1. **绝不套模板** —— 内容写作 100% AI 自主，Harness 只约束流程不约束内容
2. **绝不跳步骤** —— 代码级强制校验，文档约束 ≠ 纸上谈兵
3. **绝不硬编码** —— 所有转换、清洗、生成全部通过技能脚本执行

### 自主 vs 约束的边界

| Harness 管什么 | AI 自主什么 |
|----------------|------------|
| Agent 数量、章节去重 | 分析角度、论证方式 |
| 字数实测、图表验证 | 数据来源、案例选择 |
| 技能调用完整性 | 写作风格、表达策略 |
| 交付格式合规 | 商业判断、投资逻辑 |

---

## 📄 许可证

本项目采用 **MIT License** 开源协议。你可以自由使用、修改、分发本代码，用于个人学习或商业项目。

---

## 🙏 致谢

- 由 [Elong-svg](https://github.com/Elong-svg) 创建并维护
- 专为 **腾讯 WorkBuddy AI 编程助手** 设计开发
- 感谢每一位贡献者 ❤️

---

> *"约束写在纸上没有代码强制执行 = 没有约束。约束写在代码里，才是真正的执行力。"*
