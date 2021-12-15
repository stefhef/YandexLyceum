import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setProperty("value", 50)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout.addWidget(self.verticalSlider)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 22))
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


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pixmap = QtGui.QPixmap(451, 451)
        self.pixmap.fill(QtCore.Qt.transparent)
        self.draw = True
        self.verticalSlider.setMinimum(1)
        self.verticalSlider.setMaximum(600)
        self.verticalSlider.setValue(450)
        self.verticalSlider.valueChanged.connect(self.change_size)

    def change_size(self):
        value = self.verticalSlider.value()
        self.pixmap = self.pixmap.scaled(value, value)
        self.label.setPixmap(self.pixmap)

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter(self.pixmap)
            self.draw_smile(qp)
            qp.end()
            self.label.setPixmap(self.pixmap)
            self.draw = False

    def draw_smile(self, qp):
        qp.setPen(QColor(255, 0, 0))
        qp.drawEllipse(1, 1, 450, 450)
        qp.drawEllipse(125, 151, 75, 75)
        qp.drawEllipse(275, 151, 75, 75)
        qp.drawArc(125, 300, 225, 50, 0, -180*16)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())