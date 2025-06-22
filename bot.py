# bot.py

import logging
from binance.client import Client
from binance.enums import *
from binance.enums import TIME_IN_FORCE_GTC, ORDER_TYPE_LIMIT

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.API_URL = 'https://testnet.binancefuture.com/fapi'
        logging.basicConfig(filename='logs/bot.log', level=logging.INFO)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol.upper(),
                'side': 'BUY' if side.lower() == 'buy' else 'SELL',
                'type': order_type.upper(),
                'quantity': quantity
            }

            if order_type.upper() == ORDER_TYPE_LIMIT:
                params['price'] = price
                params['timeInForce'] = TIME_IN_FORCE_GTC

            order = self.client.futures_create_order(**params)
            logging.info(f"ORDER SUCCESS: {order}")
            return order
        except Exception as e:
            logging.error(f"ERROR: {str(e)}")
            return {"error": str(e)}
