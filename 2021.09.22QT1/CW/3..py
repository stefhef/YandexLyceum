import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Миникалькулятор')

        self.first_input = QLineEdit(self)
        self.first_input.move(20, 40)
        self.first_input.resize(60, 20)

        self.second_input = QLineEdit(self)
        self.second_input.move(20, 80)
        self.second_input.resize(60, 20)

        self.btn = QPushButton('->', self)
        self.btn.resize(20, 20)
        self.btn.move(120, 60)

        self.label1 = QLabel('Первое:', self)
        self.label1.resize(60, 20)
        self.label1.move(20, 20)

        self.label2 = QLabel('Второе:', self)
        self.label2.resize(100, 20)
        self.label2.move(20, 60)

        self.label_sum = QLabel('Cумма', self)
        self.label_sum.resize(120, 20)
        self.label_sum.move(160, 20)

        self.label_min = QLabel('Разность:', self)
        self.label_min.resize(120, 20)
        self.label_min.move(160, 40)

        self.label_pro = QLabel('Произведение:', self)
        self.label_pro.resize(120, 20)
        self.label_pro.move(160, 60)

        self.label_raz = QLabel('Разность:', self)
        self.label_raz.resize(120, 20)
        self.label_raz.move(160, 80)

        self.lcdn1 = QLCDNumber(self)
        self.lcdn1.resize(100, 20)
        self.lcdn1.move(280, 20)

        self.lcdn2 = QLCDNumber(self)
        self.lcdn2.resize(100, 20)
        self.lcdn2.move(280, 40)

        self.lcdn3 = QLCDNumber(self)
        self.lcdn3.resize(100, 20)
        self.lcdn3.move(280, 60)

        self.lcdn4 = QLCDNumber(self)
        self.lcdn4.resize(100, 20)
        self.lcdn4.move(280, 80)

        self.btn.clicked.connect(self.calc)

    def calc(self):
        num1, num2 = int(self.first_input.text()), int(self.second_input.text())
        self.lcdn1.display(str(num1 + num2))
        self.lcdn2.display(str(num1 - num2))
        self.lcdn3.display(str(num1 * num2))
        self.lcdn4.display(str(num1 / num2))


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
