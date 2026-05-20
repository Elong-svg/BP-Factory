---
name: business-plan-creator
description: >
  专业商业计划书生成超级整合包，通过 6 人专家团队（Claw 项目总监 + 行业研究员 + 财务分析师 + 战略分析师 + 流程监管专家 + 质量审核官）
  + 3 个专业子技能（data-cleaner、business-writer、markdown-processor）+ Harness 约束执行引擎协作完成。

  触发词：写商业计划书、生成商业计划书、BP

  重要：本技能内含完整的 team_create + task 工具调用语法，Harness 引擎在每个关键节点强制执行检查，任何检查未通过流程硬性停止。
version: 5.0.1
author: Claw
update_note: >
  v5.0.1 新增技能调用追踪验证 (skill_trace.py)，
  解决 data-cleaner / business-writer / markdown-to-word 等必用技能被硬编码绕过的问题。
  AI 每调用一个必用技能写入 skill_trace.json，Harness pre-deliver 验证齐全性。
  从 49KB 冗余文本压缩至可操作核心，约束流程不约束内容。
disable: false
---

# 🚨 最高铁律：约束流程，不约束内容

**核心原则：Harness 约束的是"怎么做"，AI 自主的是"写什么"。**

| 维度 | Harness 约束（不可绕过） | AI 自主（完全自由） |
|------|--------------------------|---------------------|
| Agent 数量 | ✅ 必须 = 6（1 总监 + 5 专家） | — |
| 章节数量 | ✅ 必须 = 8（摘要 + 7 章） | — |
| 图表生成 | ✅ 必须 = 图表文件真实存在 | 什么类型、什么数据、什么样式 |
| 字数下限 | ✅ 必须 ≥ 20000 字 | 超多少、怎么分配 |
| 质量门禁 | ✅ 必须逐项通过 Harness | — |
| 写作内容 | — | ✅ AI 自主决定 |
| 分析深度 | — | ✅ AI 自主判断 |
| 行文风格 | — | ✅ AI 自主把握 |
| 论证方式 | — | ✅ AI 自主选择 |

---

## 🔒 Harness 约束执行引擎（v5.0 核心新增）

**每个关键节点必须运行对应检查，未通过 = 流程硬性停止。**

```
pre-flight（团队创建前）           pre-merge（合并前）              pre-deliver（交付前）
┌──────────────────────┐    ┌──────────────────────┐    ┌──────────────────────┐
│ ✅ Agent 配额 = 6     │    │ ✅ 章节去重检查       │    │ ✅ 图表存在性检查     │
│ ✅ 项目目录初始化      │    │ ✅ 章节完整性（8章）  │    │ ✅ 字数合规（≥20000） │
└──────────┬───────────┘    └──────────┬───────────┘    │ ✅ 图表表格计数       │
           │                           │                └──────────┬───────────┘
           ▼                           ▼                           ▼
    创建 6 人团队               合并专家文档                  生成 Word/HTML 交付
```

### 检查点调用速查

```bash
# 检查点 1：团队创建前
python C:/Users/吴传奇/.workbuddy/skills/business-plan-creator/scripts/harness/master_check.py pre-flight bp_sections/

# 检查点 2：合并前
python C:/Users/吴传奇/.workbuddy/skills/business-plan-creator/scripts/harness/master_check.py pre-merge bp_sections/

# 检查点 3：交付前
python C:/Users/吴传奇/.workbuddy/skills/business-plan-creator/scripts/harness/master_check.py pre-deliver bp_final.md bp_charts/
```

**失败处理**：
- 任何检查点失败 → 输出明确的问题定位和处理建议
- 不允许绕过 Harness 直接交付
- 报告自动保存至 `scripts/harness/.harness_reports/`

---

## 一、核心架构：6 人团队 + 3 子技能 + Harness 引擎

### 1.1 6 人团队

| 角色 | 职责 | 核心技能 |
|------|------|---------|
| **Claw（项目总监）** | 数据收集、data-cleaner 清洗、进度监控、最终整合交付 | finance-data-retrieval, data-cleaner |
| **行业研究员** | 行业分析 + 竞争分析 + 行业图表制作 | business-writer, data-visualization |
| **财务分析师** | 财务分析 + 估值分析 + 财务图表制作 | finance, business-writer, data-visualization |
| **战略分析师** | 战略分析 + SWOT + 第七章投资建议 + 战略图表 | business-writer, data-visualization |
| **流程监管专家** | 全流程合规监督、Harness 检查点触发、技能调用审计 | harness/master_check.py |
| **质量审核官** | 4 层质量关口检查、一票否决权 | count_charts_tables.py, harness/* |

### 1.2 3 个专业子技能

| 子技能 | 调用时机 | 职责 |
|--------|---------|------|
| **data-cleaner** | Step 1 数据收集后 | 数据清洗、去重、可信度评级 |
| **business-writer** | Step 2 专家撰写时 | 三层论述结构、主旨标题、去 AI 味 |
| **markdown-processor** | Step 3 整合时 | 文件合并、标题修复、格式统一 |

### 1.3 Harness 约束引擎

| 脚本 | 功能 | 调用节点 |
|------|------|---------|
| `master_check.py` | 总控，按检查点路由 | pre-flight / pre-merge / pre-deliver |
| `skill_trace.py` | 必用技能调用追踪验证 | pre-deliver（v5.0.1 新增） |
| `chapter_dedup.py` | 章节编号冲突 + 标题相似度检测 | pre-merge |
| `chart_existence.py` | 图片引用有效性 + CSV→图表生成检测 | pre-deliver |
| `word_count.py` | 中文字符 + 英文单词统计，分章统计 | pre-deliver |
| `count_charts_tables.py` | 图表/表格数量统计（已有脚本） | pre-deliver |

---

## 二、工作流程（5 步法 + Harness 检查点）

```
Step 0: 加载 skill，理解架构
    ↓
Step 1: 数据收集 → data-cleaner 清洗 → Harness pre-flight → 创建 6 人团队
    ↓
Step 2: 专家并行撰写 → business-writer + 图表同步制作 + skill_trace 记录
    ↓
Step 3: Harness pre-merge（去重）→ markdown-processor 合并 → 标题修复
    ↓
Step 4: Harness pre-deliver（技能追踪+图表+字数+计数）→ 生成 Word/HTML
    ↓
Step 5: 质量关口验收 → 交付用户
```

### Step 0：加载与理解

**加载本 skill 后立即执行：**
1. 完整阅读本文档（SKILL.md）
2. 阅读 `专家职责_v4.5.4.md` 了解专家具体要求
3. 阅读 `quality-checklist-v4.5.4.md` 了解质量关口
4. **不跳读、不省略**

### Step 1：数据收集与清洗（Claw）

**Claw 执行：**
1. 使用 finance-data-retrieval 获取财务/股票数据
2. 下载 PDF 年报（巨潮网/港交所/SEC）
3. **调用 data-cleaner 清洗数据**（质量评分 ≥ 80）
4. 创建 `bp_sections/` 和 `bp_charts/` 目录
5. **初始化技能追踪文件**：
```bash
python scripts/harness/skill_trace.py <项目目录> --init
```

**交付物：**
- `cleaned_data.json` — 清洗后结构化数据
- `quality_report.json` — 质量评分报告

### Step 1.5：创建团队（强制，不可跳过）

```javascript
// Step 1.5a: 创建团队
team_create({
    team_name: "bp-team",
    description: "商业计划书 6 人专家团队"
})

// Step 1.5b: 并行启动 5 位专家（一次性发起 5 个 task 调用）
task({
    subagent_name: "research_subagent",
    name: "行业研究员",
    team_name: "bp-team",
    mode: "acceptEdits",
    prompt: "你是 BP 行业研究员。职责：行业趋势分析、竞争格局分析、市场规模测算、政策环境..."
})

task({
    subagent_name: "research_subagent",
    name: "财务分析师",
    team_name: "bp-team",
    mode: "acceptEdits",
    prompt: "你是 BP 财务分析师。职责：三大报表分析、财务比率计算、DCF估值、盈利预测..."
})

task({
    subagent_name: "research_subagent",
    name: "战略分析师",
    team_name: "bp-team",
    mode: "acceptEdits",
    prompt: "你是 BP 战略分析师。职责：SWOT分析、商业模式画布、竞争战略、第七章投资建议..."
})

task({
    subagent_name: "research_subagent",
    name: "流程监管专家",
    team_name: "bp-team",
    mode: "acceptEdits",
    prompt: "你是 BP 流程监管专家。职责：在 pre-merge 和 pre-deliver 节点运行 Harness 脚本，全流程合规监督..."
})

task({
    subagent_name: "research_subagent",
    name: "质量审核官",
    team_name: "bp-team",
    mode: "acceptEdits",
    prompt: "你是 BP 质量审核官。职责：4 层质量关口检查，图表表格数量验证，一票否决..."
})
```

**🚨 Agent 配额铁律：**
- ✅ 必须创建恰好 6 个 Agent（1 Claw + 5 task）
- ✅ 如遇 429 错误，检查是否已有结果，不再创建新 Agent
- ✅ 禁止 fork 型 Agent（fork-2/4/5...）替代 task
- ❌ 超过 6 个 Agent → Harness pre-flight 直接拒绝

### Step 2：专家并行撰写

**每位撰写专家（行业/财务/战略）必须：**
1. 使用 **business-writer** 撰写章节
2. **同步制作图表和表格**（使用 data-visualization 生成图表，Markdown 语法制作表格）
3. 图表/表格数量达标后提交
4. **记录技能调用**（每调用一个必用技能必须记录）：
```bash
# 各专家调用 business-writer 后记录
python scripts/harness/skill_trace.py <项目目录> --add business-writer-industry "business-writer（行业研究）" "行业研究员"

# Claw 调用 data-cleaner 后记录
python scripts/harness/skill_trace.py <项目目录> --add data-cleaner "data-cleaner 数据清洗" Claw "质量评分 >= 80"
```

| 专家 | 最低图表 | 最低表格 | 典型图表类型 |
|------|---------|---------|------------|
| 行业研究员 | ≥ 3 张 | ≥ 2 个 | 规模增长图、竞争格局图、趋势图 |
| 财务分析师 | ≥ 3 张 | ≥ 3 个 | 营收趋势图、利润结构图、三大报表 |
| 战略分析师 | ≥ 2 张 | ≥ 2 个 | SWOT 矩阵图、战略规划图 |

### Step 3：Harness pre-merge + 整合

**整合前必须运行 Harness：**

```bash
python scripts/harness/master_check.py pre-merge bp_sections/
```

**检查通过后，执行整合：**

```bash
# 3.1 合并专家文档
python C:/Users/吴传奇/.workbuddy/skills/markdown-processor/scripts/merge.py bp_final.md \
  bp_sections/executive_summary.md \
  bp_sections/industry_analysis.md \
  bp_sections/financial_analysis.md \
  bp_sections/product_service.md \
  bp_sections/strategy_analysis.md \
  bp_sections/marketing_strategy.md \
  bp_sections/operations_team.md \
  bp_sections/summary_investment.md

# 3.2 修复标题格式
python C:/Users/吴传奇/.workbuddy/skills/markdown-processor/scripts/process.py bp_final.md --output bp_final_clean.md
```

### Step 4：Harness pre-deliver + 文档生成

**交付前必须运行 Harness：**

```bash
python scripts/harness/master_check.py pre-deliver bp_final_clean.md bp_charts/
```

**检查通过后，生成最终文档：**

```bash
# 生成 Word
python C:/Users/吴传奇/.workbuddy/skills/markdown-to-word/scripts/markdown_to_word_pro.py bp_final_clean.md 输出.docx
```

### Step 5：质量关口验收

质量审核官执行 4 层质量关口检查（详见 `quality-checklist-v4.5.4.md`），任一关口未通过 → 打回重做。

---

## 三、子技能强制绑定

### 必须调用（不可跳过）

| 阶段 | 技能 | 调用者 | 失败处理 |
|------|------|--------|---------|
| Step 1 | **data-cleaner** | Claw | 评分 < 80 → 重新清洗 |
| Step 2 | **business-writer** | 行业/财务/战略 | 未调用 → 打回该章节 |
| Step 2 | **data-visualization** | 行业/财务/战略 | 图表缺失 → Harness pre-deliver 拦截 |
| Step 3 | **markdown-processor** | Claw | 标题格式错误 → 重新修复 |
| Step 4 | **markdown-to-word** | Claw | 硬编码替代 → 打回 |

### 禁止行为（出现即打回）

- ❌ 跳过 data-cleaner，直接使用原始数据
- ❌ 跳过 business-writer，自己硬写
- ❌ 使用 document-integrator（只有概念无实现）
- ❌ 用 python-docx 等硬编码冒充 Word 文档生成技能
- ❌ 技能调用失败后不汇报，擅自硬编码替代

---

## 四、输出标准

| 指标 | 标准 | 验证方式 |
|------|------|---------|
| 总字数 | ≥ 20000 字 | `harness/word_count.py` |
| 总图表 | ≥ 10 张 | `count_charts_tables.py` |
| 总表格 | ≥ 8 个 | `count_charts_tables.py` |
| 章节完整 | 执行摘要 + 7 章 + 参考文献 | Harness pre-merge |
| 图表存在性 | 所有引用图片文件真实存在 | `harness/chart_existence.py` |
| 无重复章节 | 编号和标题均唯一 | `harness/chapter_dedup.py` |
| 数据可信度 | A/B 级 ≥ 90% | data-cleaner 报告 |
| 参考文献 | 文末统一章节，按类型分组 | 质量关口 4 |
| 格式规范 | 标题编号统一，自动目录 | markdown-processor |

---

## 五、Harness 脚本速查

```bash
# 所有脚本位于：scripts/harness/

# 🔒 主控（推荐使用）
python master_check.py pre-flight bp_sections/
python master_check.py pre-merge bp_sections/
python master_check.py pre-deliver bp_final.md bp_charts/

# 🔧 单独检查（调试用）
python chapter_dedup.py bp_sections/               # 章节去重
python chart_existence.py bp_final.md bp_charts/   # 图表存在性
python word_count.py bp_final.md --min-chars 20000 # 字数合规

# 📊 已有脚本（位于 scripts/）
python ../count_charts_tables.py bp_final.md       # 图表表格计数
python ../quality_checker.py bp_final.md           # 质量检查
```

**退出码含义：**
- `0` = 通过
- `1` = 未通过（可修复后重试）
- `2` = 严重未通过（需回退重做）

---

## 六、版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v3.1 | 2026-03-30 | 5 人团队 + 三条铁律 + 技能绑定 |
| v4.0 | 2026-03-31 | 新增 data-cleaner、business-writer、document-integrator |
| v4.1 | 2026-04-02 | 取消图表制作师、新增流程监管专家、简化整合流程 |
| v4.2 | 2026-04-02 | 铁律五（参考文献）、第七章（投资建议）、图表规范统一 |
| v4.3 | 2026-04-02 | 修正团队人数、移除 document-integrator、监督制衡 |
| v4.5.3 | 2026-04-05 | 整合 markdown-processor 技能 |
| v4.5.4 | 2026-04-05 | 图表表格数量强制执行、专家职责细化 |
| v4.5.5 | 2026-04-05 | 修复团队创建伪代码 → 真实 tool 调用语法 |
| **v5.0.0** | **2026-05-20** | **🔥 Harness 强化版** |
| | | **新增 Harness 约束执行引擎**（master_check.py + 4 个检查脚本） |
| | | **3 个强制检查点**：pre-flight（Agent配额）、pre-merge（去重）、pre-deliver（图表+字数+计数） |
| | | **核心改进**：约束流程不约束内容，Agent 泛滥/章节重复/图表空转/门禁虚设四大问题根治 |
| | | **SKILL.md 大幅精简**：从 49KB 冗余文本压缩至可操作核心，重复内容消除 |
| **v5.0.1** | **2026-05-20** | **🔧 技能调用追踪验证** |
| | | **新增 skill_trace.py**：必用技能（data-cleaner/business-writer/markdown-to-word等）调用强制追踪 |
| | | **AI 每调用一个必用技能写入 skill_trace.json，Harness pre-deliver 验证齐全性** |
| | | 防止技能调用被硬编码绕过，10 个必用技能条目（Step 1~3）缺一不可 |

---

_**v5.0.1 发布于 2026-05-20**_
_**核心改进：技能调用追踪验证 — 必用技能调用被硬编码绕过即被 Harness 拦截**_
