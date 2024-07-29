import yfinance as yf
def get_income_statement(ticker):
    stock = yf.Ticker(ticker)
    income_statement = stock.income_stmt
    return income_statement

if __name__ == "__main__":
    ticker = 'AAPL'  # Example ticker
    income_statement = get_income_statement(ticker)
    print(income_statement)

