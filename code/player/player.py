from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, surf, player_projectile_sprites, enemy_sprites, speed, attack_damage_multiplier, attack_speed_multiplier):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # groups
        self.player_projectile_sprites = player_projectile_sprites
        self.enemy_sprites = enemy_sprites

        # movement
        self.direction = pygame.Vector2()

        # weapons
        self.main_weapon_pos = (self.rect.centerx, self.rect.top)
        self.main_weapon = None

        # stats
        self.speed = speed
        self.attack_speed_multiplier = attack_speed_multiplier
        self.attack_damage_multiplier = attack_damage_multiplier

    def update(self, delta_time):
        self.handle_movement_input()
        self.move(delta_time)
        self.shoot()
        self.main_weapon_pos = (self.rect.centerx, self.rect.top)

    def handle_movement_input(self):
        self.direction = pygame.Vector2(pygame.mouse.get_pos()) - pygame.Vector2(self.rect.center)
        self.direction = self.direction.normalize() if self.direction and self.direction.length() > 0.5 else pygame.Vector2()
        
    def move(self, delta_time):
        self.rect.center += self.direction * self.speed * delta_time

    def shoot(self):
        pass