#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown 标题检查工具
检查 Markdown 文件中的标题顺序是否正确，识别编号模式变化

用法：
    python check_headings.py 文件.md
"""

import sys
import re

if len(sys.argv) < 2:
    print("用法：python check_headings.py 文件.md")
    print("\n检查 Markdown 文件中的标题顺序：")
    print("  - 提取所有二级标题（## ）")
    print("  - 统计标题总数")
    print("  - 识别编号模式（中文数字、章节编号、阿拉伯数字、无编号）")
    print("  - 检测编号模式变化点")
    print("  - 生成详细报告")
    sys.exit(1)

md_file = sys.argv[1]

import os
if not os.path.exists(md_file):
    print(f"[错误] 文件不存在：{md_file}")
    sys.exit(1)

with open(md_file, 'r', encoding='utf-8') as f:
    content = f.read()

print("\n" + "=" * 80)
print("[标题分析报告]")
print("=" * 80)

# 提取所有二级标题
headings = []
lines = content.split('\n')
for i, line in enumerate(lines, 1):
    if line.startswith('## '):
        text = line[3:].strip()
        headings.append({'line': i, 'text': text})
        print(f"{len(headings):3d}. 行{i:4d}: {text}")

print("\n" + "=" * 80)
print(f"[统计] 共 {len(headings)} 个二级标题")
print("=" * 80)

# 检查编号模式
print("\n[编号模式分析]")
print("-" * 80)

patterns = {
    'chinese': r'^[一二三四五六七八九十]+、',
    'chapter': r'^第 [一二三四五六七八九十\d]+章',
    'arabic': r'^\d+\.',
    'none': '无编号'
}

current_pattern = None
changes = []

for i, h in enumerate(headings, 1):
    text = h['text']
    detected = 'none'
    
    for name, pattern in patterns.items():
        if name != 'none' and re.match(pattern, text):
            detected = name
            break
    
    if current_pattern and detected != current_pattern:
        changes.append({
            'index': i,
            'line': h['line'],
            'from': current_pattern,
            'to': detected,
            'text': text
        })
    
    current_pattern = detected

if changes:
    print(f"\n发现 {len(changes)} 处编号模式变化：\n")
    for c in changes:
        print(f"  第{c['index']}个标题（行{c['line']}）: {c['from']} → {c['to']}")
        print(f"    标题：{c['text']}")
    print("\n[结论] 编号模式不统一，需要调整")
else:
    print("\n[结论] 编号模式统一")

print("\n" + "=" * 80)
