
from PySide2 import QtWidgets


class LaunchMenu(QtWidgets.QMenu):
    """A custom context menu to sort launchable apps and commands"""
    def __init__(self, pipeline=None, parent=None):
        super(LaunchMenu, self).__init__(parent=parent)

        self.pipeline = pipeline

        self.addSeparator()
        self.launch_actions = [] # TODO initialize actions

        # TODO pipeline?
        # TODO read in categories
        # TODO build the category list
        # TODO add commands/launcher in the appropriate spots
        # TODO permanent actions (prefs, about, close)

        self.addSeparator()

        self.preferences_action = QtWidgets.QAction("&Preferences...")
        self.addAction(self.preferences_action)

        self.about_action = QtWidgets.QAction("&About Be Launcer...")
        self.addAction(self.about_action)

        self.addSeparator()

        self.close_action = QtWidgets.QAction("&Quit")
        self.addAction(self.close_action)

    def _refresh_menu(self):
        """Add the action to the menu"""


class PreferenceMenu():
    """App preferences"""


class AboutMenu():
    """About menu"""
