#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
初始化 business-writer 技能
创建必要的目录结构和配置文件
"""

import os
import sys
import json
from pathlib import Path

def init_skill(skill_name="business-writer"):
    """初始化技能目录结构"""
    
    # 获取技能路径
    if len(sys.argv) > 1:
        skill_path = Path(sys.argv[1])
    else:
        skill_path = Path(f"skills/{skill_name}")
    
    print(f"初始化技能：{skill_path}")
    
    # 创建目录结构
    directories = [
        "references",
        "examples",
        "templates"
    ]
    
    for dir_name in directories:
        dir_path = skill_path / dir_name
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"✓ 创建目录：{dir_path}")
    
    # 创建 .gitkeep 文件
    for dir_name in directories:
        gitkeep_path = skill_path / dir_name / ".gitkeep"
        if not gitkeep_path.exists():
            gitkeep_path.write_text("")
    
    # 创建技能元数据
    meta_file = skill_path / "_skillhub_meta.json"
    if not meta_file.exists():
        meta_data = {
            "name": "business-writer",
            "version": "1.0.0",
            "description": "商业写作引擎 - 将原始数据和分析结果转化为专业商业论述",
            "author": "Claw",
            "created_at": "2026-03-31",
            "updated_at": "2026-03-31",
            "tags": ["写作", "商业分析", "商业计划书", "财务分析"],
            "triggers": [
                "商业写作",
                "撰写商业计划书",
                "写财务分析",
                "写行业分析",
                "写竞争分析",
                "写战略分析"
            ]
        }
        meta_file.write_text(json.dumps(meta_data, ensure_ascii=False, indent=2))
        print(f"✓ 创建元数据：{meta_file}")
    
    # 创建 README
    readme_file = skill_path / "README.md"
    if not readme_file.exists():
        readme_content = """# Business Writer - 商业写作引擎

## 技能定位

将原始数据和分析结果转化为专业商业论述的 AI 写作助手。

## 核心能力

- ✅ 三层论述结构（What-Why-How）
- ✅ 主旨式标题生成
- ✅ 段落衔接优化
- ✅ AI 味消除
- ✅ 章节专属写作指南
- ✅ 质量自检清单

## 使用场景

1. 商业计划书撰写
2. 财务分析报告
3. 行业分析报告
4. 投资分析报告
5. 竞争分析报告
6. 战略规划报告

## 快速开始

```python
# 调用示例
from business_writer import write_section

content = write_section(
    chapter="财务分析",
    section="盈利能力分析",
    data={...},  # 结构化数据
    context={...}  # 上下文信息
)
```

## 文档结构

- `SKILL.md` - 技能主文档
- `references/` - 参考文档
  - `writing-standards.md` - 写作标准
  - `chapter-guides.md` - 章节指南
  - `example-library.md` - 示例库
- `examples/` - 写作示例
- `templates/` - 写作模板

## 版本

v1.0 - 2026-03-31
"""
        readme_file.write_text(readme_content)
        print(f"✓ 创建 README: {readme_file}")
    
    print(f"\n✅ 技能初始化完成：{skill_path}")
    print(f"\n下一步：")
    print(f"1. 编辑 SKILL.md 完善技能说明")
    print(f"2. 在 references/ 添加参考文档")
    print(f"3. 在 examples/ 添加写作示例")
    print(f"4. 在 templates/ 添加写作模板")

if __name__ == "__main__":
    init_skill()
