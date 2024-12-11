import pygame

background = pygame.image.load("menu/background.webp").convert()
background_scaled = pygame.transform.scale(background, (background.get_width() * 4, background.get_height() * 4))

logo = pygame.image.load("menu/logo_mock.webp").convert_alpha()
logo_scaled = pygame.transform.scale(logo, (logo.get_width() * 2, logo.get_height() * 2))

levels = pygame.image.load("menu/levels.webp").convert_alpha()

level_buttons = []
level_buttons_bright = []
level_rects = []

for i in range(6):
    level = pygame.image.load(f"menu/level_{i+1}.webp").convert_alpha()
    level_bright = level.copy()
    level_bright.fill((50,50,50), special_flags=pygame.BLEND_RGB_ADD)
    level_buttons.append(level)
    level_buttons_bright.append(level_bright)

class Menu:
    screen: pygame.Surface
    levels: list

    # 0 is menu, 1~6 are levels
    current_level: int = 0

    def __init__(self, screen: pygame.Surface, levels):
        self.levels = levels
        self.screen = screen
        button_width = level_buttons[0].get_width()
        button_height = level_buttons[0].get_height()

        for i in range(6):
            row = i // 3
            col = i % 3
            x = 40 + (col * (button_width + 100))
            y = 440 + (row * (button_height + 20))
            level_rects.append(pygame.Rect(x, y, button_width, button_height))

    def inputs(self):
        if self.current_level == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, rect in enumerate(level_rects):
                        if rect.collidepoint(event.pos):
                            print(f"Level {i+1} clicked!")
                            self.current_level = i+1
        else:
            if self.current_level <= len(self.levels):
                self.levels[self.current_level-1].inputs()

    def graphics(self):
        if self.current_level == 0:
            mouse_pos = pygame.mouse.get_pos()
            self.screen.blit(background_scaled, (0,0))
            self.screen.blit(logo_scaled, (520,40))
            self.screen.blit(levels, (40,330))

            for i, rect in enumerate(level_rects):
                if rect.collidepoint(mouse_pos):
                    self.screen.blit(level_buttons_bright[i], rect)
                else:
                    self.screen.blit(level_buttons[i], rect)
        else:
            if self.current_level <= len(self.levels):
                self.levels[self.current_level-1].graphics()
            else:
                self.screen.fill((0,0,0))
                text = pygame.font.Font(None, 36).render("Error: Level not found", True, (255, 0, 0))
                self.screen.blit(text, (100, 100))
