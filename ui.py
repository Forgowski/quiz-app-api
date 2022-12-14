from quiz_core import QuizCore
from tkinter import *
import html

CATEGORIES = {"general knowledge" : 0, "film" : 2, "music" : 3, "television" : 5, "videogames" : 6, "science & nature" : 8,
                "IT" : 9, "mythology" : 11, "sports" : 12, "geography" : 13, "politics" : 14, "art" : 15,
              "celebrities" : 16, "comics" : 19, "gadgets" : 20}

class Ui:
    def __init__(self):
        self.window = Tk()
        self.window.config(height=600, width=600, pady=20, padx=20, background="blue")
        self.window.title("Quiz")

        self.list_box = Listbox(self.window)
        self.list_box.config(height=15)
        self.loadListBox()

        self.select_button = Button(text="choose category", command=self.getSelected)
        self.select_button.grid(column=0, row=1,pady=20)

        self.window.mainloop()


    def start(self, category):
        self.list_box.grid_remove()
        self.select_button.grid_remove()
        self.quiz = QuizCore(category)

        self.question_place = Canvas(height=300, width=300, background="#b5e0f0")
        self.question_place.grid(columnspan=2, row=1, pady=50)

        self.true = PhotoImage(file="pictures/true.png")
        self.true_button = Button(image=self.true, highlightthickness=0,
                                  command=lambda: [self.quiz.checkTrue(), self.update()])
        self.true_button.grid(column=0, row=3)

        self.false = PhotoImage(file="pictures/false.png")
        self.false_button = Button(image=self.false, highlightthickness=0,
                                   command=lambda: [self.quiz.checkFalse(), self.update()])
        self.false_button.grid(column=1, row=3)

        self.score_counter = Label(text=f"score: {self.quiz.score}/10", font=("arial", 20), bg="blue")
        self.score_counter.grid(row=0, column=1)

        self.question = Label(text=f"{html.unescape(self.quiz.question)}", font=("arial", 15), bg="#b5e0f0",
                              wraplength=300)
        self.question.grid(columnspan=2, row=1, pady=50)

        self.score_holder = 0

    def update(self):
        self.feedback()
        self.question.after(1000,self.backToDefaultColor)

    def feedback(self):
        if self.score_holder == self.quiz.score:
            self.question_place.config(bg="red")
            self.question.config(bg="red")
        else:
            self.score_holder = self.quiz.score
            self.question_place.config(bg="green")
            self.question.config(bg="green")

    def backToDefaultColor(self):
        self.question_place.config(bg="#b5e0f0")
        self.question.config(bg="#b5e0f0")
        self.question.config(text=f"{html.unescape(self.quiz.question)}")
        self.score_counter.config(text=f"score: {self.quiz.score}/10")
        if self.quiz.is_empty:
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")
            self.question.config(text="End of questions")


    def loadListBox(self):
        for i in CATEGORIES:
            self.list_box.insert(END,i)

        self.list_box.grid(column=0, row=0)


    def getSelected(self):
       category = self.list_box.curselection()
       holder = list(CATEGORIES)
       holder = holder[category[0]]
       category = CATEGORIES[holder]
       self.start(category)





