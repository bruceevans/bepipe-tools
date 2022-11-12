"""System tray icon widget for BeLauncher"""


from PySide2 import QtWidgets, QtGui, QtCore


__all__ = [
    "ArcadeTrayIcon"
]


class ArcadeTrayIcon(QtWidgets.QSystemTrayIcon):
    """Wrapper for the standard system tray icon

    Args:
        parent (optional): Parent widget

    """

    notify = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(ArcadeTrayIcon, self).__init__(parent=parent)
        # TODO load icon
        self.context_menu = None
        self.show()

    def _setup_ui(self):
        pass

    def push_notification(self, msg):
        """Show a banner message

        Args:
            msg (str): Message to show

        """
        print(msg)
        self.notify.emit(msg)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tray = ArcadeTrayIcon()
    sys.exit(app.exec_())
