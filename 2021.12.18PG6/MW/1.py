import os
import sys

import pygame


pygame.init()


def load_image(name, colorkey=-1):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    # if colorkey is not None:
    # image = image.convert()
    if colorkey == -1:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


all_sprites = pygame.sprite.Group()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
fps = 20
clock = pygame.time.Clock()
running = True
im = load_image('1.png')
screen.fill('blue')
x = -600
while running:
    screen.blit(im, (x, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    if x < 0:
        x += 10
    clock.tick(fps)
pygame.quit()
