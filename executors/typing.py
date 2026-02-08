import pyautogui
import time

pyautogui.FAILSAFE = False

def type_text(text: str):
    time.sleep(0.2)  # small delay to ensure focus
    pyautogui.write(text, interval=0.02)

def press_key(key: str):
    pyautogui.press(key)
