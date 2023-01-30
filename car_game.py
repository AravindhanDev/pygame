try:
    import pygame, sys
    from pygame.locals import *
    import random
except ModuleNotFoundError as e:
    print(e)

print(pygame.ver)

pygame.init()

FSP = 60
FramesPerSecond = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
Green = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(this):
        super().__init__()
        this.image = pygame.image.load("Player.png")
        this.rect = this.image.get_rect()
        this.rect.center = (160, 520)

    def update(this):
        pressed_keys = pygame.key.get_pressed()
        # if this.rect.up > 0:
        #     if pressed_keys[K_UP]:
        #         this.rect.move_ip(-5, 0)
        # if this.rect.down < SCREEN_HEIGHT:
        #     if this.pressed_keys[K_DOWN]:
        #         this.rect.move_ip(5, 0)
        if this.rect.left > 0:
            if pressed_keys[K_LEFT]:
                this.rect.move_ip(-5, 0)
        if this.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                this.rect.move_ip(5, 0)

    def draw(this, surface):
        surface.blit(this.image, this.rect)

p1 = Player()
e1 = Enemy()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    p1.update()
    e1.move()

    DISPLAYSURF.fill(WHITE)
    p1.draw(DISPLAYSURF)
    e1.draw(DISPLAYSURF)

    pygame.display.update()
    FramesPerSecond.tick(FPS)


        
