from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, groups, enemy_sprites, surf, player, pos, direction, speed, range, angle = 0):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(centerx = pos[0], bottom = pos[1])
        self.player = player

        # groups
        self.enemy_sprites = enemy_sprites

        # movement
        self.direction = direction
        self.shoot_time = pygame.time.get_ticks()
        self.shoot_pos = pygame.Vector2(self.rect.center)
        self.angle = angle

        # stats
        self.speed = speed
        self.range = range

    def update(self, delta_time):
        current_pos = pygame.Vector2(self.rect.center)
        if (current_pos - self.shoot_pos).length() >= self.range:
            self.kill()

        self.move(delta_time)

    def move(self, delta_time):
        self.rect.center += self.direction * self.speed * delta_time