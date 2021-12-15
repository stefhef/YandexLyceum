import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor, QPainterPath, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.cars = ["car2.png", "car3.png", "car4.png"]
        self.current = "car2.png"
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Машинка')
        self.pixmap = QPixmap("cars/" + self.current)
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.show()
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        size = self.pixmap.size()
        width = size.width()
        height = size.height()
        self.lbl.move(event.x() - width // 2, event.y() - height // 2)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            cars = list(self.cars)
            cars.remove(self.current)
            self.current = random.choice(cars)
            self.pixmap.load("cars/" + self.current)
            self.lbl.setPixmap(self.pixmap)
            self.pixmap.size()


sys.__excepthook__ = sys.__excepthook__


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
