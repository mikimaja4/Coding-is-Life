import pygame

pygame.init()

CLOCK = pygame.time.Clock()
FPS = 60

# game window size
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# base background
bg1_img = pygame.image.load('assets/Hills Layer 01.png')
bg1 = pygame.transform.scale(bg1_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg2_img = pygame.image.load('assets/Hills Layer 02.png')
bg2 = pygame.transform.scale(bg2_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg3_img = pygame.image.load('assets/Hills Layer 03.png')
bg3 = pygame.transform.scale(bg3_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg4_img = pygame.image.load('assets/Hills Layer 04.png')
bg4 = pygame.transform.scale(bg4_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg5_img = pygame.image.load('assets/Hills Layer 05.png')
bg5 = pygame.transform.scale(bg5_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg6_img = pygame.image.load('assets/Hills Layer 06.png')
bg6 = pygame.transform.scale(bg6_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# animated clouds

# icons

x = 0

running = True
while running:

    rel_x = x % bg2.get_rect().width

    screen.blit(bg1, (0, 0))
    screen.blit(bg2, (rel_x - x % bg2.get_rect().width, 0))
    screen.blit(bg3, (0, 0))
    screen.blit(bg4, (0, 0))
    screen.blit(bg5, (0, 0))
    screen.blit(bg6, (0, 0))

    x -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # one pixel to the left for every iteration

        pygame.display.update()
        CLOCK.tick(FPS)