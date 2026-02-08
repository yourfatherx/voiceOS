import keyboard
import threading
from voice_runner import run_voice

_running = False

def _trigger():
    global _running
    if _running:
        return

    _running = True

    def task():
        global _running
        try:
            run_voice()
        finally:
            _running = False

    threading.Thread(target=task, daemon=True).start()

def start_hotkey():
    def hotkey_loop():
        keyboard.add_hotkey("ctrl+space", _trigger)
        keyboard.wait()  # <-- THIS IS CRITICAL

    threading.Thread(target=hotkey_loop, daemon=True).start()
