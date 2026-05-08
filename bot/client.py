import hmac
import hashlib
import time
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
import os
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger("client")

BASE_URL = "https://testnet.binancefuture.com"

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.secret_key = os.getenv("BINANCE_SECRET_KEY")

        if not self.api_key or not self.secret_key:
            raise ValueError("API key or Secret key not found in .env file")

        self.session = requests.Session()
        self.session.headers.update({
            "X-MBX-APIKEY": self.api_key
        })
        logger.info("Binance client initialized successfully")

    def _sign(self, params: dict) -> dict:
        query_string = urlencode(params)
        signature = hmac.new(
            self.secret_key.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()
        params["signature"] = signature
        return params

    def _get_timestamp(self) -> int:
        return int(time.time() * 1000)

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None) -> dict:
        endpoint = "/fapi/v1/order"
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "timestamp": self._get_timestamp()
        }

        if order_type == "LIMIT":
            if price is None:
                raise ValueError("Price is required for LIMIT orders")
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.debug(f"Order params before signing: {params}")
        signed_params = self._sign(params)

        try:
            response = self.session.post(
                BASE_URL + endpoint,
                params=signed_params
            )
            data = response.json()
            if response.status_code == 200:
                logger.info(f"Order placed successfully: {data}")
            else:
                logger.error(f"Order failed: {data}")
            return data

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error: {e}")
            raise