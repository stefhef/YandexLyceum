from PyQt5 import QtWidgets
import sys


class App(QtWidgets.QWidget):

    def __init__(self, matrix):
        self.matrix = matrix
        super(App, self).__init__()
        self.InitUi()

    def InitUi(self):
        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)
        for y, elem in enumerate(self.matrix):
            for x, el in enumerate(elem):
                button = QtWidgets.QPushButton() if el == '0' else QtWidgets.QPushButton('*')
                grid.addWidget(button, y, x)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    while True:
        print('Введите матрицу:')
        matrix = input()
        ex = App(matrix)
        ex.show()
        sys.exit(app.exec())
