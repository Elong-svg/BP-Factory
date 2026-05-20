#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
data-cleaner 技能初始化脚本
用途：创建技能目录结构、生成示例配置文件、验证技能完整性
"""

import os
import json
from pathlib import Path

SKILL_NAME = "data-cleaner"
SKILL_VERSION = "1.1.0"

def create_directory_structure(base_path):
    """创建技能目录结构"""
    directories = [
        "raw_data",       # 原始数据输入目录
        "cleaned_data",   # 清洗后数据输出目录
        "reports",        # 报告输出目录
        "config",         # 配置文件目录
        "references",     # 参考文档目录
        "scripts",        # 脚本目录
        "examples",       # 示例数据目录
    ]
    
    for dir_name in directories:
        dir_path = base_path / dir_name
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"[OK] Created directory: {dir_path}")
    
    # 创建.gitkeep 文件
    for dir_name in ["raw_data", "cleaned_data", "reports"]:
        gitkeep_path = base_path / dir_name / ".gitkeep"
        gitkeep_path.touch()
        print(f"[OK] Created .gitkeep: {gitkeep_path}")

def create_config_file(base_path):
    """创建示例配置文件"""
    config = {
        "cleaner_config": {
            "input": {
                "raw_data_directory": "./raw_data/",
                "output_directory": "./cleaned_data/",
                "reports_directory": "./reports/"
            },
            "company_info": {
                "name": "<动态> 公司名称",
                "code": "<动态> 股票代码",
                "industry": "<动态> 所属行业",
                "sub_industry": "<动态> 细分行业"
            },
            "data_scope": {
                "target_period": "<动态> 目标期间",
                "period_type": "annual",
                "unit_standard": "亿元"
            },
            "cleaning": {
                "anomaly_detection": True,
                "auto_impute": True,
                "deduplicate": True,
                "generate_report": True
            },
            "thresholds": {
                "z_score_threshold": 3,
                "yoy_surge_threshold": 2.0,
                "yoy_drop_threshold": -0.5,
                "quality_threshold": 80
            },
            "impute": {
                "method": "linear",
                "ask_user": True
            }
        }
    }
    
    config_path = base_path / "config" / "cleaner_config.yaml"
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write("# data-cleaner 配置文件\n")
        f.write("# 修改此文件以自定义清洗行为\n\n")
        
        def write_yaml(obj, indent=0):
            prefix = "  " * indent
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if isinstance(value, (dict, list)):
                        f.write(f"{prefix}{key}:\n")
                        write_yaml(value, indent + 1)
                    else:
                        if isinstance(value, bool):
                            value_str = str(value).lower()
                        elif isinstance(value, str) and value.startswith("<"):
                            value_str = f'"{value}"'
                        else:
                            value_str = str(value)
                        f.write(f"{prefix}{key}: {value_str}\n")
        
        write_yaml(config["cleaner_config"])
    
    print(f"[OK] Created config file: {config_path}")

def create_sample_data(base_path):
    """创建示例数据文件"""
    sample_data = {
        "metadata": {
            "company_name": "<示例> XX 集团股份有限公司",
            "company_code": "<示例> 000001.SZ",
            "industry": "<示例> 家用电器",
            "data_source": "示例数据"
        },
        "income_statement": [
            {
                "period": "2023",
                "revenue": 100.5,
                "cost_of_revenue": 65.3,
                "gross_profit": 35.2,
                "operating_expense": 20.1,
                "net_income": 12.8,
                "unit": "亿元"
            },
            {
                "period": "2022",
                "revenue": 88.2,
                "cost_of_revenue": 58.1,
                "gross_profit": 30.1,
                "operating_expense": 18.5,
                "net_income": 10.2,
                "unit": "亿元"
            }
        ],
        "note": "这是示例数据，实际使用时请替换为真实数据"
    }
    
    sample_path = base_path / "examples" / "sample_income_statement.json"
    with open(sample_path, 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, ensure_ascii=False, indent=2)
    
    print(f"[OK] Created sample data: {sample_path}")

def create_reference_doc(base_path):
    """创建参考文档"""
    reference = """# data-cleaner 参考文档

## 一、常见科目名称映射

### 营业收入
- 营业收入、主营业务收入、总营收、收入总额
- Revenue、Total Revenue、Turnover
- 营收、销售收入、经营收入

### 净利润
- 净利润、税后利润、净收益
- Net Income、Net Profit、Net Earnings
- 归母净利润、归属于母公司股东的净利润

### 总资产
- 总资产、资产总计、资产总额
- Total Assets、资产合计

## 二、行业特有指标参考

### 互联网/科技
- DAU（日活跃用户）
- MAU（月活跃用户）
- ARPU（每用户平均收入）
- 获客成本
- LTV（用户生命周期价值）

### 制造业
- 产能利用率
- 单位成本
- 研发强度（研发费用/营收）
- 订单储备

### 零售
- 同店销售增长率
- 客单价
- 门店数量
- 坪效

### 金融/银行
- 净息差
- 不良贷款率
- 资本充足率
- 存贷比

### 房地产
- 预收款项
- 可售面积
- 土地储备
- 竣工率

### 医药/生物科技
- 在研管线数量
- 研发费用率
- 新药获批数量
- 临床试验数量

## 三、单位换算规则

### 货币单位
- 1 亿元 = 100,000,000 元
- 1 万元 = 10,000 元
- 1 千元 = 1,000 元

### 自动检测规则
- 如果数值 > 10^12 且为营收/资产类，检查是否单位为'元'而非'万元'
- 如果数值 < 1000 且为营收/资产类，检查是否单位为'亿元'而非'元'
- 通过与同指标其他期间数据对比，检测量级突变

## 四、异常检测阈值参考

### 默认阈值
- Z 分数阈值：3（超过 3 倍标准差为异常）
- 同比激增阈值：200%（增长超过 200% 需检查）
- 同比骤降阈值：-50%（下降超过 50% 需检查）

### 行业调整建议
- **金融行业**：Z=2.5（数据波动小，阈值收紧）
- **互联网行业**：Z=3.5（数据波动大，阈值放宽）
- **制造业**：Z=3（默认）
- **新兴行业**：同比阈值放宽到 300%/-60%

## 五、缺失值处理策略

### 线性插值（linear）
- 适用：时间序列完整，仅个别缺失
- 方法：用前后数据的线性关系估算
- 置信度：medium

### 行业均值填充（industry_avg）
- 适用：有同行业可比公司数据
- 方法：取同行业同期均值
- 置信度：low
- 前提：需提供 industry_peers

### 前向填充（forward_fill）
- 适用：趋势稳定的数据
- 方法：用最近一期数据填充
- 置信度：low

### 不填充（none）
- 适用：无法可靠估算的情况
- 方法：保留为空，标注 N/A
- 置信度：n/a

## 六、可信度评分参考

### A 级（90-100 分）
- 来源：官方财报
- 一致性：多来源完全一致
- 时效性：最近 1 年数据
- 完整性：所有字段完整

### B 级（75-89 分）
- 来源：权威数据库
- 一致性：多来源轻微差异（<5%）
- 时效性：1-2 年数据
- 完整性：少量字段缺失

### C 级（60-74 分）
- 来源：券商研报/行业报告
- 一致性：多来源差异较大（5%-10%）
- 时效性：2-3 年数据
- 完整性：部分字段缺失

### D 级（40-59 分）
- 来源：媒体/非官方渠道
- 一致性：单一来源
- 时效性：3 年以上数据
- 完整性：大量字段缺失

### E 级（<40 分）
- 来源：不可靠来源
- 一致性：与其他来源严重冲突
- 时效性：过时数据
- 完整性：关键字段缺失

---

**文档结束**
"""
    
    ref_path = base_path / "references" / "reference-guide.md"
    with open(ref_path, 'w', encoding='utf-8') as f:
        f.write(reference)
    
    print(f"[OK] Created reference document: {ref_path}")

def verify_skill(base_path):
    """验证技能完整性"""
    required_files = [
        "SKILL.md",
        "README.md",
        "_skillhub_meta.json",
        "scripts/init_data_cleaner.py",
        "config/cleaner_config.yaml",
        "references/reference-guide.md"
    ]
    
    print("\n[CHECK] Skill integrity check:")
    all_exist = True
    for file_path in required_files:
        full_path = base_path / file_path
        exists = full_path.exists()
        status = "[OK]" if exists else "[MISSING]"
        print(f"{status} {file_path}")
        if not exists:
            all_exist = False
    
    if all_exist:
        print("\n[SUCCESS] Skill initialization completed! All required files are in place.")
        print(f"\nSkill location: {base_path}")
        print(f"Version: {SKILL_VERSION}")
        print("\nUsage:")
        print('  use_skill("data-cleaner", {...})')
    else:
        print("\n[ERROR] Skill initialization incomplete. Please check missing files.")
    
    return all_exist

def main():
    """主函数"""
    print(f"Initializing {SKILL_NAME} v{SKILL_VERSION}...")
    print("=" * 60)
    
    # 技能根目录是 scripts 的父目录
    base_path = Path(__file__).parent.parent
    
    # Step 1: 创建目录结构
    print("\n[Step 1] Creating directory structure...")
    create_directory_structure(base_path)
    
    # Step 2: 创建配置文件
    print("\n[Step 2] Creating configuration file...")
    create_config_file(base_path)
    
    # Step 3: 创建示例数据
    print("\n[Step 3] Creating sample data...")
    create_sample_data(base_path)
    
    # Step 4: 创建参考文档
    print("\n[Step 4] Creating reference document...")
    create_reference_doc(base_path)
    
    # Step 5: 验证技能
    print("\n[Step 5] Verifying skill integrity...")
    verify_skill(base_path)
    
    print("\n" + "=" * 60)
    print(f"{SKILL_NAME} initialization completed!")

if __name__ == "__main__":
    main()
