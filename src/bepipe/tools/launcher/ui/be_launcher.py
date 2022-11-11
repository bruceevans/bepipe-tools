"""Main launcher application"""

from enum import Enum

from ui.tray_icon import BeTrayIcon
from ui.menus import LaunchMenu
from api.api import SeverityLevel

from PySide2 import QtCore


# scrape the bin folder for be_$KEY_CMDS?


# could potentially make a fancier dialog
class BeLauncher(QtCore.QObject):
    """Main UI for BeLauncher"""
    def __init__(self, parent=None):
        super(BeLauncher, self).__init__(parent=parent)

        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        """Initialize the UI"""
        self.launch_menu = LaunchMenu()

        self.tray_icon = BeTrayIcon()
        self.tray_icon.setContextMenu(self.launch_menu)
        self.tray_icon.setVisible(True)

    def _connect_signals(self):
        """Connect signals and slots"""
        self.launch_menu.close_action.triggered.connect(self._exit_launcher)

    def _update_launch_menu(self):
        """Update the """

    @staticmethod
    def _exit_launcher():
        """Close the application"""
        QtCore.QCoreApplication.exit()
