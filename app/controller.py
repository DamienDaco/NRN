from PyQt6 import QtCore
from PyQt6 import QtWidgets
from ui.nrn import *
from app.nrn_generators import *


class Controller(QtCore.QObject):

    def __init__(self, my_app):
        super().__init__()

        self.my_app = my_app
        self.view = Ui_MainWindow()
        self.view.setupUi(self.my_app)

        self.start_first()

    def start_first(self):
        self.populate_years()
        self.populate_month()
        self.populate_days()
        self.populate_gender()
        self.view.buttonBelgium.setChecked(True)
        self.view.pushButtonGenerate.clicked.connect(self.generate_from_date)
        self.view.lineEditGenerator.setReadOnly(True)
        self.view.pushButtonCopyToClipBoard.clicked.connect(self.copy_to_clipboard)

    def populate_years(self):
        self.yearsList = [str(x) for x in list(range(1900, 2021, 1))]
        self.view.comboBoxYear.addItems(self.yearsList)
        self.view.comboBoxYear.setCurrentText('1980')

    def populate_month(self):
        self.monthsList = [f"{x:02d}" for x in list(range(1, 13, 1))]
        self.view.comboBoxMonth.addItems(self.monthsList)
        self.view.comboBoxMonth.setCurrentText('01')

    def populate_days(self):
        self.daysList = [f"{x:02d}" for x in list(range(1, 32, 1))]
        self.view.comboBoxDay.addItems(self.daysList)
        self.view.comboBoxDay.setCurrentText('01')

    def populate_gender(self):
        self.gendersList = ['Male', 'Female']
        self.view.comboBoxGender.addItems(self.gendersList)

    def view_snapshot(self):
        self.selectedYear = self.view.comboBoxYear.currentText()
        self.selectedMonth = self.view.comboBoxMonth.currentText()
        self.selectedDay = self.view.comboBoxDay.currentText()
        self.selectedGender = self.view.comboBoxGender.currentText()
        return self.selectedYear, self.selectedMonth, self.selectedDay, self.selectedGender

    def generate_from_date(self):
        w, x, y, z = self.view_snapshot()
        self.gen = NrnBelgiumGenerateFromDate(w, x, y, z)
        self.view.lineEditGenerator.setText(self.gen.nrn)
        self.view.lineEditGenerator.hasSelectedText()

    def copy_to_clipboard(self):
        self.currentText = self.view.lineEditGenerator.text()
        print(self.currentText)
        QtWidgets.QApplication.clipboard().setText(self.currentText)

