import requests
import time



CATEGORIES = ["general knowledge","books","film","music","musicals & theatres","television", "videogames", "board games", "science & nature", "IT", "mythology", "sports", "geography", "politics", "art",
              "celebrities", "animals", "vehicles", "comics", "gadgets", "manga & anime", "cartoon & animations"]

class QuizCore:
    def __init__(self):
        self.category_list = CATEGORIES
        self.my_category = 11
        self.counter = 0
        self.questionbank = requests.get('https://opentdb.com/api.php', params={"amount" : 10, "category" : self.my_category, "type" : "boolean"}).json()["results"]
        self.question_list = self.questionbank
        self.answer = self.question_list[0]["correct_answer"]
        self.question = self.question_list[0]["question"]
        self.is_empty = False
        self.score = 0


    def nextQuestion(self):
        if self.counter == 10:
            self.is_empty = True

        else:
            self.counter += 1
            self.answer = self.question_list[self.counter]["correct_answer"]
            self.question = self.question_list[self.counter]["question"]

    def is_end(self) -> bool:
        if self.is_empty:
            return True

    def checkTrue(self):
        if self.answer == True:
            self.score += 1
        self.nextQuestion()

    def checkFalse(self):
        if self.answer == False:
            self.score += 1
        self.nextQuestion()


