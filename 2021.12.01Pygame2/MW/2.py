import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Прямоугольники с Ctrl+Z')
    fps = 60
    clock = pygame.time.Clock()
    running = True
    cords = []

    flag = False

    x2 = y2 = 0
    x1 = y1 = -1

    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = event.pos
                flag = True
            elif event.type == pygame.MOUSEMOTION and x1 > -1:
                x2 = event.pos[0] - x1
                y2 = event.pos[1] - y1
            if event.type == pygame.MOUSEBUTTONUP:
                flag = False
                cords.append((x1, y1, x2, y2))
                x1 = y1 = -1
                x2 = y2 = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and event.mod & pygame.KMOD_LCTRL:
                    if cords:
                        c = cords.pop()
                        pygame.draw.rect(screen, 'black', c, 2)
        for c in cords:
            pygame.draw.rect(screen, 'white', c, 2)
        if flag:
            pygame.draw.rect(screen, 'white', (x1, y1, x2, y2), 2)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
