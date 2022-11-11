##
## 
##
##

import sys
_MODULE_PATH = "/Users/bevans/Documents/_dev/git/bepipe-launcher/src"
sys.path.append(_MODULE_PATH)

# import os
from PySide2 import QtWidgets
from ui.be_launcher import BeLauncher

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
