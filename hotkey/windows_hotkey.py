import ctypes
import threading
from ctypes import wintypes

from core.dispatcher import request_voice_run

user32 = ctypes.windll.user32

MOD_CONTROL = 0x0002
VK_SPACE = 0x20
HOTKEY_ID = 1

def hotkey_loop():
    if not user32.RegisterHotKey(None, HOTKEY_ID, MOD_CONTROL, VK_SPACE):
        raise RuntimeError("Failed to register hotkey")

    print("✅ Global hotkey Ctrl+Space registered")

    msg = wintypes.MSG()
    while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
        if msg.message == 0x0312:  # WM_HOTKEY
            request_voice_run()

def start_hotkey():
    threading.Thread(target=hotkey_loop, daemon=True).start()
