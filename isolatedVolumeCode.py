import pygame
pygame.init()
screen = pygame.display.set_mode([1280, 720])
val = 0
mini = 0
maxi = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
GREEN = (42, 168, 80)
DARKGREEN= (28, 138, 61)
BLUE = (50, 50, 255)
GREY = (200, 200, 200)
ORANGE = (200, 100, 50)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
TRANS = (1, 1, 1)
mx, my = pygame.mouse.get_pos()
font = pygame.font.SysFont(None, 12)
flow = False  # controls type of color flow



class Slider():
    def __init__(self, name, val, maxi, mini, pos):
        self.val = val  # start value
        self.maxi = maxi  # maximum at slider position right
        self.mini = mini  # minimum at slider position left
        self.xpos = pos  # x-location on screen
        self.ypos = 550
        self.surf = pygame.surface.Surface((100, 50))
        self.hit = False  # the hit attribute indicates slider movement due to mouse interaction

        self.txt_surf = font.render(name, 1, WHITE)
        self.txt_rect = self.txt_surf.get_rect(center=(50, 15))

        # Static graphics - slider background #
        self.surf.fill((42, 168, 80))
        pygame.draw.rect(self.surf, WHITE, [0, 0, 100, 50], 3)
        pygame.draw.rect(self.surf, DARKGREEN, [10, 10, 80, 15], 0)
        pygame.draw.rect(self.surf, WHITE, [10, 30, 80, 5], 0)

        self.surf.blit(self.txt_surf, self.txt_rect)  # this surface never changes

        # dynamic graphics - button surface #
        self.button_surf = pygame.surface.Surface((20, 20))
        self.button_surf.fill(TRANS)
        self.button_surf.set_colorkey(TRANS)
        pygame.draw.circle(self.button_surf, BLACK, (10, 10), 5, 0)
        pygame.draw.circle(self.button_surf, DARKGREEN, (10, 10), 4, 0)

    def draw(self):
        """ Combination of static and dynamic graphics in a copy of
    the basic slide surface
    """
        # static
        surf = self.surf.copy()

        # dynamic
        pos = (10+int((self.val-self.mini)/(self.maxi-self.mini)*80), 33)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.xpos, self.ypos)  # move of button box to correct screen position

        # screen
        screen.blit(surf, (self.xpos, self.ypos))

    def move(self):
        """
    The dynamic part; reacts to movement of the slider button.
    """
        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / 80 * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi


musicVolume = Slider("Music Volume", 3.14, 6, 0.3, 650)
fxVolume = Slider("FX Volume", 50, 150, 10, 775)
slides = [fxVolume,musicVolume]
speed = Slider("Speed", 50, 150, 10, 775)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
GREEN = (42, 168, 80)
DARKGREEN = (28, 138, 61)
BLUE = (50, 50, 255)
GREY = (200, 200, 200)
ORANGE = (200, 100, 50)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
TRANS = (1, 1, 1)
clock = pygame.time.Clock()

num = 0
#For Music volume
pygame.draw.rect(screen, WHITE, [screen.get_width() / 2 - 70, screen.get_height() / 2 - 15, 150, 30], 2)
pygame.draw.rect(screen, WHITE, [screen.get_width() / 2 - 58, screen.get_height() / 2 - 3, 125, 5], 0)
musicVolumeButton = pygame.draw.circle(screen,CYAN, (screen.get_width() / 2 - 58, screen.get_height() / 2 - 1), 7, 0)

#For FX Volume
pygame.draw.rect(screen, WHITE, [screen.get_width() / 2 - 70, screen.get_height() / 2 +45, 150, 30], 2)
pygame.draw.rect(screen, WHITE, [screen.get_width() / 2 - 58, screen.get_height() / 2 + 57, 125, 5], 0)
fxVolumeButton = pygame.draw.circle(screen, CYAN, (screen.get_width() / 2 - 58, screen.get_height() / 2 + 59), 7, 0)

# dynamic graphics - button surface #
button_surf = pygame.surface.Surface((20, 20))
button_surf.fill(TRANS)
button_surf.set_colorkey(TRANS)
pygame.draw.circle(button_surf, BLACK, (10, 10), 5, 0)
#pygame.draw.circle(button_surf, DARKGREEN, (10, 10), 4, 0)

surf = screen.copy()

    # dynamic
pos = (10 + int((val - mini) / (maxi - mini) * 80), 33)
button_rect = button_surf.get_rect(center=pos)
surf.blit(button_surf, button_rect)
button_rect.move_ip(mx, my)  # move of button box to correct screen position

loc=[mx, my]
clicked= False
hit = True
while True:
    for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for s in slides:
                    if s.button_rect.collidepoint(pos):
                        s.hit = True
            elif event.type == pygame.MOUSEBUTTONUP:
                        for s in slides:
                            s.hit = False

                # Move slides
    for s in slides:
            if s.hit:
                s.move()

    pygame.display.flip()
    clock.tick(speed.val)
