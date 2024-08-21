import pygame

from player import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid_group, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots_group, updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroid_group:
            if asteroid.collide_with(player):
                print("Game over!")
                return
            for bullet in shots_group:
                if asteroid.collide_with(bullet):
                    asteroid.split()
                    bullet.kill()
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000  # 60 frames per second

if __name__ == "__main__":
    main()