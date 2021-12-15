from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 451, 351))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.maximum = QtWidgets.QSpinBox(self.widget)
        self.maximum.setObjectName("maximum")
        self.horizontalLayout_2.addWidget(self.maximum)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.minimum = QtWidgets.QSpinBox(self.widget)
        self.minimum.setObjectName("minimum")
        self.horizontalLayout_3.addWidget(self.minimum)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.average = QtWidgets.QSpinBox(self.widget)
        self.average.setObjectName("average")
        self.horizontalLayout_4.addWidget(self.average)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.error = QtWidgets.QLabel(self.widget)
        self.error.setObjectName("error")
        self.verticalLayout.addWidget(self.error)
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
        self.label.setText(_translate("MainWindow", "Имя файла"))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
        self.label_3.setText(_translate("MainWindow", "Максимальное значение:"))
        self.label_4.setText(_translate("MainWindow", "Минимальное значение:"))
        self.label_5.setText(_translate("MainWindow", "Среднее значение"))
        self.error.setText(_translate("MainWindow", "Состояние: ожидание файла"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.push)

    def push(self):
        file_name = self.lineEdit.text()
        try:
            with open(file_name, 'r') as input_file:
                data = list(map(int, input_file.read().split()))
                min_val = min(data)
                max_val = max(data)
                aver_val = sum(data) / len(data)
                self.minimum.setText(str(min_val))
                self.maximum.setText(str(max_val))
                self.average.setText(str(aver_val))
        except (TypeError, ValueError):
            self.error.setText(f'Файл {file_name} содержит неверные данные')
            return
        except FileNotFoundError:
            self.error.setText(f'Файл {file_name} не найден')
            return
        self.error.setText(f'состояние: ОК, сохранен в file_output')
        with open('output.txt', 'w', encoding="utf-8") as output_file:
            print(f'Минимальное значение:{min_val}', file=output_file)
            print(f'Максимальное значение: {max_val}', file=output_file)
            print(f'Среднее значение: {aver_val}', file=output_file)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
    