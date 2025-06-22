# gui.py

import tkinter as tk
from tkinter import ttk, messagebox
from bot import BasicBot
from config import API_KEY, API_SECRET

# Setup the bot
bot = BasicBot(API_KEY, API_SECRET)

# Main window
root = tk.Tk()
root.title("Binance Futures Trading Bot")
root.geometry("400x400")
root.configure(bg="#f2f2f2")

# Heading
tk.Label(root, text="Trading Bot", font=("Arial", 16), bg="#f2f2f2").pack(pady=10)

# Symbol
tk.Label(root, text="Symbol (e.g., BTCUSDT):", bg="#f2f2f2").pack()
symbol_entry = tk.Entry(root)
symbol_entry.pack()

# Side
tk.Label(root, text="Side:", bg="#f2f2f2").pack()
side_combo = ttk.Combobox(root, values=["Buy", "Sell"])
side_combo.pack()

# Order Type
tk.Label(root, text="Order Type:", bg="#f2f2f2").pack()
order_type_combo = ttk.Combobox(root, values=["MARKET", "LIMIT"])
order_type_combo.pack()

# Quantity
tk.Label(root, text="Quantity:", bg="#f2f2f2").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

# Price (only for LIMIT)
tk.Label(root, text="Price (for LIMIT only):", bg="#f2f2f2").pack()
price_entry = tk.Entry(root)
price_entry.pack()

# Output Label
result_label = tk.Label(root, text="", fg="green", bg="#f2f2f2", wraplength=300)
result_label.pack(pady=10)

# Order function
def place_order():
    symbol = symbol_entry.get()
    side = side_combo.get().lower()
    order_type = order_type_combo.get().upper()
    quantity = quantity_entry.get()
    price = price_entry.get() if order_type == "LIMIT" else None

    try:
        quantity = float(quantity)
        if order_type == "LIMIT" and not price:
            result_label.config(text="Please enter a price for LIMIT order", fg="red")
            return

        order = bot.place_order(symbol, side, order_type, quantity, price)
        if "error" in order:
            result_label.config(text=f"Error: {order['error']}", fg="red")
        else:
            result_label.config(text="✅ Order Placed Successfully!", fg="green")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red")

# Button
tk.Button(root, text="Place Order", command=place_order, bg="#007acc", fg="white", padx=10, pady=5).pack(pady=20)

# Run the GUI
root.mainloop()
