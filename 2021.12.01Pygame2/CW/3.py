import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Перетаскивание')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True

    square_width = 100
    square_color = pygame.Color('green')
    square_x, square_y = 0, 0
    x1, y1 = -1, -1
    x2, y2 = 0, 0
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = event.pos
                if (x1 < square_x) or (x1 > square_x + square_width) or (y1 < square_y) or (y1 > square_y + square_width):
                    x1 = y1 = -1
            elif event.type == pygame.MOUSEMOTION and x1 > -1:
                x2 = event.pos[0] - x1
                y2 = event.pos[1] - y1
            if event.type == pygame.MOUSEBUTTONUP:
                square_x += x2
                square_y += y2
                x1, y1 = -1, -1
                x2, y2 = 0, 0
            rect_for_draw = (square_x + x2, square_y + y2, square_width, square_width)
            pygame.draw.rect(screen, square_color, rect_for_draw)
            pygame.display.flip()
            clock.tick(100)
    pygame.display.quit()
    pygame.quit()
