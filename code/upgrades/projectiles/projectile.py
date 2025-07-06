from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, groups, surf, pos, direction, speed, lifetime, angle = 0):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(centerx = pos[0], bottom = pos[1])

        # movement
        self.angle = angle
        self.speed = speed
        self.lifetime = lifetime
        self.direction = direction
        self.shoot_time = pygame.time.get_ticks()

    def update(self, delta_time):
        current_time = pygame.time.get_ticks()
        if current_time - self.shoot_time >= self.lifetime:
            self.kill()

        self.move(delta_time)

    def move(self, delta_time):
        self.rect.center += self.direction * self.speed * delta_time