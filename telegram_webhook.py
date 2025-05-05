# telegram_webhook.py
from flask import Flask, request
from whisperlink_router import handle_whisperlink_command
import requests

app = Flask(__name__)

BOT_TOKEN = "7273879329:AAGFmPBxVYZoa2Whs-P8tlXyaIgOIiAUl0k"
CHAT_ID = "-1002634780470"

def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

@app.route("/", methods=["GET"])
def home():
    return "WhisperLink is active"

@app.route("/webhook", methods=["POST"])
def telegram_webhook():
    data = request.json
    print("Received webhook POST:", data) 
    message = data["message"]["text"]
    chat_id = data["message"]["chat"]["id"]
    response = handle_whisperlink_command(message)
    send_telegram_message(chat_id, response)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)