# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import res_rc

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 496)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 20, 251, 450))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 250, 450))
        self.label.setCursor(QCursor(Qt.SizeAllCursor))
        self.label.setStyleSheet(u"QLabel{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 201, 255, 255), stop:1 rgba(200, 251, 255, 255));\n"
"border-top-left-radius:50px;\n"
"}\n"
"\n"
"")
        self.Logo = QPushButton(self.frame)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(0, 120, 251, 191))
        self.Logo.setStyleSheet(u"QPushButton{\n"
"background-color: none;\n"
"border:0px solid;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icon/icon/2821656.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Logo.setIcon(icon)
        self.Logo.setIconSize(QSize(160, 160))
        self.opn_login = QPushButton(self.frame)
        self.opn_login.setObjectName(u"opn_login")
        self.opn_login.setGeometry(QRect(80, 370, 91, 31))
        self.opn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.opn_login.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border:none;\n"
"border-bottom:2px solid #00aaff;")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/right-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.opn_login.setIcon(icon1)
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(300, 20, 250, 450))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(0, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius:50px;")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 250, 450))
        self.frame_2.setMinimumSize(QSize(250, 0))
        self.frame_2.setStyleSheet(u"border-bottom-right-radius:50px;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 50, 251, 31))
        self.label_2.setStyleSheet(u"font: 75 14pt \"Ebrima\";")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.Host = QLineEdit(self.frame_2)
        self.Host.setObjectName(u"Host")
        self.Host.setGeometry(QRect(30, 130, 191, 31))
        self.Host.setStyleSheet(u"border:none;\n"
"border-bottom: 2px solid #2fd5ff;\n"
"padding-bottom:1px;")
        self.Port = QLineEdit(self.frame_2)
        self.Port.setObjectName(u"Port")
        self.Port.setGeometry(QRect(30, 180, 71, 31))
        self.Port.setStyleSheet(u"border:none;\n"
"border-bottom: 2px solid #2fd5ff;\n"
"padding-bottom:1px;")
        self.Username = QLineEdit(self.frame_2)
        self.Username.setObjectName(u"Username")
        self.Username.setGeometry(QRect(30, 250, 191, 31))
        self.Username.setStyleSheet(u"border:none;\n"
"border-bottom: 2px solid #2fd5ff;\n"
"padding-bottom:1px;")
        self.Password = QLineEdit(self.frame_2)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(30, 300, 191, 31))
        self.Password.setStyleSheet(u"border:none;\n"
"border-bottom: 2px solid #2fd5ff;\n"
"padding-bottom:1px;")
        self.Password.setEchoMode(QLineEdit.Password)
        self.login = QPushButton(self.frame_2)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(80, 360, 91, 31))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setCursor(QCursor(Qt.PointingHandCursor))
        self.login.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 201, 255, 255), stop:1 rgba(200, 251, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(0, 170, 255);\n"
"\n"
"")
        self.close_1 = QPushButton(self.frame_2)
        self.close_1.setObjectName(u"close_1")
        self.close_1.setGeometry(QRect(210, 0, 41, 21))
        self.close_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_1.setStyleSheet(u"background-color: rgb(243, 28, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/closeAsset 43.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_1.setIcon(icon2)
        self.close_1.setIconSize(QSize(13, 13))
        self.min = QPushButton(self.frame_2)
        self.min.setObjectName(u"min")
        self.min.setGeometry(QRect(170, 0, 41, 21))
        self.min.setCursor(QCursor(Qt.PointingHandCursor))
        self.min.setStyleSheet(u"background-color: rgb(18, 205, 255);\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/hideAsset 53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.min.setIcon(icon3)
        self.min.setIconSize(QSize(13, 13))

        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.Logo.setText("")
        self.opn_login.setText(QCoreApplication.translate("MainWindow", u"Open Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.Host.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.Port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.Username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.Password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.close_1.setText("")
        self.min.setText("")
    # retranslateUi

