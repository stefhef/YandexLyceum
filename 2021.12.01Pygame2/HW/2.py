import pygame


def generate_x(x0, x1):
    a = 1 if x0 < x1 else -1
    for i in range(x0, x1 + a, a):
        yield i


def generate_y(y0, y1):
    a = 1 if y0 < y1 else -1
    for i in range(y0, y1 + a, a):
        yield i


def move_circle(x0, x1, y0, y1):
    xs = generate_x(x0, x1)
    ys = generate_y(y0, y1)
    x = x0
    y = y0
    fps = 60
    clock = pygame.time.Clock()
    while True:
        screen.fill((0, 0, 0))

        if x != x1:
            x = next(xs)
        if y != y1:
            y = next(ys)
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)
        if x == x1 and y == y1:
            break
        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    pygame.draw.circle(screen, (255, 0, 0), (250, 250), 20)
    fps = 60
    clock = pygame.time.Clock()
    x0 = y0 = 250
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                move_circle(x0, x, y0, y)
                x0 = x
                y0 = y

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
