# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

print("========================================")
print("       STOCK PORTFOLIO TRACKER")
print("========================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, "- $", price)

# Store portfolio details
portfolio = {}

# Ask how many different stocks the user wants to enter
number_of_stocks = int(input("\nHow many different stocks do you own? "))

# Take stock details from the user
for i in range(number_of_stocks):

    stock = input("\nEnter stock symbol: ").upper()

    # Check whether the stock exists
    if stock not in stock_prices:
        print("Stock not available. Please enter a valid stock symbol.")
        continue

    quantity = int(input("Enter quantity: "))

    # Calculate investment value
    value = stock_prices[stock] * quantity

    # Store the information
    portfolio[stock] = {
        "quantity": quantity,
        "price": stock_prices[stock],
        "value": value
    }

# Display portfolio
print("\n========================================")
print("          YOUR PORTFOLIO")
print("========================================")

total_value = 0

for stock, details in portfolio.items():

    print("\nStock:", stock)
    print("Quantity:", details["quantity"])
    print("Price: $", details["price"])
    print("Investment Value: $", details["value"])

    total_value += details["value"]

# Display total investment
print("\n========================================")
print("Total Portfolio Value: $", total_value)
print("========================================")