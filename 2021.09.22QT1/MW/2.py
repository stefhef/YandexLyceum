from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 291)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 341, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 60, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 60, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(180, 110, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(180, 160, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 111, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 111, 21))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
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
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.label_2.setText(_translate("MainWindow", "Осталось ходов"))
        self.label_3.setText(_translate("MainWindow", "Текущее число"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.f = False
        super().__init__()
        self.setupUi(self)
        self.start()
        for item in self.findChildren(QtWidgets.QPushButton):
            item.clicked.connect(self.step)

    def step(self):
        if self.f:
            self.start()
            self.f = False
        else:
            num = self.lcdNumber_2.value()
            num2 = num + int(self.sender().text())
            self.lcdNumber_2.display(num2)
            self.lcdNumber.display(self.lcdNumber.value() - 1)
            self.check()

    def start(self):
        number1, number2, number3 = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
        self.pushButton.setText(number1.__str__())
        self.pushButton_2.setText('-' + number2.__str__())
        self.lcdNumber_2.display(number3)
        self.lcdNumber.display(10)
        self.label.setText('')

    def check(self):
        if self.lcdNumber_2.value() == 0 or self.lcdNumber.value() == 0:
            if self.lcdNumber_2.value() == 0:
                self.label.setText("Вы победили, начинаем новую игру")
            else:
                self.label.setText("Вы проиграли, начинаем новую игру")
            self.f = True


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

