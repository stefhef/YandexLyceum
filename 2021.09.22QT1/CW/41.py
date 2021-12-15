
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 40, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 70, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 100, 81, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 130, 81, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 100, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 130, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "edit1"))
        self.checkBox_2.setText(_translate("MainWindow", "edit2"))
        self.checkBox_3.setText(_translate("MainWindow", "edit3"))
        self.checkBox_4.setText(_translate("MainWindow", "edit4"))
        self.lineEdit.setText(_translate("MainWindow", "Поле edit1"))
        self.lineEdit_2.setText(_translate("MainWindow", "Поле edit2"))
        self.lineEdit_3.setText(_translate("MainWindow", "Поле edit3"))
        self.lineEdit_4.setText(_translate("MainWindow", "Поле edit4"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkBox.stateChanged.connect(self.hide_box)
        self.checkBox_2.stateChanged.connect(self.hide_box)
        self.checkBox_3.stateChanged.connect(self.hide_box)
        self.checkBox_4.stateChanged.connect(self.hide_box)
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()

    def hide_box(self, state):
        name = self.sender().text()
        if state == 0:

            if name == 'edit1':
                self.lineEdit.hide()
            elif name == 'edit2':
                self.lineEdit_2.hide()
            elif name == 'edit3':
                self.lineEdit_3.hide()
            else:
                self.lineEdit_4.hide()

        else:
            if name == 'edit1':
                self.lineEdit.show()
            elif name == 'edit2':
                self.lineEdit_2.show()
            elif name == 'edit3':
                self.lineEdit_3.show()
            else:
                self.lineEdit_4.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
    