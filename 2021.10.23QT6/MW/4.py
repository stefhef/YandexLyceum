import sys
import csv
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Поиск на Титанике"))
        self.label.setText(_translate("MainWindow", "Подстрока для поиска:"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_table()
        self.lineEdit.textChanged.connect(self.search)

    def get_table(self):
        with open('titanic.csv', encoding='utf-8') as csvfile:
            tabel = csv.reader(csvfile, delimiter=',', quotechar='"')
            title = next(tabel)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(tabel):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(elem))
            self.tableWidget.resizeColumnsToContents()
            self.paint()

    def paint(self):
        for i in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(i, 5)
            if self.tableWidget.item(i, 5).text() == '0':
                self.color_row(i, QtGui.QColor('red'))
            else:
                self.color_row(i, QtGui.QColor('green'))

    def color_row(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)

    def search(self):
        text = self.lineEdit.text()
        if len(text) >= 3:
            with open('titanic.csv', encoding='utf-8') as csvfile:
                tabel = csv.reader(csvfile, delimiter=',', quotechar='"')
                title = next(tabel)
                self.tableWidget.setColumnCount(len(title))
                self.tableWidget.setHorizontalHeaderLabels(title)
                self.tableWidget.setRowCount(0)
                for i, row in enumerate(tabel):
                    self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                    for j, elem in enumerate(row):
                        if j == 1:
                            text: str
                            elem: str
                            if text .lower() in elem.lower():
                                self.tableWidget.setItem(i - coef, j, QtWidgets.QTableWidgetItem(elem))
                            else:
                                self.tableWidget.removeRow(i - coef)
                                break
                        else:
                            self.tableWidget.setItem(i - coef, j, QtWidgets.QTableWidgetItem(elem))

                self.tableWidget.resizeColumnsToContents()
                self.paint()
        else:
            self.get_table()


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
