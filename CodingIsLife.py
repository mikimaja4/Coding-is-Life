import pygame, random
from pygame.locals import *
pygame.init()
    
def main():
    screen = pygame.display.set_mode([500, 500], RESIZABLE)
    w, h = pygame.display.get_surface().get_size()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Coding Is Life")
    # Background
    background = pygame.image.load('background.png')
    background = pygame.transform.scale(background, (w, h))

    #Which scene the user is on
    scene = "menu"
    #max frames per second
    fps = 60
    #The min time (miliseconds) before the next frame
    nextFrame = 0

    #Main game loop
    while True:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        #Check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quit")
                return False
            
            if event.type == pygame.VIDEORESIZE:
                w, h = pygame.display.get_surface().get_size()
                background = pygame.transform.scale(background, (w, h))
                
            #print(event)
            #If the user is on the menu scene check for buttons clicked on
            if scene == "menu":
            
                #If the mouse is clicked, check where it was clicked
                if event.type == MOUSEBUTTONDOWN:
                    print("Clicked")

            elif scene == "levels":
                pass
            
        #Manage the fps and update the screen
        pygame.display.update()
        clock.tick(60)

        if scene == "menu":
            pass
            




if __name__ == '__main__':
    main()
    pygame.quit()
