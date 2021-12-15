import sys
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from collections import defaultdict
from math import inf


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("Узнать результаты")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Результат олимпиады: фильтрация"))
        self.pushButton.setText(_translate("MainWindow", "Узнать результаты"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Результат"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Логин"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_2.insertItem(0, 'все')
        self.comboBox.insertItem(0, 'все')
        self.get_table()
        self.pushButton.clicked.connect(self.write_table)

    def get_table(self):
        self.students = defaultdict(list)
        self.classes, self.schools = list(), list()
        schools_numbers = set()
        classes_numbers = set()
        with open('rez.csv', 'r', encoding='utf-8') as csvfile:
            table = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(table)
            for row in table:
                login = row[2].split('-')
                sc_n, cl_n = login[-3], login[-2]
                schools_numbers.add(sc_n)
                classes_numbers.add(cl_n)
                self.students[(sc_n, cl_n)].append((row[1].split()[3], row[-1], row[1]))
        self.schools_numbers = sorted(tuple(schools_numbers), key=lambda x: int(x))
        self.classes_numbers = sorted(tuple(classes_numbers), key=lambda x: int(x))
        for index, clas in enumerate(sorted(self.classes_numbers, key=lambda x: int(x)), 1):
            self.comboBox_2.insertItem(index, clas)
        for index, school in enumerate(sorted(self.schools_numbers, key=lambda x: int(x)), 1):
            self.comboBox.insertItem(index, school)

    def write_table(self):
        school_number = list()
        school_number.append(self.comboBox.currentText())
        class_number = list()
        class_number.append(self.comboBox_2.currentText())
        if 'все' in school_number:
            school_number = self.schools_numbers
        if 'все' in class_number:
            class_number = self.classes_numbers
        out = []

        for sc_n in school_number:
            for cl_n in class_number:
                if (sc_n, cl_n) in self.students:
                    out.extend(self.students[(sc_n, cl_n)])
        self.write(sorted(out, key=lambda x: int(x[1]), reverse=True))

    def write(self, lst):

        for i, student in enumerate(lst):
            self.tableWidget.setRowCount(len(lst))
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(i))
            for j, elem in enumerate(student):
                item = QtWidgets.QTableWidgetItem(elem)
                self.tableWidget.setItem(i, j, item)

        lst.clear()
        self.color_place()

    def color_place(self):
        color = (QtGui.QColor('Yellow'), QtGui.QColor('Grey'), QtGui.QColor(102, 51, 0), QtGui.QColor('White'))
        count = -1
        best = inf
        for j in range(self.tableWidget.rowCount()):
            elem = self.tableWidget.item(j, 1)
            elem = int(elem.text())
            if count == 3:
                break
            if elem < best:
                best = elem
                count += 1
            self.color_row(j, color[count])

    def color_row(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)


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
