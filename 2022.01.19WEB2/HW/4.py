from io import BytesIO
import pygame
import requests
from PIL import Image


def generator():
    x = 0
    while True:
        x += 1
        yield x % 3


pygame.init()
size = width, height = 600, 450
screen = pygame.display.set_mode(size)
fps = 60
clock = pygame.time.Clock()

url1 = "https://static-maps.yandex.ru/1.x/?ll=-123.007784,45.408086&z=17&l=sat,skl"
response1 = requests.get(url1)
im = Image.open(BytesIO(response1.content))
im.save('1.png', 'PNG')
bg1 = pygame.image.load("1.png")


url2 = "https://static-maps.yandex.ru/1.x/?ll=-79.72496943287877,44.50606338626438&z=17&l=sat,skl"
response2 = requests.get(url2)
im = Image.open(BytesIO(response2.content))
im.save('2.png', 'PNG')
bg2 = pygame.image.load("2.png")


url3 = "https://static-maps.yandex.ru/1.x/?ll=64.79684288461864,54.468452652002775&z=16&l=sat,skl"
response3 = requests.get(url3)
im = Image.open(BytesIO(response3.content))
im.save('3.png', 'PNG')
bg3 = pygame.image.load("3.png")

images = [bg1, bg2, bg3]
screen.blit(bg1, (0, 0))
running = True
g = generator()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                screen.blit(images[next(g)], (0, 0))
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
