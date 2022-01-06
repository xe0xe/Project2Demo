import pygame
import os
import sys
from classes import Hero, Boss, BossBullet, Bunker

pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
scene = True  # для вызова боса назначить True
lives = 25  # жизни базы

if __name__ == '__main__':
    running = True
    all_sprites = pygame.sprite.Group()

    screen.fill(pygame.Color('white'))
    FPS = 60
    clock = pygame.time.Clock()

    player = Hero(all_sprites)
    Bunker(all_sprites)

    if scene:  # проверка начата ли сцена с босом
        Boss(all_sprites)
        BossBullet(all_sprites)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                player.key_is_up = True
                print('yes i am here')
        screen.fill(pygame.Color('white'))

        all_sprites.draw(screen)
        all_sprites.update()

        pygame.display.flip()

    pygame.quit()
