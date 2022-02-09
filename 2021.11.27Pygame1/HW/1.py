import pygame

n = int(input())
width, height = 40, 300
x, y = 136.5, 0
if __name__ == '__main__':
    pygame.init()
    size = 300, 300
    screen = pygame.display.set_mode(size)
    pygame.draw.ellipse(screen, 'white', (0, 0, 300, 300), 1)
    pygame.display.flip()
    for i in range(1, n):
        pygame.draw.ellipse(screen, 'white', (x, y, width, height), 1)
        pygame.draw.ellipse(screen, 'white', (y, x, height, width), 1)
        pygame.display.flip()
        width += 28
        x -= 15
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
