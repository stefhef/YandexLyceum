import pygame
from math import cos, pi

pygame.init()
size = width, height = 201, 201
screen = pygame.display.set_mode(size)
fps = 60
clock = pygame.time.Clock()
running = True
m = 70 * cos(75 / 360 * pi * 2)
a = 20 * 0.86602540378
b = 70 * 0.96592582628
pygame.draw.circle(screen, 'white', (100, 100), 10)
pygame.draw.polygon(screen, 'white', ((100, 90), (100 - m, 100 - b), (100 + m, 100 - b)))
x = 100 - 0.5 * a
y = 90 + a * 0.86602540378
pygame.draw.polygon(screen, 'white', ((x, y), (x - b, y - m), (x - b, y + m)))
x = 100 + 0.5 * a
pygame.draw.polygon(screen, 'white', ((x, y), (x + b, y - m), (x + b, y + m)))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # s = pygame.transform.rotate(screen, 10)
    # screen.blit(s, (0, 0))
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
