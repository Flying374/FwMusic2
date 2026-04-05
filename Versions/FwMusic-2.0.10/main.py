# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow  # 确保文件名和路径正确
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 连接按钮的点击事件到槽函数
        self.pushButton.clicked.connect(self.show_settings)
        self.pushButton_2.clicked.connect(self.show_about)
        self.pushButton_3.clicked.connect(self.exit_app)
        self.commandLinkButton.clicked.connect(self.download)
    def show_settings(self):
        print("Settings button clicked")
    def show_about(self):
        print("About button clicked")
    def exit_app(self):
        print("Exit button clicked")
        QApplication.quit()
    def download(self):
        print("Download button clicked")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())