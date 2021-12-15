import pygame


def draw(screen, side, n):

    cell_size = side // n
    color_screen = 'white' if n % 2 == 1 else 'black'
    screen.fill(color_screen)
    color = 'white' if n % 2 == 0 else 'black'
    for y in range(n):
        for x in range(n):
            if (x + y) % 2 == 0:
                screen.fill(color, (cell_size * x, cell_size * y,
                                    cell_size, cell_size))


if __name__ == '__main__':
    pygame.init()
    try:
        side, n = tuple(filter(lambda x: x >= 0, map(int, input().split())))
        if side % n != 0:
            raise ValueError
    except ValueError:
        exit('Неправильный формат ввода')
    screen = pygame.display.set_mode((side, side))
    draw(screen, side, n)
    pygame.display.flip()
    pygame.display.set_caption('Шахматная доска')
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
