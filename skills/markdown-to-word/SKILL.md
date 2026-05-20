---
name: markdown-to-word
description: Markdown 转 Word 一键转换技能 - 应用 minimax-docx 企业级设计系统，支持标题、段落、表格、列表等所有元素的样式自动优化
triggers:
  - markdown 转 word
  - md 转 docx
  - 一键转换
  - 格式优化
  - 样式应用
  - 文档美化
  - markdown-to-word
  - md2docx
version: 1.2.0
author: Claw
update_date: 2026-04-03
changelog: 修复表格转换问题（Markdown 表格预处理 + 样式应用）
disable: false
---

# markdown-to-word 技能

## 技能概述

**核心功能**：将 Markdown 文档一键转换为专业的 Word 文档，自动应用企业级设计系统样式。

**设计来源**：完全学习并应用 `minimax-docx`（Word 文档生成）技能的所有设计系统。

**转换时间**：5-10 秒（不会长线程崩溃）

---

## 快速开始

### 基本用法

```bash
# 调用技能（默认使用企业报告模板）
使用 markdown-to-word 技能，将 [文件路径] 转换为 Word 文档

# 或直接运行脚本（支持模板选择）
python scripts/markdown_to_word_pro.py 输入文件.md [输出文件.docx]

# 使用特定模板
python scripts/markdown_to_word_pro.py 输入文件.md -t academic
```

### 输入输出

- **输入**：`.md` 格式的 Markdown 文件
- **输出**：`_专业版.docx` 格式的 Word 文档
- **模板**：corporate（默认）/ academic / default

---

## 支持的设计系统

### 1. 企业报告模板（corporate_styles）

**适用场景**：商业计划书、投资分析报告、企业白皮书

| 元素 | 字体配置 | 字号 | 颜色 | 间距 |
|------|---------|------|------|------|
| **H1** | Calibri Light + 黑体 | 28pt | #1F3864 深蓝 | 前 24pt/后 12pt |
| **H2** | Calibri Light + 黑体 | 24pt | #1F3864 深蓝 | 前 18pt/后 6pt |
| **H3** | Calibri Light + 黑体 | 18pt | #1F3864 深蓝 | 前 12pt/后 4pt |
| **正文** | Calibri + 微软雅黑 | 11pt | #333333 深灰 | 后 8pt, 1.15 倍行距 |
| **表格标题** | - | - | #2F5496 蓝底白字 | - |
| **表格条纹** | - | - | #D9E2F3 浅蓝 | - |

### 2. 学术论文模板（academic_styles）

**适用场景**：学术论文、研究报告、文献综述

| 元素 | 字体配置 | 字号 | 颜色 | 间距 |
|------|---------|------|------|------|
| **H1** | Times New Roman + 宋体 | 14pt | 黑色 | 前 24pt/后 12pt（居中） |
| **H2** | Times New Roman + 宋体 | 13pt | 黑色 | 前 18pt/后 6pt |
| **H3** | Times New Roman + 宋体 | 12pt | 黑色 | 前 12pt/后 4pt |
| **正文** | Times New Roman + 宋体 | 12pt | 黑色 | 双倍行距，首行缩进 0.5 寸 |

### 3. 通用文档模板（default_styles）

**适用场景**：通用文档、备忘录、信函

| 元素 | 字体配置 | 字号 | 颜色 | 间距 |
|------|---------|------|------|------|
| **H1** | Calibri Light | 28pt | #2F5496 深蓝 | 前 24pt/后 12pt |
| **H2** | Calibri Light | 24pt | #2F5496 深蓝 | 前 18pt/后 6pt |
| **H3** | Calibri Light | 18pt | #2F5496 深蓝 | 前 12pt/后 4pt |
| **H4** | Calibri Light | 14pt | #2F5496 深蓝 + 斜体 | 前 8pt/后 4pt |
| **正文** | Calibri | 11pt | #333333 | 后 8pt |

---

## 转换流程

### Step 1: 环境检查

```bash
# 检查 Python 环境
python --version

# 检查依赖库
pip show markdown python-docx beautifulsoup4

# 如无依赖，自动安装
pip install markdown python-docx beautifulsoup4
```

### Step 2: 调用转换脚本

```bash
# 执行转换
python scripts/markdown_to_word_pro.py [输入文件.md] [输出文件.docx]
```

### Step 3: 质量验证

- ✅ 标题层级正确
- ✅ 字体样式统一
- ✅ 表格格式专业
- ✅ 列表缩进规范
- ✅ 页面布局标准

---

## 支持的 Markdown 元素

| Markdown 元素 | Word 映射 | 样式说明 |
|-------------|----------|---------|
| `# H1` | 一级标题 | 应用 H1 样式（深蓝色、28pt） |
| `## H2` | 二级标题 | 应用 H2 样式（深蓝色、24pt） |
| `### H3` | 三级标题 | 应用 H3 样式（深蓝色、18pt） |
| 正文段落 | 正文 | 11pt, 1.15 倍行距，段后 8pt |
| `**粗体**` | 粗体 | `<b>` 标签保留 |
| `*斜体*` | 斜体 | `<i>` 标签保留 |
| `- 列表` | 无序列表 | 圆点符号，悬挂缩进 |
| `1. 列表` | 有序列表 | 数字编号，悬挂缩进 |
| `|表格|` | 三线表 | 表头蓝色背景，条纹行 |
| `> 引用` | 引用块 | 灰色斜体，左右缩进 |
| `---` | 分页符 | 插入分页符 |

---

## 页面布局标准

### A4 标准（企业报告）

- **纸张尺寸**：210×297mm（A4）
- **页边距**：
  - 上：2.54cm
  - 下：2.54cm
  - 左：3.17cm
  - 右：2.54cm
- **行距**：1.15 倍
- **内容覆盖率**：60-70%

### Letter 标准（学术论文）

- **纸张尺寸**：8.5×11 英寸（Letter）
- **页边距**：1 英寸（2.54cm）四面
- **行距**：2.0 倍（双倍行距）
- **段落**：首行缩进 0.5 寸

---

## 错误处理

### 常见错误及解决方案

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| `ModuleNotFoundError` | 缺少 Python 库 | 运行 `pip install markdown python-docx beautifulsoup4` |
| `FileNotFoundError` | 输入文件不存在 | 检查文件路径是否正确 |
| `PermissionError` | 文件被占用 | 关闭已打开的 Word 文档 |
| 中文乱码 | 编码问题 | 确保 Markdown 文件为 UTF-8 编码 |
| 表格变形 | Markdown 表格格式错误 | 检查表格语法，确保列对齐 |

---

## 最佳实践

### 1. 文档类型匹配

- **商业计划书** → 使用企业报告模板
- **学术报告** → 使用学术论文模板
- **通用文档** → 使用通用文档模板

### 2. 标题层级建议

```markdown
# 一级标题（文档标题，全文档 1 个）
## 二级标题（章节标题）
### 三级标题（小节标题）
#### 四级标题（可选，避免过度使用）
```

### 3. 表格优化

```markdown
| 表头 1 | 表头 2 | 表头 3 |
|-------|-------|-------|
| 数据 1 | 数据 2 | 数据 3 |
| 数据 4 | 数据 5 | 数据 6 |

# 建议：表格不超过 5 列，超过则考虑拆分
```

### 4. 列表使用

```markdown
- 列表项 1
- 列表项 2
- 列表项 3

# 避免嵌套过深（不超过 3 层）
```

---

## 输出质量检查清单

转换完成后，自动检查以下项目：

- [ ] 所有一级标题应用 H1 样式（28pt，深蓝色）
- [ ] 所有二级标题应用 H2 样式（24pt，深蓝色）
- [ ] 所有三级标题应用 H3 样式（18pt，深蓝色）
- [ ] 正文使用 11pt，1.15 倍行距
- [ ] 表格有三线表样式，表头蓝色背景
- [ ] 列表有悬挂缩进
- [ ] 页面边距符合标准
- [ ] 无格式错误
- [ ] 无乱码
- [ ] 文件可正常打开

---

## 与其他技能的关系

### 依赖关系

- **独立运行**：不依赖其他技能
- **可选集成**：可作为 `business-plan-creator` 的子技能

### 对比 minimax-docx

| 功能 | markdown-to-word | minimax-docx |
|------|-----------------|-------------|
| **输入格式** | Markdown | content.json |
| **转换速度** | 5-10 秒 | 需先转换 JSON |
| **学习成本** | 零学习成本 | 需理解 JSON 结构 |
| **样式质量** | 企业级（学习 minimax） | 企业级（原生） |
| **适用场景** | Markdown 快速转换 | 从零创建/复杂编辑 |

---

## 示例

### 输入（Markdown）

```markdown
# 会计研究趋势报告

## 1. 行业概况

会计行业正在经历**数字化转型**，主要趋势包括：

- 人工智能应用
- 区块链技术
- 云计算普及

### 1.1 市场规模

| 年份 | 市场规模（亿元） | 增长率 |
|------|----------------|-------|
| 2023 | 5000 | 15% |
| 2024 | 5750 | 15% |
| 2025 | 6612 | 15% |
```

### 输出（Word）

生成 `会计研究趋势报告_专业版.docx`，包含：
- ✅ 深蓝色一级标题（28pt，Calibri Light + 黑体）
- ✅ 深蓝色二级标题（24pt，Calibri Light + 黑体）
- ✅ 正文 11pt，1.15 倍行距
- ✅ 专业三线表（蓝色表头，条纹行）
- ✅ 标准 A4 页面布局

---

## 技术实现

### 核心算法

1. **Markdown 解析**：使用 `markdown` 库解析为 HTML
2. **HTML 解析**：使用 `BeautifulSoup` 解析 HTML AST
3. **样式映射**：将 HTML 元素映射到 Word 样式
4. **Word 生成**：使用 `python-docx` 创建文档

### 关键代码

```python
# 详见 scripts/markdown_to_word_pro.py
```

---

## 更新日志

### v1.0.0（2026-04-03）

- ✅ 初始版本发布
- ✅ 支持 3 套设计系统（企业/学术/通用）
- ✅ 支持所有 Markdown 基本元素
- ✅ 支持表格样式优化
- ✅ 支持列表样式优化
- ✅ 支持中文排版

### v2.0.0（2026-05-20）

- 🔥 **user_default 模板全面重写**：全黑标题+黑色表头（fallback bug）→ 深蓝层次标题+专业三线表
- 🔥 **颜色 fallback 安全修复**：None 不再返回 RGBColor(0,0,0)，改为安全默认色
- 🔥 **表格样式修复**：表头蓝色背景+白色粗体，条纹行浅蓝灰底色
- 🔥 **字号层次优化**：H1=22pt/H2=16pt/H3=13pt（原 16/15/14 几乎一样）
- 🔥 **H3 字体统一**：改为黑体（原为宋体）
- 🔥 **正文字体升级**：宋体 → 微软雅黑，行距 1.5 → 1.25

---

## References

| 文档 | 说明 |
|------|------|
| [design_principles.md](references/design_principles.md) | 设计原则 |
| [typography_guide.md](references/typography_guide.md) | 字体排版指南 |
| [scenario_a_create.md](references/scenario_a_create.md) | 创建场景指南 |
| [corporate_styles.xml](assets/styles/corporate_styles.xml) | 企业样式配置 |
| [academic_styles.xml](assets/styles/academic_styles.xml) | 学术样式配置 |
| [default_styles.xml](assets/styles/default_styles.xml) | 默认样式配置 |
