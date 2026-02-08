from win10toast import ToastNotifier

_toaster = ToastNotifier()

def notify(title, message):
    _toaster.show_toast(
        title,
        message,
        threaded=True,
        duration=3
    )
