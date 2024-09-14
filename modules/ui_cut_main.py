# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cut_main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1680, 919)
        Form.setStyleSheet(u"font-size: 13pt")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainTop = QHBoxLayout()
        self.MainTop.setSpacing(1)
        self.MainTop.setObjectName(u"MainTop")
        self.top_left = QVBoxLayout()
        self.top_left.setObjectName(u"top_left")
        self.top_left.setContentsMargins(-1, 0, -1, -1)
        self.horizontalFrame = QFrame(Form)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 30))
        self.horizontalFrame.setMaximumSize(QSize(16777215, 30))
        self.horizontalFrame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 6px;")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalFrame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 10pt;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.horizontalFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font-size: 10pt;\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.top_left.addWidget(self.horizontalFrame)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setMaximumSize(QSize(150, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.label_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addWidget(self.frame)

        self.stackedWidget_2 = QStackedWidget(Form)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMaximumSize(QSize(600, 16777215))
        self.stackedWidget_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.stackedWidget_2.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget_2Page1 = QWidget()
        self.stackedWidget_2Page1.setObjectName(u"stackedWidget_2Page1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.stackedWidget_2Page1.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2Page1.setSizePolicy(sizePolicy)
        self.stackedWidget_2.addWidget(self.stackedWidget_2Page1)

        self.horizontalLayout_4.addWidget(self.stackedWidget_2)


        self.top_left.addLayout(self.horizontalLayout_4)

        self.top_left.setStretch(0, 1)
        self.top_left.setStretch(1, 1)

        self.MainTop.addLayout(self.top_left)

        self.top_middle = QFrame(Form)
        self.top_middle.setObjectName(u"top_middle")
        self.verticalLayout_4 = QVBoxLayout(self.top_middle)
#ifndef Q_OS_MAC
        self.verticalLayout_4.setSpacing(-1)
#endif
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.top_middle)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 30))
        self.frame_7.setMaximumSize(QSize(16777215, 30))
        self.frame_7.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 6px;")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size: 10pt;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.stackedWidget_6 = QStackedWidget(self.top_middle)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.stackedWidget_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.stackedWidget_6.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget_6Page1 = QWidget()
        self.stackedWidget_6Page1.setObjectName(u"stackedWidget_6Page1")
        self.verticalLayout_7 = QVBoxLayout(self.stackedWidget_6Page1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 20, 0, 0)
        self.label_5 = QLabel(self.stackedWidget_6Page1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setStyleSheet(u"background-color: rgb(0, 0, 0)")

        self.verticalLayout_7.addWidget(self.label_5)

        self.frame_10 = QFrame(self.stackedWidget_6Page1)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 50))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.play_to_start = QPushButton(self.frame_10)
        self.play_to_start.setObjectName(u"play_to_start")

        self.horizontalLayout_7.addWidget(self.play_to_start)

        self.play = QPushButton(self.frame_10)
        self.play.setObjectName(u"play")

        self.horizontalLayout_7.addWidget(self.play)

        self.play_to_end = QPushButton(self.frame_10)
        self.play_to_end.setObjectName(u"play_to_end")

        self.horizontalLayout_7.addWidget(self.play_to_end)


        self.verticalLayout_7.addWidget(self.frame_10)

        self.stackedWidget_6.addWidget(self.stackedWidget_6Page1)

        self.verticalLayout_4.addWidget(self.stackedWidget_6)


        self.MainTop.addWidget(self.top_middle)

        self.top_right = QVBoxLayout()
        self.top_right.setObjectName(u"top_right")
        self.frame_9 = QFrame(Form)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 30))
        self.frame_9.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 6px;")

        self.horizontalLayout_8.addWidget(self.label_6)


        self.top_right.addWidget(self.frame_9)

        self.stackedWidget_8 = QStackedWidget(Form)
        self.stackedWidget_8.setObjectName(u"stackedWidget_8")
        self.stackedWidget_8.setMinimumSize(QSize(0, 0))
        self.stackedWidget_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.stackedWidget_8.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget_8Page1 = QWidget()
        self.stackedWidget_8Page1.setObjectName(u"stackedWidget_8Page1")
        self.verticalLayout_8 = QVBoxLayout(self.stackedWidget_8Page1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedWidget_8.addWidget(self.stackedWidget_8Page1)

        self.top_right.addWidget(self.stackedWidget_8)

        self.top_right.setStretch(0, 2)

        self.MainTop.addLayout(self.top_right)


        self.verticalLayout.addLayout(self.MainTop)

        self.MainBottom = QHBoxLayout()
        self.MainBottom.setObjectName(u"MainBottom")
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 250))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(180, 16777215))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(80, 40, 58, 16))

        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(240, 40, 58, 16))

        self.horizontalLayout_5.addWidget(self.frame_5)


        self.MainBottom.addWidget(self.frame_3)


        self.verticalLayout.addLayout(self.MainBottom)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5a92\u4f53", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6587\u672c", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5a92\u4f53\u5e93", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u64ad\u653e\u5668", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"10:00:00", None))
        self.play_to_start.setText(QCoreApplication.translate("Form", u"|<", None))
        self.play.setText(QCoreApplication.translate("Form", u">", None))
        self.play_to_end.setText(QCoreApplication.translate("Form", u">|", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u53c2\u6570", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

