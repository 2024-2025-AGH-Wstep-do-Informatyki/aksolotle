import pygame

placeholder = pygame.image.load("level_1/placeholder.webp").convert()
placeholder_scaled = pygame.transform.scale(placeholder, (placeholder.get_width() * 4, placeholder.get_height() * 4))

class Level1:
    screen: pygame.Surface
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

    def graphics(self):
        self.screen.fill((0,0,0))
        self.screen.blit(placeholder_scaled, (0,0))
