import pygame

class SpriteSheet():
    def __init__(self, sheet):
        self.sheet = sheet

    #Parameters:
        #Which frame to be returned
        #How many frames there are in the sheet
        #Factor to scale the frame by

    #Assumes that the sprite sheet is one row of sprites with equal distances between them
    def getImage(self, frame, numFrames, scale):
        width = self.sheet.get_width()
        height = self.sheet.get_height()
        #Get the width of each individual frame
        frameWidth = int(width/numFrames)
        #Create a new surface to put the frame on
        image = pygame.Surface((frameWidth, height)).convert_alpha()
        #Blit the frame onto the new surface
        image.blit(self.sheet, (0, 0), (frameWidth * frame, 0, frameWidth * (frame + 1), height))
        #Scale the frame
        image = pygame.transform.scale(image, (frameWidth * scale, height * scale))
        #Remove the black background
        image.set_colorkey((0,0,0))
        return image
