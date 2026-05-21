"""
金融数据获取示例
演示如何使用 finance-data-retrieval 插件获取各类财务数据
"""

import requests
import json

# API基础配置
BASE_URL = "https://www.codebuddy.cn/v2/tool/financedata"

def call_api(api_name: str, params: dict, fields: str = "") -> dict:
    """
    调用金融数据API
    
    Args:
        api_name: 接口名称
        params: 请求参数
        fields: 返回字段（可选）
    
    Returns:
        API响应数据
    """
    payload = {
        "api_name": api_name,
        "params": params
    }
    if fields:
        payload["fields"] = fields
    
    try:
        response = requests.post(BASE_URL, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"API调用失败: {e}")
        return {"code": -1, "msg": str(e)}


def get_stock_basic(ts_code: str) -> dict:
    """获取股票基本信息"""
    return call_api("stock_basic", {"ts_code": ts_code})


def get_daily_data(ts_code: str, start_date: str, end_date: str) -> dict:
    """获取日线行情数据"""
    return call_api("daily", {
        "ts_code": ts_code,
        "start_date": start_date,
        "end_date": end_date
    })


def get_income_statement(ts_code: str, period: str = None) -> dict:
    """
    获取利润表数据
    
    Args:
        ts_code: 股票代码（如600519.SH）
        period: 报告期（如20241231），不传返回全部
    """
    params = {"ts_code": ts_code}
    if period:
        params["period"] = period
    return call_api("income", params)


def get_balance_sheet(ts_code: str, period: str = None) -> dict:
    """获取资产负债表"""
    params = {"ts_code": ts_code}
    if period:
        params["period"] = period
    return call_api("balancesheet", params)


def get_cashflow_statement(ts_code: str, period: str = None) -> dict:
    """获取现金流量表"""
    params = {"ts_code": ts_code}
    if period:
        params["period"] = period
    return call_api("cashflow", params)


def get_financial_indicators(ts_code: str) -> dict:
    """获取财务指标数据（ROE、ROA、毛利率等）"""
    return call_api("fina_indicator", {"ts_code": ts_code})


def get_hk_stock_basic(ts_code: str) -> dict:
    """获取港股基本信息"""
    return call_api("hk_basic", {"ts_code": ts_code})


def get_hk_daily(ts_code: str, start_date: str, end_date: str) -> dict:
    """获取港股日线行情"""
    return call_api("hk_daily", {
        "ts_code": ts_code,
        "start_date": start_date,
        "end_date": end_date
    })


def get_us_stock_basic(ts_code: str) -> dict:
    """获取美股基本信息"""
    return call_api("us_basic", {"ts_code": ts_code})


def get_us_income(ts_code: str, report_type: str = "Q4") -> dict:
    """
    获取美股利润表
    
    Args:
        ts_code: 美股代码（如TCEHY）
        report_type: Q1/Q2/Q3/Q4（Q4为年报）
    """
    return call_api("us_income", {
        "ts_code": ts_code,
        "report_type": report_type
    })


# ============ 使用示例 ============

if __name__ == "__main__":
    print("=" * 60)
    print("金融数据获取示例")
    print("=" * 60)
    
    # 示例1: 获取贵州茅台基本信息
    print("\n【示例1】贵州茅台基本信息")
    result = get_stock_basic("600519.SH")
    if result.get("code") == 0:
        data = result["data"]
        print(f"返回字段: {data['fields']}")
        print(f"数据条数: {len(data['items'])}")
        if data['items']:
            item = data['items'][0]
            print(f"股票信息: {dict(zip(data['fields'], item))}")
    else:
        print(f"错误: {result.get('msg')}")
    
    # 示例2: 获取腾讯港股基本信息
    print("\n【示例2】腾讯控股港股基本信息")
    result = get_hk_stock_basic("00700.HK")
    if result.get("code") == 0:
        data = result["data"]
        if data['items']:
            item = data['items'][0]
            info = dict(zip(data['fields'], item))
            print(f"股票名称: {info.get('name')}")
            print(f"公司全称: {info.get('fullname')}")
            print(f"上市日期: {info.get('list_date')}")
            print(f"市场类别: {info.get('market')}")
    else:
        print(f"错误: {result.get('msg')}")
    
    # 示例3: 获取腾讯ADR美股基本信息
    print("\n【示例3】腾讯ADR美股基本信息")
    result = get_us_stock_basic("TCEHY")
    if result.get("code") == 0:
        data = result["data"]
        if data['items']:
            item = data['items'][0]
            info = dict(zip(data['fields'], item))
            print(f"ADR名称: {info.get('enname')}")
            print(f"上市日期: {info.get('list_date')}")
            print(f"股票类型: {info.get('classify')}")
    else:
        print(f"错误: {result.get('msg')}")
    
    print("\n" + "=" * 60)
    print("示例完成")
    print("=" * 60)
