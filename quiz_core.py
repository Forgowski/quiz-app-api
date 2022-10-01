import requests
import time

class QuizCore:
    def __init__(self, category):
        self.my_category = 9 + int(category[0])
        print(self.my_category)
        self.counter = 0
        self.questionbank = requests.get('https://opentdb.com/api.php', params={"amount" : 10, "category" : self.my_category, "type" : "boolean"})
        self.questionbank = self.questionbank.json()["results"]
        self.question_list = self.questionbank
        self.answer = self.question_list[0]["correct_answer"]
        self.question = self.question_list[0]["question"]
        self.is_empty = False
        self.score = 0


    def nextQuestion(self):
        if self.counter == 9:
            self.is_empty = True

        else:
            self.counter += 1
            self.answer = self.question_list[self.counter]["correct_answer"]
            self.question = self.question_list[self.counter]["question"]

    def is_end(self) -> bool:
        if self.is_empty:
            return True

    def checkTrue(self):
        if self.answer == "True":
            self.score += 1
        self.nextQuestion()

    def checkFalse(self):
        if self.answer == "False":
            self.score += 1
        self.nextQuestion()


