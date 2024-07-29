def calculate_mrp(expected_market_return, risk_free_rate):
    mrp = expected_market_return - risk_free_rate
    return mrp

if __name__ == "__main__":
    # Example values
    expected_market_return = 0.08  # 8%
    risk_free_rate = 0.02  # 2%
    mrp = calculate_mrp(expected_market_return, risk_free_rate)
    print(f"The Market Risk Premium is {mrp:.2f}")
