
import yfinance as yf

def get_income_statement(ticker):
    stock = yf.Ticker(ticker)
    income_statement = stock.financials
    return income_statement
