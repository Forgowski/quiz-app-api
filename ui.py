from quiz_core import QuizCore
from tkinter import *

class Ui:
    def __init__(self):
        quiz = QuizCore()
        window = Tk(screenName="Quiz")
        window.config(height=600, width=600, pady=20, padx=20,background="blue")
        question_place = Canvas(height=300, width=300, background="yellow")
        question_place.grid(columnspan=2, row=1, pady=50)
        true = PhotoImage(file="pictures/true.png")
        true_button = Button(image=true, highlightthickness=0)
        true_button.grid(column=0, row=3)
        false = PhotoImage(file="pictures/false.png")
        false_button = Button(image=false, highlightthickness=0)
        false_button.grid(column=1, row=3)

        window.mainloop()

