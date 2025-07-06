from settings import *
from upgrades.projectiles.projectile import Projectile

class Laser(Projectile):
    def __init__(self, groups, surf, pos, angle = 0):
        super().__init__(groups, surf, pos, pygame.Vector2(0, -1), 500, 500)