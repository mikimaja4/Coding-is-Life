import os, pygame, arcade, spritesheet, entity, button, dropDown, random
#from tkinter import *
#import pyrebase
from pygame.locals import *
#from kivy.clock import Clock
#from kivy.core.audio import SoundLoader
#from kivy.properties import ObjectProperty
#from kivymd.app import MDApp
#from kivymd.uix.screen import Screen
#from kivymd.uix.slider import MDSlider
#from pygame import mixer
from screeninfo import get_monitors

#firebaseConfig={
#    'apiKey': "AIzaSyCuxC-0j2O56CPFFxItN0T4ceBBk1Tlx0A",
#    'authDomain': "mikimaja4.firebaseapp.com",
#    'projectId': "mikimaja4",
#    'storageBucket': "mikimaja4.appspot.com",
#    'messagingSenderId': "830412228972",
#    'appId': "1:830412228972:web:749ba573958dea2018cb49",
#    'measurementId': "G-MYYGZFD8GT"
#}
#firebase = pyrebase.initialize_app(firebaseConfig)

#db = firebase.database()
#auth = firebase.auth()
#storage = firebase.storage()
import dropDown
import slider

monitors = get_monitors() # Get the resolution of all of the users monitors
w = monitors[0].width # Get width of first monitor found
h = monitors[0].height # Get height of first monitor found
pos_x = w/2 - 800 # Calculate the x-location
pos_y = h/2 - 450 # Calculate the y-location
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y) # Set pygame window location

#root=Tk()
pygame.init()

#Use pygame.mixer to play the input sound. **USE .wav**
def play(filename, volume):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    return True


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)
    
#Draw a box with rounded edges centered at x,y
def drawTextBox(screen, x, y, width, height, text = ''):
        thickness = 4
        roundness = 6
        #Create and color the surface for the box
        box = pygame.Surface((width, height))
        box.fill((255,255,255))
        #Display the filled surface on the input surface
        screen.blit(box, (x - width/2, y - height/2))
        #Draw the outline on the input surface
        boxRect = pygame.Rect(x - width/2 - thickness/2, y - height/2 - thickness/2, width + thickness, height + thickness)
        pygame.draw.rect(screen, (0,0,0), boxRect, thickness, roundness)
        #Draw the text if provided
        questionFont = pygame.font.Font(None, 25)

        lines = text.splitlines()
        spacing = 20
        y -= height * .33
        #Add a new line before the text, not sure if theres a better way to do this
        if len(lines) == 1:
            lines.append(lines[0])
            lines[0] = ''
        for line in lines:
            draw_text(line, questionFont, (0,0,0), screen, x, y)
            y += spacing

        #Return the rect object for collision detection
        return (boxRect, text)


def main():
    global count, language, level, scene
    screen = pygame.display.set_mode([960, 540], RESIZABLE)
    w, h = pygame.display.get_surface().get_size()
    #Set the background and adjust its size
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))

    clock = pygame.time.Clock()
    pygame.display.set_caption("Coding Is Life")

    #Create the players entity object
    player = entity.Entity(50, screen.get_height() / 2, 6, "assets/dinos/DinoBlueIdle.png", 4, "assets/dinos/DinoBlueMoving.png", 6, "assets/dinos/DinoBlueHit.png", 3)
    #Create the enemy entity objects
    pythonEnemies = []
    pythonEnemies.append(entity.Entity(screen.get_width() - 200, screen.get_height() / 2, 6, "assets/enemies/AngryPig/Idle.png", 9, "assets/enemies/AngryPig/Moving.png", 16, "assets/enemies/AngryPig/Hit.png", 5))
    pythonEnemies.append(entity.Entity(screen.get_width() - 200, screen.get_height() / 2, 6, "assets/enemies/Bat/Idle.png", 12, "assets/enemies/Bat/Moving.png", 7, "assets/enemies/Bat/Hit.png", 5))
    pythonEnemies.append(entity.Entity(screen.get_width() - 200, screen.get_height() / 2, 6, "assets/enemies/Bee/Idle.png", 6, "assets/enemies/Bee/Moving.png", 6, "assets/enemies/Bee/Hit.png", 5))
    pythonEnemies.append(entity.Entity(screen.get_width() - 200, screen.get_height() / 2, 6, "assets/enemies/BlueBird/Idle.png", 9, "assets/enemies/BlueBird/Moving.png", 9, "assets/enemies/BlueBird/Hit.png", 5))
    pythonEnemies.append(entity.Entity(screen.get_width() - 200, screen.get_height() / 2, 6, "assets/enemies/Bunny/Idle.png", 8, "assets/enemies/Bunny/Moving.png", 12, "assets/enemies/Bunny/Hit.png", 5))
    #For some reason the Chameleon gets placed an additional ~200 pixels right and idk why
    pythonEnemies.append(entity.Entity(screen.get_width() - 400, screen.get_height() / 2, 6, "assets/enemies/Chameleon/Idle.png", 13, "assets/enemies/Chameleon/Moving.png", 8, "assets/enemies/Chameleon/Hit.png", 5))
    pythonEnemies.append(entity.Entity(screen.get_width() - 200, screen.get_height() / 2, 6, "assets/enemies/Chicken/Idle.png", 13, "assets/enemies/Chicken/Moving.png", 14, "assets/enemies/Chicken/Hit.png", 5))
    pythonEnemies.append(entity.Entity(screen.get_width() - 200, screen.get_height() / 2, 6, "assets/enemies/Duck/Idle.png", 10, "assets/enemies/Duck/Moving.png", 10, "assets/enemies/Duck/Hit.png", 5))
    pythonEnemies.append(entity.Entity(screen.get_width() - 200, screen.get_height() / 2, 6, "assets/enemies/FatBird/Idle.png", 8, "assets/enemies/FatBird/Moving.png", 8, "assets/enemies/FatBird/Hit.png", 5))
    pythonEnemies.append(entity.Entity(screen.get_width() - 200, screen.get_height() / 2, 6, "assets/enemies/Ghost/Idle.png", 10, "assets/enemies/Ghost/Moving.png", 10, "assets/enemies/Ghost/Hit.png", 5))
    # Create a new question class rather than using an array
    pythonQuestions = [
        ['What is the value of x after the following statements?\nx = 10\ny=2\nx = x + y', '12', '10', '2', '102'],
        ['A variable can hold more than one value.\nTrue or False?', 'False', 'True'],
        ['Which of the following variables holds a string?', 'z = \'python\'', 'x = True', 'y = 7.29'],
        ['Which of the following variable names (identifiers) is invalid?', '9lives', '_cat4', 'meowtime', 'number_of_kittens'],
        ['Is x + y = 2 + 5 a valid assignment statement?', 'Invalid', 'Valid'],
        ['Which of the following is an invalid assignment statement?', 'x + 3 = 10', 'x = 4', 'x = y', 'x = y + 4'],
        ['What is the value of sum after the following statements?\nx = 10\nsum = x + 20', '30', '10', '20'],
        ['Which of the following is not a numeric data type?', 'boolean', 'int', 'float', 'long'],
        ['Given the following assignments, which of the following is a valid operation?\ntext = \'some words\'\nletter = \'c\'\nnumber = 27\ndigits = 9000', 'number + digits', 'text + letter', 'number + text', 'letter + digits'],
        ['What will bee the output after following statements?\nx = \'Hello\'\ny = \'world!\'\nprint(x, y)', 'Hello world!', 'Helloworld!', 'Hello, world!', 'Hello,world!']]
    # Need to load each background into this array
    pythonBackgrounds = [
        'images/bg1/l1.jpg',
        'images/bg1/l11.jpg',
        'images/bg1/l3.png',
        'images/bg1/l4.png',
        'images/bg1/l5.jpg',
        'images/bg1/l6.jpg',
        'images/bg1/l7.jpg',
        'images/bg1/l8.jpg',
        'images/bg1/l17.jpg',
        'images/bg1/l16.jpg'
    ]

    # Main game loop
    while True:

        count += 1
        screen.fill((50, 50, 50))
        screen.blit(background, (0, 0))
        #Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quit")
                return False
            if event.type == pygame.VIDEORESIZE:
                w, h = pygame.display.get_surface().get_size()
                #Adjust the size of the background
                background = pygame.image.load('menuBackground.png')
                background = pygame.transform.scale(background, (w, h))
                if scene == "battle":                    
                    #Adjust the player position, x is constant
                    player.y = screen.get_height() / 2
                    #Adjust the position of the enemy, both x and y
                    if language == "python":
                        print(level)
                        pythonEnemies[level].x = screen.get_width() - 200
                        pythonEnemies[level].y = screen.get_height() / 2
                    elif language == "java":
                        javaEnemies[level].x = screen.get_width() - 200
                        javaEnemies[level].y = screen.get_height() / 2

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
                #Might need to use the returned values from battle when dealing with hp, not sure atm
                battleReturn = battle(screen, level, player, pythonEnemies, pythonQuestions, pythonBackgrounds)
        elif scene == "pause":
            pause(screen)
        elif scene == "gameOver":
            gameOver(screen)

        # Manage the fps and update the screen
        pygame.display.update()
        clock.tick(fps)

def pause(screen):
    global scene, language
    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 900
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background_img = pygame.image.load('images/mainbackground.png')
    background = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    message_img = pygame.image.load('images/message.png')
    message = pygame.transform.scale(message_img, (1000, 300))

    play_img = pygame.image.load('images/PlayButton.png')
    play = pygame.transform.scale(play_img, (350, 150))

    exit_img = pygame.image.load('images/ExitButton.png')
    exit = pygame.transform.scale(exit_img, (350, 150))

    menu_img = pygame.image.load('images/MenuButton.png')
    menu = pygame.transform.scale(menu_img, (350, 150))

    button_play = pygame.Rect(SCREEN_WIDTH - 150, 0, 150, 100)
    button_menu = pygame.Rect(SCREEN_WIDTH - 150, 0, 150, 100)
    button_exit = pygame.Rect(SCREEN_WIDTH - 150, 0, 150, 100)


    button_play_collide = pygame.Rect(SCREEN_WIDTH / 2 - 575, SCREEN_HEIGHT / 2 - 75, 350, 150)
    button_menu_collide = pygame.Rect(SCREEN_WIDTH / 2 - 175, SCREEN_HEIGHT / 2 - 75, 350, 150)
    button_exit_collide = pygame.Rect(SCREEN_WIDTH / 2 + 225, SCREEN_HEIGHT / 2 - 75, 350, 150)
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                return True
            elif event.key == pygame.K_m:
                if language == "python":
                    scene = "pythonGame"
                elif language == "java":
                    scene = "javaGame"
                return True
            elif event.key == pygame.K_q:
                pygame.quit()
                quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_play_collide.collidepoint((mx, my)):
                scene = "battle"
                return True
            if button_menu_collide.collidepoint((mx, my)):
                if language == "python":
                    scene = "pythonGame"
                elif language == "java":
                    scene = "javaGame"
                print("menu")
                return True
            if button_exit_collide.collidepoint((mx, my)):
                pygame.quit()
                quit()

        screen.blit(background, (0, 0))
        #screen.blit(message, (SCREEN_WIDTH / 2 - 500, SCREEN_HEIGHT / 2 - 350))

        screen.blit(play, (SCREEN_WIDTH / 2 - 575, SCREEN_HEIGHT / 2 - 75))
        screen.blit(menu, (SCREEN_WIDTH / 2 - 175, SCREEN_HEIGHT / 2 - 75))
        screen.blit(exit, (SCREEN_WIDTH / 2 + 225, SCREEN_HEIGHT / 2 - 75))

        pygame.display.update()
        

def gameOver(screen):
    global scene

    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 900
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background_img = pygame.image.load('images/mainbackground.png')
    background = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    gameover_img = pygame.image.load('images/GameOver.png')
    gameover = pygame.transform.scale(gameover_img, (1000, 200))

    exit_img = pygame.image.load('images/ExitButton.png')
    exit = pygame.transform.scale(exit_img, (350, 150))

    menu_img = pygame.image.load('images/MenuButton.png')
    menu = pygame.transform.scale(menu_img, (350, 150))

    run = True
    while run:

        button_menu_collide = pygame.Rect(SCREEN_WIDTH / 2 - 375, SCREEN_HEIGHT / 2 - 75, 350, 150)
        button_exit_collide = pygame.Rect(SCREEN_WIDTH / 2 + 25, SCREEN_HEIGHT / 2 - 75, 350, 150)
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_menu_collide.collidepoint((mx, my)):
                    main()
                if button_exit_collide.collidepoint((mx, my)):
                    quit()

        screen.blit(background, (0, 0))
        screen.blit(gameover, (SCREEN_WIDTH / 2 - 500, SCREEN_HEIGHT / 2 - 350))
        screen.blit(menu, (SCREEN_WIDTH / 2 - 375, SCREEN_HEIGHT / 2 - 75))
        screen.blit(exit, (SCREEN_WIDTH / 2 + 25, SCREEN_HEIGHT / 2 - 75))

        pygame.display.update()


def mainMenu(screen, background):
    global scene

    pygame.display.set_caption('Coding is Life')
    w, h = pygame.display.get_surface().get_size()
    #Set the background and adjust its size
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))
    screen.blit(background, (0, 0))

    #Testing exit button
    #Todo figure out why the button image wont load... or why it breaks the program
    exit_img= pygame.image.load('images/button/exit.png').convert_alpha()
    exit_button = button.Button(screen.get_width() / 2, screen.get_height() / 2 + 85, exit_img, 0.2)
    #pygame.draw.rect(screen, (2, 0, 0), exit_button)
    #screen.blit(exit_button, (screen.get_width() / 2, screen.get_height() / 2 + 85))

    #quitButtonUI = pygame.image.load('images/SmallEmptyButton.png')
    #quitButtonIcon = pygame.transform.scale(quitButtonUI, (100, 50))


    font = pygame.font.SysFont(None, 30)
    titleFont = pygame.font.SysFont(None, 50)


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

    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            w, h = pygame.display.get_surface().get_size()
            background = pygame.image.load('menuBackground.png')
            background = pygame.transform.scale(background, (w, h))
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                # If the start button is clicked, switch the scene to the start menu and exit the main menu
                if startButton.collidepoint((mx, my)):
                    play('buttonClick.wav', 0.5)
                    scene = "start"
                    return True
                # If the options button is clicked, switch the scene to the options menu and exit the main menu
                elif optionsButton.collidepoint((mx, my)):
                    play('buttonClick.wav', 0.5)
                    scene = "options"
                    return True
                # If the quit button is clicked close the program
                elif quitButton.collidepoint((mx, my)):
                    play('buttonClick.wav', 0.5)
                    pygame.quit()
                    quit()

    #pygame.draw.rect(screen,(2,0,0),exit_button)
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
                play('buttonClick.wav', 0.5)
                scene = mainMenu(screen)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if pythonButton.collidepoint((mx, my)):
                    play('buttonClick.wav', 0.5)
                    scene = "pythonGame"
                    return True
                if javaButton.collidepoint((mx, my)):
                    play('buttonClick.wav', 0.5)
                    scene = "javaGame"
                    return True
                if backButton.collidepoint((mx, my)):
                    play('buttonClick.wav', 0.5)
                    scene = "mainMenu"
                    return True


def options(screen, background):
    global scene
    w, h = pygame.display.get_surface().get_size()
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))
    fullscreen = False
    font = pygame.font.SysFont(None, 30)
    titleFont = pygame.font.SysFont(None, 50)

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    draw_text('Options', titleFont, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 -100)
    draw_text('Music', font, (255, 255, 255), screen, screen.get_width() / 2 -110, screen.get_height() / 2 -50)
    draw_text('Sound Fx', font, (255, 255, 255), screen, screen.get_width() / 2 -125, screen.get_height() / 2 -10)
    #draw_text('Refresh Rate', font, (255, 255, 255), screen, screen.get_width() / 2 -140, screen.get_height() / 2 +30)
    draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 120)

    mx, my = pygame.mouse.get_pos()
    backButton = pygame.Rect(0, 0, 50, 30)
    backButton.center = (screen.get_width() / 2, screen.get_height() / 2 + 120)

    #TODO fix the slider so it shows on the game background
    #slider test begin
    #font = pygame.font.SysFont("Verdana", 12)

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
    #clock = pygame.time.Clock()

    COLORS = [MAGENTA, RED, YELLOW, GREEN, CYAN, BLUE]
    #xcolor = Gradient(COLORS, X).gradient

    #pen = slider.Slider("Pen", 10, 15, 1, 25)
    #freq = slider.Slider("Freq", 1, 3, 0.2, 150)
    #jmp = slider.Slider("Jump", 10, 20, 1, 275)
    #size = slider.Slider("Size", 200, 200, 20, 400)
    #focus = slider.Slider("Focus", 0, 6, 0, 525)
    #phase = slider.Slider("Phase", 3.14, 6, 0.3, 650)
    #speed = slider.Slider("Speed", 50, 150, 10, 775)
    #slides = [pen, freq, jmp, size, focus, phase, speed]

    #num = 0

    #while True:
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
              #  pygame.quit()
             #   exit()
            #elif event.type == pygame.MOUSEBUTTONDOWN:
               # pos = pygame.mouse.get_pos()
              #  for s in slides:
             #       if s.button_rect.collidepoint(pos):
            #            s.hit = True
           # elif event.type == pygame.MOUSEBUTTONUP:
         #       for s in slides:
          #          s.hit = False

        # Move slides
        #for s in slides:
         #   if s.hit:
          #      s.move()

        # Update screen
        #num += 2

        #for s in slides:
        #    s.draw()

        #pygame.display.flip()
        #clock.tick(speed.val)
    #slider end

    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if backButton.collidepoint((mx, my)):
                    play('buttonClick.wav', 0.5)
                    scene = "mainMenu"
                    return True
    # part of drop down
    #COLOR_INACTIVE = (84, 166, 55)
    #COLOR_ACTIVE = (137, 230, 102)
    #COLOR_LIST_INACTIVE = (255, 255, 255)
    #COLOR_LIST_ACTIVE = (137, 230, 102)

    #list1 = dropDown.DropDown(
     #   [COLOR_INACTIVE, COLOR_ACTIVE],
      #  [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
       # screen.get_width() / 2 -40, screen.get_height() / 2 +17, 100, 20,
        #pygame.font.SysFont(None, 30),
       # "FPS", ["60", "75","120","144","240"])
   # run=True
    #clock = pygame.time.Clock()
    #while run:
     #   clock.tick(30)

      #  event_list = pygame.event.get()
       # for event in event_list:
        #    if event.type == pygame.QUIT:
         #       run = False
          #  if event.type == QUIT:
           #     quit()
            #if event.type == KEYDOWN:
             #   if event.key == K_ESCAPE:
              #      quit()
            #if event.type == MOUSEBUTTONDOWN:
             #   if event.button == 1:
              #      if backButton.collidepoint((mx, my)):
               #         play('buttonClick.wav', 0.5)
                #        scene = "mainMenu"
                 #       return True

        #selected_option = list1.update(event_list)
        #if selected_option >= 0:
         #   list1.main = list1.options[selected_option]
          #  if selected_option == 0:
           #     run=False

        #list1.draw(screen)
        #pygame.display.flip()

    #todo Fix the dropdown menu to stop displaying once the new FPS is selected
    #todo link the FPS to the actual game FPS once selected
    #todo fix why the dropdown menu displays OVER The actual options menu


    #pygame.draw.rect(screen, (5, 0, 0), backButton)

    #scale = Scale (root, from_ =0, to = 100, orient=HORIZONTAL, var= set_vol)
    #scale.pack(anchor=CENTER)
    #root.mainloop()
    #todo make the scale look more appealing and also make it load on the same window as the game





def pythonGame(screen, background):
    global scene, level, count
    w, h = pygame.display.get_surface().get_size()
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    font = pygame.font.SysFont(None, 30)
    titleFont = pygame.font.SysFont(None, 50)

    draw_text('Levels', titleFont, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 - 150)
    levelButtons = []
    for i in range(5):
        draw_text('Level ' + str((i + 1)), font, (255, 255, 255), screen,
                  screen.get_width() / 2 - 50, screen.get_height() / 2 - 85 + (i * 30))
        # Create the rectangle for click detection of the current level
        newButton = pygame.Rect(0, 0, 50, 10)
        # Center the button in the correct spot
        newButton.center = (screen.get_width() / 2 - 50, screen.get_height() / 2 - 85 + (i * 30))
        levelButtons.append(newButton)
    for i in range(5):
        draw_text('Level ' + str((i + 6)), font, (255, 255, 255), screen,
                  screen.get_width() / 2 + 50, screen.get_height() / 2 - 85 + (i * 30))
        # Create the rectangle for click detection of the current level
        newButton = pygame.Rect(0, 0, 70, 15)
        # Center the button in the correct spot
        newButton.center = (screen.get_width() / 2 + 50, screen.get_height() / 2 - 85 + (i * 30))
        levelButtons.append(newButton)

    draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 90)
    backButton = pygame.Rect(0, 0, 50, 20)
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
                    play('buttonClick.wav', 0.5)
                    scene = "start"
                    return True
                    # Check if any of the level buttons have been clicked
                for i in range(len(levelButtons)):
                # Also need to check if the level has been unlocked yet
                    if levelButtons[i].collidepoint((mx, my)):
                        play('buttonClick.wav', 0.5)
                        scene = "battle"
                        language = "python"
                        level = i


def javaGame(screen, background):
    global scene
    w, h = pygame.display.get_surface().get_size()
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))

    font = pygame.font.SysFont(None, 20)
    titleFont = pygame.font.SysFont(None, 50)

    draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 90)

    mx, my = pygame.mouse.get_pos()
    backButton = pygame.Rect(0, 0, 50, 30)
    backButton.center = (screen.get_width() / 2, screen.get_height() / 2 + 120)

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
                    play('buttonClick.wav', 0.5)
                    scene = "start"
                    return True

def battle(screen, level, player, enemyList, questionList, backgroundList):
    global scene
    screen.fill((50, 50, 50))
    mx, my = pygame.mouse.get_pos()
    w, h = pygame.display.get_surface().get_size()
    #Load and display the background
    background = pygame.image.load(backgroundList[level])
    background = pygame.transform.scale(background, (w, h))
    screen.blit(background, (0, 0))

    #Load and display the menu button
    menubutton_img = pygame.image.load('images/settings.png')
    menubutton = pygame.transform.scale(menubutton_img, (50, 50))
    screen.blit(menubutton, (w - 60, 10))
    button_1 = pygame.Rect(w - 60, 10, 50, 50)

    questionDisplayOrder = questionList[:]
    random.shuffle(questionDisplayOrder)
    questionFont = pygame.font.SysFont(None, 50)
    statementsFont = pygame.font.Font("consolas.ttf", 30)

    drawTextBox(screen, w/2, 70, 500, 100, "Big box test with a lot of text\nand also a\ncouple of new lines")
    
    drawTextBox(screen, w/2 - 150, 155, 280, 50, "Medium box test for answers")
    drawTextBox(screen, w/2 + 150, 155, 280, 50, "Medium box test for answers")
    drawTextBox(screen, w/2 - 150, 220, 280, 50, "Medium box test for answers")
    drawTextBox(screen, w/2 + 150, 220, 280, 50, "Medium box test for answers")

    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            w, h = pygame.display.get_surface().get_size()
            #Adjust the size of the background
            background = pygame.image.load('menuBackground.png')
            background = pygame.transform.scale(background, (w, h))
            #Adjust the player position, x is constant
            player.y = screen.get_height() / 2
            #Adjust the position of the enemy, both x and y
            enemyList[level].x = screen.get_width() - 200
            enemyList[level].y = screen.get_height() / 2
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == K_p:
                scene = "pause"
                return True
        if event.type == MOUSEBUTTONDOWN:
            if button_1.collidepoint((mx, my)):
                scene = "pause"
                return True
            if answerBox1[0].collidepoint((mx, my)):
                print("Box 1,", answerBox1[1])
            if answerBox2[0].collidepoint((mx, my)):
                print("Box 2,", answerBox2[1])
            if answerBox3[0].collidepoint((mx, my)):
                print("Box 3,", answerBox3[1])
            if answerBox4[0].collidepoint((mx, my)):
                print("Box 4,", answerBox4[1])

    # Display player, enemy, HUD
    # Check for events
    # Check if correct is hit
    # Manage HP
    # Check if level completed

    # Moving the enemy


    #####TEST CODE TO SHOW ANIMATIONS####
    phases = ["idle", "moving", "hit"]
    phase = phases[int(count / 250 % 3)]

    ######################################

    # Display both sprites on the screen
    screen.blit(player.display(screen, .1, phase, fps), (player.x, player.y))
    screen.blit(enemyList[level].display(screen, .1, phase, fps), (enemyList[level].x, enemyList[level].y))

    #Return the updated player and enemy so that any of the changes made this frame will maintain
    return (player, enemyList)


def cutscene():
    pass
    # Play a cutscene
    # Return to level select

def play_music():
    if scene=="mainMenu":
        play('Music')
    if language == "python" & level == 1:
        play('music')
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
