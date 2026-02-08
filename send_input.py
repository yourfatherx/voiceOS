import time
import ctypes

user32 = ctypes.windll.user32

INPUT_KEYBOARD = 1
KEYEVENTF_UNICODE = 0x0004
KEYEVENTF_KEYUP = 0x0002

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

def send_char(ch):
    extra = ctypes.c_ulong(0)

    down = KEYBDINPUT(0, ord(ch), KEYEVENTF_UNICODE, 0, ctypes.pointer(extra))
    up = KEYBDINPUT(0, ord(ch), KEYEVENTF_UNICODE | KEYEVENTF_KEYUP, 0, ctypes.pointer(extra))

    inputs = (INPUT * 2)(
        INPUT(INPUT_KEYBOARD, down),
        INPUT(INPUT_KEYBOARD, up)
    )

    user32.SendInput(2, ctypes.byref(inputs), ctypes.sizeof(INPUT))

print("Click inside Notepad NOW. Typing in 3 seconds...")
time.sleep(3)

for c in "HELLO_FROM_SENDINPUT":
    send_char(c)
