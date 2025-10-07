
import sys
from GUI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    #window.resize(800, 600)
    window.show()

    sys.exit(app.exec_())


