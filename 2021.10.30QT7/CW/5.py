from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(507, 396)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_input = QtWidgets.QLineEdit(self.centralwidget)
        self.user_input.setGeometry(QtCore.QRect(210, 20, 181, 23))
        self.user_input.setObjectName("user_input")
        self.condition = QtWidgets.QComboBox(self.centralwidget)
        self.condition.setGeometry(QtCore.QRect(20, 20, 181, 23))
        self.condition.setObjectName("condition")
        self.condition.addItem("")
        self.condition.addItem("")
        self.condition.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 20, 80, 23))
        self.pushButton.setObjectName("pushButton")
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(20, 340, 461, 21))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 50, 461, 281))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_id = QtWidgets.QLabel(self.widget)
        self.label_id.setObjectName("label_id")
        self.verticalLayout.addWidget(self.label_id)
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name)
        self.label_year = QtWidgets.QLabel(self.widget)
        self.label_year.setObjectName("label_year")
        self.verticalLayout.addWidget(self.label_year)
        self.label_genre = QtWidgets.QLabel(self.widget)
        self.label_genre.setObjectName("label_genre")
        self.verticalLayout.addWidget(self.label_genre)
        self.label_duration = QtWidgets.QLabel(self.widget)
        self.label_duration.setObjectName("label_duration")
        self.verticalLayout.addWidget(self.label_duration)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.id_output = QtWidgets.QLineEdit(self.widget)
        self.id_output.setObjectName("id_output")
        self.verticalLayout_2.addWidget(self.id_output)
        self.name_output = QtWidgets.QLineEdit(self.widget)
        self.name_output.setObjectName("name_output")
        self.verticalLayout_2.addWidget(self.name_output)
        self.year_output = QtWidgets.QLineEdit(self.widget)
        self.year_output.setObjectName("year_output")
        self.verticalLayout_2.addWidget(self.year_output)
        self.genre_output = QtWidgets.QLineEdit(self.widget)
        self.genre_output.setObjectName("genre_output")
        self.verticalLayout_2.addWidget(self.genre_output)
        self.duration_output = QtWidgets.QLineEdit(self.widget)
        self.duration_output.setObjectName("duration_output")
        self.verticalLayout_2.addWidget(self.duration_output)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 20))
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
        self.condition.setItemText(0, _translate("MainWindow", "Продолжительность"))
        self.condition.setItemText(1, _translate("MainWindow", "Год выпуска"))
        self.condition.setItemText(2, _translate("MainWindow", "Название"))
        self.pushButton.setText(_translate("MainWindow", "Поиск"))
        self.label_id.setText(_translate("MainWindow", "ID:"))
        self.label_name.setText(_translate("MainWindow", "Название:"))
        self.label_year.setText(_translate("MainWindow", "Год выпуска:"))
        self.label_genre.setText(_translate("MainWindow", "Жанр:"))
        self.label_duration.setText(_translate("MainWindow", "Продолжительность:"))


class Films(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.search)

    def search(self):
        try:
            condition = self.condition.currentText()
            text = self.user_input.text()
            searching = self.selection(condition)
            with sqlite3.connect('films_db.sqlite') as con:
                cur = con.cursor()
                result = cur.execute(f"""SELECT * FROM films
            WHERE {searching} LIKE {text}""").fetchall()[0]
                print(result)
                genre = cur.execute(f"""SELECT * FROM genres
            WHERE id LIKE {str(result[3])}""").fetchall()
            self.id_output.setText(str(result[0]))
            self.name_output.setText(result[1])
            self.year_output.setText(str(result[2]))
            self.genre_output.setText(genre[0][1])
            self.duration_output.setText(str(result[4]))
        except:
            if not self.user_input.text():
                self.error_label.setText('Неверный ввод')
            else:
                self.error_label.setText('Ничего не найдено')

    def selection(self, conditions):
        name, name_of_base = ['Продолжительность', 'Год выпуска', 'Название'], \
                             ['duration', 'year', 'title']
        return name_of_base[name.index(conditions)]


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = Films()
    exe.show()
    sys.exit(app.exec())