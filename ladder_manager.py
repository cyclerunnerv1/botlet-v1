# ladder_manager.py
import json
import os

def handle_ladder_command(cmd):
    parts = cmd.strip().split()
    if len(parts) != 6:
        return "Invalid ladder format. Use: /ladder [short|long] price1 price2 price3 price4"

    _, side, *levels = parts
    if side not in ["short", "long"]:
        return "Invalid side. Must be 'short' or 'long'."

    file_path = f"shadowfill_memory/{side}_ladder.json"
    try:
        with open(file_path, "w") as f:
            json.dump({"levels": levels}, f)
        return f"{side.title()} ladder updated to: {', '.join(levels)}"
    except:
        return "Failed to update ladder."