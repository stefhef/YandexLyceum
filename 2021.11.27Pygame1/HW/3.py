import pygame as pg

pg.init()
screen = pg.display.set_mode((300, 200))
clock = pg.time.Clock()
BG_COLOR = pg.Color('red')
running = True

screen.fill(BG_COLOR)

for i in range(12):
    pg.draw.line(screen, 'white', (0, i * 15 + (i - 1) * 2), (300, i * 15 + 2 * (i - 1)), 2)
    x = 0
    if i % 2 != 0:
        x += 15
    for j in range(10):
        if j == 0 and x == 0:
            continue
        cords1 = (j * 30 + x, i * 17)
        cords2 = (j * 30 + x, i * 17 + 15)
        pg.draw.line(screen, 'white', cords1, cords2, 2)


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.flip()
    clock.tick(60)
