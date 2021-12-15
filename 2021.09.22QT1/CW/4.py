import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Прятки для виджетов")
        MainWindow.resize(511, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 40, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.toggle()

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 70, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.toggle()

        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 100, 81, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.toggle()

        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 130, 81, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.toggle()

        self.edit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit1.setGeometry(QtCore.QRect(90, 40, 113, 20))
        self.edit1.setObjectName("edit1")
        self.edit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit2.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.edit2.setObjectName("edit2")
        self.edit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit3.setGeometry(QtCore.QRect(90, 100, 113, 20))
        self.edit3.setObjectName("edit3")
        self.edit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit4.setGeometry(QtCore.QRect(90, 130, 113, 20))
        self.edit4.setObjectName("edit4")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "edit1"))
        self.checkBox_2.setText(_translate("MainWindow", "edit2"))
        self.checkBox_3.setText(_translate("MainWindow", "edit3"))
        self.checkBox_4.setText(_translate("MainWindow", "edit4"))
        self.edit1.setText(_translate("MainWindow", "Поле edit1"))
        self.edit2.setText(_translate("MainWindow", "Поле edit2"))
        self.edit3.setText(_translate("MainWindow", "Поле edit3"))
        self.edit4.setText(_translate("MainWindow", "Поле edit4"))
        # self.edit3.setEnabled(False)


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkBox.stateChanged.connect(self.hide_box)
        self.checkBox_2.stateChanged.connect(self.hide_box)
        self.checkBox_3.stateChanged.connect(self.hide_box)
        self.checkBox_4.stateChanged.connect(self.hide_box)

    def hide_box(self, state):
        if state == 0:
            name = self.sender().text()
            # self.name.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
