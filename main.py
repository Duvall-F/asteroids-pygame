import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    pygame.init() # initializing pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # create an object to help track time
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group() # holds all objects that can be updated
    drawable = pygame.sprite.Group() # holds all objects that can be drawn
    Player.containers = (updatable, drawable) # adds all future instances of "Player" to both groups
    player = Player(x, y)

    while True: # start of game loop
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,"black") # fills screen with black
        for single_drawable in drawable:
            single_drawable.draw(screen)
        #player.draw(screen) # draws the player icon on the screen
        updatable.update(dt)
        pygame.display.flip() # updates the entire contents of your computer screen with whatever you have drawn on your display Surface
        dt = clock.tick(60) / 1000

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
