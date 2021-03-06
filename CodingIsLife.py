import os, pygame, arcade, spritesheet, entity, button, dropDown, question, questionList, csv
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
import slider

monitors = get_monitors()  # Get the resolution of all of the users monitors
w = monitors[0].width  # Get width of first monitor found
h = monitors[0].height  # Get height of first monitor found
pos_x = w / 2 - 800  # Calculate the x-location
pos_y = h / 2 - 450  # Calculate the y-location
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x, pos_y)  # Set pygame window location

# root=Tk()
pygame.init()

def main():
    global count, language, level, scene, fps, pythonLevelsUnlocked
    screen = pygame.display.set_mode([1280, 720])
    w, h = pygame.display.get_surface().get_size()
    # Set the background and adjust its size
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))

    clock = pygame.time.Clock()
    pygame.display.set_caption("Coding Is Life")

    # Create the players entity object
    player = entity.Entity(50, screen.get_height() + 25, 6, 0, "assets/dinos/DinoBlueIdle.png", 4,
                           "assets/dinos/DinoBlueMoving.png", 6, "assets/dinos/DinoBlueHit.png", 3)
    # Create the enemy entity objects
    pythonEnemies = []
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 4, 25, "assets/enemies/Mushroom/Idle.png", 14,#
                      "assets/enemies/Mushroom/Moving.png", 16, "assets/enemies/Mushroom/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height() - 20, 4, 20, "assets/enemies/Radish/Idle.png", 6,#
                      "assets/enemies/Radish/Moving.png", 12, "assets/enemies/Radish/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height() + 7, 5, 18, "assets/enemies/Snail/Idle.png", 15,#
                      "assets/enemies/Snail/Moving.png", 10, "assets/enemies/Snail/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height() - 5, 4, 16, "assets/enemies/Chicken/Idle.png", 13,#
                      "assets/enemies/Chicken/Moving.png", 14, "assets/enemies/Chicken/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height() - 7, 4, 14, "assets/enemies/Duck/Idle.png", 10,#
                      "assets/enemies/Duck/Moving.png", 10, "assets/enemies/Duck/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height() - 3, 6, 12, "assets/enemies/Rino/Idle.png", 11,#
                      "assets/enemies/Rino/Moving.png", 6, "assets/enemies/Rino/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 6, 10, "assets/enemies/Slime/Idle.png", 10,#
                      "assets/enemies/Slime/Moving.png", 10, "assets/enemies/Slime/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 6, 8, "assets/enemies/AngryPig/Idle.png", 9,#
                      "assets/enemies/AngryPig/Moving.png", 16, "assets/enemies/AngryPig/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 6, 6, "assets/enemies/Skull/Idle.png", 8,
                      "assets/enemies/Skull/Moving.png", 8, "assets/enemies/Skull/Hit.png", 5))
    pythonEnemies.append(
        entity.Entity(screen.get_width() - 200, screen.get_height(), 6, 4, "assets/enemies/Ghost/Idle.png", 10,#
                      "assets/enemies/Ghost/Moving.png", 10, "assets/enemies/Ghost/Hit.png", 5))


    # Need to load each background into this array
    pythonBackgrounds = [
        'images/bg3/l3.jpg',
        'images/bg3/l5.jpg',
        'images/bg3/l1.jpg',
        'images/bg3/l4.jpg',
        'images/bg3/l2.png',
        'images/bg3/l6.jpg',
        'images/bg3/l7.jpg',
        'images/bg3/l8.jpg',
        'images/bg3/l9.jpg',
        'images/bg3/l10.jpg'
    ]

    javaEnemies = []
    javaQuestions = []
    javaBackgrounds = []

    pythonLevelsUnlocked = 1
    
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
            if event.type == KEYDOWN:
                if event.key == 1073741911 or event.key == 61:
                    pythonLevelsUnlocked = 10
                    print("All python levels unlocked", pythonLevelsUnlocked)
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
            levelQuestions = getLevelQuestions(screen, level)
        elif scene == "javaGame":
            javaGame(screen, background, javaEnemies)
            levelQuestions = getLevelQuestions(screen, level)
        elif scene == "battle":
            # Call battle() using the list of language and level dependent backgrounds and enemies
            if language == "python":
                # Might need to use the returned values from battle when dealing with hp, not sure atm
                battleReturn = battle(screen, level, player, pythonEnemies, levelQuestions, pythonBackgrounds)
        elif scene == "pause":
            pause(screen)
        elif scene == "gameOver":
            gameOver(screen)
        elif scene == "victory":
            victory(screen, player)

        # Manage the fps and update the screen
        pygame.display.update()
        clock.tick(fps)


def getLevelQuestions(screen, level):
    level += 1
    levelQuestions = []
    # Read in questions for CSV file for corresponding level
    filename = language + 'Level' + str(level) + '.csv'
    try:
        with open(filename, "r") as fh:
            reader = csv.reader(fh)
            questions = list(reader)
            for problem in questions:
                levelQuestions.append(question.Question(screen, problem[0], problem[1], problem[2:]))
    except FileNotFoundError:
        with open(language + 'Level1.csv', "r") as fh:
            reader = csv.reader(fh)
            questions = list(reader)
            for problem in questions:
                levelQuestions.append(question.Question(screen, problem[0], problem[1], problem[2:]))
    # Convert levelQuestions from a list to a questionList object
    levelQuestions = questionList.QuestionList(levelQuestions)
    # Shuffle the list so that they don't show up in the same order
    levelQuestions.shuffle()
    # Return list of questions for level as list of string, string, list of strings
    return levelQuestions


# Use pygame.mixer to play the input sound. **USE .wav**
def play(filename, volume):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    return True


def draw_text(text, font, color, surface, x, y):
    lines = text.split('   ')
    for line in lines:
        textobj = font.render(line, 1, color)
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

def victory(screen, player):
    global scene

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background_img = pygame.image.load('images/mainbackground.png')
    background = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    victory_img = pygame.image.load('images/Victory.png')
    victory = pygame.transform.scale(victory_img, (1000, 200))

    exit_img = pygame.image.load('images/ExitButton.png')
    exit = pygame.transform.scale(exit_img, (350, 150))

    menu_img = pygame.image.load('images/MenuButton.png')
    menu = pygame.transform.scale(menu_img, (350, 150))
    
    player2 = entity.Entity(50, screen.get_height() + 25, 6, 0, "assets/dinos/DinoBlueIdleReverse.png", 4,
                           "assets/dinos/DinoBlueMoving.png", 6, "assets/dinos/DinoBlueHit.png", 3)

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
        screen.blit(victory, (SCREEN_WIDTH / 2 - 500, SCREEN_HEIGHT / 2 - 350))
        screen.blit(menu, (SCREEN_WIDTH / 2 - 375, SCREEN_HEIGHT / 2 - 75))
        screen.blit(exit, (SCREEN_WIDTH / 2 + 25, SCREEN_HEIGHT / 2 - 75))

        screen.blit(player.display(screen, .2, 'idle', fps), (player.x, player.y - player.scale * player.h - 100))
        screen.blit(player2.display(screen, .2, 'idle', fps), (1150 - player2.x, player2.y - player2.scale * player2.h - 100))

        pygame.display.update()

def gameOver(screen):
    global scene

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background_img = pygame.image.load('images/GameOverBackground.jpg')
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
    global scene, volume
    screen = pygame.display.set_mode([1280, 720])
    w, h = pygame.display.get_surface().get_size()
    background = pygame.image.load('menuBackground.png')
    background = pygame.transform.scale(background, (w, h))
    fullscreen = False
    font = pygame.font.SysFont(None, 30)
    titleFont = pygame.font.SysFont(None, 50)

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    draw_text('Options', titleFont, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 - 80)
    draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 120)

    mx, my = pygame.mouse.get_pos()
    backButton = pygame.Rect(0, 0, 50, 30)
    backButton.center = (screen.get_width() / 2, screen.get_height() / 2 + 120)

    clock = pygame.time.Clock()

    musicVolume = Slider("Music Volume", 3.14, 6, 0.3, 650)
    slides = [musicVolume]
    speed = Slider("Speed", 50, 150, 10, 775)

    num = 0
    draw_text('Options', titleFont, (255, 255, 255), screen, screen.get_width() / 2,screen.get_height() / 2 - 80)

    draw_text('Back', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 2 + 120)

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
                if event.button ==1:
                    if backButton.collidepoint(mx,my):
                        play('buttonClick.wav', 0.5)
                        scene = "mainMenu"
                        return True
            elif event.type == pygame.MOUSEBUTTONUP:
                for s in slides:
                    s.hit = False
                    return False


        # Move slides
        for s in slides:
            if s.hit:
                s.move()

        # Update screen
        num += 2

        for s in slides:
            s.draw()

        pygame.display.flip()
        clock.tick(speed.val)


def pythonGame(screen, background, player, pythonEnemies):
    global scene, level, count, pythonLevelsUnlocked
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
        #Fill the left side with levels that are available in white
        if i < pythonLevelsUnlocked:
            draw_text('Level ' + str((i + 1)), font, (255,255,255), screen,
                      screen.get_width() / 2 - 50, screen.get_height() / 2 - 85 + (i * 30))
        #Fill the left side with levels that are unavailable in grey
        else:
            draw_text('Level ' + str((i + 1)), font, (169,169,169), screen,
                  screen.get_width() / 2 - 50, screen.get_height() / 2 - 85 + (i * 30))
        # Create the rectangle for click detection of the current level
        newButton = pygame.Rect(0, 0, 50, 10)
        # Center the button in the correct spot
        newButton.center = (screen.get_width() / 2 - 50, screen.get_height() / 2 - 85 + (i * 30))
        levelButtons.append(newButton)


    for i in range(5):
        #Fill the right side with levels that are available in white
        if i + 5 < pythonLevelsUnlocked:
            draw_text('Level ' + str((i + 6)), font, (255,255,255), screen,
                  screen.get_width() / 2 + 50, screen.get_height() / 2 - 85 + (i * 30))
        #Fill the right side with levels that are unavailable in grey
        else:
            draw_text('Level ' + str((i + 6)), font, (169,169,169), screen,
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
                    if (levelButtons[i].collidepoint((mx, my)) and i < pythonLevelsUnlocked):
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


def drawPHealth(character, screen):
    health_bar_length = 150
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, character.health / (character.maxHealth / health_bar_length), 25))
    pygame.draw.rect(screen, (255, 255, 255), (10, 10, health_bar_length, 25), 4)
    font = pygame.font.Font(None, 36)

    current_text = str(character.health)
    current = font.render(current_text, False, (0, 0, 0))
    current_text2 = str(character.health)
    current2 = font.render(current_text2, False, (255, 255, 255))

    screen.blit(current2, (9, 39))
    screen.blit(current2, (9, 40))
    screen.blit(current2, (9, 41))
    screen.blit(current2, (10, 41))
    screen.blit(current2, (11, 41))
    screen.blit(current2, (11, 40))
    screen.blit(current2, (11, 39))
    screen.blit(current2, (10, 39))
    screen.blit(current, (10, 40))

    slash = font.render('/', False, (0, 0, 0))
    slash2 = font.render('/', False, (255, 255, 255))

    screen.blit(slash2, (54, 39))
    screen.blit(slash2, (54, 40))
    screen.blit(slash2, (54, 41))
    screen.blit(slash2, (55, 39))
    screen.blit(slash2, (55, 41))
    screen.blit(slash2, (56, 39))
    screen.blit(slash2, (56, 40))
    screen.blit(slash2, (56, 41))
    screen.blit(slash, (55, 40))

    max_text = str(character.maxHealth)
    max_text = font.render(max_text, False, (0, 0, 0))
    max_text2 = str(character.maxHealth)
    max_text2 = font.render(max_text2, False, (255, 255, 255))

    screen.blit(max_text2, (67, 39))
    screen.blit(max_text2, (67, 40))
    screen.blit(max_text2, (67, 41))
    screen.blit(max_text2, (68, 39))
    screen.blit(max_text2, (68, 41))
    screen.blit(max_text2, (69, 39))
    screen.blit(max_text2, (69, 40))
    screen.blit(max_text2, (69, 41))
    screen.blit(max_text, (68, 40))

def drawEHealth(character, screen):
    health_bar_length = 150
    pygame.draw.rect(screen, (255, 0, 0), (1050, 10, character.health / (character.maxHealth / health_bar_length), 25))
    pygame.draw.rect(screen, (255, 255, 255), (1050, 10, health_bar_length, 25), 4)
    font = pygame.font.Font(None, 36)

    current_text = str(character.health)
    current = font.render(current_text, False, (0, 0, 0))
    current_text2 = str(character.health)
    current2 = font.render(current_text2, False, (255, 255, 255))

    screen.blit(current2, (1059, 39))
    screen.blit(current2, (1059, 40))
    screen.blit(current2, (1059, 41))
    screen.blit(current2, (1060, 41))
    screen.blit(current2, (1060, 41))
    screen.blit(current2, (1061, 40))
    screen.blit(current2, (1061, 39))
    screen.blit(current2, (1061, 39))
    screen.blit(current, (1060, 40))

    slash = font.render('/', False, (0, 0, 0))
    slash2 = font.render('/', False, (255, 255, 255))

    screen.blit(slash2, (1104, 39))
    screen.blit(slash2, (1104, 40))
    screen.blit(slash2, (1104, 41))
    screen.blit(slash2, (1105, 39))
    screen.blit(slash2, (1105, 41))
    screen.blit(slash2, (1106, 39))
    screen.blit(slash2, (1106, 40))
    screen.blit(slash2, (1106, 41))
    screen.blit(slash, (1105, 40))

    max_text = str(character.maxHealth)
    max_text = font.render(max_text, False, (0, 0, 0))
    max_text2 = str(character.maxHealth)
    max_text2 = font.render(max_text2, False, (255, 255, 255))

    screen.blit(max_text2, (1117, 39))
    screen.blit(max_text2, (1117, 40))
    screen.blit(max_text2, (1117, 41))
    screen.blit(max_text2, (1118, 39))
    screen.blit(max_text2, (1118, 41))
    screen.blit(max_text2, (1119, 39))
    screen.blit(max_text2, (1119, 40))
    screen.blit(max_text2, (1119, 41))
    screen.blit(max_text, (1118, 40))

def battle(screen, level, player, enemyList, questionList, backgroundList):
    global scene, fps, pythonLevelsUnlocked
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

    drawPHealth(player, screen)
    drawEHealth(enemyList[level], screen)

    #drawHealth(enemyList[level], screen)

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
                    play('correct.wav', 0.5)
                    print("Enemy hit!")
                    enemyList[level].takeDamage(20)
                    enemyList[level].state = "hit"
                    #If the enemies runs out of hp switch to the you win scene
                    if enemyList[level].health <= 0:
                        scene = "victory"
                        if level + 1 == pythonLevelsUnlocked:
                            pythonLevelsUnlocked += 1
                            print("Level unlocked!")
                        print("Battle Won!")
                        return True
                   
                else:
                    #If its wrong flash red and hurt the player
                    play('painroar.wav', 0.5)
                    print("Player hit!")
                    player.takeDamage(10)
                    player.state = "hit"
                    #If the player runs out of hp switch to the game over scene
                    if player.health <= 0:
                        scene = "gameOver"
                        print("Game Over!")
                        return True
                #Switch to the next question whether or not it was correct
                questionList.next()
            if button_1.collidepoint((mx, my)):
                scene = "pause"
                return True


    #If the enemy is close enough to the player deal damage every second
    if enemyList[level].x <= enemyList[level].targetX and count%fps == 0:
        player.takeDamage(5)
        player.state = "hit"
        #If the player runs out of hp switch to the game over scene
        if player.health <= 0:
            scene = "gameOver"
            print("Game Over!")
            return True

    # Display both sprites on the screen
    screen.blit(player.display(screen, .2, player.state, fps), (player.x, player.y - player.scale * player.h - 30))
    screen.blit(enemyList[level].display(screen, .3, enemyList[level].state, fps),
                (enemyList[level].x, enemyList[level].y - enemyList[level].scale * enemyList[level].h - 30))

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
font = pygame.font.SysFont(None, 20)
flow = False  # controls type of color flow
screen = pygame.display.set_mode([1280, 720])


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

if __name__ == '__main__':
    # GLOBAL VARIABLES
    global scene, language, level, fps, count, volume
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

    volume=[50]

    main()
    quit()
