"""
财务指标计算示例
演示如何基于财务数据计算关键财务指标
"""

import pandas as pd
from typing import Dict, List, Optional


class FinancialAnalyzer:
    """财务分析器"""
    
    def __init__(self, income_data: List, balance_data: List, cashflow_data: List):
        """
        初始化分析器
        
        Args:
            income_data: 利润表数据（字段名+数值列表）
            balance_data: 资产负债表数据
            cashflow_data: 现金流量表数据
        """
        self.income_df = self._to_dataframe(income_data)
        self.balance_df = self._to_dataframe(balance_data)
        self.cashflow_df = self._to_dataframe(cashflow_data)
    
    def _to_dataframe(self, data: List) -> pd.DataFrame:
        """将API返回数据转换为DataFrame"""
        if not data or len(data) < 2:
            return pd.DataFrame()
        
        fields = data[0]  # 字段名
        items = data[1]   # 数据项
        
        # 如果items是二维数组
        if items and isinstance(items[0], list):
            return pd.DataFrame(items, columns=fields)
        else:
            return pd.DataFrame([items], columns=fields)
    
    def calculate_profitability_ratios(self) -> Dict[str, float]:
        """
        计算盈利能力指标
        
        Returns:
            {
                'gross_margin': 毛利率,
                'net_margin': 净利率,
                'roe': 净资产收益率,
                'roa': 总资产收益率
            }
        """
        ratios = {}
        
        try:
            # 毛利率 = (营业收入 - 营业成本) / 营业收入
            if not self.income_df.empty:
                revenue = self.income_df.get('total_revenue', [0])[0]
                cost = self.income_df.get('oper_cost', [0])[0]
                if revenue and revenue != 0:
                    ratios['gross_margin'] = (revenue - cost) / revenue * 100
                
                # 净利率 = 净利润 / 营业收入
                net_income = self.income_df.get('net_income', [0])[0]
                if revenue and revenue != 0:
                    ratios['net_margin'] = net_income / revenue * 100
            
            # ROE = 净利润 / 股东权益
            if not self.income_df.empty and not self.balance_df.empty:
                net_income = self.income_df.get('net_income', [0])[0]
                equity = self.balance_df.get('total_hldr_eqy', [0])[0]
                if equity and equity != 0:
                    ratios['roe'] = net_income / equity * 100
            
            # ROA = 净利润 / 总资产
            if not self.income_df.empty and not self.balance_df.empty:
                net_income = self.income_df.get('net_income', [0])[0]
                total_assets = self.balance_df.get('total_assets', [0])[0]
                if total_assets and total_assets != 0:
                    ratios['roa'] = net_income / total_assets * 100
                    
        except Exception as e:
            print(f"计算盈利能力指标时出错: {e}")
        
        return ratios
    
    def calculate_solvency_ratios(self) -> Dict[str, float]:
        """
        计算偿债能力指标
        
        Returns:
            {
                'current_ratio': 流动比率,
                'quick_ratio': 速动比率,
                'debt_to_equity': 资产负债率
            }
        """
        ratios = {}
        
        try:
            if not self.balance_df.empty:
                # 流动比率 = 流动资产 / 流动负债
                current_assets = self.balance_df.get('total_cur_assets', [0])[0]
                current_liabilities = self.balance_df.get('total_cur_liab', [0])[0]
                if current_liabilities and current_liabilities != 0:
                    ratios['current_ratio'] = current_assets / current_liabilities
                
                # 速动比率 = (流动资产 - 存货) / 流动负债
                inventory = self.balance_df.get('inventories', [0])[0]
                if current_liabilities and current_liabilities != 0:
                    ratios['quick_ratio'] = (current_assets - inventory) / current_liabilities
                
                # 资产负债率 = 总负债 / 总资产
                total_liabilities = self.balance_df.get('total_liab', [0])[0]
                total_assets = self.balance_df.get('total_assets', [0])[0]
                if total_assets and total_assets != 0:
                    ratios['debt_to_equity'] = total_liabilities / total_assets * 100
                    
        except Exception as e:
            print(f"计算偿债能力指标时出错: {e}")
        
        return ratios
    
    def calculate_efficiency_ratios(self) -> Dict[str, float]:
        """
        计算运营效率指标
        
        Returns:
            {
                'asset_turnover': 总资产周转率,
                'inventory_turnover': 存货周转率
            }
        """
        ratios = {}
        
        try:
            if not self.income_df.empty and not self.balance_df.empty:
                revenue = self.income_df.get('total_revenue', [0])[0]
                total_assets = self.balance_df.get('total_assets', [0])[0]
                
                # 总资产周转率 = 营业收入 / 总资产
                if total_assets and total_assets != 0:
                    ratios['asset_turnover'] = revenue / total_assets
                    
        except Exception as e:
            print(f"计算运营效率指标时出错: {e}")
        
        return ratios
    
    def analyze_cashflow(self) -> Dict[str, any]:
        """
        分析现金流量
        
        Returns:
            {
                'operating_cashflow': 经营活动现金流,
                'investing_cashflow': 投资活动现金流,
                'financing_cashflow': 筹资活动现金流,
                'free_cashflow': 自由现金流
            }
        """
        analysis = {}
        
        try:
            if not self.cashflow_df.empty:
                # 经营活动现金流
                analysis['operating_cashflow'] = self.cashflow_df.get('net_cash_flows_fnc_act', [0])[0]
                
                # 投资活动现金流
                analysis['investing_cashflow'] = self.cashflow_df.get('net_cash_flows_inv_act', [0])[0]
                
                # 筹资活动现金流
                analysis['financing_cashflow'] = self.cashflow_df.get('net_cash_flows_fnc_act', [0])[0]
                
                # 自由现金流 = 经营现金流 - 资本支出
                operating_cf = self.cashflow_df.get('net_cash_flows_op_act', [0])[0]
                capex = self.cashflow_df.get('cash_pay_acq_const_fiolta', [0])[0]
                analysis['free_cashflow'] = operating_cf - capex if capex else operating_cf
                
        except Exception as e:
            print(f"分析现金流时出错: {e}")
        
        return analysis
    
    def generate_report(self) -> str:
        """生成财务分析报告"""
        report = []
        report.append("=" * 60)
        report.append("财务分析报告")
        report.append("=" * 60)
        
        # 盈利能力
        report.append("\n【盈利能力指标】")
        profit_ratios = self.calculate_profitability_ratios()
        for name, value in profit_ratios.items():
            report.append(f"  {name}: {value:.2f}%")
        
        # 偿债能力
        report.append("\n【偿债能力指标】")
        solvency_ratios = self.calculate_solvency_ratios()
        for name, value in solvency_ratios.items():
            report.append(f"  {name}: {value:.2f}")
        
        # 运营效率
        report.append("\n【运营效率指标】")
        efficiency_ratios = self.calculate_efficiency_ratios()
        for name, value in efficiency_ratios.items():
            report.append(f"  {name}: {value:.2f}")
        
        # 现金流
        report.append("\n【现金流分析】")
        cashflow = self.analyze_cashflow()
        for name, value in cashflow.items():
            if isinstance(value, (int, float)):
                report.append(f"  {name}: {value:,.0f}")
            else:
                report.append(f"  {name}: {value}")
        
        report.append("\n" + "=" * 60)
        
        return "\n".join(report)


# ============ 使用示例 ============

if __name__ == "__main__":
    print("财务指标计算示例")
    print("=" * 60)
    print("\n注意：本示例需要真实的财务数据才能运行")
    print("请先使用'获取财务数据.py'获取数据后再运行本示例")
    print("\n示例代码结构:")
    print("""
    from 获取财务数据 import get_income_statement, get_balance_sheet, get_cashflow_statement
    
    # 获取数据
    income = get_income_statement("600519.SH", "20241231")
    balance = get_balance_sheet("600519.SH", "20241231")
    cashflow = get_cashflow_statement("600519.SH", "20241231")
    
    # 创建分析器
    analyzer = FinancialAnalyzer(
        income_data=income["data"],
        balance_data=balance["data"],
        cashflow_data=cashflow["data"]
    )
    
    # 生成报告
    report = analyzer.generate_report()
    print(report)
    """)
