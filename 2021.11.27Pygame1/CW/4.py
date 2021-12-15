import pygame
from itertools import cycle


def draw(screen, side, n, w):
    screen.fill((0, 0, 0))
    center = side / 2
    center = (center, center)
    colors = cycle(['red', 'green', 'blue'])
    lst = [next(colors) for _ in range(n)]
    for i in range(n, 0, -1):
        pygame.draw.circle(screen, lst[i - 1], center, w * i)


if __name__ == '__main__':
    pygame.init()
    try:
        w, n = tuple(filter(lambda x: x >= 0, map(int, input().split())))
    except BaseException as e:
        exit('Неправильный формат ввода')
    side = w * 2 * n
    screen = pygame.display.set_mode((side, side))
    draw(screen, side, n, w)
    pygame.display.flip()
    pygame.display.set_caption('Мишень')
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
