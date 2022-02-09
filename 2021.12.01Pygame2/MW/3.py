import pygame


if __name__ == '__main__':
    pygame.init()
    with open('points.txt', 'r') as file:
        data = tuple(map(lambda x: x.split(';'), file.read().strip().replace(')', '').replace('(', '').split(',')))
    cntx = centy = 251
    mas = 100
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    fps = 60
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEWHEEL:
                if event.button == 4:
                    mas += 5
                    if mas > 120:
                        mas = 120
                if event.button == 5:
                    mas -= 5
                    if mas == 0:
                        mas = 5
        for i in range(len(data) - 1):
            pygame.draw.line(screen, 'white', data[i], data[i + 1])

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
