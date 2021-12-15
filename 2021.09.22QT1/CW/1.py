import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Третья программа')


        self.first_input = QLineEdit(self)
        self.first_input.move(10, 100)

        self.second_input = QLineEdit(self)
        self.second_input.move(250, 100)

        self.btn = QPushButton('->', self)
        self.btn.resize(25, 20)
        self.btn.move(175, 100)
        self.btn.clicked.connect(self.change)

    def change(self):
        first_text, second_text = self.first_input.text(), self.second_input.text()
        self.second_input.setText(first_text)
        self.first_input.setText(second_text)
        button_text = '<-' if self.btn.text() == '->' else '->'
        self.btn.setText(button_text)


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
