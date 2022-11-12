
import sys

from Qt import QtWidgets
from .ui import be_launcher

_LAUNCHER = None

def run(windowed=True):
    # Launch the launcher

    global _LAUNCHER

    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    _LAUNCHER = BeLauncher()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
