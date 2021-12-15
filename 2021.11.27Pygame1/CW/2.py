import pygame


def draw(screen, size):
    screen.fill((0, 0, 0))
    screen.fill('red', (1, 1, size[0] - 2, size[1] - 2))


if __name__ == '__main__':
    pygame.init()
    try:
        size = width, height = tuple(filter(lambda x: x >= 0, map(int, input().split())))
    except BaseException as e:
        exit('Неправильный формат ввода')
    screen = pygame.display.set_mode(size)
    draw(screen, size)
    pygame.display.flip()
    pygame.display.set_caption('Прямоугольник')
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
