import argparse
from bot.logging_config import setup_logger
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_inputs

logger = setup_logger("cli")

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol",     type=str,   required=True,  help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side",       type=str,   required=True,  help="BUY or SELL")
    parser.add_argument("--order-type", type=str,   required=True,  help="MARKET or LIMIT")
    parser.add_argument("--quantity",   type=float, required=True,  help="Order quantity e.g. 0.01")
    parser.add_argument("--price",      type=float, required=False, help="Price for LIMIT orders")

    args = parser.parse_args()

    # Convert to uppercase to be safe
    symbol     = args.symbol.upper()
    side       = args.side.upper()
    order_type = args.order_type.upper()
    quantity   = args.quantity
    price      = args.price

    try:
        # Step 1 — Validate inputs
        validate_inputs(symbol, side, order_type, quantity, price)

        # Step 2 — Initialize client
        client = BinanceClient()

        # Step 3 — Place order
        place_order(client, symbol, side, order_type, quantity, price)

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        print(f"\n❌ Invalid input: {e}")

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"\n❌ Something went wrong: {e}")

if __name__ == "__main__":
    main()