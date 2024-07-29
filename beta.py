import yfinance as yf
import numpy as np

def calculate_beta(ticker, market_index='^GSPC'):
    # Get historical market data
    stock_data = yf.download(ticker, period='5y', interval='1d')['Adj Close']
    market_data = yf.download(market_index, period='5y', interval='1d')['Adj Close']
    
    # Calculate daily returns
    stock_returns = stock_data.pct_change().dropna()
    market_returns = market_data.pct_change().dropna()
    
    # Align lengths
    min_len = min(len(stock_returns), len(market_returns))
    stock_returns = stock_returns[-min_len:]
    market_returns = market_returns[-min_len:]
    
    # Calculate covariance and variance
    covariance = np.cov(stock_returns, market_returns)[0, 1]
    variance = np.var(market_returns)
    
    # Calculate beta
    beta = covariance / variance
    return beta

if __name__ == "__main__":
    ticker = 'AAPL'  # Example ticker
    beta_value = calculate_beta(ticker)
    print(f"The beta for {ticker} is {beta_value:.2f}")
