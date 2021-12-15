import sys
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 131, 25))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QListView(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 381, 381))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 419, 22))
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
        self.pushButton.setText(_translate("MainWindow", "Загрузить строки"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.past_text)

    def past_text(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать текстовик', '', 'Файл (*.txt)')[0]
        if self.filename:
            with open(self.filename, 'r') as f:
                text = f.readlines()
                text_part1 = text[1::2]
                text_part2 = text[::2]
                text = text_part1 + text_part2
                self.model = QtGui.QStandardItemModel(self)
                for method in text:
                    item = QtGui.QStandardItem(method)
                    item.setData(method)
                    self.model.appendRow(item)

                self.lineEdit.setModel(self.model)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
