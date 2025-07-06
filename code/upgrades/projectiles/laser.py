from settings import *
from upgrades.projectiles.projectile_settings import LASER
from upgrades.projectiles.projectile import Projectile

class Laser(Projectile):
    def __init__(self, groups, enemy_sprites, surf, player, pos, angle = 0):
        super().__init__(
            groups, 
            enemy_sprites, 
            surf, 
            player, 
            pos, 
            pygame.Vector2(0, -1), 
            speed = LASER["SPEED"], 
            range = LASER["RANGE"])