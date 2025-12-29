import pygame
import sys
from player import Player
from logger import log_state
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Group creation
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #Group abilities
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        clock = pygame.time.Clock()
        dt = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for member in drawable:
             member.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for member in asteroids:
            if member.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for member in asteroids:
            for shot in shots:
                if member.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    member.split()
                


if __name__ == "__main__":
    main()
