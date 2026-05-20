---
name: markdown-processor
description: Markdown 文档处理整合技能 - 合并、检查、修复标题一站式解决
triggers:
  - markdown 处理
  - 文档整合
  - 标题修复
  - 标题检查
  - 文件合并
  - markdown processor
  - 一键处理
version: 1.0.0
author: Claw
update_date: 2026-04-05
changelog: 初始版本 - 整合文件合并、标题检查、标题修复三大功能
disable: false
---

# markdown-processor 技能

## 技能概述

**一站式 Markdown 文档处理工具**，整合了文件合并、标题检查、标题修复三大功能。

**核心功能**：
1. **文件合并** - 将多个 Markdown 文件合并成一个
2. **标题检查** - 检查标题结构是否合理
3. **标题修复** - 自动修复标题层级

**铁律**：只修改标题，不动内容！

---

## 快速开始

### 模式一：文件合并

```bash
python scripts/merge.py 输出.md 输入 1.md 输入 2.md 输入 3.md --skip 0 10 10
```

**参数说明**：
- `--skip 0 10 10` - 每个文件跳过的行数（删除重复标题）

### 模式二：标题检查

```bash
python scripts/check_headings.py 文件.md
```

**检查项目**：
- 标题总数
- 编号模式是否统一
- 编号模式变化点

### 模式三：标题修复

```bash
python scripts/fix_headings.py 输入.md [输出.md]
```

**修复内容**：
- ## → 第 X 章
- ### → X.Y（节）
- #### → X.Y.Z（小节）

### 模式四：一键处理（推荐）

```bash
python scripts/process.py 输入文件.md --output 输出文件.md
```

**自动完成**：
1. 检查标题
2. 修复标题
3. 生成报告

---

## 使用场景

### 场景一：整合专家报告

```bash
# Step 1: 合并文件
python scripts/merge.py netease_bp.md ^
    industry_report.md ^
    financial_report.md ^
    strategy_report.md ^
    --skip 0 10 10

# Step 2: 检查标题
python scripts/check_headings.py netease_bp.md

# Step 3: 修复标题
python scripts/fix_headings.py netease_bp.md netease_bp_fixed.md
```

### 场景二：修复混乱的标题

```bash
# 直接修复标题
python scripts/fix_headings.py chaotic_doc.md fixed_doc.md
```

### 场景三：检查文档质量

```bash
# 只检查不修改
python scripts/check_headings.py document.md
```

---

## 标题结构标准

### 优化前（混乱）
```markdown
## 执行摘要
## 一、互联网...
## 二、竞争格局...
## 二、成长能力...  ← 编号错误
## 第二章 业务...   ← 编号风格不统一
```

### 优化后（清晰）
```markdown
## 执行摘要

## 第一章 行业分析
### 1.1 市场规模
#### 1.1.1 整体规模
#### 1.1.2 增长趋势
### 1.2 竞争格局
#### 1.2.1 市场集中度

## 第二章 财务分析
### 2.1 盈利能力
### 2.2 成长能力

## 第三章 战略分析
### 3.1 业务多元化
### 3.2 AI 技术

## 参考文献
```

---

## 脚本说明

### 1. merge.py - 文件合并脚本

**功能**：将多个 Markdown 文件合并成一个

**用法**：
```bash
python scripts/merge.py 输出.md 输入 1.md 输入 2.md --skip 0 10
```

**参数**：
- `--skip` - 每个文件跳过的行数

### 2. check_headings.py - 标题检查脚本

**功能**：检查标题结构

**用法**：
```bash
python scripts/check_headings.py 文件.md
```

**输出**：
- 标题总数
- 编号模式分析
- 问题报告

### 3. fix_headings.py - 标题修复脚本

**功能**：自动修复标题层级

**用法**：
```bash
python scripts/fix_headings.py 输入.md [输出.md]
```

**规则**：
- 根据编号中的点数判断层级
- 1 个点（1.1）→ ###
- 2 个点（1.1.1）→ ####

### 4. process.py - 一键处理脚本

**功能**：自动完成检查 + 修复

**用法**：
```bash
python scripts/process.py 输入.md --output 输出.md
```

---

## 技术细节

### 标题层级判断逻辑

```python
# 计算编号中的点数
dots = text.count('.')

if dots >= 2:
    # 两位数字（如 1.1.1）→ #### X.Y.Z（小节）
    return f"#### {chapter}.{section}.{subsection} {clean}\n"
else:
    # 一位数字（如 1.1）→ ### X.Y（节）
    return f"### {chapter}.{section} {clean}\n"
```

### 真假参考文献判断

```python
# 检查后面 5 行内是否有以数字开头的行
for j in range(i+1, min(i+6, len(lines))):
    if re.match(r'^\d+\.', lines[j].strip()):
        is_real = True  # 真参考文献
        break
```

---

## 常见问题

### Q1: 合并后为什么有多个重复标题？

**A**: 因为每个文件都有自己的标题。解决方法：

```bash
python scripts/merge.py output.md file1.md file2.md --skip 0 10 10
# 第一个文件保留，后续文件跳过前 10 行
```

### Q2: 如何确定要跳过多少行？

**A**: 打开文件数一下：
- 标题行（`# xxx`）- 1 行
- 空行 - 1 行
- 执行摘要标题（`## 执行摘要`）- 1 行
- 空行 - 1 行
- 执行摘要内容 - 约 5-8 行

通常跳过 **8-10 行** 就够。

### Q3: 修复后标题不对怎么办？

**A**: 先用 `check_headings.py` 检查，查看问题报告，然后调整修复逻辑。

### Q4: 支持其他 Markdown 文件吗？

**A**: 支持！脚本是通用的，可以处理任何 Markdown 文件。

---

## 更新日志

### v1.0.0 (2026-04-05)

- ✅ 初始版本发布
- ✅ 整合文件合并功能
- ✅ 整合标题检查功能
- ✅ 整合标题修复功能
- ✅ 新增一键处理模式
- ✅ 支持真假参考文献识别

---

## 参考文档

- [merge.py](scripts/merge.py) - 文件合并脚本
- [check_headings.py](scripts/check_headings.py) - 标题检查脚本
- [fix_headings.py](scripts/fix_headings.py) - 标题修复脚本
- [process.py](scripts/process.py) - 一键处理脚本

---

**技能位置**: `C:\Users\吴传奇\.workbuddy\skills\markdown-processor\`

**创建日期**: 2026-04-05  
**维护者**: Claw
