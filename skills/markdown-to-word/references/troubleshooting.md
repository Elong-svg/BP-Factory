# markdown-to-word 故障排查指南

**版本**: v1.2.0  
**最后更新**: 2026-04-03  
**作者**: Claw

---

## 常见问题与解决方案

### 问题 1：表格转换为字符画而不是 Word 原生表格

**症状**：
- Word 中显示的表格是由 `|`、`-` 等字符组成的文本
- 表格不可编辑，无法选中单元格
- 看起来像是用横线竖线拼成的 ASCII 艺术

**根本原因**：
Markdown 表格前后没有空行，导致 `markdown` 库无法正确解析为 HTML `<table>` 元素。

**错误示例**：
```markdown
**设计模板**:
| 类型 | 封面图案 | 视觉风格 |
|------|---------|---------|
| report | fullbleed | 深色背景 |
```

**正确示例**：
```markdown
**设计模板**:

| 类型 | 封面图案 | 视觉风格 |
|------|---------|---------|
| report | fullbleed | 深色背景 |

**使用方式**:
```

**解决方案**：

1. **脚本自动修复**（v1.2.0+）：
   脚本已内置 Markdown 预处理功能，自动在表格前后添加空行：

   ```python
   # 1.5 预处理 Markdown：确保表格前后有空行
   import re
   table_pattern = r'^(\s*\|.+\|\s*\n\s*\|[-|\s]+\|\s*\n(?:\s*\|.+\|\s*\n)*)'
   
   def ensure_blank_lines(match):
       table = match.group(1)
       return '\n' + table + '\n'
   
   md_text = re.sub(table_pattern, ensure_blank_lines, md_text, flags=re.MULTILINE)
   ```

2. **手动修复源文件**：
   确保所有 Markdown 表格前后都有空行。

**验证方法**：
- 转换日志中显示 `[TABLE] 创建表格：X 列×Y 行`
- Word 中可以选中表格单元格
- 可以调整列宽、应用样式

---

### 问题 2：表格样式不显示（表头无背景色、无条纹）

**症状**：
- 表格是 Word 原生表格，可以编辑
- 但表头没有蓝色背景，是白色
- 没有隔行条纹
- 看起来像普通表格

**根本原因**：
1. 使用了 `Table Grid` 预设样式，覆盖了自定义背景色
2. 使用了错误的 XML 元素设置背景色

**错误代码**（v1.1.0 及更早版本）：
```python
table.style = 'Table Grid'  # ❌ 会覆盖自定义样式

# 使用 tcFill 设置背景
tcFill = OxmlElement('w:tcFill')
tcFill.set(qn('w:color'), '2F5496')
```

**解决方案**（v1.2.0+）：

1. **不使用预设样式**：
   ```python
   table = doc.add_table(rows=1 + len(rows), cols=len(headers))
   # 不设置 table.style，完全自定义
   ```

2. **使用 shading 元素**：
   ```python
   # 设置表头背景
   tc = cell._element.tcPr
   tcShd = OxmlElement('w:shd')
   tcShd.set(qn('w:val'), 'clear')
   tcShd.set(qn('w:color'), 'auto')
   tcShd.set(qn('w:fill'), '2F5496')  # RGB 顺序
   tc.append(tcShd)
   
   # 设置条纹行
   if row_idx % 2 == 0:
       tcShd = OxmlElement('w:shd')
       tcShd.set(qn('w:fill'), 'D9E2F3')  # 浅蓝色
       tc.append(tcShd)
   ```

3. **添加表格边框**：
   ```python
   tbl = table._element
   tblPr = tbl.tblPr
   if tblPr is None:
       tblPr = OxmlElement('w:tblPr')
       tbl.insert(0, tblPr)
   
   tblBorders = OxmlElement('w:tblBorders')
   for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
       border = OxmlElement(f'w:{border_name}')
       border.set(qn('w:val'), 'single')
       border.set(qn('w:sz'), '4')  # 0.5pt
       border.set(qn('w:color'), 'CCCCCC')
       tblBorders.append(border)
   
   tblPr.append(tblBorders)
   ```

**验证方法**：
- 表头显示蓝色背景（`#2F5496`）
- 偶数行显示浅蓝色条纹（`#D9E2F3`）
- 表格边框是细灰线

---

### 问题 3：表格颜色反转（蓝色变红色）

**症状**：
- 表头背景是红色或橙色，而不是蓝色
- 条纹颜色也不对

**根本原因**：
Word 的 XML 元素中，颜色顺序要求不同：
- `w:tcFill`（单元格填充）：需要 **BGR** 顺序
- `w:shd`（shading 着色）：需要 **RGB** 顺序

**错误代码**：
```python
# ❌ 错误：shading 使用了 BGR 顺序
header_color_hex = '2F5496'  # RGB: 蓝色
r, g, b = header_color_hex[0:2], header_color_hex[2:4], header_color_hex[4:6]
tcShd.set(qn('w:fill'), f'{b}{g}{r}')  # 变成 96542F: 红色
```

**正确代码**（v1.2.0+）：
```python
# ✅ 正确：shading 使用 RGB 顺序（不需要反转）
header_color_hex = str(config.COLOR_TABLE_HEADER_BG)
tcShd.set(qn('w:fill'), header_color_hex)  # 直接使用，如 '2F5496'
```

**记忆技巧**：
- **shd** (shading) = **S**ame as RGB（和 RGB 一样）
- **tcFill** = **F**lip（需要翻转）

**验证方法**：
- 表头应该是深蓝色（`#2F5496`）
- 条纹应该是浅蓝色（`#D9E2F3`）
- 不是红色、橙色或其他颜色

---

### 问题 4：emoji 导致转换失败

**症状**：
```
UnicodeEncodeError: 'gbk' codec can't encode character '\U0001f4d6'
```

**原因**：
Windows PowerShell 默认使用 GBK 编码，无法输出 emoji。

**解决方案**（v1.0.1+）：
移除所有 emoji，使用纯文本标记：
- `[INFO]` 代替 📖
- `[SUCCESS]` 代替 ✅
- `[ERROR]` 代替 ❌
- `[TABLE]` 代替 📊

---

### 问题 5：中文字体设置失败

**症状**：
```
AttributeError: 'NoneType' object has no attribute 'set'
```

**原因**：
`run._element.rPr` 可能为 `None`。

**解决方案**：
```python
def set_chinese_font(run, font_name):
    """设置中文字体"""
    rPr = run._element.get_or_add_rPr()
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:eastAsia'), font_name)
    rFonts.set(qn('w:ascii'), font_name)
    rFonts.set(qn('w:hAnsi'), font_name)
    rFonts.set(qn('w:cs'), font_name)
    rPr.insert(0, rFonts)
```

---

## 版本更新记录

### v1.2.0 (2026-04-03)

**修复**：
- ✅ 表格转换问题（Markdown 预处理，自动添加空行）
- ✅ 表格样式问题（使用 shading 而不是 tcFill）
- ✅ 颜色反转问题（RGB vs BGR 顺序）

**改进**：
- ✅ 表格边框自定义（细灰线 0.5pt）
- ✅ 表头背景：深蓝色 `#2F5496`
- ✅ 隔行条纹：浅蓝色 `#D9E2F3`

### v1.1.0 (2026-04-03)

**新增**：
- ✅ 3 套模板选择（corporate/academic/default）
- ✅ 命令行参数支持（`-t`, `-o`）
- ✅ XML 配置加载

### v1.0.0 (2026-04-03)

**初始版本**：
- ✅ Markdown → Word 基本转换
- ✅ 企业报告模板
- ✅ 中文排版支持

---

## 测试清单

转换完成后，请检查以下项目：

### 基础检查
- [ ] 文档可以正常打开
- [ ] 无乱码
- [ ] 标题层级正确（H1/H2/H3）
- [ ] 正文段落完整

### 表格检查（重要）
- [ ] 表格是 Word 原生表格（可选中、可编辑）
- [ ] 不是字符画（不是用 `|`、`-` 拼成的）
- [ ] 表头有蓝色背景（`#2F5496`）
- [ ] 表头文字是白色粗体
- [ ] 偶数行有浅蓝色条纹（`#D9E2F3`）
- [ ] 表格边框是细灰线
- [ ] 列宽可以调整
- [ ] 可以添加/删除行

### 样式检查
- [ ] 一级标题：28pt，深蓝色
- [ ] 二级标题：24pt，深蓝色
- [ ] 三级标题：18pt，深蓝色
- [ ] 正文：11pt，深灰色
- [ ] 行距：1.15 倍
- [ ] 段后距：8pt

---

## 联系支持

如果遇到问题：
1. 查看转换日志，寻找错误信息
2. 检查 Markdown 源文件格式
3. 确认表格前后有空行
4. 查看本故障排查指南

**技能位置**：`C:\Users\吴传奇\.workbuddy\skills\markdown-to-word\`

---

**最后更新**: 2026-04-03  
**版本**: v1.2.0
