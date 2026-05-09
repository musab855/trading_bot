from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger("orders")

def place_order(client: BinanceClient, symbol: str, side: str, order_type: str, quantity: float, price: float = None) -> None:
    
    print("\n--- Order Request Summary ---")
    print(f"  Symbol     : {symbol}")
    print(f"  Side       : {side}")
    print(f"  Order Type : {order_type}")
    print(f"  Quantity   : {quantity}")
    if price:
        print(f"  Price      : {price}")
    print("-----------------------------\n")

    logger.info(f"Attempting {order_type} {side} order | Symbol: {symbol} | Qty: {quantity} | Price: {price}")

    response = client.place_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price
    )

    if "orderId" in response:
        print("✅ Order placed successfully!")
        print(f"  Order ID     : {response.get('orderId')}")
        print(f"  Status       : {response.get('status')}")
        print(f"  Executed Qty : {response.get('executedQty')}")
        
        avg_price = response.get('avgPrice', '0.00')
        print(f"  Avg Price    : {avg_price if avg_price != '0.00' else 'N/A (order not yet filled)'}")

        logger.info(f"Order success | OrderID: {response.get('orderId')} | Status: {response.get('status')}")
    else:
        print("❌ Order failed!")
        print(f"  Error Code    : {response.get('code')}")
        print(f"  Error Message : {response.get('msg')}")
        logger.error(f"Order failed | Code: {response.get('code')} | Message: {response.get('msg')}")