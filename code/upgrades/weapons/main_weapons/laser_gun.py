from settings import *
from upgrades.weapons.main_weapons.main_weapon_settings import LASER_GUN
from upgrades.weapons.weapon import Weapon
from upgrades.projectiles.laser import Laser

class LaserGun(Weapon):
    def __init__(self, groups, all_sprites, player_projectile_sprites, enemy_sprites, player):
        
        super().__init__(
            groups, 
            all_sprites, 
            player_projectile_sprites, 
            enemy_sprites, 
            pygame.surface.Surface((20, 20)), 
            player, 
            cooldown = LASER_GUN["COOLDOWN"])

        self.laser_surf = pygame.image.load(join("images", "laser.png")).convert_alpha()

    def spawn_projectile(self):
        Laser((self.all_sprites, self.player_projectile_sprites), self.enemy_sprites, self.laser_surf, self.player, self.projectile_start_pos)