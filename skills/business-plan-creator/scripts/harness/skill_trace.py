#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Harness 约束 #5：技能调用追踪验证
检查 skill_trace.json 是否存在且包含所有必用技能调用记录。

原理：AI 每调用一个必用技能，必须写入 skill_trace.json。
Harness 在 pre-merge 和 pre-deliver 时验证完整度。
缺少任何必用条目 = 硬性停止。

用法：
    python skill_trace.py <trace_dir> [--phase pre-merge|pre-deliver]
    退出码：0=齐全，1=缺条目
"""

import sys
import os
import json
from pathlib import Path

# 必用技能清单（按阶段）
REQUIRED_SKILLS = {
    # Step 1: 数据收集阶段
    "step1": [
        {
            "id": "data-cleaner",
            "name": "data-cleaner 数据清洗",
            "called_by": "Claw",
            "evidence": "cleaned_data.json 存在且质量评分 >= 80"
        }
    ],
    # Step 2: 专家撰写阶段
    "step2": [
        {
            "id": "business-writer-industry",
            "name": "business-writer（行业研究章节）",
            "called_by": "行业研究员",
            "evidence": "bp_sections/industry_analysis.md 包含三层论述结构"
        },
        {
            "id": "business-writer-finance",
            "name": "business-writer（财务分析章节）",
            "called_by": "财务分析师",
            "evidence": "bp_sections/financial_analysis.md 包含三层论述结构"
        },
        {
            "id": "business-writer-strategy",
            "name": "business-writer（战略分析章节）",
            "called_by": "战略分析师",
            "evidence": "bp_sections/strategy_analysis.md 包含三层论述结构"
        },
        {
            "id": "data-visualization-industry",
            "name": "data-visualization（行业图表）",
            "called_by": "行业研究员",
            "evidence": "bp_charts/ 存在行业相关图表文件"
        },
        {
            "id": "data-visualization-finance",
            "name": "data-visualization（财务图表）",
            "called_by": "财务分析师",
            "evidence": "bp_charts/ 存在财务相关图表文件"
        },
        {
            "id": "data-visualization-strategy",
            "name": "data-visualization（战略图表）",
            "called_by": "战略分析师",
            "evidence": "bp_charts/ 存在战略相关图表文件"
        },
    ],
    # Step 3-4: 整合交付阶段
    "step3": [
        {
            "id": "markdown-processor",
            "name": "markdown-processor（合并 + 标题修复）",
            "called_by": "Claw",
            "evidence": "bp_final_clean.md 标题格式为 ## 第X章"
        },
        {
            "id": "markdown-to-word",
            "name": "markdown-to-word（Word 文档生成）",
            "called_by": "Claw",
            "evidence": "输出 .docx 文件存在"
        },
        {
            "id": "humanizer",
            "name": "humanizer（去 AI 味）",
            "called_by": "Claw",
            "evidence": "文本无 AI 味标志词"
        },
    ]
}


def init_trace(trace_dir):
    """初始化追踪文件"""
    trace_file = Path(trace_dir) / "skill_trace.json"
    trace = {
        "project": "business-plan-creator",
        "version": "5.0.0",
        "traces": [],
        "skills_required": {
            "step1": len(REQUIRED_SKILLS["step1"]),
            "step2": len(REQUIRED_SKILLS["step2"]),
            "step3": len(REQUIRED_SKILLS["step3"]),
            "total": sum(len(v) for v in REQUIRED_SKILLS.values())
        }
    }

    with open(trace_file, 'w', encoding='utf-8') as f:
        json.dump(trace, f, ensure_ascii=False, indent=2)

    print(f"  ✅ 技能追踪文件已初始化：{trace_file}")
    return trace_file


def add_trace_entry(trace_dir, skill_id, skill_name, called_by, status="completed", notes=""):
    """添加一条技能调用记录（AI 在每次调用技能后执行）"""
    trace_file = Path(trace_dir) / "skill_trace.json"

    if not trace_file.exists():
        print(f"  ⚠️  追踪文件不存在，正在初始化...")
        trace_file = init_trace(trace_dir)

    with open(trace_file, 'r', encoding='utf-8') as f:
        trace = json.load(f)

    # 检查是否已存在
    for existing in trace["traces"]:
        if existing["id"] == skill_id:
            print(f"  ⚠️  {skill_id} 已记录，跳过")
            return

    from datetime import datetime
    entry = {
        "id": skill_id,
        "name": skill_name,
        "called_by": called_by,
        "status": status,
        "timestamp": datetime.now().isoformat(),
        "notes": notes
    }
    trace["traces"].append(entry)

    with open(trace_file, 'w', encoding='utf-8') as f:
        json.dump(trace, f, ensure_ascii=False, indent=2)

    print(f"  ✅ 技能调用已记录：{skill_name} (by {called_by})")


def verify_skills(trace_dir, phase="pre-deliver"):
    """验证必用技能是否齐全"""
    trace_file = Path(trace_dir) / "skill_trace.json"

    print("=" * 70)
    print("🔧 Harness 技能调用追踪验证")
    print("=" * 70)
    print()

    if not trace_file.exists():
        print(f"❌ 技能追踪文件不存在：{trace_file}")
        print()
        print("处理建议：")
        print("  1. 在项目根目录运行 init：python skill_trace.py <dir> --init")
        print("  2. 每调用一个必用技能后，运行：python skill_trace.py <dir> --add <skill_id> <name> <called_by>")
        print("  3. 所有技能调用完成后，重新运行本验证")
        return False

    with open(trace_file, 'r', encoding='utf-8') as f:
        trace = json.load(f)

    recorded = {t["id"]: t for t in trace["traces"]}

    # 根据阶段验证
    if phase in ("pre-merge", "pre-deliver", "all"):
        phases_to_check = (
            ["step1", "step2"] if phase == "pre-merge"
            else ["step1", "step2", "step3"]
        )
    else:
        phases_to_check = [phase]

    all_passed = True
    missing = []

    for phase_name in phases_to_check:
        required = REQUIRED_SKILLS.get(phase_name, [])
        if not required:
            continue

        # Map phase names to readable labels
        phase_labels = {"step1": "数据收集阶段", "step2": "专家撰写阶段", "step3": "整合交付阶段"}
        print(f"【{phase_labels.get(phase_name, phase_name)}】")
        print()

        for skill in required:
            skill_id = skill["id"]
            if skill_id in recorded:
                rec = recorded[skill_id]
                status_icon = "✅" if rec["status"] == "completed" else "⚠️"
                print(f"  {status_icon} {skill['name']}")
                print(f"     调用者：{rec['called_by']}  |  {rec['timestamp']}")
                if rec.get("notes"):
                    print(f"     备注：{rec['notes']}")
            else:
                print(f"  ❌ {skill['name']} — 未调用！")
                print(f"     应调用者：{skill['called_by']}")
                print(f"     预期证据：{skill['evidence']}")
                all_passed = False
                missing.append(skill)

        print()

    # 汇总
    total_required = sum(len(REQUIRED_SKILLS[p]) for p in phases_to_check)
    total_recorded = len([t for t in trace["traces"]
                         if any(t["id"] == s["id"]
                               for p in phases_to_check
                               for s in REQUIRED_SKILLS.get(p, []))])

    print("=" * 70)
    if all_passed:
        print(f"✅ Harness 检查通过：所有必用技能已调用（{total_recorded}/{total_required}）")
    else:
        print(f"❌ Harness 检查失败：{len(missing)} 个必用技能未调用")
        print()
        print("缺失技能清单：")
        for s in missing:
            print(f"  📛 {s['id']} — {s['name']}（应由 {s['called_by']} 调用）")
        print()
        print("处理建议：")
        print("  1. 对每个缺失的技能，调用对应子技能")
        print("  2. 调用后运行：python skill_trace.py <dir> --add <id> <name> <by>")
        print("  3. 重新运行本验证")
    print("=" * 70)

    return all_passed


def print_usage():
    print("技能调用追踪验证工具")
    print()
    print("用法：")
    print("  python skill_trace.py <trace_dir> --init")
    print("  python skill_trace.py <trace_dir> --add <skill_id> <name> <called_by> [notes]")
    print("  python skill_trace.py <trace_dir> --verify [--phase pre-merge|pre-deliver|all]")
    print()
    print("示例：")
    print("  python skill_trace.py bp_project/ --init")
    print("  python skill_trace.py bp_project/ --add data-cleaner \"数据清洗\" Claw")
    print("  python skill_trace.py bp_project/ --verify --phase pre-deliver")


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    trace_dir = sys.argv[1]
    command = sys.argv[2] if len(sys.argv) > 2 else "--verify"

    if command == "--init":
        init_trace(trace_dir)
        sys.exit(0)

    elif command == "--add":
        if len(sys.argv) < 5:
            print("❌ --add 需要 <skill_id> <name> <called_by> [notes]")
            sys.exit(1)
        skill_id = sys.argv[3]
        name = sys.argv[4]
        called_by = sys.argv[5]
        notes = sys.argv[6] if len(sys.argv) > 6 else ""
        add_trace_entry(trace_dir, skill_id, name, called_by, "completed", notes)
        sys.exit(0)

    elif command == "--verify":
        phase = "pre-deliver"
        for i, arg in enumerate(sys.argv):
            if arg == "--phase" and i + 1 < len(sys.argv):
                phase = sys.argv[i + 1]
        passed = verify_skills(trace_dir, phase)
        sys.exit(0 if passed else 1)

    else:
        print(f"❌ 未知命令：{command}")
        print_usage()
        sys.exit(1)


if __name__ == '__main__':
    main()
