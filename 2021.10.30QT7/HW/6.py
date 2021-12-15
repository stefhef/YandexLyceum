import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Алфавитный указатель"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.InitUi()
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('films_db.sqlite')
        self.db.open()

    def InitUi(self):
        count = 0
        self.view = QtWidgets.QTableView(self)
        self.view.setGeometry(0, 20, 640, 300)
        for letter in 'абвгдеёжзийклмнопрстуфхцшщьъыэюя'.upper():

            button = QtWidgets.QPushButton(letter, self)
            button.setGeometry(20 * count, 0, 20, 20)
            button.clicked.connect(self.write)
            count += 1

        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.label.setGeometry(0, 310, 640, 50)

    def write(self):

        send = self.sender().text()
        model = QSqlTableModel(self, self.db)
        model.setTable('films')
        model.setFilter(f'title LIKE "{send}%"')
        model.select()
        self.view.setModel(model)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
