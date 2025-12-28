import pygame
from player import Player
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)

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
    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
