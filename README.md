# Binance Futures Testnet Trading Bot

A command-line Python application to place Market and Limit orders on Binance Futures Testnet (USDT-M).

---

## Project Structure

trading_bot/
bot/
init.py
client.py          # Binance API client wrapper
orders.py          # Order placement + output logic
validators.py      # Input validation
logging_config.py  # Logging setup
logs/
trading_bot.log    # Auto-generated on first run
cli.py               # CLI entry point
README.md
requirements.txt
.env                 # Not included — see setup steps

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/trading_bot.git
cd trading_bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file in the root folder
BINANCE_API_KEY=your_api_key_here
BINANCE_SECRET_KEY=your_secret_key_here

Get your API credentials from: https://testnet.binancefuture.com

### 4. Run the bot
```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.01
```

---

## How to Run — Examples

### Place a Market Buy order
```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.01
```

### Place a Market Sell order
```bash
python cli.py --symbol BTCUSDT --side SELL --order-type MARKET --quantity 0.01
```

### Place a Limit Buy order
```bash
python cli.py --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.01 --price 50000
```

### Place a Limit Sell order
```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 100000
```

---

## Arguments

| Argument | Required | Description | Example |
|---|---|---|---|
| `--symbol` | ✅ | Trading pair | `BTCUSDT` |
| `--side` | ✅ | BUY or SELL | `BUY` |
| `--order-type` | ✅ | MARKET or LIMIT | `MARKET` |
| `--quantity` | ✅ | Order quantity | `0.01` |
| `--price` | ⬜ | Required for LIMIT only | `60000` |

---

## Sample Output

--- Order Request Summary ---
Symbol     : BTCUSDT
Side       : BUY
Order Type : MARKET
Quantity   : 0.01
✅ Order placed successfully!
Order ID     : 13120631394
Status       : NEW
Executed Qty : 0.0000
Avg Price    : 0.00

---

## Logging

All API requests, responses, and errors are logged to `logs/trading_bot.log` automatically.

Log format:

2026-05-08 17:42:56 | INFO     | client | Order placed successfully: {...}
2026-05-08 17:42:56 | INFO     | orders | Order success | OrderID: 13120631394

---

## Error Handling

The bot handles:
- Invalid input (wrong side, missing price for LIMIT, negative quantity)
- API errors (invalid symbol, Binance rejection)
- Network failures (connection errors, timeouts)

Example of validation error:

❌ Invalid input: Side must be one of ['BUY', 'SELL']

---

## Assumptions

- All symbols must end with USDT (e.g. BTCUSDT, ETHUSDT)
- Quantity must be a positive number
- LIMIT orders require a positive price
- All inputs are automatically converted to uppercase
- Testnet base URL used: https://testnet.binancefuture.com

---

## Requirements

- Python 3.x
- requests
- python-dotenv