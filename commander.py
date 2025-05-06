# commander.py
from telegram_webhook import send_telegram_message
from trigger_logger import log_trigger

def handle_command(command, args):
    if command == "/xscore":
        try:
            score = int(args[0])
            msg = f"X-Score updated to {score}."
            log_trigger("X-Score Update", f"{score}")
            send_telegram_message(msg)
        except:
            send_telegram_message("Invalid X-Score value.")
    elif command == "/ladder":
        direction = args[0].lower()
        if direction in ["short", "long"]:
            log_trigger("Ladder Update", direction)
            send_telegram_message(f"Ladder direction switched to {direction.upper()}.")
        else:
            send_telegram_message("Invalid ladder direction. Use: short or long.")
    elif command == "/forecast":
        status = " ".join(args)
        log_trigger("Forecast Update", status)
        send_telegram_message(f"Forecast updated: {status}")
    else:
        send_telegram_message("Unknown command.")