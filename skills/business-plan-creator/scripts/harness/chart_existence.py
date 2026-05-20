#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Harness 约束 #3：图表存在性检查
检查 Markdown 中引用的图片文件是否真实存在于磁盘上，
并检测是否有 CSV 数据但未生成对应图表。

用法：
    python chart_existence.py <markdown_file> [charts_dir]
    退出码：0=通过，1=失败（图片缺失），2=失败（有 CSV 数据未生成图表）
"""

import sys
import os
import re
from pathlib import Path


def find_image_refs(markdown_file):
    """查找 Markdown 中的图片引用"""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Markdown 图片语法：![desc](path)
    pattern = r'!\[(.*?)\]\((.*?)\)'
    refs = re.findall(pattern, content)
    return [{'desc': desc, 'path': path} for desc, path in refs]


def find_csv_files(charts_dir):
    """查找 charts 目录下的 CSV 数据文件"""
    csv_files = []
    if os.path.isdir(charts_dir):
        for f in Path(charts_dir).glob('*.csv'):
            csv_files.append(str(f))
    return csv_files


def check_image_exists(md_file_path, image_path, charts_dir):
    """检查图片文件是否存在"""
    md_dir = os.path.dirname(os.path.abspath(md_file_path))

    # 尝试多种路径组合
    candidates = [
        os.path.join(md_dir, image_path),
        os.path.join(charts_dir, image_path) if charts_dir else None,
        os.path.join(md_dir, os.path.basename(image_path)),
        os.path.abspath(image_path),
    ]

    for candidate in candidates:
        if candidate and os.path.exists(candidate):
            return True, candidate

    return False, None


def check_chart_generation(markdown_file, charts_dir):
    """检查：有 CSV 数据文件但没有对应图表"""
    md_dir = os.path.dirname(os.path.abspath(markdown_file))

    # 查找同级目录和 charts 目录
    search_dirs = [md_dir]
    if charts_dir and os.path.isdir(charts_dir):
        search_dirs.append(charts_dir)

    all_csv = []
    for d in search_dirs:
        all_csv.extend(find_csv_files(d))

    if not all_csv:
        return True, []  # 无 CSV 数据，无需检查

    # 检查是否有对应的图片文件
    image_extensions = {'.png', '.jpg', '.jpeg', '.svg', '.gif', '.webp'}
    orphan_csv = []

    for csv_path in all_csv:
        csv_stem = os.path.splitext(os.path.basename(csv_path))[0]
        found_image = False

        # 在同目录查找同名图片
        csv_dir = os.path.dirname(csv_path)
        for ext in image_extensions:
            candidate = os.path.join(csv_dir, csv_stem + ext)
            if os.path.exists(candidate):
                found_image = True
                break

        # 在 charts_dir 查找
        if not found_image and charts_dir:
            for ext in image_extensions:
                candidate = os.path.join(charts_dir, csv_stem + ext)
                if os.path.exists(candidate):
                    found_image = True
                    break

        if not found_image:
            orphan_csv.append(csv_path)

    return len(orphan_csv) == 0, orphan_csv


def main():
    if len(sys.argv) < 2:
        print("用法：python chart_existence.py <markdown_file> [charts_dir]")
        print("示例：python chart_existence.py bp_final.md bp_charts/")
        sys.exit(1)

    md_file = sys.argv[1]
    charts_dir = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.exists(md_file):
        print(f"❌ 文件不存在：{md_file}")
        sys.exit(1)

    all_passed = True
    has_csv_issue = False

    # 检查 1：图片引用完整性
    print("=" * 70)
    print("📊 Harness 图表存在性检查")
    print("=" * 70)
    print()

    refs = find_image_refs(md_file)
    print(f"【检查 1】图片引用完整性（共 {len(refs)} 处引用）")
    print()

    missing_images = []
    for ref in refs:
        exists, found_path = check_image_exists(md_file, ref['path'], charts_dir)
        status = "✅" if exists else "❌"
        print(f"  {status} ![{ref['desc']}]({ref['path']})")
        if exists:
            print(f"      → {found_path}")
        else:
            missing_images.append(ref)
            all_passed = False
            print(f"      → 文件不存在！")

    print()
    if not missing_images:
        print("  ✅ 所有图片引用有效")
    else:
        print(f"  ❌ {len(missing_images)} 处图片引用指向不存在的文件")

    # 检查 2：CSV 数据 → 图表生成
    print()
    print("【检查 2】数据文件 → 图表生成检测")

    csv_ok, orphan_csv = check_chart_generation(md_file, charts_dir)

    if orphan_csv:
        has_csv_issue = True
        all_passed = False
        print(f"  ❌ 发现 {len(orphan_csv)} 个 CSV 数据文件未生成对应图表：")
        for f in orphan_csv:
            print(f"     📄 {os.path.basename(f)} → 需要生成图表！")
        print()
        print("  处理建议：")
        print("    1. 调用 金融财务分析整合包 → data-visualization")
        print("    2. 将 CSV 数据转换为 PNG/SVG 图表")
        print("    3. 重新运行本脚本验证")
    else:
        if csv_ok:
            csv_files = find_csv_files(charts_dir) if charts_dir else []
            if csv_files:
                print(f"  ✅ 所有 CSV 数据文件（{len(csv_files)} 个）已生成对应图表")
            else:
                print("  ℹ️  未发现 CSV 数据文件，无需检查")

    # 汇总
    print()
    print("=" * 70)
    if all_passed:
        print("✅ Harness 检查通过：所有图表就绪")
        sys.exit(0)
    elif has_csv_issue:
        print("❌ Harness 检查失败：CSV 数据未生成图表（退出码 2）")
        sys.exit(2)
    else:
        print("❌ Harness 检查失败：图片引用缺失（退出码 1）")
        sys.exit(1)


if __name__ == '__main__':
    main()
