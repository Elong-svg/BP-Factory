#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Harness 约束 #2：章节去重检查
在合并前运行，检测是否有重复章节（编号冲突 / 标题相似度 > 80%）

用法：
    python chapter_dedup.py <sections_dir>
    退出码：0=通过（无重复），1=失败（有重复）
"""

import sys
import os
import re
from pathlib import Path
from difflib import SequenceMatcher


def extract_chapter_info(filepath):
    """从 Markdown 文件中提取章节信息"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 查找章节标题
    chapter_patterns = [
        (r'^#\s+第([一二三四五六七八九十\d]+)章\s+(.+)', 'h1'),
        (r'^##\s+第([一二三四五六七八九十\d]+)章\s+(.+)', 'h2'),
        (r'^#\s+(.+)', 'h1_generic'),  # 通用 H1
    ]

    chapters = []
    for line in content.split('\n'):
        line = line.strip()
        for pattern, ptype in chapter_patterns:
            m = re.match(pattern, line)
            if m:
                if ptype in ('h1', 'h2'):
                    chapters.append({
                        'number': m.group(1),
                        'title': m.group(2).strip(),
                        'level': ptype,
                        'file': str(filepath)
                    })
                elif ptype == 'h1_generic':
                    title = m.group(1).strip()
                    # 检查是否是执行摘要
                    if '摘要' in title or 'executive' in title.lower():
                        chapters.append({
                            'number': '摘要',
                            'title': title,
                            'level': 'summary',
                            'file': str(filepath)
                        })
    return chapters


def check_duplicates(sections_dir):
    """检查章节重复"""
    section_files = sorted(Path(sections_dir).glob('*.md'))
    if not section_files:
        print("❌ 错误：sections 目录下没有 .md 文件")
        return False, []

    print(f"📁 检查 {len(section_files)} 个章节文件...")
    print()

    all_chapters = []
    for f in section_files:
        chapters = extract_chapter_info(f)
        if chapters:
            all_chapters.extend(chapters)
            print(f"  📄 {f.name}: {len(chapters)} 个章节标题")
        else:
            print(f"  ⚠️  {f.name}: 未检测到章节标题")

    print()

    # 检查 1：编号冲突
    print("【检查 1】章节编号冲突检测")
    number_map = {}
    duplicates = []
    for ch in all_chapters:
        key = ch['number']
        if key in number_map:
            existing = number_map[key]
            duplicates.append({
                'type': '编号冲突',
                'number': key,
                'file_a': existing['file'],
                'title_a': existing['title'],
                'file_b': ch['file'],
                'title_b': ch['title']
            })
            print(f"  ❌ 编号冲突：「第{key}章」")
            print(f"     A: {os.path.basename(existing['file'])} → {existing['title']}")
            print(f"     B: {os.path.basename(ch['file'])} → {ch['title']}")
        else:
            number_map[key] = ch

    if not duplicates:
        print("  ✅ 无编号冲突")

    # 检查 2：标题相似度
    print()
    print("【检查 2】标题相似度检测")
    sim_duplicates = []
    for i, ch_a in enumerate(all_chapters):
        for j, ch_b in enumerate(all_chapters):
            if j <= i:
                continue
            ratio = SequenceMatcher(None, ch_a['title'], ch_b['title']).ratio()
            if ratio > 0.75:
                sim_duplicates.append({
                    'type': '标题相似',
                    'similarity': f"{ratio:.1%}",
                    'file_a': ch_a['file'],
                    'title_a': ch_a['title'],
                    'file_b': ch_b['file'],
                    'title_b': ch_b['title']
                })
                print(f"  ❌ 标题相似 ({ratio:.1%})")
                print(f"     A: {os.path.basename(ch_a['file'])} → {ch_a['title']}")
                print(f"     B: {os.path.basename(ch_b['file'])} → {ch_b['title']}")

    if not sim_duplicates:
        print("  ✅ 无标题相似")

    # 汇总
    all_issues = duplicates + sim_duplicates
    print()
    print("=" * 70)
    if not all_issues:
        print("✅ Harness 检查通过：无章节重复")
        return True, all_chapters
    else:
        print(f"❌ Harness 检查失败：发现 {len(all_issues)} 个重复问题")
        print()
        print("处理建议：")
        print("  1. 编号冲突 → 重命名其中一个章节编号")
        print("  2. 标题相似 → 保留内容更完整的版本，删除另一个")
        print("  3. 修复后重新运行本脚本验证")
        return False, all_chapters


def main():
    if len(sys.argv) < 2:
        print("用法：python chapter_dedup.py <sections_dir>")
        print("示例：python chapter_dedup.py bp_sections/")
        sys.exit(1)

    sections_dir = sys.argv[1]
    if not os.path.isdir(sections_dir):
        print(f"❌ 目录不存在：{sections_dir}")
        sys.exit(1)

    passed, _ = check_duplicates(sections_dir)
    sys.exit(0 if passed else 1)


if __name__ == '__main__':
    main()
