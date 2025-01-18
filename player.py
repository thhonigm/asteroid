import pygame
import circleshape
from shot import Shot
from constants import *

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        self.shield = False
        self.hit_count = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        color = "green" if self.shield else "white"
        lwidth = 2
        if self.hit_count > 0:
            color = "red"
            lwidth = int(self.hit_count / 3) + 1
        pygame.draw.polygon(screen, color, self.triangle(), lwidth)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.cooldown > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        self.cooldown = 0.3

    def hit(self, dt):
        self.hit_count += 100*dt

    def destroyed(self):
        return self.hit_count > 0 and not self.shield

    def update(self, dt):
        if self.cooldown > dt:
            self.cooldown -= dt
        else:
            self.cooldown = 0
        if self.hit_count > dt:
            self.hit_count -= dt
        else:
            self.hit_count = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.shield = True
        if keys[pygame.K_a]:
            self.shield = False
        if keys[pygame.K_h]:
            self.rotate(-dt)
        if keys[pygame.K_l]:
            self.rotate(dt)
        if keys[pygame.K_i] or keys[pygame.K_j]:
            self.move(dt)
        if keys[pygame.K_k]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

