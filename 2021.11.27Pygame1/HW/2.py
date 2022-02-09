import pygame as pg
from math import floor

pg.init()
try:
    n = int(input())
except ValueError:
    exit("Неправильный формат ввода")
screen = pg.display.set_mode((300, 300))
count = floor(300 / n)
clock = pg.time.Clock()
BG_COLOR = pg.Color('yellow')
COLOR = pg.Color('orange')
points = [(200, 200), (250, 250), (200, 300), (150, 250)]
n_2 = n / 2
running = True

screen.fill(BG_COLOR)
for i in range(count):
    for j in range(count):
        pg.draw.polygon(screen, COLOR, [(n_2 + n * j, n * i),
                                        (n + n * j, n_2 + n * i),
                                        (n_2 + n * j, n + n * i),
                                        (n * j, n_2 + n * i)])

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.flip()
    clock.tick(60)
