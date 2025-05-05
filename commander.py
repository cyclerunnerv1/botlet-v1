# commander.py
import datetime

def handle_force_command(cmd):
    try:
        _, direction = cmd.strip().split()
        if direction not in ["long", "short"]:
            return "Use /force long or /force short."
        with open("trigger_log.txt", "a") as f:
            f.write(f"[FORCED TRADE] {direction.upper()} at {datetime.datetime.now()}\n")
        return f"Force {direction} signal logged."
    except:
        return "Invalid format. Use: /force long or /force short"

def handle_halt_command():
    try:
        with open("halt.flag", "w") as f:
            f.write("HALT TRADES")
        return "All trading halted. 'halt.flag' created."
    except:
        return "Failed to create halt flag."

def get_status_report():
    try:
        with open("trade_log.txt", "r") as f:
            lines = f.readlines()[-3:]  # last 3 entries
        return "Last 3 trades:\n" + "".join(lines)
    except:
        return "No trade logs found."