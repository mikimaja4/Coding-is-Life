import os, pygame, arcade, spritesheet, entity, button, dropDown, question, questionList, health
from pygame.locals import *
# from tkinter import *
# import pyrebase
# from kivy.clock import Clock
# from kivy.core.audio import SoundLoader
# from kivy.properties import ObjectProperty
# from kivymd.app import MDApp
# from kivymd.uix.screen import Screen
# from kivymd.uix.slider import MDSlider
# from pygame import mixer
from screeninfo import get_monitors

# firebaseConfig={
#    'apiKey': "AIzaSyCuxC-0j2O56CPFFxItN0T4ceBBk1Tlx0A",
#    'authDomain': "mikimaja4.firebaseapp.com",
#    'projectId': "mikimaja4",
#    'storageBucket': "mikimaja4.appspot.com",
#    'messagingSenderId': "830412228972",
#    'appId': "1:830412228972:web:749ba573958dea2018cb49",
#    'measurementId': "G-MYYGZFD8GT"
# }
# firebase = pyrebase.initialize_app(firebaseConfig)

# db = firebase.database()
# auth = firebase.auth()
# storage = firebase.storage()

monitors = get_monitors()  # Get the resolution of all of the users monitors
w = monitors[0].width  # Get width of first monitor found
h = monitors[0].height  # Get height of first monitor found
pos_x = w / 2 - 800  # Calculate the x-location
pos_y = h / 2 - 450  # Calculate the y-location
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x, pos_y)  # Set pygame window location

# root=Tk()
pygame.init()

def main():
    global count, language, level, scene, fps
    screen = pygame.display.set_mode([1280, 720])
    w, h = pygame.display.get_surface().get_size()
    # Set the background and adjust its size
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))

    clock = pygame.time.Clock()
    pygame.display.set_caption("Coding Is Life")

    # player health system
    p_HP = health.health()
    e_HP = health.health()

    # Create the players entity object
    player = entity.Entity(50, screen.get_height() + 25, 6, 0, "assets/dinos/DinoBlueIdle.png", 4,
                           "assets/dinos/DinoBlueMoving.png", 6, "assets/dinos/DinoBlueHit.png", 3)
    # Create the enemy entity objects
    pythonEnemies = []
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 6, 10, "assets/enemies/Mushroom/Idle.png", 14,#
                      "assets/enemies/Mushroom/Moving.png", 16, "assets/enemies/Mushroom/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 6, 10, "assets/enemies/Radish/Idle.png", 6,#
                      "assets/enemies/Radish/Moving.png", 12, "assets/enemies/Radish/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 6, 10, "assets/enemies/Rocks/Idle.png", 14,#
                      "assets/enemies/Rocks/Moving.png", 14, "assets/enemies/Rocks/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 6, 10, "assets/enemies/Chicken/Idle.png", 13,#
                      "assets/enemies/Chicken/Moving.png", 14, "assets/enemies/Chicken/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 6, 10, "assets/enemies/Duck/Idle.png", 10,#
                      "assets/enemies/Duck/Moving.png", 10, "assets/enemies/Duck/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 6, 10, "assets/enemies/Rino/Idle.png", 11,#
                      "assets/enemies/Rino/Moving.png", 6, "assets/enemies/Rino/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 6, 10, "assets/enemies/Slime/Idle.png", 10,#
                      "assets/enemies/Slime/Moving.png", 10, "assets/enemies/Slime/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 6, 10, "assets/enemies/AngryPig/Idle.png", 9,#
                      "assets/enemies/AngryPig/Moving.png", 16, "assets/enemies/AngryPig/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 6, 10, "assets/enemies/Skull/Idle.png", 8,
                      "assets/enemies/Skull/Moving.png", 8, "assets/enemies/Skull/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 6, 10, "assets/enemies/Ghost/Idle.png", 10,#
                      "assets/enemies/Ghost/Moving.png", 10, "assets/enemies/Ghost/Hit.png", 5))
    
    # Create a new question class rather than using an array
    pythonQuestions = []
    pythonQuestions.append(question.Question(screen, 'What is the value of x after the following statements?\nx = 10\ny=2\nx = x + y','12', ['10','2','102']))
    pythonQuestions.append(question.Question(screen, 'What is the value of sum after the following statements?\nx = 10\nsum = x + 20','30', ['10','20']))
    pythonQuestions.append(question.Question(screen, 'A variable can hold more than one value.\nTrue or False?','False', ['True']))
    pythonQuestions.append(question.Question(screen, 'Which of the following variables holds a string?','x = \'python\'', ['z = w','w = True','y = 7.29']))
    pythonQuestions.append(question.Question(screen, 'Which of the following variable names (identifiers) is invalid?','9lives', ['_cat4','meowtime','number_of_kittens']))
    pythonQuestions.append(question.Question(screen, 'Is x + y = 2 + 5 a valid assignment statement?','Invalid', ['Valid']))
    pythonQuestions.append(question.Question(screen, 'Which of the following is an invalid assignment statement?','x + 3 = 10',['x = 4','x = y','x = y + 4']))
    pythonQuestions.append(question.Question(screen, 'Which of the following is not a numeric data type?','boolean',['int','float','long']))
    pythonQuestions.append(question.Question(screen, 'Given the following assignments, which of the following is a valid operation?\ntext = \'some words\'\nletter = \'c\'\nnumber = 27\ndigits = 9000',
                                             'number + digits',['text + letter','number + text','letter + digits']))
    pythonQuestions.append(question.Question(screen, 'What will be the output after following statements?\nx = \'Hello\'\ny = \'world!\'\nprint(x, y)','Hello world!', ['Helloworld!','Hello,world!','Hello, world!']))
    #Convert pythonQuestions from a list to a questionList object
    pythonQuestions = questionList.QuestionList(pythonQuestions)
    
    #Shuffle the list so that they don't show up in the same order
    pythonQuestions.shuffle()
    #question.Question(screen, question,answer, [wrong,wrong,wrong])

    # Need to load each background into this array
    pythonBackgrounds = [
        'images/bg2/l1.png',
        'images/bg1/bl11New.png',
        'images/bg2/l3.png',
        'images/bg2/l4.png',
        'images/bg2/l5.png',
        'images/bg2/l6.png',
        'images/bg2/l7.png',
        'images/bg2/l8.png',
        'images/bg2/l17.png',
        'images/bg2/l16.png'
    ]

    javaEnemies = []
    javaQuestions = []
    javaBackgrounds = []
    
    # Main game loop
    while True:
        count += 1
        screen.fill((50, 50, 50))
        screen.blit(background, (0, 0))
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quit")
                return False
            if event.type == pygame.VIDEORESIZE:
                w, h = pygame.display.get_surface().get_size()
                # Adjust the size of the background
                background = pygame.image.load('menuBackground.png')
                background = pygame.transform.scale(background, (w, h))
                if scene == "battle":
                    # Adjust the player position, x is constant
                    player.y = screen.get_height() / 2
                    # Adjust the position of the enemy, both x and y
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
            pythonGame(screen, background, player, pythonEnemies)
        elif scene == "javaGame":
            javaGame(screen, background, javaEnemies)
        elif scene == "battle":
            # Call battle() using the list of language and level dependent backgrounds and enemies
            if language == "python":
                # Might need to use the returned values from battle when dealing with hp, not sure atm
                battleReturn = battle(screen, level, player, pythonEnemies, pythonQuestions, pythonBackgrounds)
                p_HP.update(screen)
                p_HP.basic_health(screen)
                # test hp function
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_z:
                            p_HP.take_damage(200)
                        elif event.key == K_x:
                            p_HP.get_health(200)
        elif scene == "pause":
            pause(screen)
        elif scene == "gameOver":
            gameOver(screen)

        # Manage the fps and update the screen
        pygame.display.update()
        clock.tick(fps)
        
# Use pygame.mixer to play the input sound. **USE .wav**
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

# Draw a box with rounded edges centered at x,y
def drawTextBox(surface, x, y, width, height, text=''):
    thickness = 4
    roundness = 6
    # Create and color the surface for the box
    box = pygame.Surface((width, height))
    box.fill((255, 255, 255))
    # Display the filled surface on the input surface
    screen.blit(box, (x - width / 2, y - height / 2))
    # Draw the outline on the input surface
    boxRect = pygame.Rect(x - width / 2 - thickness / 2, y - height / 2 - thickness / 2, width + thickness,
                          height + thickness)
    pygame.draw.rect(surface, (0, 0, 0), boxRect, thickness, roundness)
    # Draw the text if provided
    questionFont = pygame.font.Font(None, 25)

    lines = text.splitlines()
    spacing = 20
    y -= height * .33
    # Add a new line before the text, not sure if theres a better way to do this
    if len(lines) == 1:
        lines.append(lines[0])
        lines[0] = ''
    for line in lines:
        draw_text(line, questionFont, (0, 0, 0), surface, x, y)
        y += spacing

    # Return the rect object for collision detection
    return (boxRect, text)

def pause(screen):
    global scene, language
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
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
        # screen.blit(message, (SCREEN_WIDTH / 2 - 500, SCREEN_HEIGHT / 2 - 350))

        screen.blit(play, (SCREEN_WIDTH / 2 - 575, SCREEN_HEIGHT / 2 - 75))
        screen.blit(menu, (SCREEN_WIDTH / 2 - 175, SCREEN_HEIGHT / 2 - 75))
        screen.blit(exit, (SCREEN_WIDTH / 2 + 225, SCREEN_HEIGHT / 2 - 75))

        pygame.display.update()


def gameOver(screen):
    global scene

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
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
                    scene = "mainMenu"
                    return True
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
    # Set the background and adjust its size
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))
    screen.blit(background, (0, 0))
    val=0

    # Testing exit button
    # Todo figure out why the button image wont load... or why it breaks the program
    exit_img = pygame.image.load('images/button/exit.png').convert_alpha()
    exit_button = button.Button(screen.get_width() / 2, screen.get_height() / 2 + 85, exit_img, 0.2)
    # pygame.draw.rect(screen, (2, 0, 0), exit_button)
    # screen.blit(exit_button, (screen.get_width() / 2, screen.get_height() / 2 + 85))

    # quitButtonUI = pygame.image.load('images/SmallEmptyButton.png')
    # quitButtonIcon = pygame.transform.scale(quitButtonUI, (100, 50))

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

    # Event handling
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

    # pygame.draw.rect(screen,(2,0,0),exit_button)
    # pygame.draw.rect(screen, (225, 0, 0), optionsButton)
    # pygame.draw.rect(screen, (5, 0, 0), quitButton)
    # use this to test the side


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

    draw_text('Pick a language', titleFont, (255, 255, 255), screen, screen.get_width() / 2,
              screen.get_height() / 2 - 20)
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
    maxi = 100  # maximum at slider position right
    mini = 0
    val= 0
    offset=[0,0]

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    draw_text('Options', titleFont, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 - 80)
    draw_text('Music', font, (255, 255, 255), screen, screen.get_width() / 2 - 120, screen.get_height() / 2 )
    draw_text('Sound Fx', font, (255, 255, 255), screen, screen.get_width() / 2 - 135, screen.get_height() / 2 +60)
    draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 120)

    mx, my = pygame.mouse.get_pos()
    backButton = pygame.Rect(0, 0, 50, 30)
    backButton.center = (screen.get_width() / 2, screen.get_height() / 2 + 120)

    # TODO fix the slider so it shows on the game background
    # slider test begin
    # font = pygame.font.SysFont("Verdana", 12)

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
    musicVolumeButton = pygame.draw.circle(screen, BLACK, (screen.get_width() / 2 - 58, screen.get_height() / 2 - 1), 7, 0)

    #For FX Volume
    pygame.draw.rect(screen, WHITE, [screen.get_width() / 2 - 70, screen.get_height() / 2 +45, 150, 30], 2)
    pygame.draw.rect(screen, WHITE, [screen.get_width() / 2 - 58, screen.get_height() / 2 + 57, 125, 5], 0)
    fxVolumeButton = pygame.draw.circle(screen, BLACK, (screen.get_width() / 2 - 58, screen.get_height() / 2 + 59), 7, 0)

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
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                if backButton.collidepoint((mx, my)):
                    play('buttonClick.wav', 0.5)
                    scene = "mainMenu"
                    return True
                if musicVolumeButton.collidepoint((mx,my)):
                    clicked = True
                    while clicked == True:
                        musicVolumeButton = pygame.draw.circle(screen, BLACK, (mx,my), 7, 0)
                    #musicVolumeButton = pygame.draw.circle(screen, BLACK, (loc[0] + offset [0], loc[1] + offset[1]), 7, 0)
                    #musicVolumeButton.move((loc[0], loc[1] ))
                elif event.type == pygame.MOUSEBUTTONUP:
                    clicked = False
                        #print(mx,my)
                if fxVolumeButton.collidepoint(mx,my):
                    pass
        elif event.type == pygame.MOUSEBUTTONUP:
            if musicVolumeButton.collidepoint((mx, my)):
                print("Pressed music")
                pass
            if fxVolumeButton.collidepoint(mx, my):
                print("Pressed fx")
                pass
#Todo impliment being able to move the circle and to have it adjust the volume



def pythonGame(screen, background, player, pythonEnemies):
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
                        #Make sure the enemy has full hp
                        pythonEnemies[level].health = pythonEnemies[level].maxHealth
                        #Reset enemy position
                        pythonEnemies[level].x = pythonEnemies[level].startX
                        #Make sure the player has full hp
                        player.health = player.maxHealth
                        


def javaGame(screen, background, pythonEnemies):
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
                        language = "java"
                        level = i
                        #Make sure the enemy has full hp
                        javaEnemies[level].health = javaEnemies[level].maxHealth





def battle(screen, level, player, enemyList, questionList, backgroundList):
    global scene, fps
    screen.fill((50, 50, 50))
    mx, my = pygame.mouse.get_pos()
    w, h = pygame.display.get_surface().get_size()
    # Load and display the background
    background = pygame.image.load(backgroundList[level])
    #background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))
    screen.blit(background, (0, 0))

    # Load and display the menu button
    menubutton_img = pygame.image.load('images/settings.png')
    menubutton = pygame.transform.scale(menubutton_img, (50, 50))
    screen.blit(menubutton, (w - 60, 10))
    button_1 = pygame.Rect(w - 60, 10, 50, 50)

    questionFont = pygame.font.SysFont(None, 50)
    statementsFont = pygame.font.Font("consolas.ttf", 30)

    questionList.currentQuestion.display(screen)

    # Event handling
    for event in pygame.event.get():
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
            #Check if an answer was clicked and if the answer was correct
            selection = questionList.currentQuestion.isClicked()
            print(selection)
            #If the user clicks on an answer
            if not selection == None:
                if selection[0]:
                    #If the answer is correct flash green on the box clicked on and hurt the enemy
                    print(enemyList[level].health)
                    enemyList[level].takeDamage(10)
                    print(enemyList[level].health)
                    #If the enemies runs out of hp switch to the you win scene
                    if enemyList[level].health <= 0:
                        #scene = ""
                        #return True
                        print("Battle Won!")
                   
                else:
                    #If its wrong flash red and hurt the player
                    print(player.health)
                    player.takeDamage(10)
                    #
                    print(player.health)
                    #If the player runs out of hp switch to the game over scene
                    if player.health <= 0:
                        scene = "gameOver"
                        return True
                #Switch to the next question whether or not it was correct
                questionList.next()
            if button_1.collidepoint((mx, my)):
                scene = "pause"
                return True


    #If the enemy is close enough to the player deal damage every second
    if enemyList[level].x <= enemyList[level].targetX and count%fps == 0:
        player.takeDamage(1)
    #####TEST CODE TO SHOW ANIMATIONS####
    phases = ["idle", "moving", "hit"]
    phase = phases[int(count / 250 % 3)]
    ######################################

    # Display both sprites on the screen
    screen.blit(player.display(screen, .5, phase, fps), (player.x, player.y - player.scale * player.h - 30))
    screen.blit(enemyList[level].display(screen, .5, phase, fps),
                (enemyList[level].x, enemyList[level].y - enemyList[level].scale * enemyList[level].h - 30))

    draw_text(str(player.health), questionFont, (0,0,0), screen, w/2, h/2)

    # Return the updated player and enemy so that any of the changes made this frame will maintain
    return (player, enemyList)


def cutscene():
    pass
    # Play a cutscene
    # Return to level select


def play_music():
    if scene == "mainMenu":
        play('Music')
    if language == "python" & level == 1:
        play('music')
    # do this for all levels or whatever has different audio


def stop_music():
    # arcade.stop?
    pass


def set_vol(value):
    volume = int(value) / 100
    mixer.music.set_volume(value)

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
font = pygame.font.SysFont(None, 12)
flow = False  # controls type of color flow


class Gradient():
    def __init__(self, palette, maximum):
        self.COLORS = palette
        self.N = len(self.COLORS)
        self.SECTION = maximum // (self.N - 1)

    def gradient(self, x):
        """
        Returns a smooth color profile with only a single input value.
        The color scheme is determinated by the list 'self.COLORS'
        """
        i = x // self.SECTION
        fraction = (x % self.SECTION) / self.SECTION
        c1 = self.COLORS[i % self.N]
        c2 = self.COLORS[(i+1) % self.N]
        col = [0, 0, 0]
        for k in range(3):
            col[k] = (c2[k] - c1[k]) * fraction + c1[k]
        return col


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
    the basic slide surface"""
        screen = pygame.display.set_mode([1280, 720])
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
