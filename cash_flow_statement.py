
import yfinance as yf

def get_cash_flow_statement(ticker):
    stock = yf.Ticker(ticker)
    cash_flow = stock.cashflow
    return cash_flow
