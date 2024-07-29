import yfinance as yf

def get_balance_sheet(ticker):
    stock = yf.Ticker(ticker)
    balance_sheet = stock.balance_sheet
    return balance_sheet

if __name__ == "__main__":
    ticker = 'AAPL'  # Example ticker
    balance_sheet = get_balance_sheet(ticker)
    print(balance_sheet)

