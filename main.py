# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1002, 676)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.551, y1:0, x2:0.897727, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.988636 rgba(219, 246, 255, 255));")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QSize(80, 0))
        self.frame_8.setMaximumSize(QSize(80, 16777215))
        self.frame_8.setStyleSheet(u"QFrame:{\n"
"background-color: white;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: white;\n"
"}")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.148, y1:0.341591, x2:1, y2:1, stop:0.357955 rgba(255, 255, 255, 255), stop:0.988636 rgba(113, 189, 255, 255));\n"
"	border-radius:0px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: white;\n"
"	border-radius:0px;\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icon/309587.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.pushButton_4, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setCursor(QCursor(Qt.SizeAllCursor))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_7)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(50, 50))
        self.frame_4.setMaximumSize(QSize(50, 16777215))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Bn_Min = QPushButton(self.frame_4)
        self.Bn_Min.setObjectName(u"Bn_Min")
        sizePolicy.setHeightForWidth(self.Bn_Min.sizePolicy().hasHeightForWidth())
        self.Bn_Min.setSizePolicy(sizePolicy)
        self.Bn_Min.setCursor(QCursor(Qt.PointingHandCursor))
        self.Bn_Min.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius:0px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 133, 200);\n"
"	border-radius:0px;\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/3825999.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Bn_Min.setIcon(icon1)
        self.Bn_Min.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.Bn_Min, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(50, 50))
        self.frame_5.setMaximumSize(QSize(50, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Bn_Max = QPushButton(self.frame_5)
        self.Bn_Max.setObjectName(u"Bn_Max")
        sizePolicy.setHeightForWidth(self.Bn_Max.sizePolicy().hasHeightForWidth())
        self.Bn_Max.setSizePolicy(sizePolicy)
        self.Bn_Max.setMinimumSize(QSize(0, 0))
        self.Bn_Max.setCursor(QCursor(Qt.SizeBDiagCursor))
        self.Bn_Max.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius:0px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 133, 200);\n"
"	border-radius:0px;\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/1949135.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Bn_Max.setIcon(icon2)
        self.Bn_Max.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.Bn_Max, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(50, 50))
        self.frame_6.setMaximumSize(QSize(50, 16777215))
        self.frame_6.setStyleSheet(u"QFrame:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 53, 53);\n"
"	border-radius:none;\n"
"\n"
"}")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Bn_Close = QPushButton(self.frame_6)
        self.Bn_Close.setObjectName(u"Bn_Close")
        sizePolicy.setHeightForWidth(self.Bn_Close.sizePolicy().hasHeightForWidth())
        self.Bn_Close.setSizePolicy(sizePolicy)
        self.Bn_Close.setMinimumSize(QSize(0, 0))
        self.Bn_Close.setCursor(QCursor(Qt.ClosedHandCursor))
        self.Bn_Close.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius:none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: white;\n"
"	border-radius:none;\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/2919590.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Bn_Close.setIcon(icon3)
        self.Bn_Close.setIconSize(QSize(30, 30))
#if QT_CONFIG(shortcut)
        self.Bn_Close.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.Bn_Close, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.left_menu = QFrame(self.frame)
        self.left_menu.setObjectName(u"left_menu")
        sizePolicy.setHeightForWidth(self.left_menu.sizePolicy().hasHeightForWidth())
        self.left_menu.setSizePolicy(sizePolicy)
        self.left_menu.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.676136 rgba(255, 255, 255, 255), stop:0.988636 rgba(255, 255, 255, 255));")
        self.left_menu.setFrameShape(QFrame.NoFrame)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.left_menu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu1 = QFrame(self.left_menu)
        self.left_menu1.setObjectName(u"left_menu1")
        self.left_menu1.setMinimumSize(QSize(0, 0))
        self.left_menu1.setMaximumSize(QSize(0, 16777215))
        self.left_menu1.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.955, stop:0 rgba(30, 237, 237, 255), stop:0.988636 rgba(219, 241, 255, 255));")
        self.left_menu1.setFrameShape(QFrame.NoFrame)
        self.left_menu1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_menu1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.left_menu1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(80, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.Home = QPushButton(self.frame_3)
        self.Home.setObjectName(u"Home")
        self.Home.setGeometry(QRect(0, 0, 81, 51))
        self.Home.setCursor(QCursor(Qt.PointingHandCursor))
        self.Home.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: none;\n"
"	border-radius:0px;\n"
"	color:white;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: white;\n"
"	border-radius:0px;\n"
"    color:black;\n"
"\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/2948210.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Home.setIcon(icon4)
        self.Home.setIconSize(QSize(32, 32))
        self.Dashboard = QPushButton(self.frame_3)
        self.Dashboard.setObjectName(u"Dashboard")
        self.Dashboard.setGeometry(QRect(0, 50, 81, 51))
        self.Dashboard.setCursor(QCursor(Qt.PointingHandCursor))
        self.Dashboard.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: none;\n"
"	border-radius:0px;\n"
"	color:white;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: white;\n"
"	border-radius:0px;\n"
"    color:black;\n"
"\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/6754734.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard.setIcon(icon5)
        self.Dashboard.setIconSize(QSize(32, 32))
        self.Mangsrv = QPushButton(self.frame_3)
        self.Mangsrv.setObjectName(u"Mangsrv")
        self.Mangsrv.setGeometry(QRect(0, 102, 81, 51))
        self.Mangsrv.setCursor(QCursor(Qt.PointingHandCursor))
        self.Mangsrv.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: none;\n"
"	border-radius:0px;\n"
"	color:white;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: white;\n"
"	border-radius:0px;\n"
"    color:black;\n"
"\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/data.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Mangsrv.setIcon(icon6)
        self.Mangsrv.setIconSize(QSize(32, 32))
        self.event_log = QPushButton(self.frame_3)
        self.event_log.setObjectName(u"event_log")
        self.event_log.setGeometry(QRect(0, 152, 81, 51))
        self.event_log.setCursor(QCursor(Qt.PointingHandCursor))
        self.event_log.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: none;\n"
"	border-radius:0px;\n"
"	color:white;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: white;\n"
"	border-radius:0px;\n"
"    color:black;\n"
"\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/icons8-event-log-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.event_log.setIcon(icon7)
        self.event_log.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.left_menu1)

        self.frame_10 = QFrame(self.left_menu)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.676136 rgba(255, 255, 255, 255), stop:0.988636 rgba(255, 255, 255, 255));")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_10)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_10)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(225, 238, 246);")
        self.Home1 = QWidget()
        self.Home1.setObjectName(u"Home1")
        self.verticalLayout_4 = QVBoxLayout(self.Home1)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.frame_14 = QFrame(self.Home1)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_14)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_14)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:0px;\n"
"\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/istockphoto-1313570688-170667a.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setIconSize(QSize(500, 500))

        self.verticalLayout_5.addWidget(self.pushButton)

        self.label = QLabel(self.frame_14)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 60))
        self.label.setStyleSheet(u"font: 20pt \"Oswald\";\n"
"color: rgb(44, 159, 217);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.Home1)
        self.Dashboard1 = QWidget()
        self.Dashboard1.setObjectName(u"Dashboard1")
        self.gridLayout_6 = QGridLayout(self.Dashboard1)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_11 = QFrame(self.Dashboard1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QFrame {\n"
"background-color: #d1e5f0;\n"
"border:1px solid #00aaff;\n"
"border-radius:10px;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_2 = QPushButton(self.frame_11)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(20, 20))
        self.pushButton_2.setMaximumSize(QSize(200, 200))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(209, 229, 240);\n"
"border:0px solid;\n"
"font: 12pt \"Oswald\";\n"
"color: rgb(44, 159, 217);\n"
"\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icon/icon/ram.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon9)
        self.pushButton_2.setIconSize(QSize(49, 49))

        self.verticalLayout_7.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)

        self.ProgressBar1 = roundProgressBar(self.frame_11)
        self.ProgressBar1.setObjectName(u"ProgressBar1")
        self.ProgressBar1.setMinimumSize(QSize(200, 200))
        self.ProgressBar1.setMaximumSize(QSize(200, 200))
        self.ProgressBar1.setStyleSheet(u"background-color: rgb(209, 229, 240);")

        self.verticalLayout_7.addWidget(self.ProgressBar1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"font: 10pt \"Oswald\";\n"
"color: rgb(27, 131, 222);\n"
"border:0px solid;\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_4)


        self.gridLayout_6.addWidget(self.frame_11, 0, 1, 1, 1)

        self.frame_12 = QFrame(self.Dashboard1)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QFrame {\n"
"background-color: #d1e5f0;\n"
"border:1px solid #00aaff;\n"
"border-radius:10px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"QFrame {\n"
"background-color: #d1e5f0;\n"
"border:0px solid;\n"
"}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.frame_15)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 20))
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setStyleSheet(u"font: 10pt \"Oswald\";\n"
"color: rgb(27, 131, 222);")

        self.verticalLayout_8.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.ProgressBar2 = roundProgressBar(self.frame_15)
        self.ProgressBar2.setObjectName(u"ProgressBar2")
        self.ProgressBar2.setMinimumSize(QSize(100, 100))
        self.ProgressBar2.setMaximumSize(QSize(100, 100))
        self.ProgressBar2.setStyleSheet(u"background-color: rgb(209, 229, 240);")

        self.verticalLayout_8.addWidget(self.ProgressBar2, 0, Qt.AlignHCenter)

        self.label_7 = QLabel(self.frame_15)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 20))
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setStyleSheet(u"font: 10pt \"Oswald\";\n"
"color: rgb(27, 131, 222);")

        self.verticalLayout_8.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.widget_15 = roundProgressBar(self.frame_15)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(100, 100))
        self.widget_15.setMaximumSize(QSize(100, 100))
        self.widget_15.setStyleSheet(u"background-color: rgb(209, 229, 240);")

        self.verticalLayout_8.addWidget(self.widget_15, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"QFrame {\n"
"background-color: #d1e5f0;\n"
"border:0px solid;\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_16)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.pushButton_5 = QPushButton(self.frame_16)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(209, 229, 240);\n"
"border:0px solid;\n"
"font: 12pt \"Oswald\";\n"
"color: rgb(44, 159, 217);\n"
"\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icon/icon/hard-disk-drive (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon10)
        self.pushButton_5.setIconSize(QSize(50, 50))

        self.verticalLayout_9.addWidget(self.pushButton_5, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.frame_16)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(20, 20))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setStyleSheet(u"font: 9pt \"Oswald\";\n"
"color: rgb(40, 168, 245);\n"
"border:1px solid;\n"
"background-color: rgb(225, 238, 246);\n"
"border-radius: 5px;\n"
"border-color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_9.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.label_9 = QLabel(self.frame_16)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(20, 20))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setStyleSheet(u"font: 9pt \"Oswald\";\n"
"color: rgb(40, 168, 245);\n"
"border:1px solid;\n"
"background-color: rgb(225, 238, 246);\n"
"border-radius: 5px;\n"
"border-color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.label_10 = QLabel(self.frame_16)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(20, 20))
        self.label_10.setMaximumSize(QSize(16777215, 30))
        self.label_10.setStyleSheet(u"font: 9pt \"Oswald\";\n"
"color: rgb(40, 168, 245);\n"
"border:1px solid;\n"
"background-color: rgb(225, 238, 246);\n"
"border-radius: 5px;\n"
"border-color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.frame_16)


        self.gridLayout_6.addWidget(self.frame_12, 1, 0, 1, 1)

        self.frame_13 = QFrame(self.Dashboard1)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QFrame {\n"
"background-color: #d1e5f0;\n"
"border:1px solid #00aaff;\n"
"border-radius:10px;\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(300, 30))
        self.label_11.setMaximumSize(QSize(300, 30))
        self.label_11.setStyleSheet(u"QLabel {\n"
"font: 12pt \"Oswald\";\n"
"color: rgb(27, 131, 222);\n"
"border:0px solid;\n"
"}")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.sent_label = QLabel(self.frame_13)
        self.sent_label.setObjectName(u"sent_label")
        self.sent_label.setMinimumSize(QSize(300, 30))
        self.sent_label.setMaximumSize(QSize(300, 30))
        self.sent_label.setStyleSheet(u"font: 9pt \"Oswald\";\n"
"border:0px solid;")

        self.verticalLayout_10.addWidget(self.sent_label, 0, Qt.AlignHCenter)

        self.progressBar_1 = QProgressBar(self.frame_13)
        self.progressBar_1.setObjectName(u"progressBar_1")
        self.progressBar_1.setMinimumSize(QSize(300, 0))
        self.progressBar_1.setMaximumSize(QSize(300, 16777215))
        self.progressBar_1.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #2196F3;\n"
"    border-radius: 5px;\n"
"    background-color: #E0E0E0;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #2196F3;\n"
"    width: 10px; \n"
" \n"
"}\n"
"\n"
"")
        self.progressBar_1.setMaximum(100)
        self.progressBar_1.setValue(0)
        self.progressBar_1.setAlignment(Qt.AlignCenter)
        self.progressBar_1.setTextVisible(False)
        self.progressBar_1.setOrientation(Qt.Horizontal)
        self.progressBar_1.setInvertedAppearance(False)
        self.progressBar_1.setTextDirection(QProgressBar.BottomToTop)

        self.verticalLayout_10.addWidget(self.progressBar_1, 0, Qt.AlignHCenter)

        self.recv_label = QLabel(self.frame_13)
        self.recv_label.setObjectName(u"recv_label")
        self.recv_label.setMinimumSize(QSize(300, 30))
        self.recv_label.setMaximumSize(QSize(300, 30))
        self.recv_label.setStyleSheet(u"font: 9pt \"Oswald\";\n"
"border:0px solid;")

        self.verticalLayout_10.addWidget(self.recv_label, 0, Qt.AlignHCenter)

        self.progressBar_2 = QProgressBar(self.frame_13)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setMinimumSize(QSize(300, 0))
        self.progressBar_2.setMaximumSize(QSize(300, 16777215))
        self.progressBar_2.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid rgb(255, 170, 0);\n"
"    border-radius: 5px;\n"
"    background-color: #E0E0E0;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"   \n"
"	background-color: rgb(255, 170, 0);\n"
"    width: 10px; \n"
" \n"
"}\n"
"")
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setValue(0)
        self.progressBar_2.setAlignment(Qt.AlignCenter)
        self.progressBar_2.setTextVisible(False)

        self.verticalLayout_10.addWidget(self.progressBar_2, 0, Qt.AlignHCenter)


        self.gridLayout_6.addWidget(self.frame_13, 1, 1, 1, 1)

        self.frame_9 = QFrame(self.Dashboard1)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QFrame {\n"
"background-color: #d1e5f0;\n"
"border:1px solid #00aaff;\n"
"border-radius:10px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_3 = QPushButton(self.frame_9)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(20, 20))
        self.pushButton_3.setMaximumSize(QSize(200, 200))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(209, 229, 240);\n"
"border:0px solid;\n"
"font: 12pt \"Oswald\";\n"
"color: rgb(44, 159, 217);\n"
"\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icon/icon/cpu (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon11)
        self.pushButton_3.setIconSize(QSize(49, 49))

        self.verticalLayout_6.addWidget(self.pushButton_3, 0, Qt.AlignHCenter)

        self.ProgressBar = roundProgressBar(self.frame_9)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setMinimumSize(QSize(200, 200))
        self.ProgressBar.setMaximumSize(QSize(200, 200))
        self.ProgressBar.setStyleSheet(u"background-color: rgb(209, 229, 240);")

        self.verticalLayout_6.addWidget(self.ProgressBar, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"font: 10pt \"Oswald\";\n"
"color: rgb(27, 131, 222);\n"
"border:0px solid;\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.gridLayout_6.addWidget(self.frame_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Dashboard1)
        self.Mangsrv_1 = QWidget()
        self.Mangsrv_1.setObjectName(u"Mangsrv_1")
        self.verticalLayout_11 = QVBoxLayout(self.Mangsrv_1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_17 = QFrame(self.Mangsrv_1)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"QFrame {\n"
"\n"
"background-color: #d1e5f0;\n"
"border:1px solid #00aaff;\n"
"border-radius:10px;\n"
"}")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_17)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"QFrame {\n"
"background-color: rgb(209, 229, 240);\n"
"border:0px solid;\n"
"}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_28 = QFrame(self.frame_19)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_28)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.pushButton_6 = QPushButton(self.frame_28)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setMinimumSize(QSize(0, 40))
        self.pushButton_6.setMaximumSize(QSize(16777215, 40))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(143, 214, 214);\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 133, 200);\n"
"	border-radius:3px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icon/icon/reboot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon12)
        self.pushButton_6.setIconSize(QSize(30, 30))
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setFlat(False)

        self.verticalLayout_21.addWidget(self.pushButton_6)


        self.horizontalLayout_4.addWidget(self.frame_28)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_22)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pushButton_7 = QPushButton(self.frame_22)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 30))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")
        self.pushButton_7.setIcon(icon12)
        self.pushButton_7.setIconSize(QSize(25, 25))

        self.verticalLayout_14.addWidget(self.pushButton_7)

        self.pushButton_12 = QPushButton(self.frame_22)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 30))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icon/icon/play-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon13)
        self.pushButton_12.setIconSize(QSize(25, 25))

        self.verticalLayout_14.addWidget(self.pushButton_12)

        self.pushButton_11 = QPushButton(self.frame_22)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 30))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icon/icon/stop-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon14)
        self.pushButton_11.setIconSize(QSize(25, 25))

        self.verticalLayout_14.addWidget(self.pushButton_11)


        self.horizontalLayout_4.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_19)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_23)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pushButton_8 = QPushButton(self.frame_23)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 30))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")
        self.pushButton_8.setIcon(icon12)
        self.pushButton_8.setIconSize(QSize(25, 25))

        self.verticalLayout_15.addWidget(self.pushButton_8)

        self.pushButton_13 = QPushButton(self.frame_23)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 30))
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")
        self.pushButton_13.setIcon(icon13)
        self.pushButton_13.setIconSize(QSize(25, 25))

        self.verticalLayout_15.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_23)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 30))
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")
        self.pushButton_14.setIcon(icon14)
        self.pushButton_14.setIconSize(QSize(25, 25))

        self.verticalLayout_15.addWidget(self.pushButton_14)


        self.horizontalLayout_4.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_19)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_24)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.pushButton_9 = QPushButton(self.frame_24)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 30))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")
        self.pushButton_9.setIcon(icon12)
        self.pushButton_9.setIconSize(QSize(25, 25))

        self.verticalLayout_16.addWidget(self.pushButton_9)

        self.pushButton_15 = QPushButton(self.frame_24)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(0, 30))
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")
        self.pushButton_15.setIcon(icon13)
        self.pushButton_15.setIconSize(QSize(25, 25))

        self.verticalLayout_16.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.frame_24)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(0, 30))
        self.pushButton_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")
        self.pushButton_16.setIcon(icon14)
        self.pushButton_16.setIconSize(QSize(25, 25))

        self.verticalLayout_16.addWidget(self.pushButton_16)


        self.horizontalLayout_4.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_19)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_25)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.pushButton_10 = QPushButton(self.frame_25)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 30))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")
        self.pushButton_10.setIcon(icon12)
        self.pushButton_10.setIconSize(QSize(25, 25))

        self.verticalLayout_17.addWidget(self.pushButton_10)

        self.pushButton_17 = QPushButton(self.frame_25)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(0, 30))
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")
        self.pushButton_17.setIcon(icon13)
        self.pushButton_17.setIconSize(QSize(25, 25))

        self.verticalLayout_17.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.frame_25)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(0, 30))
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")
        self.pushButton_18.setIcon(icon14)
        self.pushButton_18.setIconSize(QSize(25, 25))

        self.verticalLayout_17.addWidget(self.pushButton_18)


        self.horizontalLayout_4.addWidget(self.frame_25)


        self.verticalLayout_12.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"QFrame {\n"
"background-color: #d1e5f0;\n"
"border:0px solid;\n"
"}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_2 = QLabel(self.frame_20)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setStyleSheet(u"font: 10pt \"Oswald\";\n"
"color: rgb(27, 131, 222);")

        self.verticalLayout_13.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.Output = QLineEdit(self.frame_20)
        self.Output.setObjectName(u"Output")
        self.Output.setMinimumSize(QSize(700, 40))
        self.Output.setStyleSheet(u"font: 8pt \"Oswald\";\n"
"color: rgb(0, 0, 0);\n"
"border:1px solid;\n"
"background-color: rgb(225, 238, 246);\n"
"border-radius: 5px;\n"
"border-color: rgb(255, 255, 255);\n"
"")
        self.Output.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.Output, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.clear = QPushButton(self.frame_20)
        self.clear.setObjectName(u"clear")
        self.clear.setMinimumSize(QSize(90, 30))
        self.clear.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 110, 112);\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(195, 0, 0);\n"
"	border-radius:3px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icon/icon/310679.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear.setIcon(icon15)
        self.clear.setIconSize(QSize(20, 20))

        self.verticalLayout_13.addWidget(self.clear, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_12.addWidget(self.frame_20)


        self.verticalLayout_11.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.Mangsrv_1)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"QFrame {\n"
"background-color: #d1e5f0;\n"
"border:1px solid #00aaff;\n"
"border-radius:10px;\n"
"}")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_18)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_18)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"QFrame {\n"
"background-color: #d1e5f0;\n"
"border:0px solid;\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_26)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_3 = QLabel(self.frame_26)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setStyleSheet(u"font: 10pt \"Oswald\";\n"
"color: rgb(27, 131, 222);")

        self.verticalLayout_18.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.lineEdit = QLineEdit(self.frame_26)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(700, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit.setStyleSheet(u"font: 9pt \"Oswald\";\n"
"color: rgb(0, 0, 0);\n"
"border:1px solid;\n"
"background-color: rgb(225, 238, 246);\n"
"border-radius: 5px;\n"
"border-color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.lineEdit, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_20.addWidget(self.frame_26)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy1)
        self.frame_21.setMinimumSize(QSize(0, 0))
        self.frame_21.setMaximumSize(QSize(16777215, 16777215))
        self.frame_21.setStyleSheet(u"QFrame {\n"
"background-color: #d1e5f0;\n"
"border:0px solid;\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ExcuteCmd = QPushButton(self.frame_21)
        self.ExcuteCmd.setObjectName(u"ExcuteCmd")
        self.ExcuteCmd.setMinimumSize(QSize(100, 30))
        self.ExcuteCmd.setMaximumSize(QSize(100, 16777215))
        self.ExcuteCmd.setFont(font)
        self.ExcuteCmd.setCursor(QCursor(Qt.PointingHandCursor))
        self.ExcuteCmd.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	color: rgb(77, 213, 255);\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: rgb(77, 213, 255);\n"
"\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icon/icon/work-in-progress.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ExcuteCmd.setIcon(icon16)
        self.ExcuteCmd.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.ExcuteCmd)

        self.Clear_2 = QPushButton(self.frame_21)
        self.Clear_2.setObjectName(u"Clear_2")
        self.Clear_2.setEnabled(True)
        self.Clear_2.setMinimumSize(QSize(100, 30))
        self.Clear_2.setMaximumSize(QSize(100, 16777215))
        self.Clear_2.setFont(font)
        self.Clear_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.Clear_2.setMouseTracking(False)
        self.Clear_2.setTabletTracking(False)
        self.Clear_2.setFocusPolicy(Qt.StrongFocus)
        self.Clear_2.setAcceptDrops(False)
        self.Clear_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 110, 112);\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(195, 0, 0);\n"
"	border-radius:3px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.Clear_2.setIcon(icon15)
        self.Clear_2.setIconSize(QSize(20, 20))
        self.Clear_2.setCheckable(False)
        self.Clear_2.setAutoDefault(False)
        self.Clear_2.setFlat(False)

        self.horizontalLayout_5.addWidget(self.Clear_2)


        self.verticalLayout_20.addWidget(self.frame_21, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_27 = QFrame(self.frame_18)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"QFrame {\n"
"background-color: #d1e5f0;\n"
"border:0px solid;\n"
"}")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_27)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_12 = QLabel(self.frame_27)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setMaximumSize(QSize(16777215, 16777215))
        self.label_12.setStyleSheet(u"font: 10pt \"Oswald\";\n"
"color: rgb(27, 131, 222);")

        self.verticalLayout_19.addWidget(self.label_12, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.output_cmd = QPlainTextEdit(self.frame_27)
        self.output_cmd.setObjectName(u"output_cmd")
        self.output_cmd.setMinimumSize(QSize(700, 0))
        self.output_cmd.setMaximumSize(QSize(700, 16777215))
        self.output_cmd.setStyleSheet(u"font:9pt \"Oswald\";\n"
"color: rgb(0, 0, 0);\n"
"border:1px solid;\n"
"background-color: rgb(225, 238, 246);\n"
"border-radius: 5px;\n"
"border-color: rgb(255, 255, 255);")
        self.output_cmd.setReadOnly(True)

        self.verticalLayout_19.addWidget(self.output_cmd, 0, Qt.AlignHCenter)


        self.verticalLayout_20.addWidget(self.frame_27)


        self.verticalLayout_11.addWidget(self.frame_18)

        self.stackedWidget.addWidget(self.Mangsrv_1)
        self.log = QWidget()
        self.log.setObjectName(u"log")
        self.gridLayout_7 = QGridLayout(self.log)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_29 = QFrame(self.log)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_29)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 100))
        self.frame_30.setMaximumSize(QSize(16777215, 16777215))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_32)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.pushButton_19 = QPushButton(self.frame_32)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(0, 30))
        self.pushButton_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")

        self.verticalLayout_23.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.frame_32)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(0, 30))
        self.pushButton_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_20.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")

        self.verticalLayout_23.addWidget(self.pushButton_20)


        self.horizontalLayout_6.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_33)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.Show_ssh_log = QPushButton(self.frame_33)
        self.Show_ssh_log.setObjectName(u"Show_ssh_log")
        self.Show_ssh_log.setMinimumSize(QSize(0, 30))
        self.Show_ssh_log.setCursor(QCursor(Qt.PointingHandCursor))
        self.Show_ssh_log.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")

        self.verticalLayout_24.addWidget(self.Show_ssh_log)

        self.pushButton_22 = QPushButton(self.frame_33)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(0, 30))
        self.pushButton_22.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_22.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")

        self.verticalLayout_24.addWidget(self.pushButton_22)


        self.horizontalLayout_6.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_30)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_34)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.Show_acc_log_httpd = QPushButton(self.frame_34)
        self.Show_acc_log_httpd.setObjectName(u"Show_acc_log_httpd")
        self.Show_acc_log_httpd.setMinimumSize(QSize(0, 30))
        self.Show_acc_log_httpd.setCursor(QCursor(Qt.PointingHandCursor))
        self.Show_acc_log_httpd.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")

        self.verticalLayout_25.addWidget(self.Show_acc_log_httpd)

        self.pushButton_24 = QPushButton(self.frame_34)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(0, 30))
        self.pushButton_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_24.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")

        self.verticalLayout_25.addWidget(self.pushButton_24)

        self.pushButton_26 = QPushButton(self.frame_34)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(0, 30))
        self.pushButton_26.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(225, 238, 246);\n"
"	border-radius:3px;\n"
"	\n"
"	color: black;\n"
"\n"
"}")

        self.verticalLayout_25.addWidget(self.pushButton_26)


        self.horizontalLayout_6.addWidget(self.frame_34)


        self.verticalLayout_22.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_31)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.plainTextEdit = QPlainTextEdit(self.frame_31)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"font:10pt \"Oswald\";\n"
"color: rgb(0, 0, 0);\n"
"border:1px solid;\n"
"background-color: rgb(225, 238, 246);\n"
"border-radius: 5px;\n"
"border-color: rgb(255, 255, 255);")

        self.gridLayout_8.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.pushButton_25 = QPushButton(self.frame_31)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(100, 30))
        self.pushButton_25.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 110, 112);\n"
"	\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(195, 0, 0);\n"
"	border-radius:3px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_25.setIcon(icon15)
        self.pushButton_25.setIconSize(QSize(20, 20))

        self.gridLayout_8.addWidget(self.pushButton_25, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_22.addWidget(self.frame_31)


        self.gridLayout_7.addWidget(self.frame_29, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.log)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_10)


        self.verticalLayout_2.addWidget(self.left_menu)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_6.setDefault(False)
        self.Clear_2.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText("")
        self.Bn_Min.setText("")
        self.Bn_Max.setText("")
        self.Bn_Close.setText("")
#if QT_CONFIG(tooltip)
        self.Home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.Home.setText("")
#if QT_CONFIG(tooltip)
        self.Dashboard.setToolTip(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#endif // QT_CONFIG(tooltip)
        self.Dashboard.setText("")
#if QT_CONFIG(tooltip)
        self.Mangsrv.setToolTip(QCoreApplication.translate("MainWindow", u"Remote Command", None))
#endif // QT_CONFIG(tooltip)
        self.Mangsrv.setText("")
#if QT_CONFIG(tooltip)
        self.event_log.setToolTip(QCoreApplication.translate("MainWindow", u"Event Log", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.event_log.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.event_log.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.event_log.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Managment Server", None))
        self.pushButton_2.setText("")
        self.label_4.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Hard Drive Activity", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Hard Drive Usage", None))
        self.pushButton_5.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Network Usage", None))
        self.sent_label.setText("")
        self.recv_label.setText("")
        self.pushButton_3.setText("")
        self.label_5.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"   Reboot Server", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"   PMTA", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"   PMTA", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"   PMTA", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"   PMTAHTTP", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"   PMTAHTTP", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"   PMTAHTTP", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"   SSH", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"   SSH", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"   SSH", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"   HTTP", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"   HTTP", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"   HTTP", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Optout", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u" Clear", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Remote Command", None))
        self.ExcuteCmd.setText(QCoreApplication.translate("MainWindow", u"Excute", None))
        self.Clear_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Optout", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Show journal logs", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Show history command", None))
        self.Show_ssh_log.setText(QCoreApplication.translate("MainWindow", u"Show ssh logs", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Show_acc_log_httpd.setText(QCoreApplication.translate("MainWindow", u"Show access log httpd", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Show error log httpd", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Clear log httpd", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

