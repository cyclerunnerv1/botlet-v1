# trigger_logger.py
from datetime import datetime

def log_trigger(event_name, details=None):
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"[{timestamp}] EVENT: {event_name}"
    if details:
        entry += f" | DETAILS: {details}"
    with open("memory/trigger_log.txt", "a") as file:
        file.write(entry + "\n")
