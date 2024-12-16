import pygame

# all the background images are loaded here
start = pygame.image.load("level_1/start-bg.png").convert()
start_scaled = pygame.transform.scale(start, (800, 600))
back = pygame.image.load("level_1/back-bg.png").convert()
back_scaled = pygame.transform.scale(back, (800, 600))
front = pygame.image.load("level_1/front-bg.png").convert()
front_scaled = pygame.transform.scale(front, (800, 600))
kitchen = pygame.image.load("level_1/kitchen-bg.png").convert()
kitchen_scaled = pygame.transform.scale(kitchen, (800, 600))
left = pygame.image.load("level_1/left-bg.png").convert()
left_scaled = pygame.transform.scale(left, (800, 600))
right = pygame.image.load("level_1/right-bg.png").convert()
right_scaled = pygame.transform.scale(right, (800, 600))
nav = pygame.image.load("level_1/nav-bg.png").convert()
nav_scaled = pygame.transform.scale(nav, (800, 600))
nav_closeup = pygame.image.load("level_1/nav-closeup.png").convert()
nav_closeup_scaled = pygame.transform.scale(nav_closeup, (800, 600))
dining = pygame.image.load("level_1/dining-bg.png").convert()
dining_scaled = pygame.transform.scale(dining, (800, 600))

# bgs array is used to store all the background images

backgrounds = [start_scaled, back_scaled, front_scaled, kitchen_scaled, left_scaled, right_scaled, nav_scaled,
               nav_closeup_scaled, dining_scaled]
# 0 - start
# 1 - back
# 2 - front
# 3 - kitchen
# 4 - left
# 5 - right
# 6 - nav
# 7 - nav_closeup
# 8 - dining

screen_rect = pygame.display.set_mode((1280, 720)).get_rect()

# all of the changes in the backgrounds
nav_closeup_display = pygame.image.load("level_1/nav-closeup-display.png").convert_alpha()
nav_closeup_display_scaled = pygame.transform.scale(nav_closeup_display, (300, 225))

interactive = {"nav_closeup_display_scaled": 0, }


# var current is used to store the current background image
class Level1:
    screen: pygame.Surface

    def coor_click(self, event, x, y, size):
        x = screen_rect.centerx + x
        y = screen_rect.centery + y
        if x >= screen_rect.centerx and y <= screen_rect.centery:
            if x <= event.pos[0] <= x + size and y <= event.pos[1] <= y + size:
                return 1
        if x <= screen_rect.centerx and y <= screen_rect.centery:
            if x - size <= event.pos[0] <= x and y <= event.pos[1] <= y + size:
                return 1
        if x >= screen_rect.centerx and y >= screen_rect.centery:
            if x <= event.pos[0] <= x + size and y - size <= event.pos[1] <= y:
                return 1
        if x <= screen_rect.centerx and y >= screen_rect.centery:
            if x - size <= event.pos[0] <= x and y - size <= event.pos[1] <= y:
                return 1

        return 0

    def right_click(self, event):
        if screen_rect.centerx + 350 <= event.pos[
            0] <= screen_rect.centerx + 400 and screen_rect.centery - 300 <= event.pos[
            1] <= screen_rect.centery + 300:
            return 1
        return 0

    def left_click(self, event):
        if screen_rect.centerx - 400 <= event.pos[
            0] <= screen_rect.centerx - 350 and screen_rect.centery - 300 <= event.pos[
            1] <= screen_rect.centery + 300:
            return 1
        return 0

    def bottom_click(self, event):
        if screen_rect.centerx - 350 <= event.pos[0] <= screen_rect.centerx + 350 and screen_rect.centery + 250 <= \
                event.pos[1] <= screen_rect.centery + 300:
            return 1
        return 0

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.current_bg = 0

    def inputs(self):
        # different cases for different backgrounds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            # events in the first background - cockpit
            if self.current_bg == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.left_click(event):
                        self.current_bg = 5

                    if self.right_click(event):
                        self.current_bg = 4

                    if self.bottom_click(event):
                        self.current_bg = 1

                    if self.coor_click(event, 45, 45, 200):
                        self.current_bg = 6

            # for events in the back
            elif self.current_bg == 1:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.bottom_click(event):
                        self.current_bg = 0

            # for events in the front
            elif self.current_bg == 2:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.left_click(event):
                        self.current_bg = 5
                    if self.right_click(event):
                        self.current_bg = 4

            # for events on the right
            elif self.current_bg == 4:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.left_click(event):
                        self.current_bg = 0

                    if self.right_click(event):
                        self.current_bg = 2

            # for events on the left
            elif self.current_bg == 5:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.right_click(event):
                        self.current_bg = 0

                    if self.left_click(event):
                        self.current_bg = 2

            # for events in the navigation
            elif self.current_bg == 6:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.bottom_click(event):
                        self.current_bg = 0

                    if self.coor_click(event, 45, 0, 150):
                        self.current_bg = 3

                    if self.coor_click(event, 1, -200, 200):
                        self.current_bg = 7

            # for events in the navigation closeup
            elif self.current_bg == 7:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.bottom_click(event):
                        self.current_bg = 6
                    if self.coor_click(event, 100, 0, 150):
                        if interactive["nav_closeup_display_scaled"]:
                            interactive["nav_closeup_display_scaled"] = 0
                        else:
                            interactive["nav_closeup_display_scaled"] = 1
            # for events in the kitchen
            elif self.current_bg == 3:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.left_click(event):
                        self.current_bg = 6
                    if self.right_click(event):
                        self.current_bg = 8

            # for events in the dining room
            elif self.current_bg == 8:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.left_click(event):
                        self.current_bg = 3

    def graphics(self):
        # after fill add the current background image
        self.screen.fill((0, 0, 0))
        self.screen.blit(backgrounds[self.current_bg],
                         (screen_rect.centerx - 400, screen_rect.centery - 300))
        if self.current_bg == 7 and interactive["nav_closeup_display_scaled"]:
            self.screen.blit(nav_closeup_display_scaled, (screen_rect.centerx - 50, screen_rect.centery - 160))
