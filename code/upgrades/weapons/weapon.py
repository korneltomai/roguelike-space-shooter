from settings import *
from upgrades.projectiles.laser import Laser

class Weapon(pygame.sprite.Sprite):
    def __init__(self, groups, all_sprites, player_projectiles, surf, player, cooldown):
        super().__init__(groups)

        self.player = player

        self.image = surf
        self.rect = self.image.get_frect(center = self.player.main_weapon_pos)

        self.all_sprites = all_sprites
        self.player_projectiles = player_projectiles

        self.projectile_start_pos = (self.rect.centerx, self.rect.top)
        self.can_shoot = True
        self.shoot_time = 0
        self.cooldown = cooldown

    def update(self, _):
        self.rect.center = self.player.main_weapon_pos
        self.projectile_start_pos = (self.rect.centerx, self.rect.top)
        self.update_shoot_timer()
        self.shoot()

    def shoot(self):
        if self.can_shoot: 
            self.spawn_projectile()
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def update_shoot_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.cooldown:
                self.can_shoot = True

    def spawn_projectile(self):
        pass