import pygame
import math

pygame.init()
tile_width = tile_height = 56


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
        if self.rect.x == 6:
            self.rect.x = Boss().rect.x

        elif self.rect.x < 6:
            self.rect.x = Boss().rect.x


class Bunker(pygame.sprite.Sprite):
    image1 = pygame.image.load("data/crateMetal.png")
    image = pygame.transform.scale(image1, (56, 56))

    def __init__(self, pos_x, pos_y, *group):
        super().__init__(*group)
        self.image = Bunker.image
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Hero(pygame.sprite.Sprite):
    image1 = pygame.image.load("data/tank_sand.png")
    image = pygame.transform.rotate(pygame.transform.scale(image1, (42, 46)), 180)

    def __init__(self, pos_x, pos_y, *group):
        super().__init__(*group)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.key_is_up = True
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.grade = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5
        # hero_x, hero_y = self.rect.x, self.rect.y
        # mouse_x, mouse_y = pygame.mouse.get_pos()
        # print("hero x y:", hero_x, hero_y)
        # print("mouse x y:", mouse_x, mouse_y)
        # len_a = abs(mouse_x - hero_x)
        # len_b = abs(mouse_y - hero_y)
        # arcTang_rad = math.atan2(len_a, len_b)
        # arcTang = arcTang_rad * (180 / math.pi)
        # if mouse_x > hero_x and mouse_y > hero_y:  # первая четверть
        #     arcTang += 270
        # elif mouse_x < hero_x and mouse_y < hero_y:  # вторая четверь
        #     arcTang += 90
        # elif mouse_x > hero_x and mouse_y < hero_y:  # четвёртая четверть
        #     arcTang += 180
        # elif mouse_x < hero_x and mouse_y > hero_y:  # третья четверь
        #     arcTang = arcTang
        # rotate_hero = arcTang - self.grade
        # print(rotate_hero, self.grade, arcTang)
        # self.grade = arcTang

        self.image = pygame.transform.rotate(self.image, 89) #rotate_hero
        self.image = pygame.transform.rotate(self.image, -89)