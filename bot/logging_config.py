import logging
import os

def setup_logger(name: str) -> logging.Logger:
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Avoid adding duplicate handlers if logger already exists
    if logger.handlers:
        return logger

    # File handler — writes everything to a log file
    file_handler = logging.FileHandler("logs/trading_bot.log")
    file_handler.setLevel(logging.DEBUG)

    # Console handler — prints INFO and above to terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Format — timestamp | level | message
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger