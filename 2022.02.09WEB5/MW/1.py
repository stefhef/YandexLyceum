import sys
from ui import Ui_MainWindow
from PyQt5 import QtWidgets


class Example(QtWidgets.QMainWindow, Ui_MainWindow):

    cities = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)


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
