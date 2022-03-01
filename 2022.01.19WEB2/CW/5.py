from io import BytesIO
import requests
import pygame
from PIL import Image

response = requests.get("https://static-maps.yandex.ru/1.x/?ll=134.699652,-24.767849&z=4&l=sat")

if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 450
    screen = pygame.display.set_mode(size)
    fps = 60
    clock = pygame.time.Clock()
    running = True
    im = Image.open(BytesIO(response.content))
    im.show()
    im.save('tmp.jpg', 'PNG')
    bg = pygame.image.load('tmp.jpg')

    screen.blit(bg, (0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
