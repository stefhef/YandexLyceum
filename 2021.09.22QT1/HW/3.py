import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 485)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioO = QtWidgets.QRadioButton(self.centralwidget)
        self.radioO.setGeometry(QtCore.QRect(240, 40, 31, 21))
        self.radioO.setObjectName("radioO")
        self.radioX = QtWidgets.QRadioButton(self.centralwidget)
        self.radioX.setGeometry(QtCore.QRect(150, 40, 31, 21))
        self.radioX.setObjectName("radioX")
        self.ButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonStart.setGeometry(QtCore.QRect(150, 380, 111, 31))
        self.ButtonStart.setObjectName("ButtonStart")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Крестики-нолики"))
        self.radioO.setText(_translate("MainWindow", "O"))
        self.radioX.setText(_translate("MainWindow", "X"))
        self.ButtonStart.setText(_translate("MainWindow", "Новая игра"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.buttons = []
        self.player = ''

        super().__init__()
        self.setupUi(self)

        self.radioO.clicked.connect(self.set_0)
        self.radioX.clicked.connect(self.set_x)
        self.radioO.click()

        self.ButtonStart.clicked.connect(self.press)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.move(150, 350)
        self.label.resize(200, 20)

        self.buttons = []
        self.start()

    def press(self):
        for i in range(9):
            self.buttons[i].setEnabled(True)
            self.buttons[i].setText('')
        self.player = 'X' if self.radioX.isChecked() else 'O'

    def start(self):
        x, y = 60, 70  # y step = 90, x step = 100
        for i in range(9):
            button = QtWidgets.QPushButton(self.centralwidget)
            self.buttons.append(button)
            button.setObjectName(str(i))
            button.setGeometry(QtCore.QRect(x, y, 90, 80))
            button.clicked.connect(self.step)

            if x == 260:
                x = 60
                y += 90
            else:
                x += 100

    def step(self):
        if not self.sender().text():
            self.sender().setText(self.player)
            self.set_0() if self.player == 'X' else self.set_x()
            winner = self.check_winner()
            if winner or not self.check_enabled():
                self.finished(winner)

    def check_enabled(self):
        for i in range(9):
            if not self.buttons[i].text():
                return True
        return False

    def set_0(self):
        self.player = '0'

    def set_x(self):
        self.player = 'X'

    def check_winner(self):
        win_pos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for pos in win_pos:
            if self.buttons[pos[0]].text() == self.buttons[pos[1]].text() == self.buttons[pos[2]].text() == "0":
                return 'o'
            if self.buttons[pos[0]].text() == self.buttons[pos[1]].text() == self.buttons[pos[2]].text() == "X":
                return 1

    def finished(self, winner):
        for i in range(9):
            self.buttons[i].setEnabled(False)
        if winner == 'o':
            self.label.setText("игрок 0 выиграл")
        elif winner == 1:
            self.label.setText("игрок X выиграл")
        else:
            self.label.setText("ничья")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
