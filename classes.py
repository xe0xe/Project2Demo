import pygame

pygame.init()


class Boss(pygame.sprite.Sprite):
    image1 = pygame.image.load("data/tank_huge.png")
    image = pygame.transform.scale(image1, (62, 76))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Boss.image
        self.rect = self.image.get_rect()
        self.rect.x = 800 + self.rect[2]
        self.rect.y = 175

    def update(self):
        self.rect.x -= 0.5


class BossBullet(pygame.sprite.Sprite):
    image1 = pygame.image.load("data/bulletRed2.png")
    image = pygame.transform.scale(image1, (16, 24))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = BossBullet.image
        self.rect = self.image.get_rect()
        self.rect.x = Boss().rect.x
        self.rect.y = Boss().rect.y

    def update(self):
        self.rect.x -= 10
        if self.rect.x == Bunker().rect.x:
            self.rect.x = Boss().rect.x

        elif self.rect.x < Bunker().rect.x:
            self.rect.x = Boss().rect.x


class Bunker(pygame.sprite.Sprite):
    image1 = pygame.image.load("data/crateMetal.png")
    image = pygame.transform.scale(image1, (28, 28))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bunker.image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 175


class Hero(pygame.sprite.Sprite):
    image1 = pygame.image.load("data/tank_sand.png")
    image = pygame.transform.scale(image1, (42, 46))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.key_is_up = True
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        print(self.key_is_up)
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5
        if keys[pygame.K_LEFT] and self.key_is_up:
            self.image = pygame.transform.rotate(self.image, 90)
            self.key_is_up = False
        if keys[pygame.K_RIGHT] and self.key_is_up:
            self.image = pygame.transform.rotate(self.image, -90)
            self.key_is_up = False


