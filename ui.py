from quiz_core import QuizCore
from tkinter import *
import html

class Ui:
    def __init__(self):
        self.quiz = QuizCore()
        self.window = Tk(screenName="Quiz")
        self.window.config(height=600, width=600, pady=20, padx=20,background="blue")

        self.question_place = Canvas(height=300, width=300, background="#b5e0f0")
        self.question_place.grid(columnspan=2, row=1, pady=50)

        self.true = PhotoImage(file="pictures/true.png")
        self.true_button = Button(image=self.true, highlightthickness=0, command=lambda: [self.quiz.checkTrue(), self.update()])
        self.true_button.grid(column=0, row=3)

        self.false = PhotoImage(file="pictures/false.png")
        self.false_button = Button(image=self.false, highlightthickness=0, command=lambda: [self.quiz.checkFalse(), self.update()])
        self.false_button.grid(column=1, row=3)

        self.score_counter = Label(text=f"score: {self.quiz.score}",font=("arial", 20), bg="blue")
        self.score_counter.grid(row=0, column=1)

        self.question = Label(text=f"{html.unescape(self.quiz.question)}",font=("arial", 15), bg="#b5e0f0", wraplength=300)
        self.question.grid(columnspan=2, row=1, pady=50)

        self.window.mainloop()

    def update(self):
        self.question.config(text=f"{html.unescape(self.quiz.question)}")
        self.score_counter.config(text=f"score: {self.quiz.score}")


