import sys
import random

import pygame
import os


# def generate_cordinate():
#     for i in range(0, 500, 100):
#         for j in range(0, 500, 100):
#             yield i, j
# gen_cord = generate_cordinate()

def load_image(name, colorkey=-1):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        # image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
size = width, height = (500, 500)


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image_boom = load_image("boom.png")

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        # cord = next(gen_cord)
        # self.rect.x = x
        # self.rect.y = y

        while True:
            self.rect.x = random.randrange(width - 100)
            self.rect.y = random.randrange(height - 100)
            if len(pygame.sprite.spritecollide(self, group[0], False)) == 1:
                break

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
# for i in range(0, 500, 100):
#     for j in range(0, 500, 100):
#         Bomb(i, j, all_sprites)
for _ in range(10):
    Bomb(all_sprites)
running = True
cords_mouse = None, None
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for bomb in all_sprites:
                bomb.update(event)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()

pygame.quit()
