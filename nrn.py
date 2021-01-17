import sys
from ui.nrn import *
from PyQt6 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    my_app = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(my_app)
    my_app.show()
    sys.exit(app.exec())
