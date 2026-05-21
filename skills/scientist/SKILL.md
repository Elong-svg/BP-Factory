---
name: scientist
description: 科研全流程整合包 — 头脑风暴→文献研究→数据分析→可视化→论文写作→PPT 汇报→示意图生成，7 合 1 超级技能，覆盖科研全生命周期
triggers:
  - 科研
  - 论文
  - 研究
  - 课题
  - 实验
  - 数据分析
  - 可视化
  - 投稿
  - 学术
  - 文献
  - hypothesis
  - manuscript
  - paper
  - research
disable: false
---

# Scientist — 科研全流程整合包

## 核心定位

**这是 7 个 scientific 系列技能的整合包**，提供从科研想法到论文发表的端到端支持。

## 技能组成

| 子技能 | 用途 | 触发场景 |
|---|---|---|
| **scientific-brainstorming** | 科研头脑风暴 | 选题、找方向、想 hypothesis、找创新点 |
| **scientific-critical-thinking** | 批判性思维 | 评估文献、找漏洞、质疑假设 |
| **scientific-visualization** | 期刊级可视化 | 画 Nature/Science/Cell 级别图表 |
| **scientific-writing** | 论文写作 | 写 IMRAD 结构论文、段落式论述 |
| **scientific-schematics** | 科研示意图 | 画技术路线图、流程图、机制图 |
| **scientific-slides** | 科研 PPT | 学术汇报、会议 poster、答辩 PPT |
| **exploratory-data-analysis** | 探索性数据分析 | 数据清洗、EDA、异常检测 |

## 工作流程（科研全生命周期）

```
Phase 1 选题 → Phase 2 文献 → Phase 3 方法 → Phase 4 实验 → Phase 5 分析 → Phase 6 写作 → Phase 7 汇报
   ↓            ↓            ↓            ↓            ↓            ↓            ↓
brainstorming  critical     EDA          visualization writing      slides
                            + visualization
```

## 快速启动指南

### 场景 1：我要选题/找研究方向
```
调用：scientific-brainstorming
流程：
1. 描述你的研究领域和兴趣
2. AI 帮你发散思维、跨学科联想
3. 产出 3-5 个可行研究方向
4. 用 scientific-critical-thinking 评估每个方向的可行性
```

### 场景 2：我要写论文/比赛报告
```
调用：scientific-writing（自动联动 scientific-visualization + scientific-schematics）
流程：
1. 确定目标期刊/比赛要求
2. 用 research-lookup 查找文献
3. 创建 IMRAD 大纲（bullet points）
4. 转换成段落式论述（禁止 bullet points 出现在最终稿）
5. 自动生成 1-2 张示意图（scientific-schematics）
6. 生成期刊级图表（scientific-visualization）
7. 输出完整论文
```

### 场景 3：我要画期刊级图表
```
调用：scientific-visualization
支持：
- Nature/Science/Cell 样式预设
- 色盲友好配色（Okabe-Ito）
- 多面板图（Panel A/B/C）
- 误差条、显著性标记（*, **, ***）
- 导出 PDF/EPS/TIFF（300-1200 DPI）
图表类型：折线图、散点图、柱状图、箱线图、小提琴图、热图、聚类图等
```

### 场景 4：我要画技术路线图/机制图
```
调用：scientific-schematics
方法：用自然语言描述图长什么样 → AI 自动生成
示例：
- "画一个随机对照试验的 CONSORT 流程图"
- "画一个 AI 赋能数据全链路的技术架构图"
- "画一个细胞信号通路的机制图"
```

### 场景 5：我要做学术汇报 PPT
```
调用：scientific-slides
场景：组会汇报、会议报告、论文答辩、基金申请
自动包含：技术路线图、结果图表、结论总结
```

### 场景 6：我有数据要分析
```
调用：exploratory-data-analysis
流程：
1. 数据质量评估（缺失值、异常值）
2. 描述性统计
3. 可视化探索（分布、相关性）
4. 假设检验
5. 生成分析报告
```

## 核心原则（铁律）

### 1. 论文写作铁律
- ✅ **必须段落式论述**，禁止 bullet points 出现在最终稿（仅用于大纲阶段）
- ✅ **必须 IMRAD 结构**（Introduction, Methods, Results, Discussion）
- ✅ **必须引用文献**（APA/AMA/Vancouver 格式）
- ✅ **必须包含 1-2 张示意图**（scientific-schematics）
- ✅ **必须包含期刊级图表**（scientific-visualization）

### 2. 可视化铁律
- ✅ **必须色盲友好配色**（Okabe-Ito、viridis）
- ✅ **必须标注误差条**（SD/SEM/CI，明确说明）
- ✅ **必须导出矢量图**（PDF/EPS）或高分辨率 TIFF（300+ DPI）
- ✅ **必须适配期刊尺寸**（Nature 单栏 89mm，双栏 183mm）
- ❌ **禁止使用 jet/rainbow 色图**
- ❌ **禁止 3D 效果**
- ❌ **禁止红绿对比**

### 3. 数据分析铁律
- ✅ **必须先做 EDA**（探索性数据分析）
- ✅ **必须报告样本量**（n=?）
- ✅ **必须报告效应量**（effect size）
- ✅ **必须检验假设**（正态性、方差齐性）
- ❌ **禁止 p-hacking**
- ❌ **禁止选择性报告**

## 任务路由表

根据用户需求自动分流：

| 用户意图关键词 | 路由到 | 自动联动 |
|---|---|---|
| 选题、方向、idea、hypothesis | brainstorming | critical-thinking |
| 写论文、投稿、manuscript | writing | visualization + schematics |
| 画图、图表、figure、plot | visualization | - |
| 示意图、流程图、机制图 | schematics | - |
| PPT、汇报、slides | slides | visualization |
| 数据、分析、EDA、统计 | EDA | visualization |
| 文献、批判、评估 | critical-thinking | - |

## 质量检查清单（交付前必查）

### 论文检查（writing）
- [ ] 全文段落式论述，无 bullet points（Methods 除外）
- [ ] IMRAD 结构完整
- [ ] 至少 1-2 张示意图
- [ ] 至少 3-5 个期刊级图表
- [ ] 文献引用格式统一
- [ ] 字数符合要求

### 图表检查（visualization）
- [ ] 色盲友好配色
- [ ] 轴标签带单位
- [ ] 误差条定义明确
- [ ] 字体≥6pt（最终尺寸）
- [ ] 矢量格式（PDF/EPS）或 300+ DPI
- [ ] 灰度测试通过

### 示意图检查（schematics）
- [ ] 清晰表达核心概念
- [ ] 配色专业
- [ ] 文字可读
- [ ] 嵌入论文合适位置

## 可用脚本工具

### scripts/ 目录（待创建）
- `workflow_launcher.py` - 一键启动完整科研流程
- `figure_batch_export.py` - 批量导出图表
- `manuscript_validator.py` - 论文格式检查

## 参考文献目录

| 文件 | 内容 |
|---|---|
| `references/imrad_structure.md` | IMRAD 结构详解 |
| `references/citation_styles.md` | 引用格式指南（APA/AMA/Vancouver） |
| `references/publication_guidelines.md` | 期刊投稿要求 |
| `references/color_palettes.md` | 色盲友好配色方案 |
| `references/journal_requirements.md` | 各大期刊规格 |
| `references/brainstorming_methods.md` | 头脑风暴方法库 |

## 典型工作流示例

### 示例 1：比赛论文全流程
```
用户：我要写一篇比赛论文，主题是 AI 赋能数据全链路

1. brainstorming → 确定研究问题和创新点
2. EDA → 分析比赛数据
3. visualization → 生成结果图表
4. schematics → 生成技术路线图
5. writing → 撰写完整论文（IMRAD 结构）
6. slides → 生成答辩 PPT

交付：完整论文 + 图表包 + PPT
```

### 示例 2：期刊投稿全流程
```
用户：我要投 Nature Communications

1. writing → 确定目标期刊要求
2. brainstorming → 提炼核心贡献
3. visualization → 按 Nature 规格画图（89mm/183mm）
4. schematics → 生成机制图
5. writing → 撰写论文（段落式）
6. critical-thinking → 自我审查、找漏洞

交付：符合 Nature 规格的完整稿件
```

## 与其他技能协作

- **finance-data-retrieval** → 获取金融数据
- **data** → 数据分析
- **Word 文档生成** → 输出 Word 格式
- **PDF 文档生成** → 输出 PDF 格式
- **PPT 演示文稿** → 生成 PPT

## 禁止事项

- ❌ 不生成 bullet points 论文（仅大纲阶段可用）
- ❌ 不使用 jet/rainbow 色图
- ❌ 不导出低分辨率图（<300 DPI）
- ❌ 不做 p-hacking 或选择性报告
- ❌ 不抄袭或学术不端

## 版本信息

- **版本**：1.0
- **来源**：整合自 davila7/claude-code-templates 的 scientific 系列 skill（623 次安装）
- **安装日期**：2026-04-07
- **维护**：自动从 7 个子技能同步最佳实践
