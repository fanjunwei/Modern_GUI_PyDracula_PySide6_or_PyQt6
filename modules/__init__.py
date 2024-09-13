# ///////////////////////////////////////////////////////////////
#
# BY: fjw
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# GUI FILE
from .ui_main import Ui_MainWindow

# APP SETTINGS
from .app_settings import Settings

# IMPORT FUNCTIONS
from .ui_functions import *

# APP FUNCTIONS
from .app_functions import *

from .ui_cut_main import Ui_Form as _cut_main_from


class CutMain(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = _cut_main_from()
        self.ui.setupUi(self)
