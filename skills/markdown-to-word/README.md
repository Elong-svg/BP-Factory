# markdown-to-word 技能

**一键将 Markdown 转换为专业 Word 文档，应用企业级设计系统。**

**最新版本**: v1.2.0（2026-04-03）  
**更新内容**: 修复表格转换问题（Markdown 预处理 + 样式应用）

---

## 快速开始

### 1. 安装依赖

```bash
pip install markdown python-docx beautifulsoup4
```

### 2. 使用技能

```bash
# 调用技能
python scripts/markdown_to_word_pro.py 输入文件.md

# 示例
python scripts/markdown_to_word_pro.py 会计研究趋势.md
# 输出：会计研究趋势_专业版.docx
```

---

## 核心功能

✅ **一键转换** - Markdown → Word，5-10 秒完成  
✅ **企业级样式** - 应用 minimax-docx 设计系统  
✅ **中文优化** - 完美支持中文排版（黑体 + 微软雅黑）  
✅ **表格美化** - 自动应用三线表 + 条纹样式（v1.2.0 修复）  
✅ **不会长线程** - 纯本地 Python 脚本，稳定可靠  
✅ **模板选择** - 支持 3 套模板（corporate/academic/default）  

---

## 设计系统

### 企业报告模板（默认）

| 元素 | 字体 | 字号 | 颜色 | 间距 |
|------|------|------|------|------|
| H1 | Calibri Light + 黑体 | 28pt | #1F3864 深蓝 | 前 24pt/后 12pt |
| H2 | Calibri Light + 黑体 | 24pt | #1F3864 深蓝 | 前 18pt/后 6pt |
| H3 | Calibri Light + 黑体 | 18pt | #1F3864 深蓝 | 前 12pt/后 4pt |
| 正文 | Calibri + 微软雅黑 | 11pt | #333333 深灰 | 后 8pt, 1.15 倍行距 |
| 表格 | - | - | #2F5496 蓝底白字 | 条纹行 #D9E2F3 |

---

## 文件结构

```
markdown-to-word/
├── SKILL.md                      # 技能主文档
├── README.md                     # 快速入门
├── scripts/
│   └── markdown_to_word_pro.py   # 核心转换脚本
├── references/
│   ├── design_principles.md      # 设计原则
│   ├── usage_guide.md            # 使用指南
│   └── troubleshooting.md        # 故障排查（v1.2.0 新增）
└── assets/
    └── styles/
        ├── corporate_styles.xml  # 企业样式
        ├── academic_styles.xml   # 学术样式
        └── default_styles.xml    # 默认样式
```

---

## 支持的 Markdown 元素

| Markdown | Word 映射 | 样式说明 |
|---------|----------|---------|
| `# H1` | 一级标题 | 28pt，深蓝色，粗体 |
| `## H2` | 二级标题 | 24pt，深蓝色，粗体 |
| `### H3` | 三级标题 | 18pt，深蓝色，粗体 |
| 正文 | 正文 | 11pt，深灰色，1.15 倍行距 |
| `**粗体**` | 粗体 | 保留格式 |
| `*斜体*` | 斜体 | 保留格式 |
| `- 列表` | 无序列表 | 圆点符号，悬挂缩进 |
| `1. 列表` | 有序列表 | 数字编号，悬挂缩进 |
| `|表格|` | 三线表 | 蓝色表头，条纹行 |
| `> 引用` | 引用块 | 灰色斜体，左右缩进 |
| `---` | 分页符 | 插入分页符 |

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
- ✅ 深蓝色一级标题（28pt）
- ✅ 深蓝色二级标题（24pt）
- ✅ 正文 11pt，1.15 倍行距
- ✅ 专业三线表（蓝色表头，条纹行）
- ✅ 标准 A4 页面布局

---

## 与其他工具对比

| 功能 | markdown-to-word | Pandoc | Word 原生导入 |
|------|-----------------|--------|-------------|
| **样式质量** | ⭐⭐⭐⭐⭐ 企业级 | ⭐⭐⭐ 基础 | ⭐⭐⭐⭐⭐ 手动设置 |
| **中文支持** | ⭐⭐⭐⭐⭐ 完美 | ⭐⭐⭐ 需配置 | ⭐⭐⭐⭐⭐ 完美 |
| **表格样式** | ⭐⭐⭐⭐⭐ 自动美化 | ⭐⭐ 基础 | ⭐⭐⭐⭐⭐ 手动设置 |
| **转换速度** | ⭐⭐⭐⭐⭐ 5-10 秒 | ⭐⭐⭐⭐⭐ 1-3 秒 | ⭐ 30 分钟 + |
| **学习成本** | ⭐⭐⭐⭐⭐ 零学习 | ⭐⭐⭐ 中等 | ⭐ 高 |

---

## 常见问题

### Q: 支持图片吗？

A: 当前版本不支持。转换后需手动在 Word 中插入图片。

### Q: 支持数学公式吗？

A: 不支持 LaTeX 公式。需使用 Word 公式编辑器。

### Q: 如何切换样式模板？

A: 修改 `scripts/markdown_to_word_pro.py` 中的 `StyleConfig` 类。

### Q: 批量转换？

A: 
```bash
# PowerShell
Get-ChildItem *.md | ForEach-Object {
    python scripts/markdown_to_word_pro.py $_.Name
}
```

---

## 技术实现

### 依赖库

```bash
pip install markdown python-docx beautifulsoup4
```

### 转换流程

```
Markdown (.md)
    ↓ (markdown 库)
HTML
    ↓ (BeautifulSoup)
AST (抽象语法树)
    ↓ (python-docx)
Word (.docx)
```

### 核心代码

```python
# 详见 scripts/markdown_to_word_pro.py
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

## 许可证

MIT License

---

## 联系方式

- **作者**: Claw（董事长助理 AI）
- **技能来源**: 学习自 `minimax-docx` 设计系统
- **创建日期**: 2026-04-03

---

## 下一步

1. **测试技能**：找一个 Markdown 文件测试转换
2. **反馈问题**：如有问题，查看 [usage_guide.md](references/usage_guide.md)
3. **自定义样式**：修改 `StyleConfig` 类来自定义样式

**享受一键转换的便利！** 🎉
