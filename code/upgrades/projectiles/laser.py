from settings import *

class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, surf, pos, angle = 0):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)

        # movement
        self.speed = 500
        self.lifetime = 500
        self.angle = angle
        self.direction = pygame.Vector2(0, -1)
        self.shoot_time = pygame.time.get_ticks()

    def update(self, delta_time):
        current_time = pygame.time.get_ticks()
        if current_time - self.shoot_time >= self.lifetime:
            self.kill()

        self.move(delta_time)

    def move(self, delta_time):
        self.rect.center += self.direction * self.speed * delta_time