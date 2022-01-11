import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QByteArray
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Каталог библиотеки"))
        self.pushButton.setText(_translate("MainWindow", "Искать"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        with sqlite3.connect('books.db') as con:
            self.con = con
        cur = self.con.cursor()
        self.comboBox.addItem('Автор')
        self.comboBox.addItem('Название')
        self.pushButton.clicked.connect(self.search)

    def search(self):
        cur = self.con.cursor()
        param = self.comboBox.currentText()
        req = self.lineEdit.text()
        if param == 'Автор':
            query = f"SELECT tile FROM boks INNER JOIN authors on boks.author=authors.id WHERE authors.author LIKE '%{req}%'"
        else:
            query = f"SELECT tile FROM boks WHERE tile LIKE '%{req}%'"
        tiles = cur.execute(query).fetchall()
        for tile in tiles:
            if type(tile) == tuple:
                tile = tile[0]
            button = QtWidgets.QPushButton(tile)
            button.clicked.connect(self.execute_dialog)
            listWidgetItem = QtWidgets.QListWidgetItem()
            listWidgetItem.setSizeHint(button.sizeHint())
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, button)
            self.listWidget.scrollToItem(listWidgetItem)

    def execute_dialog(self):
        text = self.sender().text()
        query = f"""SELECT tile, authors.author, years.year, genres.genre, photo 
        FROM boks
        INNER JOIN authors ON authors.id=boks.author 
        INNER JOIN genres ON genres.id=boks.genre
        INNER JOIN years ON years.id=boks.year
        WHERE tile='{text}'"""
        cur = self.con.cursor()
        data = cur.execute(query).fetchone()
        self.second_window = dialog(data)
        self.second_window.show()


class dialog(QtWidgets.QWidget):

    def __init__(self, data):
        super().__init__()
        self.setObjectName("Form")
        self.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.setStyleSheet('QLabel {color:black}')

        self.photo = QtWidgets.QLabel(self)
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        pixmap = QPixmap()
        if data[-1]:
            pixmap.loadFromData(QByteArray(data[-1]))

        else:
            with open('default.jpg', 'rb') as file:
                b = file.read()
                pixmap.loadFromData(QByteArray(b))
        self.photo.setPixmap(pixmap)
        self.verticalLayout.addWidget(self.photo)

        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setText("Название")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet('{font-size:300%; font:bold}')
        self.verticalLayout.addWidget(self.label_8)

        self.tile = QtWidgets.QLabel(self)
        self.tile.setText(data[0])
        self.tile.setAlignment(QtCore.Qt.AlignCenter)
        self.tile.setObjectName("tile")
        self.verticalLayout.addWidget(self.tile)

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("Автор")
        self.label_5.setStyleSheet('font-size:300%; font:bold')
        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setText(str(data[1]))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setText('Год выпуска')
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet('font-size:300%; font:bold')
        self.verticalLayout.addWidget(self.label_4)

        self.year = QtWidgets.QLabel(self)
        self.year.setAlignment(QtCore.Qt.AlignCenter)
        self.year.setObjectName("year")
        self.year.setText(str(data[2]))
        self.verticalLayout.addWidget(self.year)

        self.label = QtWidgets.QLabel(self)
        self.label.setText('Жанр')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet('font-size:300%; font:bold')
        self.verticalLayout.addWidget(self.label)

        self.genre = QtWidgets.QLabel(self)
        self.genre.setText(str(data[3]))
        self.genre.setAlignment(QtCore.Qt.AlignCenter)
        self.genre.setObjectName("genre")
        self.verticalLayout.addWidget(self.genre)


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
