from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, surf, player_projectiles):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # groups
        self.player_projectiles = player_projectiles

        # movement
        self.direction = pygame.Vector2()

        # weapons
        self.main_weapon_pos = (self.rect.centerx, self.rect.top)
        self.main_weapon = None

    def update(self, delta_time):
        self.handle_movement_input()
        self.move(delta_time)
        self.shoot()
        self.main_weapon_pos = (self.rect.centerx, self.rect.top)

    def handle_movement_input(self):
        self.direction = pygame.Vector2(pygame.mouse.get_pos()) - pygame.Vector2(self.rect.center)
        print(self.direction)
        self.direction = self.direction.normalize() if self.direction and self.direction.length() > 0.5 else pygame.Vector2()
        
    def move(self, delta_time):
        self.rect.center += self.direction * self.speed * delta_time

    def shoot(self):
        pass