import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(623, 349)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(50, 240, 57, 15))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 220, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(52, 89, 87, 105))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1)
        self.radioButton1_1 = QtWidgets.QRadioButton(self.widget)
        self.radioButton1_1.setChecked(True)
        self.radioButton1_1.setObjectName("radioButton1_1")
        self.verticalLayout.addWidget(self.radioButton1_1)
        self.radioButton1_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton1_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton1_2)
        self.radioButton1_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton1_3.setObjectName("radioButton1_3")
        self.verticalLayout.addWidget(self.radioButton1_3)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(287, 89, 87, 105))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.verticalLayout_2.addWidget(self.label2)
        self.radioButton2_1 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton2_1.setChecked(True)
        self.radioButton2_1.setObjectName("radioButton2_1")
        self.verticalLayout_2.addWidget(self.radioButton2_1)
        self.radioButton2_2 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton2_2.setObjectName("radioButton2_2")
        self.verticalLayout_2.addWidget(self.radioButton2_2)
        self.radioButton2_3 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton2_3.setObjectName("radioButton2_3")
        self.verticalLayout_2.addWidget(self.radioButton2_3)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(522, 89, 87, 105))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label3 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.verticalLayout_3.addWidget(self.label3)
        self.radioButton3_1 = QtWidgets.QRadioButton(self.widget2)
        self.radioButton3_1.setChecked(True)
        self.radioButton3_1.setObjectName("radioButton3_1")
        self.verticalLayout_3.addWidget(self.radioButton3_1)
        self.radioButton3_2 = QtWidgets.QRadioButton(self.widget2)
        self.radioButton3_2.setObjectName("radioButton3_2")
        self.verticalLayout_3.addWidget(self.radioButton3_2)
        self.radioButton3_3 = QtWidgets.QRadioButton(self.widget2)
        self.radioButton3_3.setObjectName("radioButton3_3")
        self.verticalLayout_3.addWidget(self.radioButton3_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 20))
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
        self.pushButton.setText(_translate("MainWindow", "Сделать флаг"))
        self.label1.setText(_translate("MainWindow", "Цвет №1"))
        self.radioButton1_1.setText(_translate("MainWindow", "Синий"))
        self.radioButton1_2.setText(_translate("MainWindow", "Красный"))
        self.radioButton1_3.setText(_translate("MainWindow", "Зелёный"))
        self.label2.setText(_translate("MainWindow", "Цвет №2"))
        self.radioButton2_1.setText(_translate("MainWindow", "Синий"))
        self.radioButton2_2.setText(_translate("MainWindow", "Красный"))
        self.radioButton2_3.setText(_translate("MainWindow", "Зелёный"))
        self.label3.setText(_translate("MainWindow", "Цвет №3"))
        self.radioButton3_1.setText(_translate("MainWindow", "Синий"))
        self.radioButton3_2.setText(_translate("MainWindow", "Красный"))
        self.radioButton3_3.setText(_translate("MainWindow", "Зелёный"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.inintUi()

    def inintUi(self):
        self.label_4.resize(300, 20)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        btn1 = filter(lambda x: x.isChecked(), [getattr(self, f"radioButton1_{i}") for i in range(1, 4)]).__next__()
        btn2 = filter(lambda x: x.isChecked(), [getattr(self, f"radioButton2_{i}") for i in range(1, 4)]).__next__()
        btn3 = filter(lambda x: x.isChecked(), [getattr(self, f"radioButton3_{i}") for i in range(1, 4)]).__next__()
        self.label_4.setText(f'Цвета: {btn1.text()}, {btn2.text()} и {btn3.text()}')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
    