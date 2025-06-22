import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font
from bot import BasicBot
from config import API_KEY, API_SECRET

class TradingBotGUI:
    def __init__(self, root):
        self.root = root
        self.bot = BasicBot(API_KEY, API_SECRET)
        self.setup_styles()
        self.setup_ui()
        self.setup_bindings()

    def setup_styles(self):
        """Configure all visual styles for the application"""
        self.style = ttk.Style()
        
        # Color scheme
        self.bg_color = "#ffffff"
        self.primary_color = "#2563eb"
        self.success_color = "#16a34a"
        self.error_color = "#dc2626"
        self.text_color = "#1f2937"
        self.border_color = "#d1d5db"
        
        # Fonts
        self.title_font = Font(family="Segoe UI", size=16, weight="bold")
        self.label_font = Font(family="Segoe UI", size=10)
        self.entry_font = Font(family="Segoe UI", size=10)
        self.button_font = Font(family="Segoe UI", size=10, weight="bold")
        
        # Configure styles
        self.root.configure(bg=self.bg_color)
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("TLabel", background=self.bg_color, foreground=self.text_color, font=self.label_font)
        self.style.configure("TButton", font=self.button_font, borderwidth=1)
        self.style.configure("Accent.TButton", background=self.primary_color, foreground="white")
        self.style.map("Accent.TButton",
                      background=[("active", self.primary_color), ("disabled", "#9ca3af")])
        self.style.configure("TCombobox", font=self.entry_font, fieldbackground="white")
        self.style.configure("TEntry", font=self.entry_font, fieldbackground="white", bordercolor=self.border_color)

    def setup_ui(self):
        """Initialize and configure all UI components"""
        self.root.title("Crypto Trading Bot Pro")
        self.root.geometry("480x580")
        self.root.resizable(False, False)
        
        # Main container
        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.header = ttk.Label(
            self.main_frame,
            text="CRYPTO TRADING BOT",
            font=self.title_font,
            anchor="center"
        )
        self.header.pack(pady=(0, 20))
        
        # Form container
        self.form_frame = ttk.Frame(self.main_frame)
        self.form_frame.pack(fill=tk.X, pady=5)
        
        # Symbol field
        self.symbol_label = ttk.Label(self.form_frame, text="Trading Pair (e.g. BTCUSDT):")
        self.symbol_label.pack(anchor="w", pady=(5, 0))
        self.symbol_entry = ttk.Entry(self.form_frame)
        self.symbol_entry.pack(fill=tk.X, pady=2, ipady=5)
        
        # Side selection
        self.side_label = ttk.Label(self.form_frame, text="Trade Side:")
        self.side_label.pack(anchor="w", pady=(10, 0))
        self.side_combo = ttk.Combobox(self.form_frame, values=["BUY", "SELL"], state="readonly")
        self.side_combo.current(0)
        self.side_combo.pack(fill=tk.X, pady=2, ipady=5)
        
        # Order type
        self.order_type_label = ttk.Label(self.form_frame, text="Order Type:")
        self.order_type_label.pack(anchor="w", pady=(10, 0))
        self.order_type_combo = ttk.Combobox(self.form_frame, values=["MARKET", "LIMIT"], state="readonly")
        self.order_type_combo.current(0)
        self.order_type_combo.pack(fill=tk.X, pady=2, ipady=5)
        
        # Price field (initially hidden)
        self.price_frame = ttk.Frame(self.form_frame)
        self.price_label = ttk.Label(self.price_frame, text="Limit Price:")
        self.price_label.pack(anchor="w", pady=(0, 0))
        self.price_entry = ttk.Entry(self.price_frame)
        self.price_entry.pack(fill=tk.X, pady=2, ipady=5)
        
        # Quantity field
        self.quantity_label = ttk.Label(self.form_frame, text="Quantity:")
        self.quantity_label.pack(anchor="w", pady=(10, 0))
        self.quantity_entry = ttk.Entry(self.form_frame)
        self.quantity_entry.pack(fill=tk.X, pady=2, ipady=5)
        
        # Result display
        self.result_frame = ttk.Frame(self.main_frame)
        self.result_frame.pack(fill=tk.X, pady=(15, 5))
        self.result_label = ttk.Label(
            self.result_frame,
            text="",
            wraplength=400,
            anchor="center",
            justify="center"
        )
        self.result_label.pack(fill=tk.X)
        
        # Action buttons
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.submit_btn = ttk.Button(
            self.button_frame,
            text="PLACE ORDER",
            style="Accent.TButton",
            command=self.place_order
        )
        self.submit_btn.pack(fill=tk.X, ipady=8)
        
        # Status bar
        self.status_bar = ttk.Label(
            self.main_frame,
            text="Ready",
            relief=tk.SUNKEN,
            anchor=tk.W,
            font=("Segoe UI", 8)
        )
        self.status_bar.pack(fill=tk.X, pady=(15, 0), ipady=3)

    def setup_bindings(self):
        """Set up event bindings"""
        self.order_type_combo.bind("<<ComboboxSelected>>", self.toggle_price_field)
        self.root.bind("<Return>", lambda e: self.place_order())
        
        # Set focus to symbol field on startup
        self.symbol_entry.focus_set()

    def toggle_price_field(self, event=None):
        """Toggle visibility of price field based on order type"""
        if self.order_type_combo.get() == "LIMIT":
            self.price_frame.pack(fill=tk.X, pady=(5, 0))
        else:
            self.price_frame.pack_forget()

    def validate_inputs(self):
        """Validate all form inputs"""
        symbol = self.symbol_entry.get().strip().upper()
        side = self.side_combo.get()
        order_type = self.order_type_combo.get()
        quantity = self.quantity_entry.get().strip()
        price = self.price_entry.get().strip() if order_type == "LIMIT" else None
        
        if not symbol:
            self.show_error("Please enter a trading pair (e.g. BTCUSDT)")
            return False
        
        try:
            quantity = float(quantity)
            if quantity <= 0:
                self.show_error("Quantity must be a positive number")
                return False
        except ValueError:
            self.show_error("Invalid quantity - must be a number")
            return False
        
        if order_type == "LIMIT":
            if not price:
                self.show_error("Please enter a price for LIMIT orders")
                return False
            try:
                price = float(price)
                if price <= 0:
                    self.show_error("Price must be a positive number")
                    return False
            except ValueError:
                self.show_error("Invalid price - must be a number")
                return False
        
        return True

    def place_order(self, event=None):
        """Handle order placement"""
        if not self.validate_inputs():
            return
            
        symbol = self.symbol_entry.get().strip().upper()
        side = self.side_combo.get().lower()
        order_type = self.order_type_combo.get()
        quantity = float(self.quantity_entry.get().strip())
        price = float(self.price_entry.get().strip()) if order_type == "LIMIT" else None
        
        self.set_status(f"Placing {order_type} {side} order for {symbol}...")
        self.submit_btn.config(state=tk.DISABLED)
        
        try:
            order = self.bot.place_order(symbol, side, order_type, quantity, price)
            
            if "error" in order:
                self.show_error(f"Order failed: {order['error']}")
            else:
                self.show_success(f"Order placed successfully!\nOrder ID: {order.get('orderId', 'N/A')}")
        except Exception as e:
            self.show_error(f"Error placing order: {str(e)}")
        finally:
            self.submit_btn.config(state=tk.NORMAL)

    def set_status(self, message):
        """Update status bar"""
        self.status_bar.config(text=message)

    def show_error(self, message):
        """Display error message"""
        self.result_label.config(text=message, foreground=self.error_color)
        self.set_status("Error: " + message)

    def show_success(self, message):
        """Display success message"""
        self.result_label.config(text=message, foreground=self.success_color)
        self.set_status("Order placed successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = TradingBotGUI(root)
    root.mainloop()