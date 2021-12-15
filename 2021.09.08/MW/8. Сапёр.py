import numpy
import numpy as np
import random as rd


class Board:

    def __init__(self, size_x=5, size_y=5, count_mine=8):
        # self.board = [[0] * size_x] * size_y
        self.size_x = size_x
        self.size_y = size_y
        self.board = [['0'] * size_x for _ in range(size_y)]
        self.count_mine = count_mine
        self.lose = False

    def generate_mine(self):
        """
        Создаёт мины на поле
        Криво но работает
        :return:
        """
        count = 0
        while True:
            if count == self.count_mine:
                break
            x = rd.choice(range(5))
            y = rd.choice(range(5))

            if self.board[y][x] == '0':
                self.board[y][x] = '1'
                count += 1

    def open_neighbors(self, x, y):
        neighbors = self.get_neighbors(y, x)
        count_neighbors = 0
        for neighbor in neighbors:
            y1, x1 = neighbor
            if self.board[y1][x1] == '0':
                count_neighbors += 1
                self.board[y1][x1] = "-1"
                self.open_neighbors(y1, x1)
            else:
                self.board[x][y] = str(sum(map(lambda x: int(self.board[x[0]][x[1]]), filter(lambda x: self.board[x[0]][x[1]] == '1', neighbors))))

    def get_neighbors(self, i, j):
        result = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                  (i, j - 1), (i, j + 1),
                  (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
        return list(filter(lambda x: 0 <= x[0] < self.size_x and
                                     0 <= x[1] < self.size_y, result))

    def check_step(self, x: int, y: int):
        field = self.board[y][x]
        if field == '1':
            self.board[y][x] = 'X'
            self.lose = True
            return False
        if field == '0':
            self.board[y][x] = "-1"
            self.open_neighbors(x, y)
            return True
        if '2' in field or '3' in field:
            print('Yes?')

    def first_step(self, x, y):
        self.board[y][x] = "-1"

    def __str__(self):
        st = ''
        for i in self.board:
            for j in i:
                if j == '-1':
                    st += '   '

                elif j == '[F]':
                    st += '[F]'
                elif j == '[?]':
                    st += '[?]'
                elif '1' in j:
                    st += '[test]'
                elif j == 'X':
                    st += '[X]'
                elif j == '0':
                    st += '[ ]'
                else:
                    st += j
            st += '\n'
        return st


def main():
    board = Board()
    x, y = tuple(map(int, input().split()))
    board.first_step(x, y)
    board.generate_mine()
    print(board)
    while not board.lose:
        x, y = tuple(map(int, input().split()))
        board.check_step(x, y)
        print(board)
    print('LOSE')
    print(board)


if __name__ == '__main__':
    main()
