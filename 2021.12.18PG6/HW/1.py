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

    def move_up(self):
        if pygame.sprite.spritecollideany(self, ladder):
            self.rect = self.rect.move(0, -10)

    def move_down(self):
        if pygame.sprite.spritecollideany(self, ladder):
            self.rect = self.rect.move(0, 10)


class Board(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.add(wall)
        self.x = pos[0]
        self.y = pos[1]
        self.image = pygame.Surface([50, 10])
        self.image.fill('gray')
        self.rect = pygame.Rect(self.x, self.y, 50, 10)


class Ladder(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.add(wall)
        self.add(ladder)
        self.x = pos[0]
        self.y = pos[1]
        self.image = pygame.Surface([10, 50])
        self.image.fill('red')
        self.rect = pygame.Rect(self.x, self.y, 10, 50)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    fps = 50
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    wall = pygame.sprite.Group()
    ladder = pygame.sprite.Group()
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
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        Ladder(event.pos)
                    else:
                        Board(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    square.move_left()
                elif event.key == pygame.K_RIGHT:
                    square.move_right()
                elif event.key == pygame.K_UP:
                    square.move_up()
                elif event.key == pygame.K_DOWN:
                    square.move_down()
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
