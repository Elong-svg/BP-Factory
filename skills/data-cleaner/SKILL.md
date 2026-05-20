---
name: data-cleaner
version: 1.1.0
description: 通用数据清洗与集中引擎，将多来源、多格式的杂乱原始数据，清洗为干净、完整、结构化的标准化数据集。适配所有行业和公司。
triggers:
  - 数据清洗
  - 数据去重
  - 数据标准化
  - 数据集中
  - 清洗原始数据
  - 数据质量检查
  - 异常值检测
  - 缺失值处理
  - 数据结构化
  - 通用数据清洗
  - 多源数据合并
  - 数据可信度评级
disable: false
---

# data-cleaner - 通用数据清洗与集中引擎

## 一、技能定位与核心理念

### 1.1 技能定位

`data-cleaner` 是一个**通用型数据清洗引擎**，位于数据收集之后、专家分析之前。它将多来源、多格式的杂乱原始数据，清洗为干净、完整、结构化的标准化数据集。

**核心原则**：本技能不硬编码任何公司、行业、数值相关信息。所有内容均由领导 AI 在调用时通过输入参数动态提供，技能根据输入自动适配。

### 1.2 核心理念

```
输入：多来源原始数据（JSON/HTML/CSV/文本/PDF/Excel）+ 公司信息
处理：格式解析→去重合并→缺失值处理→异常值检测→标准化→可信度评级
输出：结构化清洗数据集 + 质量报告 + 数据字典
适配：通用型，通过输入的公司信息和行业信息自动适配
```

### 1.3 与其他技能的关系

```
数据收集阶段（上游）
├── finance-data-retrieval → API 获取的财务数据
├── web-scraper → 网页抓取的行业和竞争数据
├── pdf-parser → PDF 报告解析后的数据
└── user-upload → 用户手动提供的数据
        ↓
  【data-cleaner 清洗阶段】  ← 本技能
        ↓
专家分析阶段（下游）
├── 行业研究员 → 读取行业数据
├── 财务分析师 → 读取财务数据
├── 战略分析师 → 读取竞争和行业数据
├── 图表制作师 → 读取所有数值型数据
└── document-integrator → 参考数据字典
```

---

## 二、动态输入规范

### 2.1 必填输入参数

```yaml
required_input:
  company_info:
    name: "<动态> 公司全称（如：XX 集团股份有限公司）"
    code: "<动态> 股票代码或统一社会信用代码（如：XXXXXX.XX）"
    industry: "<动态> 所属行业（如：家用电器/新能源/生物医药）"
    sub_industry: "<动态> 细分行业（如：白色家电/光伏组件/创新药）"
  data_scope:
    target_period: "<动态> 目标分析期间（如：2019-2023）"
    period_type: "<动态> 期间类型（annual / quarterly / monthly）"
    unit_standard: "<动态> 目标单位（元 / 万元 / 亿元）"
  raw_data_path: "<动态> 原始数据目录路径（如：./raw_data/）"
```

### 2.2 可选输入参数

```yaml
optional_input:
  config:
    anomaly_thresholds:
      z_score_threshold: "<动态> Z 分数阈值（默认 3）"
      yoy_surge_threshold: "<动态> 同比激增阈值（默认 2.0，即 200%）"
      yoy_drop_threshold: "<动态> 同比骤降阈值（默认 -0.5，即 -50%）"
    impute:
      method: "<动态> 缺失值填充方法（linear / industry_avg / forward_fill / none）"
      ask_user: "<动态> 关键缺失是否询问用户（true / false）"
    output:
      generate_report: "<动态> 是否生成报告（true / false）"
      quality_threshold: "<动态> 质量合格分数线（默认 80）"
  custom_metrics:
    - name: "<动态> 自定义指标名称"
      formula: "<动态> 计算公式"
  industry_peers:
    - name: "<动态> 同行业可比公司 1"
      code: "<动态> 股票代码"
```

### 2.3 领导 AI 的动态思考指引

领导 AI 在调用 data-cleaner 前，应根据公司和行业特征进行以下思考：

**Step 1: 识别行业特征**
- 该行业的主要财务特征是什么？（如：制造业重资产、互联网轻资产、金融业高杠杆）
- 该行业有哪些特有的指标？（如：互联网行业的 DAU/MAU、制造业的产能利用率）
- 该行业的数据来源有哪些特点？

**Step 2: 识别数据特征**
- 原始数据包含哪些格式？（JSON/HTML/CSV/PDF/Excel）
- 数据覆盖期间是多久？是否有中断？
- 数据来源的可信度如何？

**Step 3: 识别分析需求**
- 后续分析需要哪些核心指标？
- 是否需要竞争对手对比数据？
- 对数据精度的要求有多高？

**Step 4: 确定清洗策略**
- 该行业最常见的数据问题是什么？
- 哪些指标最容易出现异常值？
- 异常检测阈值应如何设置？

---

## 三、动态指标体系

### 3.1 通用基础指标（适用于所有行业）

**利润表指标**（领导 AI 根据公司实际科目动态映射）：
- `revenue` - 营业收入（营业收入/主营业务收入/总营收）
- `cost_of_revenue` - 营业成本
- `gross_profit` - 毛利润（可计算：revenue - cost_of_revenue）
- `operating_expense` - 营业费用
- `selling_expense` - 销售费用
- `admin_expense` - 管理费用
- `rd_expense` - 研发费用
- `finance_expense` - 财务费用
- `operating_income` - 营业利润
- `net_income` - 净利润
- `parent_net_income` - 归母净利润

**资产负债表指标**：
- `total_assets` - 总资产
- `current_assets` - 流动资产
- `cash_and_equivalents` - 货币资金
- `accounts_receivable` - 应收账款
- `inventory` - 存货
- `total_liabilities` - 总负债
- `total_equity` - 所有者权益

**现金流量表指标**：
- `operating_cash_flow` - 经营活动现金流
- `investing_cash_flow` - 投资活动现金流
- `financing_cash_flow` - 筹资活动现金流
- `net_cash_flow` - 净现金流

### 3.2 动态关键指标（根据行业自动生成）

**盈利能力**（通用）：
- `gross_margin` - 毛利率 = gross_profit / revenue × 100
- `net_margin` - 净利率 = net_income / revenue × 100
- `roe` - 净资产收益率 = net_income / total_equity × 100
- `roa` - 总资产收益率 = net_income / total_assets × 100

**成长能力**（通用）：
- `revenue_growth` - 营收增长率
- `net_income_growth` - 净利润增长率

**营运能力**（制造业/零售适用）：
- `asset_turnover` - 总资产周转率
- `inventory_turnover` - 存货周转率
- `receivable_turnover` - 应收账款周转率

**偿债能力**（通用）：
- `debt_ratio` - 资产负债率
- `current_ratio` - 流动比率
- `quick_ratio` - 速动比率
- `interest_coverage` - 利息保障倍数

**行业特有指标**（领导 AI 根据行业动态选择）：
- **互联网**：DAU、MAU、ARPU、获客成本、LTV
- **制造业**：产能利用率、单位成本、研发强度
- **房地产**：预收款项、可售面积、平均售价
- **零售**：同店销售增长率、客单价、门店数量
- **金融**：净息差、不良贷款率、资本充足率
- **医药**：在研管线数量、研发费用率、新药获批数量

---

## 四、清洗流程（6 步法）

### 流程总览

```
Step 1: 数据接收与格式解析
    ↓
Step 2: 去重与合并
    ↓
Step 3: 缺失值处理
    ↓
Step 4: 异常值检测
    ↓
Step 5: 标准化与结构化
    ↓
Step 6: 可信度评级与输出
```

---

### Step 1: 数据接收与格式解析

**动作**：
1. 扫描 raw_data_path 指定目录下所有文件
2. 按文件格式调用对应解析器
3. 提取所有数值型数据点
4. 将科目名称与动态指标映射表进行匹配
5. 转换为统一的 data_record_schema 格式
6. 保留原始文本供溯源

**支持格式**：
- **JSON** - 直接解析 JSON 结构
- **HTML** - 提取表格数据
- **CSV** - 按行解析，自动检测分隔符
- **XLSX** - 读取指定 Sheet
- **PDF** - OCR/文本提取，识别表格
- **Text** - NLP 提取数值和指标

**输出**：
- `parsed_records.json` - 所有解析后的原始记录
- `parse_report.md` - 解析过程报告
- `unmapped_fields.json` - 未识别的科目名称

---

### Step 2: 去重与合并

**匹配准则**：
- metric_code 相同
- period 相同

**合并规则**：

| 情况 | 条件 | 处理方式 |
|------|------|---------|
| 数值一致 | 差异 ≤ 1% | 取可信度最高来源的值 |
| 数值轻微差异 | 差异 1%-5% | 取可信度最高来源的值，记录差异警告 |
| 数值严重冲突 | 差异 > 5% | 保留两条记录，标记冲突，需人工确认 |
| 单位不一致 | 量级差异为 10 的整数次幂 | 统一换算后合并 |

**来源优先级**（默认）：
1. 官方财报（年报/半年报/季报）
2. 权威数据库 API
3. 行业协会报告
4. 券商研报
5. 主流财经媒体
6. 公司官网/新闻稿
7. 其他来源

**输出**：
- `deduplicated_records.json`
- `merge_log.md`
- `conflict_report.md`

---

### Step 3: 缺失值处理

**检测内容**：
- 检查每个指标在目标期间内是否有完整时间序列
- 检查每条记录的必填字段是否完整
- 检查时间序列是否有中断

**处理策略**：

| 策略 | 适用场景 | 方法 | 置信度 |
|------|---------|------|--------|
| 线性插值 | 时间序列数据，缺失值前后有数据 | linear_interpolation | medium |
| 前向填充 | 趋势稳定的数据 | forward_fill | low |
| 行业均值 | 有同行业可比公司数据 | industry_average | low |
| 标记缺失 | 无法可靠补全的情况 | mark_missing | n/a |
| 询问用户 | 关键指标缺失且无法自动补全 | ask_user | depends |

**输出**：
- `imputed_records.json`
- `missing_value_report.md`
- `user_questions.md`（如有）

---

### Step 4: 异常值检测

**检测规则**：

| 规则 | 描述 | 严重程度 |
|------|------|---------|
| negative_value | 不应为负的指标出现负值 | critical |
| extreme_value | 偏离同行业同指标均值超过 Z 阈值 | warning |
| logical_violation | 违反财务逻辑 | critical |
| unit_error | 数值量级与预期严重不符 | warning |
| trend_break | 同比变化率异常（>200% 或 <-50%） | warning |

**逻辑检查**：
- net_income > revenue（净利润大于营收，需检查）
- current_assets > total_assets（流动资产大于总资产，不可能）
- 资产负债表勾稽关系：total_assets ≈ total_liabilities + total_equity

**处理方式**：
- 不删除任何数据
- 异常记录标记 `is_anomaly: true`
- 确认为错误的数据移入 `excluded_records`

**输出**：
- `anomaly_report.md`
- `excluded_records.json`

---

### Step 5: 标准化与结构化

**输出结构**（动态生成）：

```json
{
  "metadata": {
    "company_name": "<动态>",
    "company_code": "<动态>",
    "industry": "<动态>",
    "sub_industry": "<动态>",
    "data_period": "<动态>",
    "period_type": "<动态>",
    "total_records": "<动态>",
    "clean_records": "<动态>",
    "excluded_records": "<动态>",
    "imputed_records": "<动态>",
    "generation_time": "<动态>",
    "cleaner_version": "v1.1.0"
  },
  "financial_data": {
    "income_statement": ["<动态>"],
    "balance_sheet": ["<动态>"],
    "cash_flow_statement": ["<动态>"]
  },
  "key_metrics": {
    "profitability": ["<动态>"],
    "growth": ["<动态>"],
    "efficiency": ["<动态>"],
    "solvency": ["<动态>"],
    "industry_specific": ["<动态>"]
  },
  "industry_data": "<动态>",
  "competitive_data": "<动态>",
  "custom_metrics": "<动态>",
  "excluded_records": "<动态>",
  "quality_report": {}
}
```

---

### Step 6: 可信度评级与输出

**评分维度**：

| 维度 | 权重 | 评分方法 |
|------|------|---------|
| 来源权威性 | 40% | 根据 source_type 和 source_priority 映射 |
| 数据一致性 | 30% | 根据多来源一致性计算 |
| 时效性 | 20% | 根据数据期间与当前时间的差距 |
| 完整性 | 10% | 根据字段完整度计算 |

**可信度等级**：

| 等级 | 分数 | 说明 | 使用建议 |
|------|------|------|---------|
| A | 90-100 | 高可信 | 可直接使用 |
| B | 75-89 | 可信 | 建议标注来源 |
| C | 60-74 | 参考 | 需交叉验证 |
| D | 40-59 | 存疑 | 需人工确认 |
| E | <40 | 不可信 | 建议排除 |

**最终输出**：
- `cleaned_data.json` - 清洗后的数据集
- `quality_report.json` - 质量评分报告
- `cleaning_report.md` - 清洗过程报告
- `data_summary.md` - 数据摘要
- `data_dictionary.md` - 数据字典
- `excluded_records.json` - 排除记录

---

## 五、数据记录结构

每条清洗后的数据记录结构：

```yaml
record_id: "<动态> 系统自动生成唯一 ID>"
metric_name: "<动态> 从原始数据提取并标准化后的指标名称>"
metric_code: "<动态> 通过动态映射匹配的标准代码>"
category: "<动态> 所属类别"
raw_value: "<动态> 原始值（保留原文）>"
numeric_value: "<动态> 纯数字值（已换算为标准单位）>"
unit: "<动态> 标准单位>"
period: "<动态> 期间>"
period_type: "<动态> 期间类型>"
source_name: "<动态> 来源名称>"
source_url: "<动态> 来源链接>"
source_type: "<动态> api/web/document/manual>"
reliability_score: "<动态> 计算得出>"
reliability_level: "<动态> 计算得出>"
confidence: "<动态> high/medium/low/uncertain>"
is_estimated: "<动态> true/false>"
is_anomaly: "<动态> true/false>"
raw_text: "<动态> 原始文本>"
parse_status: "<动态> success/failed/partial>"
issues: "<动态> 问题列表>"
```

---

## 六、质量评分体系

### 评分维度

| 维度 | 权重 | 计算方法 | 默认合格线 |
|------|------|---------|-----------|
| 完整性 | 25% | 实际记录数 / 应有记录数 × 100 | 缺失率 < 15% |
| 准确性 | 30% | （总记录数 - 异常记录数）/ 总记录数 × 100 | 异常率 < 5% |
| 一致性 | 25% | 多来源数据一致的比例 | 差异率 < 5% |
| 时效性 | 20% | 根据数据期间与当前时间差距评分 | 由领导 AI 指定 |

**总分计算**：加权平均

**默认合格线**：80 分

### 动态调整

领导 AI 可根据行业特征调整权重：
- **金融行业**：准确性权重提高到 40%
- **新兴行业**：时效性权重提高到 30%
- **非上市公司**：完整性权重降低

---

## 七、调用示例

### 7.1 基本调用

```yaml
call:
  skill: "data-cleaner"
  action: "clean"
input:
  company_info:
    name: "<动态> 领导 AI 填入实际公司名称>"
    code: "<动态> 领导 AI 填入实际股票代码>"
    industry: "<动态> 领导 AI 填入实际行业>"
    sub_industry: "<动态> 领导 AI 填入细分行业>"
  data_scope:
    target_period: "<动态> 领导 AI 填入目标期间>"
    period_type: "<动态> 领导 AI 填入期间类型>"
    unit_standard: "<动态> 领导 AI 填入目标单位>"
  raw_data_path: "<动态> 领导 AI 填入原始数据路径>"
  config:
    anomaly_detection: true
    auto_impute: true
    generate_report: true
output:
  status: "<动态>"
  quality_score: "<动态>"
  grade: "<动态>"
  total_records: "<动态>"
  clean_records: "<动态>"
  excluded_records: "<动态>"
  imputed_records: "<动态>"
  output_files:
    cleaned_data: "<动态>"
    quality_report: "<动态>"
    cleaning_report: "<动态>"
    data_summary: "<动态>"
    data_dictionary: "<动态>"
    excluded_records: "<动态>"
```

### 7.2 分步调用

**Step 1: 仅执行格式解析**
```yaml
call:
  skill: "data-cleaner"
  action: "parse"
input:
  raw_data_path: "<动态>"
  company_info:
    industry: "<动态>"
output:
  parsed_records: "<动态>"
  parse_report: "<动态>"
  unmapped_fields: "<动态>"
```

**Step 2: 仅执行去重合并**
```yaml
call:
  skill: "data-cleaner"
  action: "deduplicate"
input:
  parsed_records: "<动态>"
  source_priority: "<动态>"
output:
  before_count: "<动态>"
  after_count: "<动态>"
  merged_count: "<动态>"
  conflict_count: "<动态>"
```

**Step 3: 仅执行异常检测**
```yaml
call:
  skill: "data-cleaner"
  action: "detect_anomalies"
input:
  records: "<动态>"
  anomaly_thresholds:
    z_score: "<动态>"
    yoy_surge: "<动态>"
    yoy_drop: "<动态>"
output:
  anomalies_detected: "<动态>"
  excluded: "<动态>"
  anomaly_report: "<动态>"
```

---

## 八、质量关口定义

**位置**：data-cleaner 之后，专家分析之前

**检查项**：

| 检查项 | 规则 | 失败处理 |
|--------|------|---------|
| 综合质量评分 | overall >= quality_threshold（默认 80） | 返回数据收集阶段补充数据 |
| 关键指标完整性 | required 字段完整率 >= 95% | 标记缺失指标，向用户询问 |
| 异常值处理状态 | 所有异常值已标记并有处理记录 | 人工确认异常值处理方式 |
| 来源覆盖率 | source_name 字段覆盖率 = 100% | 补充来源信息 |
| 可信度分布 | A+B 级记录占比 >= 90% | 检查低可信度数据 |

**通过**：进入专家分析阶段  
**失败**：返回数据收集阶段，生成补充数据清单

---

## 九、与其他技能的协作接口

### 9.1 上游接口

- **finance-data-retrieval** - API 获取的财务数据
- **web-scraper** - 网页抓取的行业和竞争数据
- **pdf-parser** - PDF 报告解析后的数据
- **user-upload** - 用户手动提供的数据

### 9.2 下游接口

- **industry_researcher** - 读取行业数据
- **financial_analyst** - 读取财务数据
- **strategy_analyst** - 读取竞争和行业数据
- **chart_maker** - 读取所有数值型数据
- **document-integrator** - 参考数据字典

---

## 十、常见问题与解决方案

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| 科目名称匹配失败 | 公司使用的会计准则不同或科目名称特殊 | 领导 AI 动态扩展 name_patterns |
| JSON 文件解析失败 | 文件编码不是 UTF-8 或 JSON 格式不规范 | 检查文件编码，尝试自动转换 |
| HTML 表格提取为空 | 表格使用 JavaScript 动态加载 | 使用支持 JS 渲染的方式重新获取 |
| PDF 数据提取不完整 | PDF 为扫描件而非文字版 | 使用 OCR 识别后重新提交 |
| 单位换算错误 | 原始数据单位标注不清 | 领导 AI 根据数值量级和行业常识推断 |
| 估算值过多 | 原始数据缺失严重 | 补充原始数据来源，减少估算依赖 |
| 异常值误判 | 行业特殊导致正常值被误判 | 领导 AI 根据行业特征调整阈值 |
| 质量评分过低 | 多个维度同时不达标 | 领导 AI 逐项排查，优先解决准确性问题 |
| 非上市公司数据不足 | 缺乏公开财报数据 | 领导 AI 降低完整性要求，使用更多估算 |

---

## 十一、最佳实践

### 11.1 领导 AI 调用前

| 实践项 | 说明 |
|--------|------|
| **充分识别公司特征** | 明确公司名称、代码、行业、会计准则 |
| **预判数据特征** | 了解原始数据的格式、来源、覆盖期间 |
| **选择行业指标** | 根据行业特征选择适用的关键指标 |
| **设置合理阈值** | 根据行业波动性设置异常检测阈值 |
| **准备可比公司** | 如需行业均值填充，提前准备可比公司列表 |

### 11.2 数据收集阶段

| 实践项 | 说明 |
|--------|------|
| **多来源采集** | 至少从 2 个独立来源获取关键财务数据 |
| **保留原始文件** | 所有原始数据文件保留不动，清洗只读取不修改 |
| **来源标注** | 采集时即标注数据来源和获取时间 |
| **格式统一** | 尽量统一为 JSON 格式，减少格式解析错误 |

### 11.3 清洗后检查

| 实践项 | 说明 |
|--------|------|
| **阅读清洗报告** | 了解清洗过程中的所有操作 |
| **检查排除记录** | 确认被排除的数据确实应排除 |
| **核实估算值** | 对关键指标的估算值进行人工核实 |
| **确认质量评分** | 确保综合评分达到设定的合格线 |
| **审阅决策记录** | 确认领导 AI 的决策合理 |

---

## 十二、版本历史

| 版本 | 日期 | 变更内容 |
|------|------|---------|
| v1.0.0 | 2026-03-31 | 初始版本，包含完整 6 步清洗流程 |
| v1.1.0 | 2026-03-31 | 通用化重构，移除所有硬编码内容，全部改为动态参数 |

---

## 附录：触发词列表

**13 个触发词**：
数据清洗、数据去重、数据标准化、数据集中、清洗原始数据、数据质量检查、异常值检测、缺失值处理、数据结构化、通用数据清洗、多源数据合并、数据可信度评级、data-cleaner

---

**文档结束**
