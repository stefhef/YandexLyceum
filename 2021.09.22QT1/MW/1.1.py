import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setStyleSheet("QWidget {\n"
                                 "    color: white;\n"
                                 "   background-color: #121212;\n"
                                 "    font-family: Rubik;\n"
                                 "    font-size: 16pt;\n"
                                 "    font-weight: 600;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "    background-color: transparent;\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"    
                                 "    background-color: #666;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #888;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel {\n"
                                 "    color: #888;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdir {\n"
                                 "    font-size: 40pt;\n"
                                 "    border: none;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_temp = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_temp.setObjectName("lbl_temp")
        self.verticalLayout.addWidget(self.lbl_temp)
        self.le_entry = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy)
        self.le_entry.setStyleSheet("font-size: 40pt;\n"
                                    "border: none;")
        self.le_entry.setMaxLength(12)
        self.le_entry.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.le_entry.setReadOnly(True)
        self.le_entry.setObjectName("le_entry")
        self.verticalLayout.addWidget(self.le_entry)
        self.layout_buttons = QtWidgets.QGridLayout()
        self.layout_buttons.setObjectName("layout_buttons")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setObjectName("btn_2")
        self.layout_buttons.addWidget(self.btn_2, 2, 0, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setObjectName("btn_clear")
        self.layout_buttons.addWidget(self.btn_clear, 3, 0, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setObjectName("btn_7")
        self.layout_buttons.addWidget(self.btn_7, 2, 2, 1, 1)
        self.btn_mul_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mul_2.sizePolicy().hasHeightForWidth())
        self.btn_mul_2.setSizePolicy(sizePolicy)
        self.btn_mul_2.setObjectName("btn_mul_2")
        self.layout_buttons.addWidget(self.btn_mul_2, 2, 4, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setObjectName("btn_plus")
        self.layout_buttons.addWidget(self.btn_plus, 3, 4, 1, 1)
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy)
        self.btn_mul.setObjectName("btn_mul")
        self.layout_buttons.addWidget(self.btn_mul, 1, 4, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)
        self.btn_div.setObjectName("btn_div")
        self.layout_buttons.addWidget(self.btn_div, 0, 4, 1, 1)
        self.btn_neg = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_neg.sizePolicy().hasHeightForWidth())
        self.btn_neg.setSizePolicy(sizePolicy)
        self.btn_neg.setObjectName("btn_neg")
        self.layout_buttons.addWidget(self.btn_neg, 4, 2, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setObjectName("btn_9")
        self.layout_buttons.addWidget(self.btn_9, 0, 3, 1, 1)
        self.btn_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy)
        self.btn_point.setObjectName("btn_point")
        self.layout_buttons.addWidget(self.btn_point, 4, 0, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setObjectName("btn_1")
        self.layout_buttons.addWidget(self.btn_1, 3, 2, 1, 1)
        self.btn_sub = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy)
        self.btn_sub.setObjectName("btn_sub")
        self.layout_buttons.addWidget(self.btn_sub, 4, 3, 1, 2)
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setObjectName("btn_4")
        self.layout_buttons.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setObjectName("btn_6")
        self.layout_buttons.addWidget(self.btn_6, 1, 3, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setObjectName("btn_5")
        self.layout_buttons.addWidget(self.btn_5, 1, 2, 1, 1)
        self.btn_ce = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ce.sizePolicy().hasHeightForWidth())
        self.btn_ce.setSizePolicy(sizePolicy)
        self.btn_ce.setObjectName("btn_ce")
        self.layout_buttons.addWidget(self.btn_ce, 3, 3, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setObjectName("btn_0")
        self.layout_buttons.addWidget(self.btn_0, 0, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setObjectName("btn_8")
        self.layout_buttons.addWidget(self.btn_8, 0, 0, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setObjectName("btn_3")
        self.layout_buttons.addWidget(self.btn_3, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.layout_buttons)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????????"))
        self.lbl_temp.setText(_translate("MainWindow", ""))
        self.le_entry.setText(_translate("MainWindow", "0"))
        self.btn_2.setText(_translate("MainWindow", "1"))
        self.btn_2.setShortcut(_translate("MainWindow", "1"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_7.setText(_translate("MainWindow", "2"))
        self.btn_7.setShortcut(_translate("MainWindow", "2"))
        self.btn_mul_2.setText(_translate("MainWindow", "-"))
        self.btn_mul_2.setShortcut(_translate("MainWindow", "-"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_plus.setShortcut(_translate("MainWindow", "+"))
        self.btn_mul.setText(_translate("MainWindow", "*"))
        self.btn_mul.setShortcut(_translate("MainWindow", "*"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_div.setShortcut(_translate("MainWindow", "/"))
        self.btn_neg.setText(_translate("MainWindow", "+/-"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_9.setShortcut(_translate("MainWindow", "9"))
        self.btn_point.setText(_translate("MainWindow", "."))
        self.btn_point.setShortcut(_translate("MainWindow", "."))
        self.btn_1.setText(_translate("MainWindow", "0"))
        self.btn_1.setShortcut(_translate("MainWindow", "0"))
        self.btn_sub.setText(_translate("MainWindow", "="))
        self.btn_sub.setShortcut(_translate("MainWindow", "="))
        self.btn_sub.setShortcut(_translate("MainWindow", "Enter"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_4.setShortcut(_translate("MainWindow", "4"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_6.setShortcut(_translate("MainWindow", "6"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_5.setShortcut(_translate("MainWindow", "5"))
        self.btn_ce.setText(_translate("MainWindow", "CE"))
        self.btn_0.setText(_translate("MainWindow", "8"))
        self.btn_0.setShortcut(_translate("MainWindow", "8"))
        self.btn_8.setText(_translate("MainWindow", "7"))
        self.btn_8.setShortcut(_translate("MainWindow", "7"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_3.setShortcut(_translate("MainWindow", "3"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):

    flag = False
    comma = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_0.clicked.connect(self.add_number)
        self.btn_1.clicked.connect(self.add_number)
        self.btn_2.clicked.connect(self.add_number)
        self.btn_3.clicked.connect(self.add_number)
        self.btn_4.clicked.connect(self.add_number)
        self.btn_5.clicked.connect(self.add_number)
        self.btn_6.clicked.connect(self.add_number)
        self.btn_7.clicked.connect(self.add_number)
        self.btn_8.clicked.connect(self.add_number)
        self.btn_9.clicked.connect(self.add_number)
        self.btn_point.clicked.connect(self.add_number)

        self.btn_neg.clicked.connect(self.change_sign)

        self.btn_ce.clicked.connect(self.all_clear)
        self.btn_clear.clicked.connect(self.clear)

        self.btn_plus.clicked.connect(self.action)
        self.btn_div.clicked.connect(self.action)
        self.btn_mul.clicked.connect(self.action)
        self.btn_mul_2.clicked.connect(self.action)

        self.btn_sub.clicked.connect(self.equal)

    def add_number(self):
        text = self.le_entry.text()
        s_text = self.sender().text()
        if self.flag:
            self.le_entry.setText('')
            self.flag = False
        if self.comma and s_text == '.':
            return
        elif s_text == '.':
            self.comma = True

        if len(text) == 1 and text == '0' and s_text != '.':
            self.le_entry.setText('')
        self.le_entry.setText(self.le_entry.text() + self.sender().text())

    def clear(self):
        self.le_entry.setText('0')

    def all_clear(self):
        self.lbl_temp.setText('')
        self.clear()

    def change_sign(self):
        tx = self.le_entry.text()
        tx = tx[1:] if tx.startswith('-') else '-' + tx
        self.le_entry.setText(str(tx))

    def action(self):
        zn = self.sender().text()
        self.lbl_temp.setText(self.le_entry.text() + zn)
        self.flag = True

    def equal(self):
        try:
            self.le_entry.setText(str(eval(self.lbl_temp.text() + self.le_entry.text())))
            self.lbl_temp.setText('')
        except ZeroDivisionError:
            self.all_clear()
            self.le_entry.setText('Error')


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
