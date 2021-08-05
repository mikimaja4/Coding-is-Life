import pygame, spritesheet

class Entity():
    #Input the spritesheet image location, number of frames in the spritesheet, pos, and scale
    def __init__(self, x, y, scale, moveSpeed, idleSheet, idleFrames, movingSheet, movingFrames, hitSheet, hitFrames):
        self.idle = spritesheet.SpriteSheet(pygame.image.load(idleSheet).convert_alpha())
        self.idleFrames = idleFrames
        
        self.moving = spritesheet.SpriteSheet(pygame.image.load(movingSheet).convert_alpha()) 
        self.movingFrames = movingFrames
        
        self.hit = spritesheet.SpriteSheet(pygame.image.load(hitSheet).convert_alpha())
        self.hitFrames = hitFrames
        
        self.count = 0
        #How many frames the entity has been in their hit animation for
        self.hitCounter = 0
        #Which state the sprite is in. Either idle, moving, or hit
        self.state = "idle"
        #What state the entity was in last frame
        self.prevState = "idle"
        self.scale = scale

        self.updateSize()
        self.x, self.startX = x, x
        self.y, self.startY = y + self.h, y + self.h
        #The x position of the target to move towards
        self.targetX = 150
        #Update the width and height of a frame
        self.updateSize()
        #Time in seconds to reach the player
        #NOT ACCURATE because of lag i think
        self.moveSpeed = moveSpeed
        #Trying to account for the lag I think
        self.moveSpeed /= 3

        self.health = 150
        #Maximum number of health points the entity can have
        self.maxHealth = 100


    def display(self, screen, speed, state, fps):
        w, h = pygame.display.get_surface().get_size()
        self.updateSize()
        #Check if the state changed since last frame
        if(state != self.prevState):
            #If it did reset count to 0 so we dont miss and vital frame
            self.count = 0
            self.hitCounter = 0
        self.prevState = self.state
        self.state = state
        #If the entity has been hit but hasnt finished their hit animation stay hit
        if(self.hitCounter < self.hitFrames and self.prevState == "hit"):
            self.state = "hit"
        #If theyre at their target switch them to idle
        elif (self.x <= self.targetX):
            self.state = "idle"
        #If theyre not at their target switch them to moving
        elif (self.x > self.targetX):
            self.state = "moving"
        if self.state == "idle":
            frame = self.idle.getImage(int(self.count) % self.idleFrames, self.idleFrames, self.scale)
            #(self.count * speed) % self.idleFrames
        elif self.state == "moving":
            frame = self.moving.getImage(int(self.count) % self.movingFrames, self.movingFrames, self.scale)
        elif self.state == "hit":
            frame = self.hit.getImage(int(self.count) % self.hitFrames, self.hitFrames, self.scale)
            self.hitCounter += (1 * speed)
        if(self.moveSpeed > 0 and self.x > self.targetX):
            self.move(self.x - (self.startX - self.targetX)/(fps * self.moveSpeed), self.y)
        self.count += (1 * speed)
        #return pygame.transform.flip(frame, True, False)
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

    def updateSize(self):
        #Update the width and height of an individual frame
        if self.state == "idle":
            self.w, self.h = self.idle.get_size()
            self.w /= self.idleFrames
        elif self.state == "moving":
            self.w, self.h = self.idle.get_size()
            self.w /= self.movingFrames
        elif self.state == "hit":
            self.w, self.h = self.idle.get_size()
            self.w /= self.hitFrames
