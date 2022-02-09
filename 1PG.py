import pygame


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
fps = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
