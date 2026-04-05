# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'FwMusic_20109DBkHRj.ui'
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
        MainWindow.resize(1100, 700)  # 放大到原来的两倍大小
        MainWindow.setMinimumSize(QSize(1100, 700))
        MainWindow.setMaximumSize(QSize(1100, 700))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"border-image: url('D:/Python Projects/FwMusic2/FwMusic-2.0-beta4_PIC/CityTheme2_use.png')\n" "")

        self.actionAbout_FwMusic = QAction(MainWindow)
        self.actionAbout_FwMusic.setObjectName(u"actionAbout_FwMusic")

        self.actionAbout_me = QAction(MainWindow)
        self.actionAbout_me.setObjectName(u"actionAbout_me")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 302, 162))  # 放大位置和大小
        self.label.setStyleSheet(u"font: 60pt \"Times New Roman\";\n" "color:rgb(58, 153, 255);\n" "border-image: Transparent")  # 字体放大到原来的两倍

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 60, 182, 32))  # 放大位置和大小
        self.label_2.setStyleSheet(u"font: 24pt \"Times New Roman\";\n" "color:rgb(102, 88, 255);\n" "border-image: Transparent")  # 字体放大到原来的两倍

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 200, 202, 32))  # 放大位置和大小
        self.checkBox.setStyleSheet(u"font: 16pt \"Times New Roman\";\n" "color:rgb(71, 99, 255);\n" "border-image: Transparent")  # 字体放大到原来的两倍

        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(840, 120, 202, 82))  # 放大位置和大小
        self.commandLinkButton.setStyleSheet(u"font: 16pt \"Times New Roman\";\n" "background:rgb(184, 201, 255);\n" "border-image: Transparent;")  # 字体放大到原来的两倍

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 120, 782, 62))  # 放大位置和大小
        self.lineEdit.setStyleSheet(u"background:rgb(184, 201, 255);\n" "border-image: Transparent;")

        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(200, 200, 142, 32))  # 放大位置和大小
        self.checkBox_3.setStyleSheet(u"font: 16pt \"Times New Roman\";\n" "color:rgb(71, 99, 255);\n" "border-image: Transparent")  # 字体放大到原来的两倍

        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(400, 200, 162, 32))  # 放大位置和大小
        self.checkBox_4.setStyleSheet(u"font: 16pt \"Times New Roman\";\n" "color:rgb(71, 99, 255);\n" "border-image: Transparent")  # 字体放大到原来的两倍

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(920, 540, 162, 62))  # 放大位置和大小
        self.pushButton.setStyleSheet(u"font: 16pt \"Times New Roman\";\n" "background: rgb(175, 203, 255);\n" "border-image: Transparent;")  # 字体放大到原来的两倍

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(920, 460, 162, 62))  # 放大位置和大小
        self.pushButton_2.setStyleSheet(u"font: 16pt \"Times New Roman\";\n" "background: rgb(175, 203, 255);\n" "border-image: Transparent;")  # 字体放大到原来的两倍

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 620, 202, 32))  # 放大位置和大小
        self.label_3.setStyleSheet(u"font: 16pt \"Times New Roman\";\n" "color:rgb(199, 212, 255);\n" "border-image: Transparent")  # 字体放大到原来的两倍

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 640, 342, 32))  # 放大位置和大小
        self.label_4.setStyleSheet(u"font: 16pt \"Times New Roman\";\n" "color:rgb(199, 212, 255);\n" "border-image: Transparent")  # 字体放大到原来的两倍

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 660, 322, 32))  # 放大位置和大小
        self.label_5.setStyleSheet(u"font: 16pt \"Times New Roman\";\n" "color:rgb(199, 212, 255);\n" "border-image: Transparent")  # 字体放大到原来的两倍

        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(620, 200, 162, 32))  # 放大位置和大小
        self.checkBox_5.setStyleSheet(u"font: 16pt \"Times New Roman\";\n" "color:rgb(71, 99, 255);\n" "border-image: Transparent")  # 字体放大到原来的两倍

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 580, 102, 40))  # 放大位置和大小
        self.pushButton_3.setStyleSheet(u"font: 16pt \"Times New Roman\";\n" "background: rgb(175, 203, 255);\n" "border-image: Transparent;")  # 字体放大到原来的两倍

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FwMusic", None))
        self.actionAbout_FwMusic.setText(QCoreApplication.translate("MainWindow", u"About FwMusic", None))
        self.actionAbout_me.setText(QCoreApplication.translate("MainWindow", u"About me", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"FwMusic", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"v2.1.0(20109)", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Artist", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.lineEdit.setText("")
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Album", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Theme: CityOfRain", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Picture: CsLrisEto(Unauthorized)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Program: Flying374", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Playlist_v2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
