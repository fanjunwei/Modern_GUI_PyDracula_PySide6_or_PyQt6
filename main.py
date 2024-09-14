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

import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtWidgets import QMainWindow
from qt_material import apply_stylesheet

from modules.app_functions import AppFunctions
from modules.app_settings import Settings
from modules.ui_functions import UIFunctions
from modules.ui_main import Ui_MainWindow
from modules import CutMain

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(UIFunctions, AppFunctions, QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cutMain = CutMain()
        self.ui.stackedWidget.addWidget(self.cutMain)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        # 判断操作系统，如果为 mac 系统
        if os.name == "posix":
            Settings.ENABLE_CUSTOM_TITLE_BAR = False
        else:
            Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "SQ Cut"
        wname = "工程名称"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.workspaceName.setText(wname)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: self.toggleMenu(True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            self.toggleLeftBox(True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            self.toggleRightBox(True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes/py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            self.theme(themeFile, True)

            # SET HACKS
            self.setThemeHack()
        else:
            pass
            self.theme("themes/base.qss", True)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setChecked(True)

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            self.resetOtherMenuStyle(btnName)
            btn.setChecked(True)

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            # widgets.stackedWidget.setCurrentWidget(widgets.widgets)

            widgets.stackedWidget.setCurrentWidget(self.cutMain)

            self.resetOtherMenuStyle(btnName)
            btn.setChecked(True)

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page)  # SET PAGE
            self.resetOtherMenuStyle(btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setChecked(True)

        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print("Mouse click: LEFT CLICK")
        if event.buttons() == Qt.RightButton:
            print("Mouse click: RIGHT CLICK")


class TestWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.resize(300, 200)
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("This is a test"))
        self.button = QPushButton("Open")
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    extra = {
        # Button colors
        "danger": "#dc3545",
        "warning": "#ffc107",
        "success": "#17a2b8",
        # Font
        "font_size": "10px",
        "line_height": "10px",
        # Density Scale
        "density_scale": "0",
        # environ
        "pyside6": True,
        "linux": True,
    }
    apply_stylesheet(
        app,
        theme="dark_purple.xml",
        css_file="themes/custom.qss.j2",
        extra=extra,
    )
    # apply_stylesheet(app, theme="dark_purple.xml")

    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    # test = TestWidget()
    # test.show()
    # test = CutMain()
    # test.show()
    sys.exit(app.exec())
