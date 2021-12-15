import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шарики')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True

    circle_color = pygame.Color('white')
    circle_radius = 10
    circles = []
    speeds = []
    screen2 = pygame.Surface(screen.get_size())

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    circles.append(list(event.pos))
                    speeds.append([-1, -1])
        screen2.fill((0, 0, 0))
        for i in range(len(circles)):
            if circles[i][0] >= width - circle_radius or circles[i][0] <= circle_radius:
                speeds[i][0] = -speeds[i][0]
            if circles[i][1] >= height - circle_radius or circles[i][1] < circle_radius:
                speeds[i][1] = -speeds[i][1]
            circles[i][0] += speeds[i][0]
            circles[i][1] += speeds[i][1]
            pygame.draw.circle(screen2, circle_color, circles[i], circle_radius)
        screen.blit(screen2, (0, 0))
        pygame.display.flip()
        clock.tick(100)
    pygame.display.quit()
    pygame.quit()
