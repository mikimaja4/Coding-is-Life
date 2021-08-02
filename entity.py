import pygame, spritesheet

class Entity():
    #Input the spritesheet image location, number of frames in the spritesheet, pos, and scale
    def __init__(self, x, y, scale, idleSheet, idleFrames, movingSheet, movingFrames, hitSheet, hitFrames):
        self.idle = spritesheet.SpriteSheet(pygame.image.load(idleSheet).convert_alpha())
        self.idleFrames = idleFrames
        
        self.moving = spritesheet.SpriteSheet(pygame.image.load(movingSheet).convert_alpha()) 
        self.movingFrames = movingFrames
        
        self.hit = spritesheet.SpriteSheet(pygame.image.load(hitSheet).convert_alpha())
        self.hitFrames = hitFrames
        
        self.count = 0
        #Which state the sprite is in. Either idle, moving, or hit
        self.state = "idle"
        #What state the entity was in last frame
        self.prevState = "idle"
        self.scale = scale
        
        self.x = x
        self.y = y
        #Percent of screen moved per second (between 0 and 1)
        #Default to 0 for the player
        self.moveSpeed = 0

        self.health = 100
        #Maximum number of health points the entity can have
        self.maxHealth = 100


    def display(self, screen, speed, state, fps):
        self.state = state
        #Check if the state changed since last frame
        if(self.state != self.prevState):
            self.count = 0
        self.prevState = self.state
        #If it did reset count to 0 so we dont miss and vital frames
        w, h = pygame.display.get_surface().get_size()
        if self.state == "idle":
            frame = self.idle.getImage(int(self.count) % self.idleFrames, self.idleFrames, self.scale)
            #(self.count * speed) % self.idleFrames
        elif self.state == "moving":
            frame = self.moving.getImage(int(self.count) % self.movingFrames, self.movingFrames, self.scale)
        elif self.state == "hit":
            frame = self.hit.getImage(int(self.count) % self.hitFrames, self.hitFrames, self.scale)
        self.move(self.x - (w * self.moveSpeed)/fps, self.y)
        self.count += 1 * speed

        return frame
        
    def move(self, newX, newY):
        self.x = newX
        self.y = newY

    def takeDamage(self, damage):
        if(self.health - damage < 0):
            self.health = 0
        else:
            self.health -= damage

    def heal(self, health):
        if(self.health + health > self.maxHealth):
            self.health = self.maxHealht
        else:
            self.health += health
