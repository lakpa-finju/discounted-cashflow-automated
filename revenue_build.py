import yfinance as yf
import numpy as np

def revenue_build(ticker):
    # Fetch historical financial data
    stock = yf.Ticker(ticker)
    financials = stock.financials

    # Extract revenue data
    revenue = financials.loc['Total Revenue']

    # Calculate average growth rate
    growth_rates = revenue.pct_change().dropna()
    avg_growth_rate = growth_rates.mean()

    # Forecast future revenue
    last_revenue = revenue.iloc[0]
    forecast_years = 5
    revenue_forecast = [last_revenue * (1 + avg_growth_rate) ** i for i in range(1, forecast_years + 1)]

    # Format the output
    formatted_forecast = [f"${value:,.2f}" for value in revenue_forecast]

    return formatted_forecast

if __name__ == "__main__":
    ticker = 'AAPL'  # Example ticker
    revenue_forecast = revenue_build(ticker)
    print("Revenue Forecast for the next 5 years:", revenue_forecast)

#this is the new script
python
import yfinance as yf
import pandas as pd

def get_revenue_build(ticker, start_date):
    """
    Calculates the revenue build for a given company by
itemizing revenue from income statement.

    Parameters:
    ticker (str): The stock ticker symbol.
    start_date (str): The date to start calculating revenue
from. Should be in 'YYYY-MM-DD' format.

    Returns:
    A pandas DataFrame with items generating revenue and
their respective shares of total revenue.
    """
    # Get the income statement for the given company
    income_statement = yf.Ticker(ticker).financials

    # Select only the income statements that are relevant
(i.e., not 'Cash Flow Statement')
    income_statement =
income_statement[income_statement.index.str.contains('Income
Statement')].iloc[0]

    # Calculate total revenue
    total_revenue = income_statement.loc['Total Revenue',
'Total Revenue']

    # Extract items generating revenue from the income
statement
    items_generating_revenue =
income_statement.loc[income_statement.iloc[:, 1] > 0, :]

    # Group by item and calculate share of total revenue
    revenue_build =
(items_generating_revenue.groupby(items_generating_revenue.ind(items_generating_revenue.groupby(items_geerating_revenue.index)['Total Revenue'].sum()
                     / total_revenue * 100).to_frame('Share
of Total Revenue')

    return revenue_build

# Usage example:
ticker = 'AAPL'
start_date = '2020-01-01'

revenue_build_df = get_revenue_build(ticker, start_date)
print(revenue_build_df)
