from settings import *
from player.player_settings import LASER_SHIP
from player.player import Player
from upgrades.weapons.main_weapons.laser_gun import LaserGun

class LaserShip(Player):
    def __init__(self, groups, all_sprites, player_projectile_sprites, enemy_sprites):
        surf = pygame.transform.scale_by(pygame.image.load(join("images", "player.png")).convert_alpha(), (0.5, 0.5))

        super().__init__(
            groups, 
            surf, 
            player_projectile_sprites, 
            enemy_sprites, 
            speed = LASER_SHIP["SPEED"], 
            attack_damage_multiplier = LASER_SHIP["ATTACK_DAMAGE_MUL"],
            attack_speed_multiplier = LASER_SHIP["ATTACK_SPEED_MUL"]
            )

        # movement
        

        # weapons
        self.main_weapon = LaserGun(all_sprites, all_sprites, player_projectile_sprites, enemy_sprites, self)

    def update(self, delta_time):
        super().update(delta_time)
        self.main_weapon.shoot()
