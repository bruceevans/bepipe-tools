"""System tray icon widget for BeLauncher"""


from PySide2 import QtWidgets, QtGui, QtCore


__all__ = [
    "BeTrayIcon"
]


_ICON = "/Users/bevans/Documents/_dev/git/bepipe-launcher/resources/icons/be_launcher_icon.png"


class BeTrayIcon(QtWidgets.QSystemTrayIcon):
    """Wrapper for the standard system tray icon

    Args:
        parent (optional): Parent widget

    """

    notify = QtCore.Signal(object, str)

    def __init__(self, parent=None):
        super(BeTrayIcon, self).__init__(parent=parent)

        self._icon = QtGui.QIcon(_ICON)
        self.setIcon(self._icon)
        self.context_menu = ""
        self.notify.connect(self.send_notification)

    def _setup_ui(self):
        """Initialize the UI"""
        # TODO add a reference to the context menu

    def send_notification(self, level, msg):
        """Show a banner message

        Args:
            level (api.LEVEL) : Notification level
            msg (str) : Message

        """

        # TODO currently you're just wrapping the same stuff,
        # use the base showMessage unless you add extra funcionality
        self.showMessage(
            "BePipe - {}".format(level.value),
            msg,
            # TODO derive icon from level
            self._icon)
