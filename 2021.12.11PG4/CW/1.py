import pygame
from copy import deepcopy


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 20

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                width = 1 if self.board[i][j] == 0 else 0
                pygame.draw.rect(screen,
                                 'white',
                                 (self.left + j * self.cell_size,
                                  self.top + i * self.cell_size,
                                  self.cell_size,
                                  self.cell_size),
                                 width)

    def get_cell(self, mouse_pos):
        n1 = (mouse_pos[0] - 10) // self.cell_size
        n2 = (mouse_pos[1] - 10) // self.cell_size
        if n1 >= self.width or n2 >= self.height:
            return None
        return n2, n1

    def on_click(self, cell):
        i, j = cell

        self.board[i][j] = 0 if self.board[i][j] == 1 else 1

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


class Life(Board):

    def check_neighbors(self, i, j):
        result = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                  (i, j - 1), (i, j + 1),
                  (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
        return list(filter(lambda x: 0 <= x[0] < self.height and
                                     0 <= x[1] < self.width, result))

    def next_move(self):
        new_board = deepcopy(self.board)
        for i in range(self.width):
            for j in range(self.height):
                neighbors = self.check_neighbors(i, j)
                count_of_neighbors_life = sum(map(lambda x: self.board[x[0]][x[1]], neighbors))
                if self.board[i][j] == 0 and count_of_neighbors_life == 3:
                    new_board[i][j] = 1
                elif self.board[i][j] == 1 and not (count_of_neighbors_life in [2, 3]):
                    new_board[i][j] = 0
                # elif self.board[i][j] == 1 and not (count_of_neighbors_life in [2, 3]):
                #     new_board[i][j] = 0
        self.board = new_board


pygame.init()
screen = pygame.display.set_mode((1020, 1020))
board = Life(20, 20)
running = True
fps = 10
clock = pygame.time.Clock()
flag = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                flag = not flag
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            board.get_click(event.pos)
            print(board.get_cell(event.pos))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                fps += 5
                if fps > 120:
                    fps = 120
            if event.button == 5:
                fps -= 5
                if fps == 0:
                    fps = 5
            print(fps)

    screen.fill((0, 0, 0))
    if flag:
        board.next_move()
    board.render(screen)
    pygame.display.flip()
    clock.tick(fps)
