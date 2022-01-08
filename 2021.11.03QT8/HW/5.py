import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import date


class Dialog(QtWidgets.QWidget):

    def __init__(self, con, window):
        super(Dialog, self).__init__()
        self.con = con
        self.window = window
        self.initUI()

    def initUI(self):
        self.resize(300, 100)
        self.setWindowTitle('Добавить элемент')

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QLineEdit(self)
        self.title.setMinimumSize(QtCore.QSize(0, 30))
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.year = QtWidgets.QLineEdit(self)
        self.year.setMinimumSize(QtCore.QSize(0, 30))
        self.year.setObjectName("year")
        self.verticalLayout_2.addWidget(self.year)
        self.genre = QtWidgets.QComboBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genre.sizePolicy().hasHeightForWidth())
        self.genre.setSizePolicy(sizePolicy)
        self.genre.setMinimumSize(QtCore.QSize(0, 30))
        self.genre.setObjectName("genre")
        self.verticalLayout_2.addWidget(self.genre)
        self.lenght = QtWidgets.QLineEdit(self)
        self.lenght.setMinimumSize(QtCore.QSize(0, 30))
        self.lenght.setObjectName("lenght")
        self.verticalLayout_2.addWidget(self.lenght)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.error = QtWidgets.QLabel(self)
        self.error.setObjectName("error")
        self.horizontalLayout_2.addWidget(self.error)
        self.add_button = QtWidgets.QPushButton(self)
        self.add_button.setMinimumSize(QtCore.QSize(50, 40))
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_2.addWidget(self.add_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label_2.setText("Название")
        self.label_5.setText("Год выпуска")
        self.label_4.setText("Жанр")
        self.label_3.setText("Длина")
        self.error.setText("")
        self.add_button.setText("Добавить")

        cur = self.con.cursor()
        query = f"""SELECT title FROM genres"""
        for elem in cur.execute(query).fetchall():
            self.genre.addItem(elem[0])

        self.add_button.clicked.connect(self.close_)

    def close_(self):
        title = self.title.text()
        genre = self.genre.currentText()
        year = self.year.text()
        lenght = self.lenght.text()
        try:
            if not all((title, genre, year, lenght)) or int(year) > date.today().year or int(lenght) < 0:
                self.error.setText('Неверно заполнена форма')
            else:
                cur = self.con.cursor()
                q = f"""SELECT id FROM genres WHERE title='{genre}'"""
                genre = cur.execute(q).fetchone()
                query = f"""INSERT INTO films (title, year, genre, duration) VALUES ('{title}', {year}, '{genre[0]}', {lenght})"""

                cur.execute(query)
                self.con.commit()
                self.window.write_table()
                self.close()
        except TypeError:
            self.error.setText('Неверно заполнена форма')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Добавить"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        with sqlite3.connect('films_db.sqlite') as con:
            self.con = con
        self.write_table()
        self.pushButton.clicked.connect(self.dialog)

    def write_table(self):
        cur = self.con.cursor()
        query = f"""SELECT films.id, films.title, films.year, genres.title, films.duration
        FROM films INNER JOIN genres on genres.id = films.genre"""
        data = cur.execute(query).fetchall()

        if not data:
            return
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        headers = ('ИД', 'Название фильма', 'Год выпуска', 'Жанр', 'Продолжительность')
        self.tableWidget.setColumnCount(5)
        for i in range(5):
            self.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(str(headers[i])))
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(elem)))

    def dialog(self):
        self.d = Dialog(self.con, self)
        self.d.show()


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
