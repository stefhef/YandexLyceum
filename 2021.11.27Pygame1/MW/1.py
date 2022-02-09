import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    try:
        w = int(input())
        if w % 4 != 0 or w > 100:
            raise ValueError
        hue = int(input())
        if not 0 <= hue <= 360:
            raise ValueError
    except ValueError:
        exit("Неправильный формат ввода")



    screen = pygame.display.set_mode(size)
    fps = 10
    clock = pygame.time.Clock()
    running = True

    nx = 130 - (w / 2)
    ny = 180 - (w / 2)
    w2 = w / 2

    color = pygame.Color(255, 255, 255)
    hsv = color.hsva
    color2 = pygame.Color(255, 255, 255)
    hsv2 = color2.hsva
    color3 = pygame.Color(255, 255, 255)
    hsv3 = color3.hsva

    color.hsva = (hue, hsv[1] + 100, hsv[2] - 25, hsv[3])
    color2.hsva = (hue, hsv2[1] + 100, hsv2[2], hsv[3])
    color3.hsva = (hue, hsv3[1] + 100, hsv3[2] - 50, hsv[3])

    pygame.draw.polygon(screen, color, ((nx, ny), (nx + w, ny),
                                        (nx + w, ny + w), (nx, ny + w)))

    pygame.draw.polygon(screen, color2, ((nx + w2, ny - w2), (nx + w2 + w, ny - w2),
                                         (nx + w, ny), (nx, ny)))

    pygame.draw.polygon(screen, color3,
                        ((nx + w, ny), (nx + w2 + w, ny - w2),
                         (nx + w2 + w, ny + w2), (nx + w, ny + w)))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
