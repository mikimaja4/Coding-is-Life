# Setup Python ----------------------------------------------- #
import pygame, sys
from PIL import Image

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False

def main():
    pygame.display.set_caption('Coding is Life')
    screen = pygame.display.set_mode([500, 500], RESIZABLE)
    w, h = pygame.display.get_surface().get_size()
    fullscreen = False

    font = pygame.font.SysFont(None, 20)
    titleFont = pygame.font.SysFont(None, 50)

    # Background
    background = pygame.image.load('actual game background.png')
    background = pygame.transform.scale(background, (w, h))

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        draw_text('game', font, (255, 255, 255), screen, 20, 20)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                if not fullscreen:
                    w, h = pygame.display.get_surface().get_size()
                    background = pygame.transform.scale(background, (w, h))
            if event.type == KEYDOWN:
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((monitor_size), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height), pygame.RESIZABLE)
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def main_menu():
    pygame.display.set_caption('Coding is Life')
    screen = pygame.display.set_mode([500, 500], RESIZABLE)
    w, h = pygame.display.get_surface().get_size()
    fullscreen = False

    font = pygame.font.SysFont(None, 20)
    titleFont = pygame.font.SysFont(None, 50)

    # Background
    background = pygame.image.load('actual game background.png')
    background = pygame.transform.scale(background, (w, h))

    while True:
        screen.fill((0, 0, 0))
        # Main Menu Background
        screen.blit(background, (0, 0))
        draw_text('Coding is Life',titleFont, (255, 255, 255), screen, w/2 -100,h/2 -20)
        draw_text('Start', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 40)
        draw_text('Options', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 70)
        draw_text('Quit', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 100)

        mx , my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 40, 100, 20)
        button_2 = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 70, 100, 20)
        button_3 = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 100, 100, 20)
        if button_1.collidepoint((mx , my)):
            if click:
                start()
        if button_2.collidepoint((mx , my)):
            if click:
                options()
        if button_3.collidepoint((mx , my)):
            if click:
                quit()
        #pygame.draw.rect(screen, (0, 0, 0), button_1) # todo bring the text in front of the button OR not have a colored button
        #pygame.draw.rect(screen, (0, 0, 0), button_2)
        #pygame.draw.rect(screen, (0, 0, 0), button_3)


        click = False
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                if not fullscreen:
                    w, h = pygame.display.get_surface().get_size()
                    background = pygame.transform.scale(background, (w, h))
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def start():
    running = True
    screen = pygame.display.set_mode([500, 500], RESIZABLE)
    w, h = pygame.display.get_surface().get_size()
    fullscreen = False
    background = pygame.image.load('actual game background.png')
    font = pygame.font.SysFont(None, 20)
    titleFont = pygame.font.SysFont(None, 50)
    background = pygame.transform.scale(background, (w, h))
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        draw_text('Pick a language', titleFont, (255, 255, 255), screen , screen.get_width()/2 -100, screen.get_height()/2)
        draw_text('Java', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 50)
        draw_text('Python', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 70)
        draw_text('Quit', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 90)

        mx, my = pygame.mouse.get_pos()
        startbutton_1 = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 50, 50, 10)
        startbutton_2 = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 70, 50, 10)
        startbutton_3 = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 90, 50, 10)


        if startbutton_1.collidepoint((mx, my)): #todo figure out why it is not registering the click to new menu
            if click:
                javaGame()
        if startbutton_2.collidepoint((mx, my)):
            if click:
                pythonGame()
        if startbutton_3.collidepoint((mx, my)):
            if click:
                quit()

        click = False

        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                if not fullscreen:
                    w, h = pygame.display.get_surface().get_size()
                    background = pygame.transform.scale(background, (w, h))
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
def options():
    running = True
    screen = pygame.display.set_mode([500, 500], RESIZABLE)
    w, h = pygame.display.get_surface().get_size()
    fullscreen = False
    background = pygame.image.load( 'actual game background.png')
    font = pygame.font.SysFont(None, 20)
    titleFont = pygame.font.SysFont(None, 50)
    background = pygame.transform.scale(background, (w, h))
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        draw_text('options', font, (255, 255, 255), screen, screen.get_width()/2,screen.get_height()/2)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def javaGame():
    running=True
    while running:
        screen.fill((0,0,0))
        screen.blit(background, (0, 0))
        #todo fill in the rest of the game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

    pygame.display.update()
    mainClock.tick(60)
def pythonGame():
    running=True
    while running:
        screen.fill((0,0,0))
        screen.blit(background, (0, 0))
        #todo fill in the rest of the game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

    pygame.display.update()
    mainClock.tick(60)


if __name__ == '__main__':
    main_menu()
    main()
    pygame.quit()

