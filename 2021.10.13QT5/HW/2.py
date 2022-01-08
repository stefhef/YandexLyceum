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
        self.pixmap = QtGui.QPixmap(600, 600)

        self.verticalSlider.setMinimum(1)
        self.verticalSlider.setMaximum(700)
        self.verticalSlider.setValue(450)
        self.verticalSlider.valueChanged.connect(self.update)
        self.pixmap.fill(QtCore.Qt.transparent)

    def paintEvent(self, event):
        qp = QPainter(self)
        val = self.verticalSlider.value()
        qp.setPen(QColor(255, 0, 0))
        qp.drawEllipse(1, 1, val, val)
        qp.drawEllipse(round(0.3125 * val),
                       round(0.3 * val),
                       round(0.17 * val),
                       round(0.17 * val))

        qp.drawEllipse(round(0.61 * val),
                       round(0.3 * val),
                       round(0.17 * val),
                       round(0.17 * val))

        qp.drawArc(round(0.3125 * val),
                   round(0.67 * val),
                   round(0.5 * val),
                   round(0.1 * val),
                   0, -180 * 16)
        qp.end()
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
