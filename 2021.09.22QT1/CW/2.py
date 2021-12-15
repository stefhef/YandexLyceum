import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Третья программа')

        self.first_input = QLineEdit(self)
        self.first_input.move(10, 100)
        self.first_input.resize(100, 25)

        self.second_input = QLineEdit(self)
        self.second_input.move(155, 100)
        self.second_input.resize(100, 25)

        self.btn = QPushButton('->', self)
        self.btn.resize(25, 25)
        self.btn.move(120, 100)

        self.label1 = QLabel('Выражение:', self)
        self.label1.resize(100, 25)
        self.label1.move(10, 80)

        self.label1 = QLabel('Результат:', self)
        self.label1.resize(100, 25)
        self.label1.move(155, 80)

        self.btn.clicked.connect(self.change)

    def change(self):
        try:
            result = eval(self.first_input.text())
            self.second_input.setText(str(result))
        except BaseException as e:
            print(e)


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
