#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图表表格自动计数脚本
用于 business-plan-creator 质量检查关口
自动统计 Markdown 文档中的图表和表格数量
"""

import re
import sys
from pathlib import Path

def count_images(markdown_file):
    """统计 Markdown 文件中的图片数量"""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Markdown 图片语法：![描述](路径)
    image_pattern = r'!\[.*?\]\(.*?\)'
    images = re.findall(image_pattern, content)
    
    return len(images), images

def count_tables(markdown_file):
    """统计 Markdown 文件中的表格数量"""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    table_count = 0
    in_table = False
    
    for i, line in enumerate(lines):
        # 表格开始：包含 | 且下一行包含 |---|
        if '|' in line and i + 1 < len(lines):
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            if re.match(r'\s*\|?\s*[-:]+[-|\s:]+\|?\s*', next_line):
                table_count += 1
                in_table = True
        # 简单表格检测：连续的 | 分隔行
        elif '|' in line and not in_table:
            # 检查是否是表格行（至少 2 个 |）
            if line.count('|') >= 2:
                # 向前检查是否有表头
                if i > 0 and lines[i-1].count('|') >= 2:
                    table_count += 1
                    in_table = True
    
    return table_count

def count_by_chapter(markdown_file):
    """按章节统计图表和表格数量"""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = f.readlines() if content else []
    
    # 重新读取用于分行处理
    with open(markdown_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    chapters = {}
    current_chapter = "执行摘要"
    chapter_images = 0
    chapter_tables = 0
    
    for i, line in enumerate(lines):
        # 检测章节标题（## 或 # 开头）
        chapter_match = re.match(r'^#+\s+(.+)', line)
        if chapter_match:
            # 保存前一章的统计
            if current_chapter:
                chapters[current_chapter] = {
                    'images': chapter_images,
                    'tables': chapter_tables
                }
            current_chapter = chapter_match.group(1).strip()
            chapter_images = 0
            chapter_tables = 0
        
        # 统计图片
        if re.search(r'!\[.*?\]\(.*?\)', line):
            chapter_images += 1
        
        # 统计表格
        if '|' in line and i + 1 < len(lines):
            next_line = lines[i + 1]
            if re.match(r'\s*\|?\s*[-:]+[-|\s:]+\|?\s*', next_line):
                chapter_tables += 1
    
    # 保存最后一章
    chapters[current_chapter] = {
        'images': chapter_images,
        'tables': chapter_tables
    }
    
    return chapters

def generate_report(markdown_file):
    """生成图表表格统计报告"""
    total_images, image_list = count_images(markdown_file)
    total_tables = count_tables(markdown_file)
    chapter_stats = count_by_chapter(markdown_file)
    
    print("=" * 80)
    print(f"图表表格统计报告 - {Path(markdown_file).name}")
    print("=" * 80)
    print(f"\n文件：{markdown_file}")
    print(f"统计时间：{Path(markdown_file).stat().st_mtime}")
    print()
    
    # 总体统计
    print("【总体统计】")
    print(f"  图表总数：{total_images} 张")
    print(f"  表格总数：{total_tables} 个")
    print()
    
    # 质量标准检查
    print("【质量标准检查】")
    if total_images >= 10:
        print(f"  ✅ 图表数量达标（{total_images}/10）")
    else:
        print(f"  ❌ 图表数量不足（{total_images}/10）- 需要至少 10 张图表")
    
    if total_tables >= 8:
        print(f"  ✅ 表格数量达标（{total_tables}/8）")
    else:
        print(f"  ❌ 表格数量不足（{total_tables}/8）- 需要至少 8 个表格")
    print()
    
    # 分章节统计
    print("【分章节统计】")
    print("-" * 80)
    for chapter, stats in chapter_stats.items():
        image_status = "✅" if stats['images'] >= 2 else "❌"
        table_status = "✅" if stats['tables'] >= 2 else "❌"
        print(f"  {chapter}")
        print(f"    图表：{stats['images']} 张 {image_status}（标准：≥2 张）")
        print(f"    表格：{stats['tables']} 个 {table_status}（标准：≥2 个）")
    print("-" * 80)
    print()
    
    # 问题章节
    print("【问题章节警告】")
    issues_found = False
    for chapter, stats in chapter_stats.items():
        if stats['images'] == 0:
            print(f"  ⚠️  {chapter}：图表数量为 0 - 必须添加至少 2 张图表")
            issues_found = True
        if stats['tables'] == 0:
            print(f"  ⚠️  {chapter}：表格数量为 0 - 必须添加至少 2 个表格")
            issues_found = True
    
    if not issues_found:
        print("  ✅ 所有章节图表表格数量均达标")
    print()
    
    # 最终结论
    print("【最终结论】")
    if total_images >= 10 and total_tables >= 8:
        print("  ✅ 通过质量检查 - 图表表格数量符合标准")
        return True
    else:
        print("  ❌ 未通过质量检查 - 图表表格数量不足")
        print()
        print("  处理建议：")
        if total_images < 10:
            print(f"    1. 需要增加 {10 - total_images} 张图表")
        if total_tables < 8:
            print(f"    2. 需要增加 {8 - total_tables} 个表格")
        print()
        print("  打回重做：根据质量检查清单 v4.5.4，图表表格数量不足直接打回重做")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python count_charts_tables.py <markdown 文件路径>")
        print("示例：python count_charts_tables.py integrated/bp_final.md")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    
    if not Path(markdown_file).exists():
        print(f"错误：文件不存在 - {markdown_file}")
        sys.exit(1)
    
    success = generate_report(markdown_file)
    sys.exit(0 if success else 1)
