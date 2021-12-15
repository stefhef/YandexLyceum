import pygame


def draw(number):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 100)
    text = font.render(str(number), True, (255, 0, 0))
    text_w = text.get_width()
    text_h = text.get_height()
    text_x = 100 - text_w // 2
    text_y = 100 - text_h // 2
    screen.blit(text, (text_x, text_y))


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((200, 200))
    running = True
    number = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.VIDEOEXPOSE:
                number += 1
            elif event.type == pygame.QUIT:
                running = False
        draw(number)
        pygame.display.flip()

