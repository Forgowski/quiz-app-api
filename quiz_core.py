import requests
import time
import html


CATEGORIES = ["general knowledge","books","film","music","musicals & theatres","television", "videogames", "board games", "science & nature", "IT", "mythology", "sports", "geography", "politics", "art",
              "celebrities", "animals", "vehicles", "comics", "gadgets", "manga & anime", "cartoon & animations"]

class QuizCore:
    def __init__(self):
        self.category_list = CATEGORIES
        self.my_category = 11
        self.counter = 0
        self.questionbank = requests.get('https://opentdb.com/api.php', params={"amount" : 10, "category" : my_category}).json()["results"]
        self.question_list = html.unescape(self.questionbank)
        self.answer = self.question_list[0]["correct_answer"]
        self.question = self.question_list[0]["question"]


    def nextQuestion(self):
        self.counter += 1
        self.answer = self.question_list[counter]["correct_answer"]
        self.question = self.question_list[counter]["question"]

Q = QuizCore()
print(Q.answer)
