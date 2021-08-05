import random, pygame
from pygame.locals import *
class Question:
    def __init__(self, screen, question, answer, wrongAnswers):
        #Surface to draw the question and answers to
        self.screen = screen
        #String
        self.question = question
        #String
        self.answer = answer
        #List
        self.wrongAnswers = wrongAnswers
        random.shuffle(self.wrongAnswers)
        #All answers together, wrong or not. If there are more than 3 wrong answers
        #only pick 3 of them to have as options
        if len(wrongAnswers) > 3:
            self.allAnswers = [self.answer, self.wrongAnswers[0], self.wrongAnswers[1], self.wrongAnswers[2]]
        else:
            self.allAnswers = [self.answer] + self.wrongAnswers
        #Shuffle all the available answers again so the correct one isnt always first
        random.shuffle(self.allAnswers)
        self.answer1 = self.allAnswers[0]
        self.answer2 = self.allAnswers[1]
        #If there was only one wrong answer passed leave the other two answers blank
        if len(self.allAnswers) < 3:
            self.answer3 = ""
        else:
            self.answer3 = self.allAnswers[2]
        if len(self.allAnswers) < 4:
            self.answer4 = ""
        else:
            self.answer4 = self.allAnswers[3]
        #Boolean to show if the question has been shown
        self.shown = False
        #Whether or not the question is animating a correct/incorrect guess
        self.animating = False

        self.answerBox1 = None
        self.answerBox2 = None
        self.answerBox3 = None
        self.answerBox4 = None

    # Draw a box with rounded edges centered at x,y
    def drawTextBox(self, screen, x, y, width, height, backgroundColor, text=''):
        thickness = 4
        roundness = 6
        # Create and color the surface for the box
        box = pygame.Surface((width, height))
        box.fill(backgroundColor)
        # Display the filled surface on the input surface
        screen.blit(box, (x - width / 2, y - height / 2))
        # Draw the outline on the input surface
        boxRect = pygame.Rect(x - width / 2 - thickness / 2, y - height / 2 - thickness / 2, width + thickness,
                              height + thickness)
        pygame.draw.rect(screen, (0, 0, 0), boxRect, thickness, roundness)
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
            self.draw_text(line, questionFont, (0, 0, 0), screen, x, y)
            y += spacing

        # Return the rect object for collision detection
        return (boxRect, text)
    
    def draw_text(self, text, font, color, surface, x, y):
        lines = text.split('   ')
        spacing = 13
        for line in lines:
            if len(lines) > 1:
                y += spacing
            textobj = font.render(line, 1, color)
            textrect = textobj.get_rect()
            textrect.center = (x, y)
            surface.blit(textobj, textrect)
    
    #Will return a random answer and then remove it from the pool of choices
    def chooseRandom():
        randInt = random.randint(0,len(self.allAnswers) - 1)
        selected = self.allAnswers[randInt]
        self.allAnswers.remove(self.allAnswers[randInt])
        return selected
    
    def checkAnswer(self, answer):
        return answer == self.answer

    def isClicked(self):
        #Mouse position
        mx, my = pygame.mouse.get_pos()
        if self.answerBox1[0].collidepoint((mx, my)):
            print("Box 1,", self.answerBox1[1], ",", self.checkAnswer(self.answerBox1[1]))
            return [self.checkAnswer(self.answerBox1[1]), 0]
        if self.answerBox2[0].collidepoint((mx, my)):
            print("Box 2,", self.answerBox2[1], ",", self.checkAnswer(self.answerBox2[1]))
            return [self.checkAnswer(self.answerBox2[1]), 1]
        if self.answerBox3 and self.answerBox3[0].collidepoint((mx, my)):
            print("Box 3,", self.answerBox3[1], ",", self.checkAnswer(self.answerBox3[1]))
            return [self.checkAnswer(self.answerBox3[1]), 2]
        if self.answerBox4 and self.answerBox4[0].collidepoint((mx, my)):
            print("Box 4,", self.answerBox4[1], ",", self.checkAnswer(self.answerBox4[1]))
            return [self.checkAnswer(self.answerBox4[1]), 3]

    def display(self, screen):
        #Width and height of the game window
        w, h = pygame.display.get_surface().get_size()
        #Draw the box with the question
        self.drawTextBox(screen, w / 2, 70, 550, 100, (255, 255, 255), self.question)
        #Draw the 4 available options
        self.answerBox1 = self.drawTextBox(self.screen, w / 2 - 150, 155, 280, 50, (255, 255, 255), self.answer1)
        self.answerBox2 = self.drawTextBox(self.screen, w / 2 + 150, 155, 280, 50, (255, 255, 255), self.answer2)
        
        #If there was only one wrong answer passed dont show the other two answers
        if len(self.allAnswers) < 3:
            pass
        else:
            self.answerBox3 = self.drawTextBox(self.screen, w / 2 - 150, 220, 280, 50, (255, 255, 255), self.answer3)
        if len(self.allAnswers) < 4:
            pass
        else:
            self.answerBox4 = self.drawTextBox(self.screen, w / 2 + 150, 220, 280, 50, (255, 255, 255), self.answer4)
        #self.isClicked()
        
    #isClicked() return whether or not the mousebutton is down right now
        #on one of the answers and if it is also return which answer was click
#function to flash either red or green when an answer is clicked    
