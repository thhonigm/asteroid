import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        left = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        left.velocity = self.velocity.rotate(-random_angle) * 1.2
        right = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        right.velocity = self.velocity.rotate(random_angle) * 1.2

