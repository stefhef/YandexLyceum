import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')
        self.cords = tuple()
        self.flag = False
        self.status = 0
        self.setMouseTracking(True)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event) -> None:
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.qp.setBrush(color)
            self.draw(self.status)
            self.qp.end()

    def draw(self, status):
        x, y = self.cords
        random_int = random.randint(20, 100)
        if status == 1:
            x, y = x - random_int // 2, y - random_int // 2
            self.qp.drawEllipse(x, y, random_int, random_int)
        elif status == 2:
            x, y = x - random_int // 2, y - random_int // 2
            self.qp.drawRect(x, y, random_int, random_int)
        elif status == 3:
            r = random.randint(10, 50)
            a = random.randint(10, 50)
            coords = [(x, y + r), (x + a, y - r), (x - a, y - r)]
            path = QPainterPath()
            path.moveTo(*coords[0])
            path.lineTo(*coords[1])
            path.lineTo(*coords[2])
            path.lineTo(*coords[0])
            self.qp.drawPath(path)

    def mouseMoveEvent(self, event) -> None:
        self.cords = (event.x(), event.y())

    def mousePressEvent(self, event) -> None:
        self.cords = (event.x(), event.y())
        if event.button() == Qt.LeftButton:
            self.status = 1
        elif event.button() == Qt.RightButton:
            self.status = 2
        self.drawf()

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key_Space:
            self.status = 3
        self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
