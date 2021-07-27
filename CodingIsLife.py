import arcade
import pygame, spritesheet
from pygame.locals import *
#from RenPyTools import label
from bs4 import BeautifulSoup
pygame.init()

def soupTest():
    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
    print(soup.prettify())
    xmlSoup = BeautifulSoup("<tag0>Some<tag1/>bad<tag2>XML", "xml")
    print(soup.prettify())

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
def main():
    global count
    screen = pygame.display.set_mode([500, 500], RESIZABLE)
    w, h = pygame.display.get_surface().get_size()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Coding Is Life")
    # Background
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))
    
    pythonQuestionOne = [["Question 1", "DamageSelf", "DamageEnemy", "Answer 1", "Answer 2", "Answer 3", "Answer 4", "Answer 5"], ["Question 2", "Answer 1", "Answer 2", "Answer 3", "Answer 4", "Answer 5"]]


    #Main game loop
    while True:
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
                    
        count += 1
        screen.fill((50, 50, 50))
        screen.blit(background, (0,0))
        #Check for closing and resizing window events
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
        elif scene == "javaGame":
            javaGame(screen, background)
        elif scene == "pythonGame":
            pythonGame(screen, background)
        elif scene == "level":
            if language == "python":
                if level == 0:
                    level(background, player, enemy, questions[0])
                elif level == 1:
                    level(background, player, enemy, questions[1])
            elif language == "java":
                pass
                
        
            
        #Manage the fps and update the screen
        pygame.display.update()
        clock.tick(fps)
            
def mainMenu(screen, background):
    global scene
    pygame.display.set_caption('Coding is Life')
    w, h = pygame.display.get_surface().get_size()
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))

    font = pygame.font.SysFont(None, 20)
    titleFont = pygame.font.SysFont(None, 50)

    # Main Menu Background
    #background = pygame.image.load('menuBackground.png')
    #background = pygame.transform.scale(background, (w, h))
    screen.blit(background, (0, 0))
    draw_text('Coding is Life',titleFont, (255, 255, 255), screen, w/2 -100,h/2 -20)
    draw_text('Start', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 40)
    draw_text('Options', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 70)
    draw_text('Quit', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 100)
    
    startButton = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 40, 100, 20)
    optionsButton = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 70, 100, 20)
    quitButton = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 100, 100, 20)
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mx , my = pygame.mouse.get_pos()
                #If the start button is clicked, switch the scene to the start menu and exit the main menu
                if startButton.collidepoint((mx, my)):
                    arcade.play_sound(arcade.load_sound('button-30.mp3'))
                    scene = "start"
                    return True
                #If the options button is clicked, switch the scene to the options menu and exit the main menu
                elif optionsButton.collidepoint((mx, my)):
                    arcade.play_sound(arcade.load_sound('button-30.mp3'))
                    scene = "options"
                    return True
                #If the quit button is clicked close the program
                elif quitButton.collidepoint((mx, my)):
                    arcade.play_sound(arcade.load_sound('button-30.mp3'))
                    quit()

def start(screen, background):
    global scene
    w, h = pygame.display.get_surface().get_size()
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))
    fullscreen = False
    font = pygame.font.SysFont(None, 20)
    titleFont = pygame.font.SysFont(None, 50)
    
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    draw_text('Pick a language', titleFont, (255, 255, 255), screen , screen.get_width()/2 -100, screen.get_height()/2)
    draw_text('Java', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 50)
    draw_text('Python', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 70)
    draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 90)
        
    mx, my = pygame.mouse.get_pos()
    startbutton_1 = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 50, 50, 10)
    startbutton_2 = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 70, 50, 10)
    backButton = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 90, 50, 10)


    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                arcade.play_sound(arcade.load_sound('button-30.mp3'))
                scene = mainMenu(screen)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if startbutton_1.collidepoint((mx, my)):
                    arcade.play_sound(arcade.load_sound('button-30.mp3'))
                    scene = "javaGame"
                    return True
                if startbutton_2.collidepoint((mx, my)):
                    arcade.play_sound(arcade.load_sound('button-30.mp3'))
                    scene = "pythonGame"
                    return True
                if backButton.collidepoint((mx, my)):
                    arcade.play_sound(arcade.load_sound('button-30.mp3'))
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
    
    draw_text('Options', titleFont, (255, 255, 255), screen , screen.get_width()/2 -100, screen.get_height()/2)
    draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 90)
    
    mx, my = pygame.mouse.get_pos()
    backButton = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 90, 50, 10)
                
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if backButton.collidepoint((mx, my)):
                    arcade.play_sound(arcade.load_sound('button-30.mp3'))
                    scene = "mainMenu"
                    return True

def javaGame(screen, background):
    global scene
    w, h = pygame.display.get_surface().get_size()
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))
    
    font = pygame.font.SysFont(None, 20)
    titleFont = pygame.font.SysFont(None, 50)
    
    draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 90)
    
    mx, my = pygame.mouse.get_pos()
    backButton = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 90, 50, 10)
                
    #todo fill in the rest of the game
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if backButton.collidepoint((mx, my)):
                    arcade.play_sound(arcade.load_sound('button-30.mp3'))
                    scene = "start"
                    return True

def pythonGame(screen, background):
    global scene, count
    w, h = pygame.display.get_surface().get_size()
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))
    
    font = pygame.font.SysFont(None, 20)
    titleFont = pygame.font.SysFont(None, 50)
    
    draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 90)
    
    mx, my = pygame.mouse.get_pos()
    backButton = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2 + 90, 50, 10)
                
    #todo fill in the rest of the game
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if backButton.collidepoint((mx, my)):
                    arcade.play_sound(arcade.load_sound('button-30.mp3'))
                    scene = "start"
                    return True
                
    #for event in pygame.event.get():
        #pass
                
    #----Putting the sprite animations here as a filler, will move later-----#
    #Load the sprite sheet
    playerSheet = pygame.image.load("assets/dinos/DinoBlue.png").convert_alpha()
    #Create a sprite sheet object
    playerSprite = spritesheet.SpriteSheet(playerSheet)
    #Load the desired frame from the sprite sheet
    #Divide count by what factor you want to slow down the animation by
    playerFrame = playerSprite.getImage(int(count/6)%4, 24, 5)
    
    #Load the sprite sheet
    enemySheet = pygame.image.load("assets/enemies/ghost/Idle.png").convert_alpha()
    #Create a sprite sheet object
    enemySprite = spritesheet.SpriteSheet(enemySheet)
    #Load the desired frame from the sprite sheet
    #Divide count by what factor you want to slow down the animation by
    enemyFrame = enemySprite.getImage(int(count/5)%10, 10, 4)

    #Display both sprites on the screen
    screen.blit(playerFrame, (50, screen.get_height()/2))
    screen.blit(enemyFrame, (screen.get_width() - 200, screen.get_height()/2))

    
def battle(screen, background, player, enemy, questions):
    global scene
    screen.fill((50, 50, 50))
    screen.blit(background, (0, 0))
    #Display player, enemy, HUD
    #Check for events
        #Check if correct is hit
        #Manage HP
            #Check if level completed
        
    #Moving the enemy
    
def cutscene():
    pass
    #Play a cutscene
    #Return to level select

if __name__ == '__main__':
    #GLOBAL VARIABLES
    global scene, language, level, fps, count
    #Which scene the user is on
    scene = "mainMenu"
    #Which language is being practiced, irrelevant if in a menu
    language = "python"
    #Which level is being played, irrelevant if in a menu
    level = 0
    #max frames per second
    fps = 60
    #number of frames elapsed
    count = 0
    
    main()
    quit()
