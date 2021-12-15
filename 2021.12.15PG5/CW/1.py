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


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    image = load_image('arrow.png')
    fps = 120
    clock = pygame.time.Clock()
    running = True
    pygame.mouse.set_visible(False)
    while running:
        if not pygame.mouse.get_focused():
            screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                screen.fill((0, 0, 0))
                x, y = event.pos
                screen.blit(image, (x, y))
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
