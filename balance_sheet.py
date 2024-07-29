
import yfinance as yf

def get_balance_sheet(ticker):
    stock = yf.Ticker(ticker)
    balance_sheet = stock.balance_sheet
    return balance_sheet
