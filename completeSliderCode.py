import pygame, math, sys, os

import CodingIsLife

pygame.init()
screen = pygame.display.set_mode([1280, 720])
w, h = pygame.display.get_surface().get_size()
background = pygame.image.load('menuBackground.png')
background = pygame.transform.scale(background, (w, h))
fullscreen = False
font = pygame.font.SysFont(None, 20)
titleFont = pygame.font.SysFont(None, 50)

screen.fill((0, 0, 0))
screen.blit(background, (0, 0))

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

flow = False  # controls type of color flow



class Slider():
    def __init__(self, name, val, maxi, mini, pos):
        self.val = val  # start value
        self.maxi = maxi  # maximum at slider position right
        self.mini = mini  # minimum at slider position left
        self.xpos = 590 # x-location on screen
        self.ypos = 350
        self.surf = pygame.surface.Surface((100, 50))
        self.hit = False  # the hit attribute indicates slider movement due to mouse interaction

        self.txt_surf = font.render(name, 1, WHITE)
        self.txt_rect = self.txt_surf.get_rect(center=(50, 15))

        # Static graphics - slider background #
        self.surf.fill((42, 168, 80))
        #white border of the box
        pygame.draw.rect(self.surf, WHITE, [0, 0, 100, 50], 3)
        # white background of the slider bar
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
        screen.blit(surf, (590,350))

    def move(self):
        """
    The dynamic part; reacts to movement of the slider button.
    """
        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / 80 * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi



clock = pygame.time.Clock()



musicVolume = Slider("Music Volume", 3.14, 6, 0.3, 650)
slides = [musicVolume]
speed = Slider("Speed", 50, 150, 10, 775)


num = 0
CodingIsLife.draw_text('Options', titleFont, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 - 80)
CodingIsLife.draw_text('Music', font, (255, 255, 255), screen, screen.get_width() / 2 - 120, screen.get_height() / 2)
CodingIsLife.draw_text('Sound Fx', font, (255, 255, 255), screen, screen.get_width() / 2 - 135, screen.get_height() / 2 + 60)
CodingIsLife.draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 120)

mx, my = pygame.mouse.get_pos()
backButton = pygame.Rect(0, 0, 50, 30)
backButton.center = (screen.get_width() / 2, screen.get_height() / 2 + 120)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
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

    # Update screen
    #screen.fill(BLACK)
    num += 2


    for s in slides:
        s.draw()

    pygame.display.flip()
    clock.tick(speed.val)