import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(150, 30, 192, 91))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.side = QtWidgets.QLabel(self.widget)
        self.side.setObjectName("side")
        self.verticalLayout.addWidget(self.side)
        self.coeff = QtWidgets.QLabel(self.widget)
        self.coeff.setObjectName("coeff")
        self.verticalLayout.addWidget(self.coeff)
        self.n = QtWidgets.QLabel(self.widget)
        self.n.setObjectName("n")
        self.verticalLayout.addWidget(self.n)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_side = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_side.setObjectName("lineEdit_side")
        self.verticalLayout_2.addWidget(self.lineEdit_side)
        self.lineEdit_coeff = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_coeff.setObjectName("lineEdit_coeff")
        self.verticalLayout_2.addWidget(self.lineEdit_coeff)
        self.lineEdit_n = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_n.setObjectName("lineEdit_n")
        self.verticalLayout_2.addWidget(self.lineEdit_n)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
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
        self.pushButton.setText(_translate("MainWindow", "Показать"))
        self.side.setText(_translate("MainWindow", "Side"))
        self.coeff.setText(_translate("MainWindow", "Coeff"))
        self.n.setText(_translate("MainWindow", "n"))


SCREEN_SIZE = (600, 650)


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(*SCREEN_SIZE)
        self.initUi()

    def initUi(self):
        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.side = float(self.lineEdit_side.text())
        self.coeff = float(self.lineEdit_coeff.text())
        self.n = int(self.lineEdit_n.text())
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(250, 0, 0))
            self.x , self.y = SCREEN_SIZE[0] // 2 - self.side // 2, SCREEN_SIZE[1] // 2 - self.side // 2
            for i in range(self.n):

                qp.drawRect(self.x, self.y, self.side, self.side)
                delta = self.side * (1 - self.coeff) / 2
                self.side *= self.coeff
                self.x += delta
                self.y += delta
            qp.end()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
