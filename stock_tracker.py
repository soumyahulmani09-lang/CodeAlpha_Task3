# --- Stock Portfolio Tracker ---

# Hardcoded stock prices (you can modify these)
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOGL": 140,  # Google
    "AMZN": 130,   # Amazon
    "MSFT": 320    # Microsoft
}

portfolio = {}  # To store user-entered stocks and quantities

print("📈 Welcome to Stock Portfolio Tracker!")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"  {stock}: ${price}")

# Taking user inputs
while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not found in list. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# Calculate total investment
total_investment = 0
print("\n🧾 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares × ${price} = ${investment}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# --- Optional: Save result to a file ---
save_choice = input("\nDo you want to save this summary to a file? (yes/no): ").lower()

if save_choice == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-----------------------\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${investment}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("✅ Summary saved as 'portfolio_summary.txt'")
else:
    print("📁 File not saved.")