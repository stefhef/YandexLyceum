from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys
from PIL import Image
from PIL.ImageQt import ImageQt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.R = QtWidgets.QPushButton(self.centralwidget)
        self.R.setObjectName("R")
        self.verticalLayout.addWidget(self.R)
        self.G = QtWidgets.QPushButton(self.centralwidget)
        self.G.setObjectName("G")
        self.verticalLayout.addWidget(self.G)
        self.B = QtWidgets.QPushButton(self.centralwidget)
        self.B.setObjectName("B")
        self.verticalLayout.addWidget(self.B)
        self.all = QtWidgets.QPushButton(self.centralwidget)
        self.all.setObjectName("all")
        self.verticalLayout.addWidget(self.all)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setText("")
        self.picture.setObjectName("picture")
        self.horizontalLayout_2.addWidget(self.picture)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hour = QtWidgets.QPushButton(self.centralwidget)
        self.hour.setObjectName("hour")
        self.horizontalLayout.addWidget(self.hour)
        self.reversehour = QtWidgets.QPushButton(self.centralwidget)
        self.reversehour.setObjectName("reversehour")
        self.horizontalLayout.addWidget(self.reversehour)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 22))
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
        self.R.setText(_translate("MainWindow", "R"))
        self.G.setText(_translate("MainWindow", "G"))
        self.B.setText(_translate("MainWindow", "B"))
        self.all.setText(_translate("MainWindow", "ALL"))
        self.hour.setText(_translate("MainWindow", "Против часовой стрелки"))
        self.reversehour.setText(_translate("MainWindow", "По часововй стрелке"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.degree = 0
        super().__init__()
        self.setupUi(self)
        self.initui()

    def initui(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.original_photo = Image.open(self.filename)
        self.currnet_image = Image.open(self.filename)
        self.qt_image = ImageQt(self.currnet_image)
        self.pixmap = QPixmap.fromImage(self.qt_image)
        self.picture.setPixmap(self.pixmap)
        self.B.clicked.connect(self.set_channel)
        self.G.clicked.connect(self.set_channel)
        self.R.clicked.connect(self.set_channel)
        self.all.clicked.connect(self.set_channel)
        self.hour.clicked.connect(self.rotate)
        self.reversehour.clicked.connect(self.rotate)

    def set_channel(self):
        self.currnet_image = self.original_photo.copy()
        pixels = self.currnet_image.load()
        x, y = self.currnet_image.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if self.sender().text() == 'R':
                    pixels[i, j] = r, 0, 0
                elif self.sender().text() == 'G':
                    pixels[i, j] = 0, g, 0
                elif self.sender().text() == 'B':
                    pixels[i, j] = 0, 0, b
                else:
                    continue
        self.currnet_image = self.currnet_image.rotate(self.degree, expand=True)
        self.qt_image = ImageQt(self.currnet_image)
        self.pixmap = QPixmap.fromImage(self.qt_image)
        self.picture.setPixmap(self.pixmap)

    def rotate(self):
        if self.sender() is self.hour:
            self.degree -= 90
            degree = -90
        else:
            self.degree -= 90
            degree = 90

        self.degree %= 360
        self.currnet_image = self.currnet_image.rotate(degree, expand=True)
        self.qt_image = ImageQt(self.currnet_image)
        self.pixmap = QPixmap.fromImage(self.qt_image)
        self.picture.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())