---
name: 金融财务分析整合包
description: |
  金融财务分析完整解决方案，整合数据获取、财务分析、交易决策、报表生成等全链路能力。
  覆盖A股/港股/美股/期货/基金等全市场数据，支持财务报表分析、投资交易决策、可视化展示。
  触发词：金融分析、财务分析、财报、股票数据、投资分析、交易决策、财务数据、年报分析、财务报表、股票研究
version: 1.0.0
author: Claw
disable: false
---

# 金融财务分析整合包

## 概述

本整合包汇集了金融财务分析领域的全部能力，形成完整的分析工作流：

```
数据获取 → 财务分析 → 交易决策 → 报表生成 → 可视化展示
```

## 包含组件

### 1. 金融数据检索插件 (finance-data)
**路径**: `marketplaces/cb_teams_marketplace/plugins/finance-data/`

**能力**:
- **股票数据**: A股/港股/美股行情、财务数据、基本面指标
- **基金数据**: 公募基金净值、持仓、分红信息
- **期货数据**: 合约信息、行情、持仓排名
- **宏观数据**: GDP、CPI、利率、汇率
- **特色数据**: 龙虎榜、资金流向、融资融券

**核心接口**:
| 类别 | 接口 | 用途 |
|------|------|------|
| 行情 | `daily`, `hk_daily`, `us_daily` | 日线行情 |
| 财务 | `income`, `balancesheet`, `cashflow` | 三大报表 |
| 指标 | `fina_indicator`, `daily_basic` | 财务指标 |
| 公告 | `anns_d` | 公告原文PDF |

### 2. 交易分析插件 (trading-assistant)
**路径**: `marketplaces/cb_teams_marketplace/plugins/trading-assistant/`

**能力**:
- **多角色投资分析**: 市场分析师、基本面分析师、新闻分析师、情绪分析师
- **投资决策辩论**: 牛市/熊市观点辩论，研究经理仲裁
- **交易决策**: 买入/卖出/持有建议
- **风险评估**: 激进/保守/中性三方辩论

**分析流程**:
1. 数据收集（调用finance-data）
2. 投资辩论（Bull vs Bear）
3. 交易决策（Trader决策）
4. 风险评估（3-way debate）
5. 最终报告

### 3. 财务会计插件 (finance)
**路径**: `marketplaces/cb_teams_marketplace/plugins/finance/`

**能力**:
- **会计分录**: 预提、固定资产、预付账款、工资、收入确认
- **对账**: 总账vs明细账、银行对账
- **报表生成**: 损益表、资产负债表、现金流量表
- **差异分析**: 预算vs实际、期间比较
- **SOX合规**: 控制测试、抽样、工作底稿

### 4. 数据分析插件 (data)
**路径**: `marketplaces/cb_teams_marketplace/plugins/data/`

**能力**:
- **SQL查询**: 金融数据查询优化
- **数据探索**: 财务数据质量检查
- **可视化**: 财务图表、仪表板
- **统计分析**: 财务指标趋势、异常检测

### 5. 股权研究插件 (equity-research)
**路径**: `marketplaces/cb_teams_marketplace/plugins/equity-research/`

**能力**:
- 股票研究报告生成
- 估值模型（DCF、可比公司）
- 行业分析
- 公司基本面研究

### 6. 投资银行插件 (investment-banking)
**路径**: `marketplaces/cb_teams_marketplace/plugins/investment-banking/`

**能力**:
- M&A分析
- 融资方案
- 财务建模
- 尽职调查

### 7. 财富管理插件 (wealth-management)
**路径**: `marketplaces/cb_teams_marketplace/plugins/wealth-management/`

**能力**:
- 资产配置
- 投资组合分析
- 风险管理
- 客户报告

## 快速开始

### 场景1: 股票财务分析
```
用户: 分析贵州茅台的财务状况

流程:
1. finance-data-retrieval → 获取财务数据
2. finance → 财务指标分析
3. data → 可视化展示
```

### 场景2: 投资决策
```
用户: 腾讯股票现在能不能买

流程:
1. trading-analysis → 启动分析流程
   - Phase 1: 调用finance-data获取数据
   - Phase 2-5: 多角色辩论决策
2. 输出BUY/SELL/HOLD建议
```

### 场景3: 财报生成
```
用户: 生成月度财务分析报告

流程:
1. finance → 会计分录、对账
2. finance → 生成报表
3. data → 可视化图表
4. document-skills → 生成报告文档
```

## 数据权限说明

| 接口类型 | 权限限制 | 备注 |
|---------|---------|------|
| 基础行情 | 无限制 | 日线、分钟线 |
| 财务数据 | 10-100次/天 | 利润表、资产负债表 |
| 公告原文 | 需申请 | PDF下载链接 |
| 实时数据 | 限流 | tick、实时排名 |

## 工作流示例

### 完整财务分析工作流

```yaml
workflow: 上市公司财务分析

步骤1_数据获取:
  技能: finance-data-retrieval
  操作:
    - 获取股票基本信息 (stock_basic)
    - 获取历史行情 (daily)
    - 获取财务报表 (income, balancesheet, cashflow)
    - 获取财务指标 (fina_indicator)

步骤2_财务分析:
  技能: finance
  操作:
    - 分析三大报表
    - 计算关键指标 (ROE, ROA, 毛利率等)
    - 期间对比分析
    - 行业对标

步骤3_投资决策 (可选):
  技能: trading-analysis
  操作:
    - 多维度分析
    - 生成投资建议

步骤4_可视化:
  技能: data
  操作:
    - 生成财务图表
    - 创建仪表板

步骤5_报告生成:
  技能: document-skills
  操作:
    - 生成PDF/Word报告
    - 包含图表和分析结论
```

## 常用代码示例

### 获取财务数据
```python
import requests

url = "https://www.codebuddy.cn/v2/tool/financedata"
payload = {
    "api_name": "income",
    "params": {"ts_code": "600519.SH", "period": "20241231"}
}
response = requests.post(url, json=payload)
data = response.json()
```

### 港股数据
```python
payload = {
    "api_name": "hk_basic",
    "params": {"ts_code": "00700.HK"}
}
```

### 美股数据
```python
payload = {
    "api_name": "us_income",
    "params": {"ts_code": "TCEHY", "report_type": "Q4"}
}
```

## 目录结构

```
金融财务分析整合包/
├── SKILL.md                    # 本文件
├── README.md                   # 使用指南
├── workflows/                  # 工作流模板
│   ├── 股票分析.yaml
│   ├── 财报生成.yaml
│   └── 投资决策.yaml
├── examples/                   # 示例代码
│   ├── 获取财务数据.py
│   ├── 财务指标计算.py
│   └── 可视化展示.py
├── references/                 # 参考资料
│   ├── 财务指标说明.md
│   ├── 数据字典.md
│   └── API限制.md
└── templates/                  # 报告模板
    ├── 财务分析报告.docx
    └── 投资研究报告.pptx
```

## 相关链接

- finance-data: `~/.workbuddy/plugins/marketplaces/cb_teams_marketplace/plugins/finance-data/`
- trading-assistant: `~/.workbuddy/plugins/marketplaces/cb_teams_marketplace/plugins/trading-assistant/`
- finance: `~/.workbuddy/plugins/marketplaces/cb_teams_marketplace/plugins/finance/`
- data: `~/.workbuddy/plugins/marketplaces/cb_teams_marketplace/plugins/data/`
- equity-research: `~/.workbuddy/plugins/marketplaces/cb_teams_marketplace/plugins/equity-research/`

## 更新日志

### v1.0.0 (2026-03-29)
- 初始版本
- 整合5个核心插件
- 提供完整工作流模板
