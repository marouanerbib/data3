import numpy as np
from scipy import stats

class IndicatorCalculator:
    @staticmethod
    def calculate_fcf_margin(free_cash_flow, revenue):
        return [fcf / rev for fcf, rev in zip(free_cash_flow, revenue)]

    @staticmethod
    def calculate_invested_capital(total_assets, account_payables, tax_payables, cash_and_investments, current_liabilities, current_assets):
        invested_capital = []
        for i in range(len(total_assets)):
            max_value = max(0, current_liabilities[i] - current_assets[i] + cash_and_investments[i])
            invested_capital.append(
                total_assets[i] - account_payables[i] - tax_payables[i] - cash_and_investments[i] + max_value
            )
        return invested_capital

    @staticmethod
    def calculate_fcf_roc(free_cash_flow, invested_capital):
        return [fcf / ic for fcf, ic in zip(free_cash_flow, invested_capital)]

    @staticmethod
    def calculate_cagr(free_cash_flow_per_share):
        return (free_cash_flow_per_share[-1] / free_cash_flow_per_share[0]) ** (1 / (len(free_cash_flow_per_share) - 1)) - 1

    @staticmethod
    def calculate_fcf_5yr_rsq(free_cash_flow_per_share):
        x = np.arange(1, len(free_cash_flow_per_share) + 1)
        y = np.array(free_cash_flow_per_share)
        res = stats.linregress(x, y)
        return res.rvalue ** 2


    @staticmethod
    def calculate_fcf_margin_5yr_exp(fcf_margin):
        """Évolution sur 5 ans du FCF Margin."""
        return (fcf_margin[-1] - fcf_margin[0]) / fcf_margin[0] * 100

    @staticmethod
    def calculate_5yr_min_fcf_roc(fcf_roc):
        """Minimum des FCF ROC historiques."""
        return min(fcf_roc)

    @staticmethod
    def calculate_difference(fcf_roc, min_fcf_roc):
        """Différence entre dernier FCF ROC et minimum."""
        return fcf_roc[-1] - min_fcf_roc

    @staticmethod
    def calculate_payout_ratio(free_cash_flow, dividends_paid):
        """Ratio de distribution."""
        return [div / fcf * 100 for div, fcf in zip(dividends_paid, free_cash_flow)]

    @staticmethod
    def calculate_fcf_yield(free_cash_flow, market_cap):
        """FCF Yield."""
        return [fcf / market_cap * 100 for fcf, market_cap in zip(free_cash_flow, market_cap)]