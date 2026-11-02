import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init() # initializing pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # sets the width and height of the screen
    clock = pygame.time.Clock() # create an object to help track time
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group() # holds all objects that can be updated
    drawable = pygame.sprite.Group() # holds all objects that can be drawn
    asteroids = pygame.sprite.Group() # holds all the asteroids

    Player.containers = (updatable, drawable) # adds all future instances of "Player" to both groups
    Asteroid.containers = (asteroids, updatable, drawable) # adds all future instances of "Asteroids" to 3 groups
    AsteroidField.containers = (updatable) # it's not drawable, and it's not an asteroid itself

    player = Player(x, y) # instance of the Player class
    asteroidfield = AsteroidField() # instance of AsteroidField class

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
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        dt = clock.tick(60) / 1000

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
