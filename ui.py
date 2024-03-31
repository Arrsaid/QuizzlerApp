from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=450, height=350, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(225, 175, width=400,
                                                   text="Hello world",
                                                   font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        # Label
        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR, font=("bold", 18))
        self.score_label.grid(row=0, column=1)

        # Buttons
        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=1)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=0)

        # generate questions
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.configure(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=question)
        else:
            self.canvas.itemconfig(self.canvas_text, text="No more questions")
            self.wrong_button.config(state="disabled")
            self.right_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_wright):
        if is_wright:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
