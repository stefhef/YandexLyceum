import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 251, 25))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.pushButton.setText(_translate("MainWindow", "Введите количество цветов флага"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.count = 0
        self.flag = False
        self.pushButton.clicked.connect(self.showDialog)

    def showDialog(self):
        count, ok = QtWidgets.QInputDialog.getInt(self, 'Введите количество цветов флага', 'Сколько цветов?')

        if ok:
            self.count = count
            self.flag = True
            self.update()

    def paintEvent(self, event):
        if self.flag:
            # self.resize(300, self.count * 20 + 80)
            qp = QtGui.QPainter()
            qp.begin(self)
            for i in range(self.count):
                qp.setBrush(QtGui.QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
                qp.drawRect(60, 60 + 20 * i, 200, 20)
            qp.end()
            self.flag = False

sys.__excepthook__ = sys.__excepthook__


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
