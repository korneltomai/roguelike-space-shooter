from settings import *
from player.player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Roguelike Space Shooter')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups 
        self.all_sprites = pygame.sprite.Group()

        self.import_assets()

    def run(self):

        while self.running:
            delta_time = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
           
            # update
            self.all_sprites.update(delta_time)

            # draw  
            self.display_surface.fill("#3a2e3f")
            self.all_sprites.draw(self.display_surface)
            
            pygame.display.update()
        
        pygame.quit()

    def import_assets(self):
        self.laser_surf = pygame.image.load(join("images", "laser.png")).convert_alpha()

if __name__ == '__main__':
    game = Game()
    game.run()