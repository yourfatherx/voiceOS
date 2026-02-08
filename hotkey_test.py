import keyboard
print("Waiting for Ctrl+Space...")

keyboard.add_hotkey("ctrl+space", lambda: print("HOTKEY FIRED"))
keyboard.wait()
