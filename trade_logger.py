# trade_logger.py

import os
from datetime import datetime

TRADE_LOG_PATH = "memory/trade_log.txt"
CAPITAL_PATH = "memory/capital.txt"

def log_trade(action, price, capital):
    position_size = 100.0  # Simulated static size for now
    new_capital = capital

    if action == "buy":
        new_capital -= position_size
    elif action == "sell":
        new_capital += position_size

    # Write to capital
    with open(CAPITAL_PATH, "w") as f:
        f.write(str(new_capital))

    # Append to trade log
    with open(TRADE_LOG_PATH, "a") as f:
        f.write(f"{datetime.now()} | Action: {action.upper()} | Price: ${price:.2f} | Capital: ${new_capital:.2f}\n")

    return new_capital