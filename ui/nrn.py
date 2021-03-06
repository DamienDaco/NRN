# Form implementation generated from reading ui file '.\nrn.ui'
#
# Created by: PyQt6 UI code generator 6.0.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(437, 281)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_0 = QtWidgets.QWidget()
        self.tab_0.setObjectName("tab_0")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupboxGenerator = QtWidgets.QGroupBox(self.tab_0)
        self.groupboxGenerator.setObjectName("groupboxGenerator")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupboxGenerator)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBoxYear = QtWidgets.QComboBox(self.groupboxGenerator)
        self.comboBoxYear.setObjectName("comboBoxYear")
        self.gridLayout_4.addWidget(self.comboBoxYear, 0, 0, 1, 1)
        self.comboBoxMonth = QtWidgets.QComboBox(self.groupboxGenerator)
        self.comboBoxMonth.setObjectName("comboBoxMonth")
        self.gridLayout_4.addWidget(self.comboBoxMonth, 0, 1, 1, 2)
        self.comboBoxDay = QtWidgets.QComboBox(self.groupboxGenerator)
        self.comboBoxDay.setObjectName("comboBoxDay")
        self.gridLayout_4.addWidget(self.comboBoxDay, 0, 3, 1, 1)
        self.comboBoxGender = QtWidgets.QComboBox(self.groupboxGenerator)
        self.comboBoxGender.setObjectName("comboBoxGender")
        self.gridLayout_4.addWidget(self.comboBoxGender, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 1, 1, 1)
        self.pushButtonGenerate = QtWidgets.QPushButton(self.groupboxGenerator)
        self.pushButtonGenerate.setObjectName("pushButtonGenerate")
        self.gridLayout_4.addWidget(self.pushButtonGenerate, 0, 5, 1, 1)
        self.pushButtonCopyToClipBoard = QtWidgets.QPushButton(self.groupboxGenerator)
        self.pushButtonCopyToClipBoard.setObjectName("pushButtonCopyToClipBoard")
        self.gridLayout_4.addWidget(self.pushButtonCopyToClipBoard, 2, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 2, 1, 1, 1)
        self.lineEditGenerator = QtWidgets.QLineEdit(self.groupboxGenerator)
        self.lineEditGenerator.setObjectName("lineEditGenerator")
        self.gridLayout_4.addWidget(self.lineEditGenerator, 2, 3, 1, 2)
        self.gridLayout_2.addWidget(self.groupboxGenerator, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonBelgium = QtWidgets.QRadioButton(self.tab_0)
        self.buttonBelgium.setObjectName("buttonBelgium")
        self.horizontalLayout.addWidget(self.buttonBelgium)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_0, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 437, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "National Number Generator"))
        self.tab_0.setToolTip(_translate("MainWindow", "Generate NRN from a date"))
        self.tab_0.setStatusTip(_translate("MainWindow", "Generate NRN from a date"))
        self.groupboxGenerator.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButtonGenerate.setText(_translate("MainWindow", "Generate!"))
        self.pushButtonCopyToClipBoard.setText(_translate("MainWindow", "Copy"))
        self.buttonBelgium.setText(_translate("MainWindow", "Belgium"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_0), _translate("MainWindow", "Generate"))
        self.groupBox_4.setTitle(_translate("MainWindow", "GroupBox"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Validate"))
