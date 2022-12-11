# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 300)
        MainWindow.setMinimumSize(QSize(650, 300))
        MainWindow.setMaximumSize(QSize(650, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 651, 301))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(18, 155, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Wekcome = QLabel(self.frame)
        self.Wekcome.setObjectName(u"Wekcome")
        self.Wekcome.setGeometry(QRect(260, 20, 161, 41))
        self.Wekcome.setStyleSheet(u"QLabel{\n"
"font: 30pt \"Rockwell\";\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.lSearch = QLineEdit(self.frame)
        self.lSearch.setObjectName(u"lSearch")
        self.lSearch.setGeometry(QRect(170, 80, 331, 21))
        self.lSearch.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: black;\n"
"}")
        self.lName = QLabel(self.frame)
        self.lName.setObjectName(u"lName")
        self.lName.setGeometry(QRect(100, 120, 60, 16))
        self.lDate = QLabel(self.frame)
        self.lDate.setObjectName(u"lDate")
        self.lDate.setGeometry(QRect(100, 150, 60, 16))
        self.lTime = QLabel(self.frame)
        self.lTime.setObjectName(u"lTime")
        self.lTime.setGeometry(QRect(100, 180, 60, 16))
        self.lSize = QLabel(self.frame)
        self.lSize.setObjectName(u"lSize")
        self.lSize.setGeometry(QRect(100, 210, 60, 16))
        self.btDownload = QPushButton(self.frame)
        self.btDownload.setObjectName(u"btDownload")
        self.btDownload.setGeometry(QRect(260, 240, 120, 50))
        self.dName = QLabel(self.frame)
        self.dName.setObjectName(u"dName")
        self.dName.setGeometry(QRect(160, 120, 211, 16))
        self.dDate = QLabel(self.frame)
        self.dDate.setObjectName(u"dDate")
        self.dDate.setGeometry(QRect(160, 150, 211, 16))
        self.dTime = QLabel(self.frame)
        self.dTime.setObjectName(u"dTime")
        self.dTime.setGeometry(QRect(160, 180, 211, 16))
        self.dSize = QLabel(self.frame)
        self.dSize.setObjectName(u"dSize")
        self.dSize.setGeometry(QRect(160, 210, 211, 16))
        self.lName_2 = QLabel(self.frame)
        self.lName_2.setObjectName(u"lName_2")
        self.lName_2.setGeometry(QRect(100, 80, 60, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Youtube Downloader", None))
        self.Wekcome.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.lSearch.setText("")
        self.lName.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.lDate.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.lTime.setText(QCoreApplication.translate("MainWindow", u"Time :", None))
        self.lSize.setText(QCoreApplication.translate("MainWindow", u"Size :", None))
        self.btDownload.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.dName.setText("")
        self.dDate.setText("")
        self.dTime.setText("")
        self.dSize.setText("")
        self.lName_2.setText(QCoreApplication.translate("MainWindow", u"Enter URL :", None))
    # retranslateUi

