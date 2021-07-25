import pygame

pygame.init()

# game window size
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# base background
bg1_img = pygame.image.load('assets/bg1/l1.png')
bg1 = pygame.transform.scale(bg1_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg2_img = pygame.image.load('assets/bg1/l2.png')
bg2 = pygame.transform.scale(bg2_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg3_img = pygame.image.load('assets/bg1/l3.png')
bg3 = pygame.transform.scale(bg3_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg4_img = pygame.image.load('assets/bg1/l4.png')
bg4 = pygame.transform.scale(bg4_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg5_img = pygame.image.load('assets/bg1/l5.png')
bg5 = pygame.transform.scale(bg5_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg6_img = pygame.image.load('assets/bg1/l6.png')
bg6 = pygame.transform.scale(bg6_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# icons
settings_img = pygame.image.load('assets/settings.png')
settings = pygame.transform.scale(settings_img, (50, 50))

# button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()

        # position top left
        self.rect.topleft = (x, y)

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # if mouse is over the icon
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        # will return true if icon is clicked
        return action

# button instances
settings_button = Button(SCREEN_WIDTH - 50, 0, settings)

running = True
while running:

    # if the settings button is clicked
    if settings_button.draw() == True:
        # navigate to settings page
        print('clicked')

    screen.blit(bg1, (0, 0))
    screen.blit(bg2, (0, 0))
    screen.blit(bg3, (0, 0))
    screen.blit(bg4, (0, 0))
    screen.blit(bg5, (0, 0))
    screen.blit(bg6, (0, 0))

    settings_button.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # one pixel to the left for every iteration

    pygame.display.update()

pygame.quit()
