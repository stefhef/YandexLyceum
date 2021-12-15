import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтый круг')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    fps = 60
    circle_width = 0
    circle_exist = False
    circle_color = pygame.Color('yellow')
    PLUS_RADIUS = pygame.USEREVENT + 1
    pygame.time.set_timer(PLUS_RADIUS, 10)
    clock = pygame.time.Clock()
    screen.fill((0, 0, 255))
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                screen.fill((0, 0, 255))
                circle_exist = True
                circle_pos = event.pos
                circle_radius = 10
                pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
            elif event.type == PLUS_RADIUS and circle_exist:
                circle_radius += 1
                pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
        clock.tick(fps)
        pygame.display.flip()
