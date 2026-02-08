import time
from hotkey.windows_hotkey import start_hotkey
from core.dispatcher import command_queue
from voice_runner import run_voice

if __name__ == "__main__":
    start_hotkey()
    print("VoiceOS running. Press Ctrl+Space to speak.")

    while True:
        try:
            cmd = command_queue.get(timeout=0.1)
            if cmd == "RUN_VOICE":
                run_voice()  # MAIN THREAD
        except Exception:
            pass
