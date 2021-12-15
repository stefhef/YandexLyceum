from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber, QTextEdit
import sys


class Example(QWidget):
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Азбука Морзе 2')

        self.line = QTextEdit(self)
        self.line.resize(380, 240)
        self.line.move(10, 100)
        self.line.font()

        self.x, self.count, self.y = 10, 0, 10
        for letter, code in self.MORSE_CODE_DICT.items():

            if self.count == 19:  # Хехе, костыль но работает. Да надо Layout тщ так ли сильно?
                self.y += 20
                self.x = 10
                self.count = 0

            self.btn = QPushButton(self)
            self.btn.clicked.connect(lambda state, code=code: self.line.setText(self.line.toPlainText() + code))
            self.btn.setText(letter)
            self.btn.resize(20, 20)
            self.btn.move(self.x, self.y)
            self.x += 20
            self.count += 1

        def add_letter(self, symbol: str):
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())