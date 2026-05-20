# markdown-to-word 使用指南

## 快速开始

### 1. 安装依赖

```bash
pip install markdown python-docx beautifulsoup4
```

### 2. 基本用法

```bash
# 最简单用法（自动生成输出文件名）
python scripts/markdown_to_word_pro.py 输入文件.md

# 指定输出文件名
python scripts/markdown_to_word_pro.py 输入文件.md 输出文件.docx
```

### 3. 示例

```bash
# 示例 1：转换会计研究趋势报告
python scripts/markdown_to_word_pro.py 会计研究趋势.md
# 输出：会计研究趋势_专业版.docx

# 示例 2：转换商业计划书
python scripts/markdown_to_word_pro.py 商业计划书.md 商业计划书_最终版.docx
# 输出：商业计划书_最终版.docx
```

---

## 支持的 Markdown 语法

### 标题

```markdown
# 一级标题（文档标题）
## 二级标题（章节标题）
### 三级标题（小节标题）
#### 四级标题（可选）
```

**转换效果**：
- H1: 28pt，深蓝色，Calibri Light + 黑体
- H2: 24pt，深蓝色，Calibri Light + 黑体
- H3: 18pt，深蓝色，Calibri Light + 黑体
- H4: 14pt，深蓝色，Calibri Light + 黑体

### 正文

```markdown
这是普通段落。

支持**粗体**和*斜体*。

还支持`行内代码`。
```

**转换效果**：
- 字号：11pt
- 字体：Calibri + 微软雅黑
- 颜色：深灰色 #333333
- 行距：1.15 倍
- 段后距：8pt

### 列表

#### 无序列表

```markdown
- 列表项 1
- 列表项 2
- 列表项 3
```

#### 有序列表

```markdown
1. 第一步
2. 第二步
3. 第三步
```

**转换效果**：
- 悬挂缩进：0.36 英寸
- 段后距：8pt
- 符号：圆点（无序）或数字（有序）

### 表格

```markdown
| 表头 1 | 表头 2 | 表头 3 |
|-------|-------|-------|
| 数据 1 | 数据 2 | 数据 3 |
| 数据 4 | 数据 5 | 数据 6 |
```

**转换效果**：
- 表头：深蓝色背景 #2F5496，白色粗体文字
- 数据行：隔行浅蓝色条纹 #D9E2F3
- 边框：0.5pt 细灰线
- 对齐：表头居中，数据左对齐

### 引用

```markdown
> 这是一段引用文字。
> 可以跨越多行。
```

**转换效果**：
- 左右缩进：1.27cm
- 字体：斜体
- 颜色：灰色 #404040

### 分页符

```markdown
---
```

**转换效果**：插入分页符

---

## 样式模板选择

脚本目前默认使用**企业报告模板**（corporate_styles）。

如需切换到其他模板，修改脚本顶部的 `StyleConfig` 类：

### 切换到学术论文模板

```python
class StyleConfig:
    # 修改字体配置
    FONT_EN_TITLE = 'Times New Roman'
    FONT_EN_BODY = 'Times New Roman'
    FONT_CN_TITLE = '宋体'
    FONT_CN_BODY = '宋体'
    
    # 修改字号
    FONT_SIZE_H1 = Pt(14)
    FONT_SIZE_H2 = Pt(13)
    FONT_SIZE_H3 = Pt(12)
    FONT_SIZE_BODY = Pt(12)
    
    # 修改行距
    LINE_SPACING = 2.0  # 双倍行距
```

### 切换到通用文档模板

通用文档模板与企业报告模板类似，但颜色使用 #2F5496（较浅的蓝色）。

---

## 最佳实践

### 1. 文档结构建议

```markdown
# 文档标题（全文档仅 1 个 H1）

## 第一章：概述（H2）

### 1.1 背景（H3）
正文内容...

### 1.2 目标（H3）
正文内容...

## 第二章：分析（H2）

### 2.1 数据分析（H3）
正文内容...

#### 2.1.1 详细数据（H4，可选）
正文内容...
```

### 2. 表格优化

```markdown
# ✅ 好的表格（列数适中）
| 指标 | 2023 年 | 2024 年 | 增长率 |
|------|-------|-------|-------|
| 营收 | 100   | 120   | 20%   |
| 利润 | 20    | 25    | 25%   |

# ❌ 坏的表格（列数过多）
| 列 1 | 列 2 | 列 3 | 列 4 | 列 5 | 列 6 | 列 7 | 列 8 |
```

**建议**：表格不超过 5 列，超过则考虑拆分或转置。

### 3. 列表使用

```markdown
# ✅ 好的列表（层次清晰）
- 主要观点 1
  - 子观点 1.1
  - 子观点 1.2
- 主要观点 2

# ❌ 坏的列表（嵌套过深）
- 观点 1
  - 子观点 1.1
    - 孙观点 1.1.1
      - 曾孙观点 1.1.1.1  # 避免！
```

**建议**：列表嵌套不超过 3 层。

### 4. 段落长度

```markdown
# ✅ 好的段落（3-5 句）
这是第一句话，引出主题。这是第二句话，展开论述。
这是第三句话，提供论据。这是第四句话，总结观点。

# ❌ 坏的段落（过长）
这是第一句话...（继续写了 20 句话，500 字）读者会疲劳！

# ❌ 坏的段落（过短）
这是一句话。

这也是单独一段。（太碎了！）
```

**建议**：每段 3-8 句话，100-300 字。

---

## 常见问题

### Q1: 转换后中文乱码

**原因**：Markdown 文件编码不是 UTF-8

**解决**：
1. 用文本编辑器打开 Markdown 文件
2. 另存为 UTF-8 编码
3. 重新运行转换脚本

### Q2: 表格变形

**原因**：Markdown 表格语法错误

**解决**：
```markdown
# ✅ 正确语法
| 表头 1 | 表头 2 |
|-------|-------|
| 数据 1 | 数据 2 |

# ❌ 错误语法（分隔行缺失）
| 表头 1 | 表头 2 |
| 数据 1 | 数据 2 |
```

### Q3: 图片无法转换

**现状**：当前版本不支持图片转换

**解决**：
1. 先转换文字内容
2. 在 Word 中手动插入图片
3. 或使用 `minimax-docx` 的完整功能

### Q4: 数学公式无法转换

**现状**：LaTeX 公式不支持

**解决**：
1. 使用 Word 的公式编辑器
2. 或转换为图片后插入

---

## 输出质量检查

转换完成后，请检查以下项目：

- [ ] 所有一级标题：28pt，深蓝色，粗体
- [ ] 所有二级标题：24pt，深蓝色，粗体
- [ ] 所有三级标题：18pt，深蓝色，粗体
- [ ] 正文：11pt，深灰色，1.15 倍行距
- [ ] 表格：蓝色表头，条纹行
- [ ] 列表：悬挂缩进
- [ ] 页面边距：标准 A4 布局
- [ ] 无乱码
- [ ] 文件可正常打开

---

## 高级用法

### 批量转换

```bash
# Windows PowerShell
Get-ChildItem *.md | ForEach-Object {
    python scripts/markdown_to_word_pro.py $_.Name
}

# Linux / macOS
for file in *.md; do
    python scripts/markdown_to_word_pro.py "$file"
done
```

### 自定义样式

修改 `scripts/markdown_to_word_pro.py` 中的 `StyleConfig` 类：

```python
class StyleConfig:
    # 自定义颜色
    COLOR_PRIMARY = RGBColor(0x00, 0x66, 0xCC)  # 改为亮蓝色
    
    # 自定义字号
    FONT_SIZE_H1 = Pt(32)  # 更大的标题
    
    # 自定义间距
    SPACING_BODY_AFTER = Pt(12)  # 更大的段后距
```

---

## 与其他工具对比

| 功能 | markdown-to-word | Pandoc | Word 原生导入 |
|------|-----------------|--------|-------------|
| **样式质量** | 企业级 | 基础 | 手动设置 |
| **中文支持** | 完美 | 需配置 | 完美 |
| **表格样式** | 三线表 + 条纹 | 基础 | 手动设置 |
| **转换速度** | 5-10 秒 | 1-3 秒 | 30 分钟 + |
| **学习成本** | 零 | 中 | 高 |
| **批量处理** | 支持 | 支持 | 不支持 |

---

## 技术细节

### 依赖库

- `markdown`：Markdown 解析器
- `python-docx`：Word 文档生成
- `beautifulsoup4`：HTML 解析

### 转换流程

```
Markdown → HTML (markdown 库) → AST (BeautifulSoup) → Word (python-docx)
```

### 样式映射

```python
# Markdown
# H1 → HTML <h1> → Word H1 样式（28pt，深蓝）

# Markdown
正文 → HTML <p> → Word 正文样式（11pt，深灰）

# Markdown
|表格 | → HTML <table> → Word 三线表（蓝底白字）
```

---

## 更新日志

### v1.0.0 (2026-04-03)

- ✅ 初始版本发布
- ✅ 支持企业报告模板
- ✅ 支持所有基本 Markdown 元素
- ✅ 支持表格样式优化
- ✅ 支持中文排版

---

## 参考文献

1. [design_principles.md](design_principles.md) - 设计原则
2. [../SKILL.md](../SKILL.md) - 技能主文档
3. [../assets/styles/corporate_styles.xml](../assets/styles/corporate_styles.xml) - 企业样式配置
