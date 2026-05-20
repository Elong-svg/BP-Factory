# Step 3: 文档整合与输出（简化版）

## 核心流程

```
markdown-merger 合并 → markdown-processor 修复标题 → markdown-to-word 生成 Word
```

## 调用方法

### Step 3.1: 合并专家文档

```bash
python C:/Users/吴传奇/.workbuddy/skills/markdown-processor/scripts/merge.py 拼接.md 行业.md 财务.md 战略.md --skip 0 10 10
```

**参数说明**：
- `--skip 0 10 10` - 第一个文件保留，后续文件跳过前 10 行（删除重复标题）

### Step 3.2: 修复标题（一键处理）

```bash
python C:/Users/吴传奇/.workbuddy/skills/markdown-processor/scripts/process.py 拼接.md --output 修复.md
```

**自动完成**：
- ✅ 标题层级识别（根据编号中的点数）
- ✅ 标题格式统一（## → 第 X 章，### → X.Y，#### → X.Y.Z）
- ✅ 假参考文献识别与删除
- ✅ 检查 + 修复一键完成

### Step 3.3: 生成 Word 文档

```bash
python C:/Users/吴传奇/.workbuddy/skills/markdown-to-word/scripts/markdown_to_word_pro.py 修复.md 输出.docx
```

## 技能位置

- **markdown-processor**: `C:\Users\吴传奇\.workbuddy\skills\markdown-processor\`
  - `merge.py` - 文件合并脚本
  - `process.py` - 一键处理脚本
  - `fix_headings.py` - 标题修复脚本
  - `check_headings.py` - 标题检查脚本

- **markdown-to-word**: `C:\Users\吴传奇\.workbuddy\skills\markdown-to-word\`
  - `markdown_to_word_pro.py` - Word 文档生成脚本

## 核心优势

- ✅ 自动化 - 无需手动整合
- ✅ 智能化 - 自动识别标题层级
- ✅ 简洁化 - 一键完成检查 + 修复
- ✅ 专业化 - 统一标题格式

---

**版本**：v4.5.3（2026-04-05 更新）  
**更新内容**：整合 markdown-processor 技能，简化 Step 3 流程  
**维护者**：Claw
