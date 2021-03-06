import random, question
class QuestionList:
    def __init__(self, questions):
        #List of Question objects
        self.questions = questions
        #Shuffle the questions before selecting which will be first
        self.shuffle()
        #Which question is currently being displayed
        self.currentQuestion = questions[0]
        #Index for which question we are currently displaying
        self.index = 0

    def shuffle(self):
        random.shuffle(self.questions)

    def next(self):
        self.currentQuestion = self.questions[self.index]
        self.index += 1
        #Just have the questions loop if you make it through all of them
        if self.index == len(self.questions):
            self.index = 0

    
