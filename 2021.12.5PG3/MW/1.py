import pygame
from random import randint


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        for _ in range(height):
            lst = list()
            for i in range(width):
                lst.append(randint(0, 1))
            self.board.append(lst)
        # self.board = [[0] * width for _ in range(height)]
        self.color = ('red', 'blue')
        self.player = True
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen,
                                 'white',
                                 (self.left + j * self.cell_size,
                                  self.top + i * self.cell_size,
                                  self.cell_size,
                                  self.cell_size),
                                 1)
                color = self.color[self.board[i][j]]
                pygame.draw.circle(screen,
                                   color,
                                   (self.left + j * self.cell_size + self.cell_size / 2,
                                    self.top + i * self.cell_size + self.cell_size / 2),
                                   self.cell_size / 2 - 3)

    def get_cell(self, mouse_pos):
        n1 = mouse_pos[0] // self.cell_size
        n2 = mouse_pos[1] // self.cell_size
        if n1 >= self.width or n2 >= self.height:
            return None
        return n2, n1

    def on_click(self, cell):
        if cell:
            x, y = cell
            if self.board[x][y] == 0 and self.player:
                for i in range(self.height):
                    self.board[i][y] = 0

                for i in range(self.width):
                    self.board[x][i] = 0

                self.player = not self.player

            if self.board[x][y] == 1 and not self.player:
                for i in range(self.height):
                    self.board[i][y] = 1

                for i in range(self.width):
                    self.board[x][i] = 1

                self.player = not self.player

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


pygame.init()
screen = pygame.display.set_mode((500, 700))
# поле 5 на 7
board = Board(5, 7)
board.set_view(5, 7, 75)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            board = Board(5, 7)
            board.set_view(5, 7, 75)
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
            print(board.get_cell(event.pos))
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
