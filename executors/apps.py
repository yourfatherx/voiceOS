import subprocess

APP_MAP = {
    "chrome": "chrome",
    "notepad": "notepad",
    "calculator": "calc"
}

def open_app(name):
    exe = APP_MAP.get(name.lower())
    if exe:
        subprocess.Popen(exe)
