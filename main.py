# main.py

from bot import BasicBot
from config import API_KEY, API_SECRET

def main():
    bot = BasicBot(API_KEY, API_SECRET)

    symbol = input("Enter symbol (e.g., BTCUSDT): ")
    side = input("Buy or Sell: ").lower()
    order_type = input("Order Type (MARKET / LIMIT): ").upper()
    quantity = float(input("Quantity: "))

    price = None
    if order_type == "LIMIT":
        price = input("Enter limit price: ")

    result = bot.place_order(symbol, side, order_type, quantity, price)
    print("Order Result:", result)

if __name__ == "__main__":
    main()
