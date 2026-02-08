import sys
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction

app = QApplication(sys.argv)

tray = QSystemTrayIcon(QIcon())
tray.setToolTip("Tray Test")

menu = QMenu()

exit_action = QAction("Exit")
exit_action.triggered.connect(app.quit)
menu.addAction(exit_action)

tray.setContextMenu(menu)
tray.show()

print("Tray shown, entering event loop")
sys.exit(app.exec())
