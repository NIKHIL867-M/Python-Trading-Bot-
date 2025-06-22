# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

A simple and beginner-friendly crypto trading bot built with Python. This project connects to the Binance **Futures Testnet** and allows you to place basic orders like **Market** and **Limit** for Buy or Sell sides.

The bot supports both **command-line interface (CLI)** and a clean **graphical interface (GUI)** built using Tkinter.

---

## 📌 What This Project Does

This bot lets users:

- Place Market or Limit orders on Binance Testnet (USDT-M Futures)
- Choose Buy or Sell side manually
- Run from terminal or use a simple desktop-style app (GUI)
- Log all order activity and errors for debugging
- Learn how real crypto exchange bots interact with APIs

---

## 🛠 How to Use This Project

### 1. Clone this Repo

Clone or download the folder to your local system.

```bash
git clone https://github.com/yourusername/trading-bot.git
cd trading-bot
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, simply run:

```bash
pip install python-binance
```

### 4. Add API Keys

Go to `config.py` and paste your Binance Testnet API credentials:

```python
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"
```

> If you couldn’t get keys from Binance Testnet, you can still test the GUI with mock values.

---

## ▶️ Run CLI Bot

```bash
python main.py
```

You'll be asked for:

- Symbol (e.g., BTCUSDT)
- Order type (Market or Limit)
- Buy or Sell
- Quantity (and price if Limit)

---

## 🖥 Run the GUI

```bash
python gui.py
```

A simple app will open where you can:

- Choose order type and direction
- Fill symbol, quantity, price (if needed)
- Click “Place Order” and see result message

---

## 🧾 Logging

All order activity and errors are automatically stored in `logs/bot.log`

---

## 🧠 Why I Built This

This project was built as part of a hiring challenge for a Junior Python Developer role in the crypto trading space. I wanted to:

- Learn how APIs work with Binance
- Practice safe and modular coding in Python
- Build both a CLI and GUI interface from scratch
- Show real-world application of Python in Web3 trading
