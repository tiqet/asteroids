# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from pygame import display
from pygame.examples.aliens import Player

from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)

        display.flip()
        dt = clock.tick(60)/1000  # 60 frames per second

if __name__ == "__main__":
    main()