# whisperlink_router.py
from ladder_manager import handle_ladder_command
#from sentience_control import handle_xscore_command
from commander import handle_force_command, handle_halt_command, get_status_report

def handle_whisperlink_command(command_text):
    if command_text.startswith("/ladder"):
        return handle_ladder_command(command_text)
    elif command_text.startswith("/force"):
        return handle_force_command(command_text)
    elif command_text.startswith("/halt"):
        return handle_halt_command()
    elif command_text.startswith("/status"):
        return get_status_report()
    else:
        return "Unknown command."