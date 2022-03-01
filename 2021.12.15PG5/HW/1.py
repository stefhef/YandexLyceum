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


class Car(pygame.sprite.Sprite):
    image = load_image("car2.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0
        self.v = 2

    def update(self, *args):
        self.rect.x += self.v
        if self.rect.x == 450 or self.rect.x == 0:
            self.v *= -1
            self.image = pygame.transform.flip(self.image, flip_y=False, flip_x=True)


all_sprites = pygame.sprite.Group()
size = width, height = 600, 95
screen = pygame.display.set_mode(size)
fps = 60
clock = pygame.time.Clock()
running = True
Car(all_sprites)
im = load_image('car2.png')
x = 0
while running:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
