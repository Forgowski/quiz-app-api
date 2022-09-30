from quiz_core import QuizCore
from tkinter import *
import html

class Ui:
    def __init__(self):
        quiz = QuizCore()
        window = Tk(screenName="Quiz")
        window.config(height=600, width=600, pady=20, padx=20,background="blue")

        question_place = Canvas(height=300, width=300, background="#b5e0f0")
        question_place.grid(columnspan=2, row=1, pady=50)

        true = PhotoImage(file="pictures/true.png")
        true_button = Button(image=true, highlightthickness=0, command=quiz.checkTrue)
        true_button.grid(column=0, row=3)

        false = PhotoImage(file="pictures/false.png")
        false_button = Button(image=false, highlightthickness=0, command=quiz.checkFalse)
        false_button.grid(column=1, row=3)

        score_counter = Label(text=f"score: {quiz.score}",font=("arial", 20), bg="blue")
        score_counter.grid(row=0, column=1)

        question = Label(text=f"{html.unescape(quiz.question)}",font=("arial", 15), bg="#b5e0f0", wraplength=300)
        question.grid(columnspan=2, row=1, pady=50)

        window.mainloop()

