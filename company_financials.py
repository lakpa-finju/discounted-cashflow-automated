"""
This returns all companies IS, BS, CF
"""
import yfinance as yf

def get_company_data(ticker):
    """
    Fetch financial data for the given company from Yahoo Finance.
    """
    company = yf.Ticker(ticker)
    income_statement = company.income_stmt
    balance_sheet = company.balance_sheet
    cash_flow = company.cashflow
    # Fetch additional data, such as comps and risk factors
    return income_statement, balance_sheet, cash_flow

if __name__ == "__main__":
    ticker = 'AAPL'  # Example ticker
    financials = get_company_data(ticker)
    income_statement = financials[0]
    balance_sheet = financials[1]
    cash_flow = financials[2]
    print(income_statement)
    print(balance_sheet)
    print(cash_flow)
