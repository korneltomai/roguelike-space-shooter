from settings import *
from upgrades.projectiles.laser import Laser

class LaserGun(pygame.sprite.Sprite):
    def __init__(self, groups, all_sprites, player_projectiles, player):
        super().__init__(groups)
        self.image = pygame.surface.Surface((10, 10))
        self.rect = self.image.fill("blue")
        self.rect.center = (player.rect.centerx, player.rect.top)

        self.laser_surf = pygame.image.load(join("images", "laser.png")).convert_alpha()
        self.all_sprites = all_sprites
        self.player_projectiles = player_projectiles

        self.player = player

        self.can_shoot = True
        self.shoot_time = 0
        self.cooldown = 1000

    def update(self, delta_time):
        self.rect.center = (self.player.rect.centerx, self.player.rect.top)
        self.update_shoot_timer()
        self.shoot()

    def shoot(self):
        if self.can_shoot: 
            Laser((self.all_sprites, self.player_projectiles), self.laser_surf, (self.rect.centerx, self.rect.top))
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def update_shoot_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.cooldown:
                self.can_shoot = True