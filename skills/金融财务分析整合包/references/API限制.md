# 金融数据API使用限制

## 接口调用限制汇总

| 接口类别 | 接口名称 | 日限制次数 | 备注 |
|---------|---------|-----------|------|
| **基础数据** | stock_basic | 无限制 | 股票列表、基本信息 |
| | hk_basic | 无限制 | 港股基本信息 |
| | us_basic | 无限制 | 美股基本信息 |
| **行情数据** | daily | 无限制 | A股日线行情 |
| | hk_daily | 10次/天 | 港股日线行情 |
| | us_daily | 无限制 | 美股日线行情 |
| | stk_mins | 无限制 | 分钟线行情 |
| **财务数据** | income | 100次/天 | A股利润表 |
| | balancesheet | 100次/天 | A股资产负债表 |
| | cashflow | 100次/天 | A股现金流量表 |
| | fina_indicator | 100次/天 | 财务指标数据 |
| | us_income | 2次/天 | 美股利润表 |
| | us_balancesheet | 2次/天 | 美股资产负债表 |
| | us_cashflow | 2次/天 | 美股现金流量表 |
| | us_fina_indicator | 2次/天 | 美股财务指标 |
| **公告数据** | anns_d | 需申请 | 公告原文PDF |
| **特色数据** | moneyflow | 无限制 | 资金流向 |
| | top_list | 无限制 | 龙虎榜 |
| | limit_list_d | 无限制 | 涨跌停数据 |

## 代码格式要求

### 股票代码格式
- **A股**: 必须带交易所后缀
  - 上海证券交易所: `.SH` (如 `600519.SH`)
  - 深圳证券交易所: `.SZ` (如 `000001.SZ`)
  - 北京证券交易所: `.BJ` (如 `430047.BJ`)
- **港股**: 必须带 `.HK` 后缀
  - 如: `00700.HK`
- **美股**: 直接使用代码
  - 如: `TCEHY` (腾讯ADR)

### 日期格式
- **标准日期**: `YYYYMMDD` (如 `20240329`)
- **报告期**: `YYYYMMDD` (季度末日期，如 `20241231`)
- **时间段**: start_date 和 end_date 配合使用

## 权限申请

### 需要特殊权限的接口
1. **公告原文** (`anns_d`)
   - 用途: 获取上市公司公告PDF下载链接
   - 申请: https://tushare.pro/document/1?doc_id=108

2. **实时行情爬虫接口**
   - 用途: 实时tick、逐笔成交
   - 说明: 仅限SDK调用，不支持HTTP

### 权限等级
- **免费用户**: 基础行情、部分财务数据
- **付费用户**: 全部财务数据、公告数据
- **专业用户**: 实时数据、特色数据

## 最佳实践

### 1. 减少调用次数
```python
# ❌ 不推荐：多次调用
for code in stock_list:
    get_daily_data(code)  # 每天只能调用10次

# ✅ 推荐：批量获取
# 使用stock_basic获取列表，本地缓存
```

### 2. 本地缓存
```python
import json
import os

CACHE_DIR = ".cache"

def get_cached_or_fetch(cache_key: str, fetch_func):
    """带缓存的数据获取"""
    cache_file = os.path.join(CACHE_DIR, f"{cache_key}.json")
    
    # 检查缓存
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            return json.load(f)
    
    # 获取新数据
    data = fetch_func()
    
    # 保存缓存
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(cache_file, 'w') as f:
        json.dump(data, f)
    
    return data
```

### 3. 错误处理
```python
import time

def call_api_with_retry(api_func, max_retries=3, delay=1):
    """带重试的API调用"""
    for i in range(max_retries):
        try:
            result = api_func()
            if result.get("code") == 0:
                return result
            elif "最多访问" in result.get("msg", ""):
                print(f"达到调用限制，请明天再试")
                return None
        except Exception as e:
            print(f"调用失败({i+1}/{max_retries}): {e}")
            time.sleep(delay)
    
    return None
```

## 错误代码

| 错误代码 | 说明 | 解决方案 |
|---------|------|---------|
| 0 | 成功 | - |
| 40203 | 访问次数限制 | 明天再试或升级权限 |
| 40204 | 无接口权限 | 申请开通权限 |
| -1 | 网络错误 | 检查网络连接 |

## 联系方式

- 权限申请: https://tushare.pro/document/1?doc_id=108
- 接口文档: https://tushare.pro/document/2
- 问题反馈: support@tushare.pro
