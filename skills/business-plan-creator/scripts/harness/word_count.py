#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Harness 约束 #4：字数合规性检查
检查 Markdown 文档的字数是否达标，防止虚报。

用法：
    python word_count.py <markdown_file> [--min-chars 20000]
    退出码：0=达标，1=字数不足，2=严重不足（< 50% 标准）
"""

import sys
import os
import re
from pathlib import Path


def count_chinese_chars(text):
    """统计中文字符数（不含标点空格）"""
    chinese_pattern = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf]')
    return len(chinese_pattern.findall(text))


def count_english_words(text):
    """统计英文单词数"""
    # 移除中文后统计英文单词
    cleaned = re.sub(r'[\u4e00-\u9fff\u3400-\u4dbf]', ' ', text)
    words = cleaned.split()
    # 过滤纯数字和单字符
    meaningful = [w for w in words if not w.isdigit() and len(w) > 1]
    return len(meaningful)


def total_word_count(text):
    """总字数 = 中文字符 + 英文单词"""
    return count_chinese_chars(text) + count_english_words(text)


def count_by_chapter(markdown_file):
    """按章节统计字数"""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    chapters = {}
    current_chapter = "前言"
    current_text = []

    for line in lines:
        # 检测章节标题
        chapter_match = re.match(r'^#{1,3}\s+(.+)', line)
        if chapter_match and ('章' in line or '摘要' in line):
            # 保存前一章
            text = '\n'.join(current_text)
            if text.strip():
                chapters[current_chapter] = total_word_count(text)
            current_chapter = chapter_match.group(1).strip()
            current_text = []
        else:
            current_text.append(line)

    # 保存最后一章
    text = '\n'.join(current_text)
    if text.strip():
        chapters[current_chapter] = total_word_count(text)

    return chapters


def main():
    min_chars = 20000

    if len(sys.argv) < 2:
        print("用法：python word_count.py <markdown_file> [--min-chars N]")
        print("示例：python word_count.py bp_final.md --min-chars 20000")
        sys.exit(1)

    md_file = sys.argv[1]
    for i, arg in enumerate(sys.argv):
        if arg == '--min-chars' and i + 1 < len(sys.argv):
            min_chars = int(sys.argv[i + 1])

    if not os.path.exists(md_file):
        print(f"❌ 文件不存在：{md_file}")
        sys.exit(1)

    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    file_size = len(content.encode('utf-8'))
    chinese = count_chinese_chars(content)
    english = count_english_words(content)
    total = chinese + english

    chapter_counts = count_by_chapter(md_file)

    print("=" * 70)
    print("📝 Harness 字数合规性检查")
    print("=" * 70)
    print()
    print(f"文件：{os.path.basename(md_file)}")
    print(f"文件大小：{file_size:,} 字节")
    print(f"中文字符：{chinese:,}")
    print(f"英文单词：{english:,}")
    print(f"总字数：{total:,}")
    print(f"最低标准：{min_chars:,}")
    print()

    # 按章节显示
    if chapter_counts:
        print("【分章节统计】")
        for ch, count in chapter_counts.items():
            pct = count / max(total, 1) * 100
            bar = '█' * int(pct / 5) + '░' * (20 - int(pct / 5))
            print(f"  {ch[:20]:<20} {count:>6,} 字  {bar} {pct:.0f}%")
        print()

    # 判定
    print("=" * 70)
    if total >= min_chars:
        print(f"✅ Harness 检查通过：字数达标（{total:,}/{min_chars:,}）")
        sys.exit(0)
    elif total >= min_chars * 0.5:
        print(f"⚠️  Harness 警告：字数不足（{total:,}/{min_chars:,} = {total/min_chars:.0%}）")
        print(f"   需要补充 {min_chars - total:,} 字")
        sys.exit(1)
    else:
        print(f"❌ Harness 检查失败：字数严重不足（{total:,}/{min_chars:,} = {total/min_chars:.0%}）")
        print(f"   需要补充 {min_chars - total:,} 字，请回退到专家撰写阶段")
        sys.exit(2)


if __name__ == '__main__':
    main()
