from tkinter import *
from quiz_brain import QuizBrain
from data import get_question_data
from question_model import Question

THEME_COLOR = "#375362"


class QuizInterface:
    """
    Interface class for the Quiz Game using Tkinter.
    Manages the window, canvas, buttons, and updates the UI based on game state.
    """

    def __init__(self, quiz_brain: QuizBrain):
        """Initialize the QuizInterface with the given QuizBrain logic controller."""
        self.quiz = quiz_brain
        self.quiz_ended = False
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="assets/true.png")
        self.true_button = Button(
            image=self.true_image, highlightthickness=0, command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="assets/false.png")
        self.false_button = Button(
            image=self.false_image, highlightthickness=0, command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """
        Fetches the next question from the quiz brain and updates the UI.
        Resets the canvas background to white and updates the score label.
        """
        self.canvas.config(bg="white")
        if self.quiz.question_number == 0:
            self.score_label.config(text="Score: 0/0 (0.0%)")
        else:
            percent = (self.quiz.score / self.quiz.question_number) * 100
            self.score_label.config(
                text=f"Score: {self.quiz.score}/{self.quiz.question_number} ({percent:.1f}%)"
            )
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You've reached the end of the quiz.\nTry another quiz?",
            )
            self.quiz_ended = True
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")

    def true_pressed(self):
        """Callback for the True button. Checks answer as 'True'."""
        if self.quiz_ended:
            self.start_new_quiz()
        else:
            self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """Callback for the False button. Checks answer as 'False'."""
        if self.quiz_ended:
            self.window.destroy()
        else:
            self.give_feedback(self.quiz.check_answer("False"))

    def start_new_quiz(self):
        self.quiz_ended = False
        self.canvas.itemconfig(self.question_text, text="Loading new questions...")
        self.window.update()

        new_data = get_question_data()
        new_question_bank = []
        for question in new_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            new_question_bank.append(new_question)

        self.quiz = QuizBrain(new_question_bank)
        self.get_next_question()

    def give_feedback(self, is_correct):
        """
        Provides visual feedback to the user.
        Flashes green for correct answers and red for incorrect answers.
        """
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
