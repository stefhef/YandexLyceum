import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]
        # значения по умолчанию
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
                width = 1 if self.board[i][j] == 1 else 0
                pygame.draw.rect(screen,
                                 'white',
                                 (self.left + j * self.cell_size,
                                  self.top + i * self.cell_size,
                                  self.cell_size,
                                  self.cell_size),
                                 width)

    def get_cell(self, mouse_pos):
        n1 = mouse_pos[0] // self.cell_size
        n2 = mouse_pos[1] // self.cell_size
        if n1 >= self.width or n2 >= self.height:
            return None
        return n1, n2

    def on_click(self, cell):
        if cell:

            for i in range(self.height):
                a = self.board[i][cell[0]]
                self.board[i][cell[0]] = -a

            for i in range(self.width):
                a = self.board[cell[1]][i]
                self.board[cell[1]][i] = -a

            self.board[cell[1]][cell[0]] = -self.board[cell[1]][cell[0]]

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
            print(board.get_cell(event.pos))
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
