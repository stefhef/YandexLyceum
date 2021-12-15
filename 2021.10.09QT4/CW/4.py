import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QPushButton


class RandomStringFromFile(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 700, 50)
        self.setWindowTitle('Random string')
        self.button = QPushButton('Получить', self)
        self.button.move(10, 10)
        self.button.resize(100, 30)
        self.textBrowser = QTextBrowser(self)

        self.textBrowser.move(120, 10)
        self.textBrowser.resize(570, 30)
        self.button.clicked.connect(self.get_random_string)

    def get_random_string(self):
        try:
            with open('lines.txt', encoding='UTF-8') as f:
                text = f.readlines()
                self.textBrowser.setText(random.choice(text) if text else 'Файл пустой')
        except FileNotFoundError:
            self.textBrowser.setText('Файл не найден')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomStringFromFile()
    ex.show()
    sys.exit(app.exec())
