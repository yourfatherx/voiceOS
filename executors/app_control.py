import subprocess

# SAFE ALLOWLIST
APP_MAP = {
    "notepad": {
        "open": ["notepad.exe"],
        "process": "notepad.exe",
    },
    "chrome": {
        "open": ["chrome"],
        "process": "chrome.exe",
    },
    "calculator": {
        "open": ["calc.exe"],
        "process": "Calculator.exe",
    },
}

def open_app(app: str):
    print("🧪 open_app received:", repr(app), type(app))
    app = app.lower()
    if app not in APP_MAP:
        print(f"❌ App not allowed: {app}")
        return

    try:
        subprocess.Popen(APP_MAP[app]["open"])
        print(f"🚀 Opened {app}")
    except Exception as e:
        print(f"❌ Failed to open {app}: {e}")

def close_app(app: str):
    app = app.lower()
    if app not in APP_MAP:
        print(f"❌ App not allowed: {app}")
        return

    proc = APP_MAP[app]["process"]

    try:
        subprocess.run(
            ["taskkill", "/f", "/im", proc],
            capture_output=True,
            text=True
        )
        print(f"🛑 Closed {app}")
    except Exception as e:
        print(f"❌ Failed to close {app}: {e}")
