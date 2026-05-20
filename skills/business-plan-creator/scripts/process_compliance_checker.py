#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
流程监管专家专用脚本 - 全流程合规性检查

功能：
1. 检查团队是否完整创建
2. 检查技能调用是否正确
3. 检查流程步骤是否按顺序执行
4. 检查质量关口是否全部通过
5. 生成流程合规性报告

用法：
    python process_compliance_checker.py [项目目录]
"""

import sys
import os
import json
from datetime import datetime

class ProcessComplianceChecker:
    """流程合规性检查器"""
    
    def __init__(self, project_dir):
        self.project_dir = project_dir
        self.report = {
            'timestamp': datetime.now().isoformat(),
            'checks': [],
            'issues': [],
            'passed': True
        }
    
    def check_team_creation(self):
        """检查团队创建"""
        print("\n[检查 1] 团队创建...")
        
        # 检查是否有团队创建记录
        team_file = os.path.join(self.project_dir, '.workbuddy', 'team.json')
        if os.path.exists(team_file):
            with open(team_file, 'r', encoding='utf-8') as f:
                team_data = json.load(f)
            
            required_roles = ['claw', 'industry_researcher', 'financial_analyst', 
                            'strategy_analyst', 'process_supervisor', 'quality_auditor']
            
            missing_roles = [role for role in required_roles if role not in team_data]
            
            if missing_roles:
                self.report['issues'].append(f"缺少专家角色：{', '.join(missing_roles)}")
                self.report['passed'] = False
                print(f"  ❌ 缺少专家角色：{', '.join(missing_roles)}")
            else:
                print(f"  ✅ 6 人团队已完整创建")
                self.report['checks'].append("团队创建：通过")
        else:
            self.report['issues'].append("未找到团队创建记录")
            self.report['passed'] = False
            print(f"  ❌ 未找到团队创建记录")
    
    def check_skill_calls(self):
        """检查技能调用"""
        print("\n[检查 2] 技能调用...")
        
        # 检查 Claw 是否调用 data-cleaner
        claw_skills_file = os.path.join(self.project_dir, '.workbuddy', 'claw_skills.json')
        if os.path.exists(claw_skills_file):
            with open(claw_skills_file, 'r', encoding='utf-8') as f:
                claw_skills = json.load(f)
            
            if 'data-cleaner' not in claw_skills:
                self.report['issues'].append("Claw 未调用 data-cleaner")
                self.report['passed'] = False
                print(f"  ❌ Claw 未调用 data-cleaner")
            else:
                print(f"  ✅ Claw 已调用 data-cleaner")
                self.report['checks'].append("Claw 技能调用：通过")
        else:
            print(f"  ⚠️ 未找到 Claw 技能调用记录")
            self.report['checks'].append("Claw 技能调用：未找到记录")
        
        # 检查专家是否只使用分析类技能
        expert_skills_file = os.path.join(self.project_dir, '.workbuddy', 'expert_skills.json')
        if os.path.exists(expert_skills_file):
            with open(expert_skills_file, 'r', encoding='utf-8') as f:
                expert_skills = json.load(f)
            
            forbidden_skills = ['finance-data-retrieval', 'baidu-search']
            issues_found = False
            
            for expert, skills in expert_skills.items():
                for skill in skills:
                    if skill in forbidden_skills:
                        self.report['issues'].append(f"{expert} 使用了禁止的技能：{skill}")
                        self.report['passed'] = False
                        issues_found = True
                        print(f"  ❌ {expert} 使用了禁止的技能：{skill}")
            
            if not issues_found:
                print(f"  ✅ 专家只使用分析类技能")
                self.report['checks'].append("专家技能调用：通过")
        else:
            print(f"  ⚠️ 未找到专家技能调用记录")
            self.report['checks'].append("专家技能调用：未找到记录")
    
    def check_process_steps(self):
        """检查流程步骤"""
        print("\n[检查 3] 流程步骤...")
        
        steps_file = os.path.join(self.project_dir, '.workbuddy', 'steps.json')
        if os.path.exists(steps_file):
            with open(steps_file, 'r', encoding='utf-8') as f:
                steps = json.load(f)
            
            required_steps = ['step1_data_collection', 'step2_expert_writing', 
                            'step3_integration', 'step4_monitoring', 'step5_quality']
            
            missing_steps = [step for step in required_steps if step not in steps]
            
            if missing_steps:
                self.report['issues'].append(f"缺少流程步骤：{', '.join(missing_steps)}")
                self.report['passed'] = False
                print(f"  ❌ 缺少流程步骤：{', '.join(missing_steps)}")
            else:
                print(f"  ✅ 5 步法流程完整执行")
                self.report['checks'].append("流程步骤：通过")
        else:
            print(f"  ⚠️ 未找到流程步骤记录")
            self.report['checks'].append("流程步骤：未找到记录")
    
    def check_quality_gates(self):
        """检查质量关口"""
        print("\n[检查 4] 质量关口...")
        
        gates_file = os.path.join(self.project_dir, '.workbuddy', 'quality_gates.json')
        if os.path.exists(gates_file):
            with open(gates_file, 'r', encoding='utf-8') as f:
                gates = json.load(f)
            
            passed_gates = [gate for gate, status in gates.items() if status == 'passed']
            total_gates = len(gates)
            
            print(f"  ✅ 通过 {len(passed_gates)}/{total_gates} 个质量关口")
            self.report['checks'].append(f"质量关口：{len(passed_gates)}/{total_gates} 通过")
            
            if len(passed_gates) < total_gates:
                failed_gates = [gate for gate, status in gates.items() if status == 'failed']
                self.report['issues'].append(f"未通过的质量关口：{', '.join(failed_gates)}")
                self.report['passed'] = False
        else:
            print(f"  ⚠️ 未找到质量关口记录")
            self.report['checks'].append("质量关口：未找到记录")
    
    def generate_report(self):
        """生成报告"""
        print("\n" + "=" * 80)
        print("[流程合规性检查报告]")
        print("=" * 80)
        
        print("\n检查项：")
        for check in self.report['checks']:
            print(f"  ✅ {check}")
        
        if self.report['issues']:
            print("\n问题：")
            for issue in self.report['issues']:
                print(f"  ❌ {issue}")
        
        print("\n" + "=" * 80)
        if self.report['passed']:
            print("[结论] ✅ 流程合规性检查通过")
        else:
            print("[结论] ❌ 流程合规性检查不通过，需要整改")
        print("=" * 80)
        
        # 保存报告
        report_file = os.path.join(self.project_dir, '.workbuddy', 'compliance_report.json')
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(self.report, f, indent=2, ensure_ascii=False)
        
        print(f"\n[报告已保存] {report_file}")
        
        return self.report['passed']

def main():
    if len(sys.argv) < 2:
        print("用法：python process_compliance_checker.py [项目目录]")
        print("\n流程监管专家专用 - 全流程合规性检查")
        sys.exit(1)
    
    project_dir = sys.argv[1]
    
    if not os.path.exists(project_dir):
        print(f"[错误] 目录不存在：{project_dir}")
        sys.exit(1)
    
    checker = ProcessComplianceChecker(project_dir)
    
    # 执行检查
    checker.check_team_creation()
    checker.check_skill_calls()
    checker.check_process_steps()
    checker.check_quality_gates()
    
    # 生成报告
    passed = checker.generate_report()
    
    sys.exit(0 if passed else 1)

if __name__ == '__main__':
    main()
