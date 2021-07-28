import arcade
import pygame, spritesheet
from pygame.locals import *
from tkinter import *
from pygame import mixer
# from RenPyTools import label
from bs4 import BeautifulSoup

root=Tk()
pygame.init()


def soupTest():
    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
    print(soup.prettify())
    xmlSoup = BeautifulSoup("<tag0>Some<tag1/>bad<tag2>XML", "xml")
    print(soup.prettify())


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


def main():
    global count, language, level, scene
    screen = pygame.display.set_mode([500, 500], RESIZABLE)
    w, h = pygame.display.get_surface().get_size()
    # Background
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))

    clock = pygame.time.Clock()
    pygame.display.set_caption("Coding Is Life")

    player = 'FILLER'
    # Create a new Enemy class to easily fill this array
    pythonEnemies = []
    # Create a new question class rather than using an array
    pythonQuestions = [
        ["Question 1", "DamageSelf", "DamageEnemy", "Answer 1", "Answer 2", "Answer 3", "Answer 4", "Answer 5"],
        ["Question 2", "Answer 1", "Answer 2", "Answer 3", "Answer 4", "Answer 5"]]
    # Need to load each background into this array
    pythonBackgrounds = [background]

    # Main game loop
    while True:

        count += 1
        screen.fill((50, 50, 50))
        screen.blit(background, (0, 0))
        # Check for closing window event
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quit")
                return False

        if scene == "mainMenu":
            mainMenu(screen, background)
        elif scene == "start":
            start(screen, background)
        elif scene == "options":
            options(screen, background)
        elif scene == "pythonGame":
            pythonGame(screen, background)
        elif scene == "javaGame":
            javaGame(screen, background)
        elif scene == "battle":
            # Call battle() using the list of language and level dependent backgrounds and enemies
            if language == "python":
                battle(screen, level, player, pythonEnemies, pythonQuestions, pythonBackgrounds)
            # elif language == "Java":
            # battle(screen, level, player, javaEnemies, javaQuestions, javaBackgrounds)

        # Manage the fps and update the screen
        pygame.display.update()
        clock.tick(fps)


def game_background():
    clock = pygame.time.Clock()
    fps = 60

    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 900
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # base background
    bg1_img = pygame.image.load('images/bg1/l1.jpg')
    bg1 = pygame.transform.scale(bg1_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # icons
    menubutton_img = pygame.image.load('images/button/menubutton.png')
    menubutton = pygame.transform.scale(menubutton_img, (100, 50))

    running = True
    click = False

    while running:
        clock.tick(fps)

        screen.blit(bg1, (0, 0))

        screen.blit(menubutton, (SCREEN_WIDTH - 110, 10))

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(SCREEN_WIDTH - 150, 0, 150, 100)
        if button_1.collidepoint((mx, my)):
            if click:
                pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        pygame.display.update()

    pygame.quit()


def pause():
    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 900
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background_img = pygame.image.load('images/mainbackground.png')
    background = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    message_img = pygame.image.load('images/message.png')
    message = pygame.transform.scale(message_img, (1000, 300))

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_m:
                    main()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        screen.blit(background, (0, 0))
        screen.blit(message, (SCREEN_WIDTH / 2 - 500, SCREEN_HEIGHT / 2 - 150))
        pygame.display.update()


def mainMenu(screen, background):
    global scene

    fullscreen = False
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            if not fullscreen:
                w, h = pygame.display.get_surface().get_size()
                background = pygame.transform.scale(background, (w, h))
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
    pygame.display.set_caption('Coding is Life')
    w, h = pygame.display.get_surface().get_size()
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))

    font = pygame.font.SysFont(None, 30)
    titleFont = pygame.font.SysFont(None, 50)

    # Main Menu Background
    # background = pygame.image.load('menuBackground.png')
    # background = pygame.transform.scale(background, (w, h))
    screen.blit(background, (0, 0))
    draw_text('Coding is Life', titleFont, (255, 255, 255), screen, w / 2, h / 2 - 20)
    draw_text('Start', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 25)
    draw_text('Options', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 55)
    draw_text('Quit', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 85)


    startButton = pygame.Rect(0, 0, 80, 25)
    startButton.center = (screen.get_width() / 2, screen.get_height() / 2 + 25)
    optionsButton = pygame.Rect(0, 0, 100, 25)
    optionsButton.center = (screen.get_width() / 2, screen.get_height() / 2 + 55)
    quitButton = pygame.Rect(0, 0, 100, 25)
    quitButton.center = (screen.get_width() / 2, screen.get_height() / 2 + 85)

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                # If the start button is clicked, switch the scene to the start menu and exit the main menu
                if startButton.collidepoint((mx, my)):
                    mixer.music.load('button-30.mp3')
                    scene = "start"
                    return True
                # If the options button is clicked, switch the scene to the options menu and exit the main menu
                elif optionsButton.collidepoint((mx, my)):
                    mixer.music.load('button-30.mp3')
                    scene = "options"
                    return True
                # If the quit button is clicked close the program
                elif quitButton.collidepoint((mx, my)):
                    mixer.music.load('button-30.mp3')
                    quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
    #pygame.draw.rect(screen,(2,0,0),startButton)
    #pygame.draw.rect(screen, (225, 0, 0), optionsButton)
    #pygame.draw.rect(screen, (5, 0, 0), quitButton)
    #use this to test the side

def start(screen, background):
    global scene
    w, h = pygame.display.get_surface().get_size()
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))
    fullscreen = False
    font = pygame.font.SysFont(None, 30)
    titleFont = pygame.font.SysFont(None, 50)

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    draw_text('Pick a language', titleFont, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2-20)
    draw_text('Python', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 25)
    draw_text('Java', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 55)
    draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 85)

    mx, my = pygame.mouse.get_pos()
    pythonButton = pygame.Rect(0, 0, 50, 10)
    pythonButton.center = (screen.get_width() / 2, screen.get_height() / 2 + 25)
    javaButton = pygame.Rect(0, 0, 50, 10)
    javaButton.center = (screen.get_width() / 2, screen.get_height() / 2 + 55)
    backButton = pygame.Rect(0, 0, 50, 10)
    backButton.center = (screen.get_width() / 2, screen.get_height() / 2 + 85)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                mixer.music.load('button-30.mp3')
                scene = mainMenu(screen)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if pythonButton.collidepoint((mx, my)):
                    mixer.music.load('button-30.mp3')
                    scene = "pythonGame"
                    return True
                if javaButton.collidepoint((mx, my)):
                    mixer.music.load('button-30.mp3')
                    scene = "javaGame"
                    return True
                if backButton.collidepoint((mx, my)):
                    mixer.music.load('button-30.mp3')
                    scene = "mainMenu"
                    return True


def options(screen, background):
    global scene
    w, h = pygame.display.get_surface().get_size()
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))
    fullscreen = False
    font = pygame.font.SysFont(None, 20)
    titleFont = pygame.font.SysFont(None, 50)

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))



    draw_text('Options', titleFont, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2)
    draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 90)

    mx, my = pygame.mouse.get_pos()
    backButton = pygame.Rect(0, 0, 50, 10)
    backButton.center = (screen.get_width() / 2, screen.get_height() / 2 + 90)

    scale = Scale (root, from_ =0, to = 100, orient=HORIZONTAL, var= set_vol)
    scale.pack(anchor=CENTER)
    root.mainloop()
    #todo make the scale look more appealing and also make it load on the same window as the game

    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if backButton.collidepoint((mx, my)):
                    mixer.music.load('button-30.mp3')
                    scene = "mainMenu"
                    return True


def pythonGame(screen, background):
    global scene, count
    w, h = pygame.display.get_surface().get_size()
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))

    font = pygame.font.SysFont(None, 30)
    titleFont = pygame.font.SysFont(None, 50)

    draw_text('Levels', titleFont, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 - 150)
    levelButtons = []
    for i in range(5):
        for j in range(2):
            draw_text('Level ' + str((i + 1) + (j * 5)), font, (255, 255, 255), screen,
                      screen.get_width() / 2 - 50 + (j * 100), screen.get_height() / 2 - 85 + (i * 30))
            # Create the rectangle for click detection of the current level
            newButton = pygame.Rect(0, 0, 50, 10)
            # Center the button in the correct spot
            newButton.center = (screen.get_width() / 2 + 50 - (j * 100), screen.get_height() / 2 - 85 + (i * 30))
            levelButtons.append(newButton)

    draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 90)
    backButton = pygame.Rect(0, 0, 50, 10)
    backButton.center = (screen.get_width() / 2, screen.get_height() / 2 + 90)

    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                if backButton.collidepoint((mx, my)):
                    mixer.music.load('button-30.mp3')
                    scene = "start"
                    return True
                # Check if any of the level buttons have been clicked
                for i in range(len(levelButtons)):
                    game_background()
                    # Also need to check if the level has been unlocked yet
                    if levelButtons[i].collidepoint((mx, my)):
                        mixer.music.load('button-30.mp3')
                        scene = "battle"
                        language = "python"
                        level = i + 1


def javaGame(screen, background):
    global scene
    w, h = pygame.display.get_surface().get_size()
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))

    font = pygame.font.SysFont(None, 20)
    titleFont = pygame.font.SysFont(None, 50)

    draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 90)

    mx, my = pygame.mouse.get_pos()
    backButton = pygame.Rect(0, 0, 50, 10)
    backButton.center = (screen.get_width() / 2, screen.get_height() / 2 + 90)

    # todo fill in the rest of the game
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if backButton.collidepoint((mx, my)):
                    mixer.music.load('button-30.mp3')
                    scene = "start"
                    return True

# testing
def battle(screen, level, player, enemyList, questionList, backgroundList):
    global scene
    screen.fill((50, 50, 50))
    # TEMPORARY TO REMOVE LATER
    w, h = pygame.display.get_surface().get_size()
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))

    screen.blit(background, (0, 0))
    # Display player, enemy, HUD
    # Check for events
    # Check if correct is hit
    # Manage HP
    # Check if level completed

    # Moving the enemy

    # ----Putting the sprite animations here as a filler, will move later-----#
    # Load the sprite sheet
    playerSheet = pygame.image.load("assets/dinos/DinoBlue.png").convert_alpha()
    # Create a sprite sheet object
    playerSprite = spritesheet.SpriteSheet(playerSheet)
    # Load the desired frame from the sprite sheet
    # Divide count by what factor you want to slow down the animation by
    playerFrame = playerSprite.getImage(int(count / 6) % 4, 24, 5)

    # Load the sprite sheet
    enemySheet = pygame.image.load("assets/enemies/ghost/Idle.png").convert_alpha()
    # Create a sprite sheet object
    enemySprite = spritesheet.SpriteSheet(enemySheet)
    # Load the desired frame from the sprite sheet
    # Divide count by what factor you want to slow down the animation by
    enemyFrame = enemySprite.getImage(int(count / 5) % 10, 10, 4)

    # Display both sprites on the screen
    screen.blit(playerFrame, (50, screen.get_height() / 2))
    screen.blit(enemyFrame, (screen.get_width() - 200, screen.get_height() / 2))


def cutscene():
    pass
    # Play a cutscene
    # Return to level select

def play_music():
    if scene=="mainMenu":
        mixer.music.load('Music')
    if language == "python" & level == 1:
        mixer.music.load('music')
    #do this for all levels or whatever has different audio

def stop_music():
    #arcade.stop?
    pass

def set_vol(value):
    volume= int(value) / 100
    mixer.music.set_volume(value)

if __name__ == '__main__':
    # GLOBAL VARIABLES
    global scene, language, level, fps, count
    # Which scene the user is on
    scene = "mainMenu"
    # Which language is being practiced, irrelevant if in a menu
    language = "python"
    # Which level is being played, irrelevant if in a menu
    level = 0
    # max frames per second
    fps = 120
    # number of frames elapsed
    count = 0

    main()
    quit()

