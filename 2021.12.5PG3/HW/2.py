import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
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
                if self.board[i][j] == 1:
                    pygame.draw.line(screen,
                                     'blue',
                                     (self.left + j * self.cell_size + 4,
                                      self.top + i * self.cell_size + 4),
                                     (self.left + (j + 1) * self.cell_size - 4,
                                      self.top + (i + 1) * self.cell_size - 4),
                                     2)
                    pygame.draw.line(screen,
                                     'blue',
                                     (self.left + (j + 1) * self.cell_size - 4,
                                      self.top + i * self.cell_size + 4),
                                     (self.left + j * self.cell_size + 4,
                                      self.top + (i + 1) * self.cell_size - 4),
                                     2)

                elif self.board[i][j] == 2:
                    pygame.draw.circle(screen,
                                       'red',
                                       (self.left + j * self.cell_size + self.cell_size / 2,
                                        self.top + i * self.cell_size + self.cell_size / 2),
                                       self.cell_size / 2 - 3,
                                       2)

    def get_cell(self, mouse_pos):
        n1 = mouse_pos[0] // self.cell_size
        n2 = mouse_pos[1] // self.cell_size
        if n1 >= self.width or n2 >= self.height:
            return None
        return n2, n1

    def on_click(self, cell):
        if cell:
            x, y = cell
            if self.board[x][y] == 0:
                self.board[x][y] = 1 if self.player else 2
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
