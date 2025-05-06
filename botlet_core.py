import json
import os
from datetime import datetime
from trade_logger import log_trade
from flask import Flask, request, jsonify
from commander import handle_command
import threading
import time
import requests

# === File Paths ===
MEMORY_PATH = "memory"
LADDER_PATH = os.path.join(MEMORY_PATH, "ladder.json")
CAPITAL_PATH = os.path.join(MEMORY_PATH, "capital.txt")
STOPLOSS_PATH = os.path.join(MEMORY_PATH, "stoploss.txt")
TRADE_LOG_PATH = os.path.join(MEMORY_PATH, "trade_log.txt")

# path

app = Flask(__name__)

 # === Heart beat ===
def heartbeat():
    while True:
        try:
            requests.get("https://web-production-0c97c.up.railway.app/")
        except Exception as e:
            print("Heartbeat failed:", e)
        time.sleep(300)  # Ping every 5 minutes

# Start the heartbeat in the background
threading.Thread(target=heartbeat, daemon=True).start()


# === Botlet Core Logic ===
def load_capital():
    try:
        with open(CAPITAL_PATH, "r") as f:
            return float(f.read().strip())
    except:
        return 1000.0  # Default starting capital

def load_ladder():
    try:
        with open(LADDER_PATH, "r") as f:
            data = json.load(f)
            return data.get("levels", [])
    except:
        return []

def load_stoploss():
    try:
        with open(STOPLOSS_PATH, "r") as f:
            return float(f.read().strip())
    except:
        return None

def simulate_price():
    return 95000.0  # Replace with real price feed later

def determine_action(price, ladder, stoploss):
    if stoploss and price >= stoploss:
        return "sell"
    for level in ladder:
        if price <= float(level):
            return "buy"
    return "hold"

def main():
    print("=== Botlet Core Running ===")
    ladder = load_ladder()
    stoploss = load_stoploss()
    capital = load_capital()

    for loop in range(10):  # Run 10 simulated loops
        price = simulate_price()
        action = determine_action(price, ladder, stoploss)

        print(f"[{datetime.now()}] Price: ${price} | Action: {action}")

        if action in ["buy", "sell"]:
            capital = log_trade(action, price, capital)

@app.route('/')
def root():
    return 'Botlet is alive'

@app.route('/webhook/trigger', methods=['POST'])
def receive_trigger():
    data = request.json
    try:
        event = data.get("event", "")
        details = data.get("details", {})
        handle_command(f"/{event}", list(details.values()))
        return jsonify({"status": "received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)