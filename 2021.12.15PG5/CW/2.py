import os
import sys

import pygame


def load_image(name, colorkey=-1):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
    if colorkey == -1:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def draw(x, y):
    screen.fill((255, 255, 255))
    screen.blit(image, (x, y))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    image = load_image('creature.png')
    fps = 120
    clock = pygame.time.Clock()
    running = True
    x = 0
    y = 0
    pygame.mouse.set_visible(False)
    draw(x, y)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 10
                elif event.key == pygame.K_DOWN:
                    y += 10
                elif event.key == pygame.K_RIGHT:
                    x += 10
                elif event.key == pygame.K_LEFT:
                    x -= 10
                draw(x, y)

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
