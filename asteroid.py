import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_state, log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        num = random.uniform(20, 50) # creates a random angle between 20 and 50 degress
        
        positive = self.velocity.rotate(num) # a new vector representing the first new asteroids movement
        negative = self.velocity.rotate(-num) # negative angle
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS # makes the new asteroirds smaller
        
        one_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius) # creates two new smaller asteroids
        two_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        
        one_new_asteroid.velocity = positive * 1.2 # sets the velocity (direction) and makes it moves 1.2 times faster
        two_new_asteroid.velocity = negative * 1.2