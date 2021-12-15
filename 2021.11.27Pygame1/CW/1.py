import pygame


def draw(screen, size):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, 'white', (0, 0), (size[0], size[1]), 5)
    pygame.draw.line(screen, 'white', (0, size[1]), (size[0], 0), 5)


if __name__ == '__main__':
    pygame.init()
    try:
        size = width, height = tuple(filter(lambda x: x >= 0, map(int, input().split())))
    except BaseException as e:
        exit('Неправильный формат ввода')
    screen = pygame.display.set_mode(size)
    draw(screen, size)
    pygame.display.flip()
    pygame.display.set_caption('Крест')
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
