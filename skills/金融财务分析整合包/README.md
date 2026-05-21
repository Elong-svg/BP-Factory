# 金融财务分析整合包

## 简介

这是一个完整的金融财务分析解决方案，整合了数据获取、财务分析、交易决策、报表生成等全链路能力。

## 整合的插件

| 插件 | 功能 | 路径 |
|------|------|------|
| **finance-data** | 金融数据检索（A股/港股/美股/基金/期货） | `marketplace/plugins/finance-data/` |
| **trading-assistant** | 交易分析与投资决策 | `marketplace/plugins/trading-assistant/` |
| **finance** | 财务会计与报表生成 | `marketplace/plugins/finance/` |
| **data** | 数据分析与可视化 | `marketplace/plugins/data/` |
| **equity-research** | 股权研究 | `marketplace/plugins/equity-research/` |
| **investment-banking** | 投资银行 | `marketplace/plugins/investment-banking/` |
| **wealth-management** | 财富管理 | `marketplace/plugins/wealth-management/` |

## 快速开始

### 1. 获取股票财务数据

```python
from examples.获取财务数据 import get_income_statement, get_financial_indicators

# 获取茅台利润表
income = get_income_statement("600519.SH", "20241231")

# 获取财务指标
indicators = get_financial_indicators("600519.SH")
```

### 2. 分析财务指标

```python
from examples.财务指标计算 import FinancialAnalyzer

analyzer = FinancialAnalyzer(income_data, balance_data, cashflow_data)

# 计算ROE、ROA等
ratios = analyzer.calculate_profitability_ratios()
print(ratios)

# 生成完整报告
report = analyzer.generate_report()
print(report)
```

### 3. 投资决策分析

使用 trading-analysis 插件进行多维度分析：

```
技能: trading-analysis
输入: 股票代码 + 分析需求
输出: BUY/SELL/HOLD 建议 + 详细报告
```

## 目录结构

```
金融财务分析整合包/
├── SKILL.md              # 技能定义文件
├── README.md             # 本文件
├── workflows/            # 工作流模板
│   ├── 股票分析.yaml
│   ├── 财报生成.yaml
│   └── 投资决策.yaml
├── examples/             # 示例代码
│   ├── 获取财务数据.py
│   └── 财务指标计算.py
└── references/           # 参考资料
    └── API限制.md
```

## 数据覆盖范围

### 股票市场
- **A股**: 全市场5000+股票
- **港股**: 主板+创业板
- **美股**: 中概股+主要美股

### 数据类型
- 基础信息（公司资料、股本结构）
- 行情数据（日线、分钟线、tick）
- 财务数据（三大报表、财务指标）
- 特色数据（资金流向、龙虎榜、融资融券）

### 基金数据
- 公募基金基本信息
- 净值数据
- 持仓明细

### 期货数据
- 合约信息
- 日线/分钟线行情
- 持仓排名

### 宏观数据
- GDP、CPI、PPI
- 利率（Shibor、LPR、Libor）
- 汇率

## 使用场景

### 场景1: 上市公司研究
1. 使用 finance-data 获取公司财务数据
2. 使用 finance 进行财务指标分析
3. 使用 data 生成可视化图表
4. 使用 document-skills 生成研究报告

### 场景2: 投资决策
1. 使用 trading-analysis 启动分析流程
2. 自动调用 finance-data 获取数据
3. 多角色辩论生成投资建议
4. 输出完整的交易决策报告

### 场景3: 财务报表生成
1. 使用 finance 进行会计处理
2. 生成三大报表
3. 使用 document-skills 输出标准格式

## API限制

详见 `references/API限制.md`

**重要限制**:
- 美股财务数据：2次/天
- 港股日线：10次/天
- A股财务数据：100次/天
- 公告原文：需申请权限

## 注意事项

1. **股票代码格式**: A股必须带后缀（如600519.SH）
2. **日期格式**: 使用YYYYMMDD格式
3. **权限申请**: 部分接口需要单独申请权限
4. **本地缓存**: 建议实现本地缓存减少API调用

## 相关链接

- [finance-data 插件文档](../marketplace/plugins/finance-data/)
- [trading-analysis 技能文档](../marketplace/plugins/trading-assistant/skills/trading-analysis/)
- [Tushare Pro 官方文档](https://tushare.pro/document/2)

## 更新日志

### v1.0.0 (2026-03-29)
- 初始版本发布
- 整合7个核心插件
- 提供完整工作流模板
- 包含示例代码和文档
