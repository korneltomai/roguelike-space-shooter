from settings import *
from player.player import Player
from upgrades.weapons.main_weapons.laser_gun import LaserGun

class LaserShip(Player):
    def __init__(self, groups, all_sprites, player_projectiles):
        surf = pygame.transform.scale_by(pygame.image.load(join("images", "player.png")).convert_alpha(), (0.5, 0.5))
        super().__init__(groups, surf, player_projectiles)

        # movement
        self.speed = 350

        # weapons
        self.main_weapon = LaserGun(all_sprites, all_sprites, player_projectiles, self)

    def update(self, delta_time):
        super().update(delta_time)
        self.main_weapon.shoot()
