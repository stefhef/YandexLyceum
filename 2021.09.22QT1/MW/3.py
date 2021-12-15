import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(404, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 170, 371, 381))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 102, 131))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(110, 0, 31, 131))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 404, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Заказать"))
        self.checkBox.setText(_translate("MainWindow", "Чизбургер"))
        self.checkBox_2.setText(_translate("MainWindow", "Гамбургер"))
        self.checkBox_3.setText(_translate("MainWindow", "Кока-кола"))
        self.checkBox_4.setText(_translate("MainWindow", "Нагетсы"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    price = {1: ('Чизбургер', 100),
             2: ('Гамбургер', 20),
             3: ('Кока-кола', 40),
             4: ('Нагетсы', 300)}

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.lineEdit.setText('0')
        self.lineEdit_2.setText('0')
        self.lineEdit_3.setText('0')
        self.lineEdit_4.setText('0')
        self.checkBox.stateChanged.connect(self.cheese)
        self.checkBox_2.stateChanged.connect(self.gam)
        self.checkBox_3.stateChanged.connect(self.coca)
        self.checkBox_4.stateChanged.connect(self.nag)
        self.pushButton.clicked.connect(self.order)

    def nag(self, state):
        if state == QtCore.Qt.Checked:
            self.lineEdit_4.setEnabled(True)
            self.lineEdit_4.setText('1')
        else:
            self.lineEdit_4.setEnabled(False)
            self.lineEdit_4.setText('0')

    def coca(self, state):
        if state == QtCore.Qt.Checked:
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_3.setText('1')
        else:
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_3.setText('0')

    def cheese(self, state):
        if state == QtCore.Qt.Checked:
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_2.setText('1')
        else:
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_2.setText('0')

    def gam(self, state):
        if state == QtCore.Qt.Checked:
            self.lineEdit.setEnabled(True)
            self.lineEdit.setText('1')
        else:
            self.lineEdit.setEnabled(False)
            self.lineEdit.setText('0')

    def order(self):
        price_total = 0
        text = "Ваш заказ\n\n"
        for number, child in enumerate(self.findChildren(QtWidgets.QLineEdit), 1):
            if child.text().isalnum() and child.isEnabled():
                name, price = self.price[number]
                price = int(child.text()) * price
                st = f'{name}-----{child.text()}-----{price}'
                text += st + '\n'
                price_total += price
        text += '\n'
        text += f'Итого: {price_total}'
        self.lineEdit_5.setText(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
