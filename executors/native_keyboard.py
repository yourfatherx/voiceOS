import ctypes
import time

user32 = ctypes.windll.user32

INPUT_KEYBOARD = 1
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004

class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong)),
    ]

class INPUT(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ulong),
        ("ki", KEYBDINPUT),
    ]

def _send_unicode_char(char):
    extra = ctypes.c_ulong(0)

    # Key down
    ki_down = KEYBDINPUT(
        wVk=0,
        wScan=ord(char),
        dwFlags=KEYEVENTF_UNICODE,
        time=0,
        dwExtraInfo=ctypes.pointer(extra)
    )

    # Key up
    ki_up = KEYBDINPUT(
        wVk=0,
        wScan=ord(char),
        dwFlags=KEYEVENTF_UNICODE | KEYEVENTF_KEYUP,
        time=0,
        dwExtraInfo=ctypes.pointer(extra)
    )

    inputs = (INPUT * 2)(
        INPUT(INPUT_KEYBOARD, ki_down),
        INPUT(INPUT_KEYBOARD, ki_up),
    )

    user32.SendInput(2, ctypes.byref(inputs), ctypes.sizeof(INPUT))

def type_text(text: str):
    time.sleep(0.3)  # allow focus to settle
    for ch in text:
        _send_unicode_char(ch)

def press_key(key: str):
    VK = {
        "enter": 0x0D,
        "backspace": 0x08,
        "tab": 0x09,
        "space": 0x20,
    }

    vk = VK.get(key.lower())
    if not vk:
        return

    extra = ctypes.c_ulong(0)

    ki_down = KEYBDINPUT(vk, 0, 0, 0, ctypes.pointer(extra))
    ki_up = KEYBDINPUT(vk, 0, KEYEVENTF_KEYUP, 0, ctypes.pointer(extra))

    inputs = (INPUT * 2)(
        INPUT(INPUT_KEYBOARD, ki_down),
        INPUT(INPUT_KEYBOARD, ki_up),
    )

    user32.SendInput(2, ctypes.byref(inputs), ctypes.sizeof(INPUT))
