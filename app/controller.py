from PyQt6 import QtCore
from ui.nrn import *


class Controller(QtCore.QObject):

    def __init__(self, my_app):
        super().__init__()

        self.my_app = my_app
        self.view = Ui_MainWindow()
        self.view.setupUi(self.my_app)
