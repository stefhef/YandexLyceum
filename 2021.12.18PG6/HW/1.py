import pygame


class Square(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.x = pos[0]
        self.y = pos[1]
        self.image = pygame.Surface([20, 20])
        self.image.fill('blue')
        self.rect = pygame.Rect(self.x, self.y, 20, 20)

    def update(self):
        if not pygame.sprite.spritecollideany(self, wall):
            self.rect = self.rect.move(0, 1)

    def re_move(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.rect = pygame.Rect(self.x, self.y, 20, 20)

    def move_left(self):
        self.rect = self.rect.move(-10, 0)

    def move_right(self):
        self.rect = self.rect.move(10, 0)


class Board(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.add(wall)
        self.x = pos[0]
        self.y = pos[1]
        self.image = pygame.Surface([50, 10])
        self.image.fill('gray')
        self.rect = pygame.Rect(self.x, self.y, 50, 10)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    fps = 50
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    wall = pygame.sprite.Group()
    square = Square(size)
    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    square.re_move(event.pos)
                elif event.button == 1:
                    Board(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    square.move_left()
                elif event.key == pygame.K_RIGHT:
                    square.move_right()
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
