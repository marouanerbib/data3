from indicator_calculator import IndicatorCalculator

class DataProcessor:
    def __init__(self, api_client):
        self.api_client = api_client

    def process_company_data(self, symbol):
        # Données nécessaires
        free_cash_flow = self.api_client.get_financial_data("cash-flow-statement", symbol, "freeCashFlow")
        revenue = self.api_client.get_financial_data("income-statement", symbol, "revenue")
        total_assets = self.api_client.get_financial_data("balance-sheet-statement", symbol, "totalAssets")
        account_payables = self.api_client.get_financial_data("balance-sheet-statement", symbol, "accountPayables")
        tax_payables = self.api_client.get_financial_data("balance-sheet-statement", symbol, "taxPayables")
        cash_and_investments = self.api_client.get_financial_data("balance-sheet-statement", symbol, "cashAndShortTermInvestments")
        current_liabilities = self.api_client.get_financial_data("balance-sheet-statement", symbol, "totalCurrentLiabilities")
        current_assets = self.api_client.get_financial_data("balance-sheet-statement", symbol, "totalCurrentAssets")
        dividends_paid = self.api_client.get_financial_data("cash-flow-statement", symbol, "dividendsPaid")
        market_cap = self.api_client.get_financial_data("key-metrics", symbol, "marketCap")
        free_cash_flow_per_share = self.api_client.get_financial_data("key-metrics", symbol, "freeCashFlowPerShare")

        # Calculs
        fcf_margin = IndicatorCalculator.calculate_fcf_margin(free_cash_flow, revenue)
        invested_capital = IndicatorCalculator.calculate_invested_capital(total_assets, account_payables, tax_payables, cash_and_investments, current_liabilities, current_assets)
        fcf_roc = IndicatorCalculator.calculate_fcf_roc(free_cash_flow, invested_capital)
        cagr = IndicatorCalculator.calculate_cagr(free_cash_flow_per_share)
        fcf_5yr_rsq = IndicatorCalculator.calculate_fcf_5yr_rsq(free_cash_flow_per_share)
        fcf_margin_5yr_exp = IndicatorCalculator.calculate_fcf_margin_5yr_exp(fcf_margin)
        min_fcf_roc = IndicatorCalculator.calculate_5yr_min_fcf_roc(fcf_roc)
        difference = IndicatorCalculator.calculate_difference(fcf_roc, min_fcf_roc)
        payout_ratio = IndicatorCalculator.calculate_payout_ratio(free_cash_flow, dividends_paid)
        fcf_yield = IndicatorCalculator.calculate_fcf_yield(free_cash_flow, market_cap)

        return {
            "Symbol": symbol,
            "FCF Margin (%)": fcf_margin[-1],
            "5yr FCF CAGR (%)": cagr,
            "5yr FCF RSq": fcf_5yr_rsq,
            "5yr FCF Margin Exp (%)": fcf_margin_5yr_exp,
            "FCF ROC (%)": fcf_roc[-1],
            "5yr Min FCF ROC (%)": min_fcf_roc,
            "Difference (%)": difference,
            "Payout Ratio (%)": payout_ratio[-1],
            "FCF Yield (%)": fcf_yield[-1],
        }