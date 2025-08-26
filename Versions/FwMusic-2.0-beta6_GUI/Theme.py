# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FwMusic_20006SXGrUp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 350)
        MainWindow.setMinimumSize(QSize(550, 350))
        MainWindow.setMaximumSize(QSize(550, 350))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"border-image: url('D:/Python Projects/FwMusic2/FwMusic-2.0-beta4_PIC/CityTheme2_use.png')\n"
"")
        self.actionAbout_FwMusic = QAction(MainWindow)
        self.actionAbout_FwMusic.setObjectName(u"actionAbout_FwMusic")
        self.actionAbout_me = QAction(MainWindow)
        self.actionAbout_me.setObjectName(u"actionAbout_me")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, -10, 211, 81))
        self.label.setStyleSheet(u"font: 30pt \"Times New Roman\";\n"
"color:rgb(58, 153, 255);\n"
"border-image: Transparent")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 30, 91, 16))
        self.label_2.setStyleSheet(u"font: 12pt \"Times New Roman\";\n"
"color:rgb(102, 88, 255);\n"
"border-image: Transparent")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 100, 101, 16))
        self.checkBox.setStyleSheet(u"font: 8pt \"Times New Roman\";\n"
"color:rgb(71, 99, 255);\n"
"border-image: Transparent")
        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(420, 60, 101, 41))
        self.commandLinkButton.setStyleSheet(u"background:rgb(184, 201, 255);\n"
"border-image: Transparent;")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 60, 391, 31))
        self.lineEdit.setStyleSheet(u"background:rgb(184, 201, 255);\n"
"border-image: Transparent;")
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(130, 100, 101, 16))
        self.checkBox_3.setStyleSheet(u"font: 8pt \"Times New Roman\";\n"
"color:rgb(71, 99, 255);\n"
"border-image: Transparent")
        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(250, 100, 81, 16))
        self.checkBox_4.setStyleSheet(u"font: 8pt \"Times New Roman\";\n"
"color:rgb(71, 99, 255);\n"
"border-image: Transparent")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(460, 270, 81, 31))
        self.pushButton.setStyleSheet(u"background: rgb(175, 203, 255);\n"
"border-image: Transparent;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(460, 230, 81, 31))
        self.pushButton_2.setStyleSheet(u"background: rgb(175, 203, 255);\n"
"border-image: Transparent;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 310, 101, 16))
        self.label_3.setStyleSheet(u"font: 8pt \"Times New Roman\";\n"
"color:rgb(199, 212, 255);\n"
"border-image: Transparent;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 320, 151, 16))
        self.label_4.setStyleSheet(u"font: 8pt \"Times New Roman\";\n"
"color:rgb(199, 212, 255);\n"
"border-image: Transparent;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 330, 91, 16))
        self.label_5.setStyleSheet(u"font: 8pt \"Times New Roman\";\n"
"color:rgb(199, 212, 255);\n"
"border-image: Transparent;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(410, 320, 131, 21))
        self.label_6.setStyleSheet(u"font: 10pt \"Times New Roman\";\n"
"color:rgb(71, 99, 255);\n"
"border-image: Transparent;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FwMusic", None))
        self.actionAbout_FwMusic.setText(QCoreApplication.translate("MainWindow", u"About FwMusic", None))
        self.actionAbout_me.setText(QCoreApplication.translate("MainWindow", u"About me", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"FwMusic", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"v2.0.0(20006)", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Use Official Api", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Music url...", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Use Ncm Api(s)", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Use Vip Api", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Theme: CityOfRain2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Picture: CsLrisEto(Unauthorized)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Program: Flying374", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"BGM:\u5b64\u5c9b\u57ce\u5e02\u7684\u4f20\u8bf4", None))
    # retranslateUi


ui = Ui_MainWindow()
ui.objectName = 'ui'
ui.retranslateUi(ui)
