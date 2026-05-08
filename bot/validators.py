from bot.logging_config import setup_logger

logger = setup_logger("validators")

VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]

def validate_inputs(symbol: str, side: str, order_type: str, quantity: float, price: float = None) -> None:

    # Validate symbol
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string e.g. BTCUSDT")
    symbol = symbol.upper()
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT e.g. BTCUSDT, ETHUSDT")

    # Validate side
    if side.upper() not in VALID_SIDES:
        raise ValueError(f"Side must be one of {VALID_SIDES}")

    # Validate order type
    if order_type.upper() not in VALID_ORDER_TYPES:
        raise ValueError(f"Order type must be one of {VALID_ORDER_TYPES}")

    # Validate quantity
    if not isinstance(quantity, (int, float)) or quantity <= 0:
        raise ValueError("Quantity must be a positive number")

    # Validate price for LIMIT orders
    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")

    logger.info(f"Input validation passed | Symbol: {symbol} | Side: {side} | Type: {order_type} | Qty: {quantity} | Price: {price}")