import argparse
from colorama import Fore, Style, init
from bot.logging_config import setup_logger
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_inputs

init(autoreset=True)
logger = setup_logger("cli")

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol",     type=str,   required=True,  help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side",       type=str,   required=True,  help="BUY or SELL")
    parser.add_argument("--order-type", type=str,   required=True,  help="MARKET or LIMIT")
    parser.add_argument("--quantity",   type=float, required=True,  help="Order quantity e.g. 0.01")
    parser.add_argument("--price",      type=float, required=False, help="Price for LIMIT orders")

    args = parser.parse_args()

    symbol     = args.symbol.upper()
    side       = args.side.upper()
    order_type = args.order_type.upper()
    quantity   = args.quantity
    price      = args.price

    try:
        validate_inputs(symbol, side, order_type, quantity, price)

        # Confirmation prompt
        print(f"\n{Fore.CYAN}--- Order Confirmation ---")
        print(f"  Symbol     : {symbol}")
        print(f"  Side       : {side}")
        print(f"  Order Type : {order_type}")
        print(f"  Quantity   : {quantity}")
        if price:
            print(f"  Price      : {price}")
        confirm = input(f"\n{Fore.YELLOW}Confirm order? (y/n): {Style.RESET_ALL}").strip().lower()

        if confirm != "y":
            print(f"{Fore.RED}Order cancelled by user.")
            logger.info("Order cancelled by user at confirmation prompt")
            return

        client = BinanceClient()
        place_order(client, symbol, side, order_type, quantity, price)

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        print(f"\n{Fore.RED}❌ Invalid input: {e}")

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"\n{Fore.RED}❌ Something went wrong: {e}")

if __name__ == "__main__":
    main()