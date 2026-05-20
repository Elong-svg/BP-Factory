#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Harness 主控脚本 — business-plan-creator v5.0 约束执行引擎

在所有关键节点运行，确保流程合规性。
每项检查必须通过，否则流程硬性停止。

用法：
    python master_check.py <checkpoint> [参数...]

检查点（checkpoint）：
    pre-flight     — 团队创建前检查（Agent 配额）
    pre-merge      — 合并前检查（章节去重）
    pre-deliver    — 交付前检查（图表存在性 + 字数 + 图表表格计数）

退出码：
    0  = 所有检查通过
    1  = 至少一项未通过（硬性停止）
"""

import sys
import os
import subprocess
import json
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
SKILL_DIR = SCRIPT_DIR.parent.parent  # scripts/harness -> scripts -> skill root
SCRIPTS_DIR = SKILL_DIR / 'scripts'


def run_script(script_name, args, description):
    """运行检查脚本并返回结果"""
    script_path = SCRIPT_DIR / script_name

    if not script_path.exists():
        script_path = SCRIPTS_DIR / script_name

    if not script_path.exists():
        print(f"  ❌ 脚本不存在：{script_name}")
        return False, f"脚本 {script_name} 不存在"

    cmd = [sys.executable, str(script_path)] + args
    print(f"  ▶  {description}")
    print(f"     {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30,
                                cwd=str(SKILL_DIR), encoding='utf-8')
        output = result.stdout + result.stderr
        # 显示输出（缩进）
        for line in output.split('\n'):
            if line.strip():
                print(f"     {line}")
        passed = result.returncode == 0
        status = "✅ 通过" if passed else "❌ 失败"
        print(f"  {status} (exit={result.returncode})")
        print()
        return passed, output
    except subprocess.TimeoutExpired:
        print(f"  ❌ 超时（30s）")
        print()
        return False, "检查超时"
    except Exception as e:
        print(f"  ❌ 异常：{e}")
        print()
        return False, str(e)


def run_pre_flight(sections_dir=None, charts_dir=None):
    """pre-flight 检查：Agent 配额 + 初始环境"""
    print("=" * 70)
    print("🔒 Harness 检查点：pre-flight（团队创建前）")
    print("=" * 70)
    print(f"时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    all_passed = True

    # 检查 1：项目目录结构
    print("【检查 1】项目目录结构")
    if sections_dir and os.path.isdir(sections_dir):
        existing = list(Path(sections_dir).glob('*.md'))
        if existing:
            print(f"  ⚠️  发现 {len(existing)} 个已有章节文件，将创建新文件覆盖")
        else:
            print(f"  ✅ 空目录，可以开始")
    print()

    # 检查 2：Agent 配额
    print("【检查 2】Agent 配额约束")
    print(f"  最大允许：6 个 Agent（1 Claw + 5 专家）")
    print(f"  ⚠️  请确认：不创建超过 6 个 Agent")
    print(f"  ⚠️  如遇 429 错误，复用已有结果，不创建新 Agent")
    print()

    print("=" * 70)
    if all_passed:
        print("✅ pre-flight 检查通过，可以开始创建团队")
    print("=" * 70)

    return all_passed


def run_pre_merge(sections_dir):
    """pre-merge 检查：章节去重"""
    print("=" * 70)
    print("🔒 Harness 检查点：pre-merge（合并前）")
    print("=" * 70)
    print(f"时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    all_passed = True

    # 检查 1：章节文件概览
    print("【检查 1】章节文件概览")
    if os.path.isdir(sections_dir):
        section_files = sorted(Path(sections_dir).glob('*.md'))
        print(f"  文件数：{len(section_files)}")
        for f in section_files:
            size = f.stat().st_size
            print(f"    📄 {f.name} ({size:,} 字节)")
    else:
        print(f"  ❌ 目录不存在：{sections_dir}")
        return False
    print()

    # 检查 2：章节去重
    passed, _ = run_script('chapter_dedup.py', [sections_dir], '章节去重检查')
    all_passed = all_passed and passed

    # 检查 3：章节完整性（预期 7 章 + 执行摘要）
    section_files = sorted(Path(sections_dir).glob('*.md'))
    expected_count = 8  # 执行摘要 + 7 章
    if len(section_files) < expected_count:
        print(f"  ⚠️  章节文件不足：{len(section_files)}/{expected_count}")
    elif len(section_files) > expected_count + 2:
        print(f"  ⚠️  章节文件过多：{len(section_files)}（预期 ~{expected_count}）")

    print()
    print("=" * 70)
    if all_passed:
        print("✅ pre-merge 检查通过，可以开始合并")
    else:
        print("❌ pre-merge 检查失败，合并操作被阻止！")
    print("=" * 70)

    return all_passed


def run_pre_deliver(merged_file, charts_dir=None, project_dir=None):
    """pre-deliver 检查：技能调用 + 图表存在性 + 字数 + 图表表格计数"""
    print("=" * 70)
    print("🔒 Harness 检查点：pre-deliver（交付前）")
    print("=" * 70)
    print(f"时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    all_passed = True

    if not os.path.exists(merged_file):
        print(f"❌ 合并文件不存在：{merged_file}")
        return False

    # 检查 1：技能调用追踪（v5.0.1 新增）
    if project_dir:
        passed, _ = run_script('skill_trace.py', [project_dir, '--verify', '--phase', 'pre-deliver'],
                               '技能调用追踪验证')
        all_passed = all_passed and passed
    else:
        # 从 merged_file 推断项目目录
        inferred_dir = os.path.dirname(os.path.dirname(os.path.abspath(merged_file)))
        passed, _ = run_script('skill_trace.py', [inferred_dir, '--verify', '--phase', 'pre-deliver'],
                               '技能调用追踪验证')
        all_passed = all_passed and passed

    # 检查 2：图表存在性
    charts_arg = [merged_file]
    if charts_dir:
        charts_arg.append(charts_dir)
    passed, output = run_script('chart_existence.py', charts_arg, '图表存在性检查')
    all_passed = all_passed and passed

    # 检查 3：字数合规
    passed, _ = run_script('word_count.py', [merged_file, '--min-chars', '20000'], '字数合规检查')
    all_passed = all_passed and passed

    # 检查 4：图表表格计数（复用已有脚本）
    count_script = SCRIPTS_DIR / 'count_charts_tables.py'
    if count_script.exists():
        passed, _ = run_script('count_charts_tables.py', [merged_file], '图表表格计数')
        all_passed = all_passed and passed
    else:
        print("  ⚠️  count_charts_tables.py 不存在，跳过")
        print()

    print("=" * 70)
    if all_passed:
        print("✅ pre-deliver 检查通过，可以生成交付文档")
    else:
        print("❌ pre-deliver 检查失败，交付操作被阻止！")
        print()
        print("处理流程：")
        print("  1. 技能未调用 → 加载对应子技能（data-cleaner/business-writer/...）")
        print("  2. 图表缺失 → 调用 data-visualization 生成图表")
        print("  3. 字数不足 → 回退到专家撰写阶段补充内容")
        print("  4. 图表表格不足 → 要求专家补充")
    print("=" * 70)

    return all_passed


def generate_report(checkpoint, passed, details=None):
    """生成检查报告 JSON"""
    report = {
        'timestamp': datetime.now().isoformat(),
        'checkpoint': checkpoint,
        'passed': passed,
        'details': details or {}
    }

    report_dir = SKILL_DIR / '.harness_reports'
    report_dir.mkdir(exist_ok=True)
    report_file = report_dir / f'{checkpoint}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'

    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\n📋 检查报告已保存：{report_file}")


def print_usage():
    print("Harness 主控脚本 — business-plan-creator v5.0")
    print()
    print("用法：python master_check.py <checkpoint> [参数...]")
    print()
    print("检查点：")
    print("  pre-flight   <sections_dir>")
    print("  pre-merge    <sections_dir>")
    print("  pre-deliver  <merged_file> [charts_dir]")
    print()
    print("示例：")
    print("  python master_check.py pre-flight bp_sections/")
    print("  python master_check.py pre-merge bp_sections/")
    print("  python master_check.py pre-deliver bp_final.md bp_charts/")


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    checkpoint = sys.argv[1]

    if checkpoint == 'pre-flight':
        sections_dir = sys.argv[2] if len(sys.argv) > 2 else None
        passed = run_pre_flight(sections_dir)
        generate_report(checkpoint, passed)

    elif checkpoint == 'pre-merge':
        if len(sys.argv) < 3:
            print("❌ pre-merge 需要 sections_dir 参数")
            print_usage()
            sys.exit(1)
        sections_dir = sys.argv[2]
        passed = run_pre_merge(sections_dir)
        generate_report(checkpoint, passed)

    elif checkpoint == 'pre-deliver':
        if len(sys.argv) < 3:
            print("❌ pre-deliver 需要 merged_file 参数")
            print_usage()
            sys.exit(1)
        merged_file = sys.argv[2]
        charts_dir = sys.argv[3] if len(sys.argv) > 3 else None
        passed = run_pre_deliver(merged_file, charts_dir)
        generate_report(checkpoint, passed)

    else:
        print(f"❌ 未知检查点：{checkpoint}")
        print_usage()
        sys.exit(1)

    sys.exit(0 if passed else 1)


if __name__ == '__main__':
    main()
