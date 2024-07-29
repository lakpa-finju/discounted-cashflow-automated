import yfinance as yf
import pandas as pd
#from dcf_model import perform_dcf_analysis

def get_company_data(company_name):
    """
    Fetch financial data for the given company from Yahoo Finance.
    """
    company = yf.Ticker(company_name)
    income_statement = company.income_stmt
    balance_sheet = company.balance_sheet
    cash_flow = company.cashflow
    # Fetch additional data, such as comps and risk factors
    return income_statement, balance_sheet, cash_flow

def main():
    company_name = input("Enter the company name: ")
    income_statement, balance_sheet, cash_flow = get_company_data(company_name)
    print("income_statement: ", income_statement)
    print("cash_flow: ", cash_flow)
    print("balance_sheet: ", balance_sheet)



    # Preprocess the data
    # ...

    # Perform the DCF analysis
    #fair_value = perform_dcf_analysis(income_statement, balance_sheet, cash_flow)

    # Display the results
    #print(f"The fair value of {company_name} is: {fair_value}")

if __name__ == "__main__":
    main()

