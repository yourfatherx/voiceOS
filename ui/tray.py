import sys
import os
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import QThread

from voice_runner import run_voice

# --- KEEP GLOBAL REFERENCES (CRITICAL) ---
app = None
tray = None
voice_thread = None


class VoiceThread(QThread):
    def run(self):
        run_voice()


def start_tray():
    global app, tray, voice_thread

    app = QApplication(sys.argv)

    # --- ICON (MUST EXIST) ---
    icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
    if not os.path.exists(icon_path):
        # fallback: use empty icon to avoid crash
        tray_icon = QIcon()
    else:
        tray_icon = QIcon(icon_path)

    tray = QSystemTrayIcon(tray_icon)
    tray.setToolTip("VoiceOS")

    menu = QMenu()

    def start_listening():
        global voice_thread
        if voice_thread is None or not voice_thread.isRunning():
            voice_thread = VoiceThread()
            voice_thread.start()

    listen_action = QAction("🎤 Listen")
    listen_action.triggered.connect(start_listening)
    menu.addAction(listen_action)

    exit_action = QAction("Exit")
    exit_action.triggered.connect(app.quit)
    menu.addAction(exit_action)

    tray.setContextMenu(menu)
    tray.show()

    # --- THIS LINE KEEPS APP ALIVE ---
    sys.exit(app.exec())
