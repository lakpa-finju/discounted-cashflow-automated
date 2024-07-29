
import yfinance as yf

def get_cash_flow_statement(ticker):
    stock = yf.Ticker(ticker)
    cash_flow = stock.cashflow
    return cash_flow

if __name__ == "__main__":
    ticker = 'AAPL'  # Example ticker
    cash_flow_statement = get_cash_flow_statement(ticker)
    print(cash_flow_statement)

