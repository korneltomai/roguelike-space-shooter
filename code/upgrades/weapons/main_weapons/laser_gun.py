from settings import *
from upgrades.weapons.weapon import Weapon
from upgrades.projectiles.laser import Laser

class LaserGun(Weapon):
    def __init__(self, groups, all_sprites, player_projectiles, player):
        super().__init__(groups, all_sprites, player_projectiles, pygame.surface.Surface((20, 20)), player, 1000)

        self.laser_surf = pygame.image.load(join("images", "laser.png")).convert_alpha()

    def spawn_projectile(self):
        Laser((self.all_sprites, self.player_projectiles), self.laser_surf, self.projectile_start_pos)