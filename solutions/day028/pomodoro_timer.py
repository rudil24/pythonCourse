import math
from tkinter import Canvas, Label, Button, PhotoImage

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMAGE_PATH = "assets/tomato.png"


class PomodoroTimer:
    """
    A class to represent the Pomodoro Timer application.
    Manages the UI setup, timer logic, and state transitions.
    """

    def __init__(self, window):
        """
        Initialize the PomodoroTimer with a tkinter window.

        :param window: The main tkinter window object.
        """
        self.window = window
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=YELLOW)

        self.reps = 0
        self.timer = None

        self.setup_ui()

    def setup_ui(self):
        """Creates and places all UI widgets (Labels, Canvas, Buttons)."""
        # Title Label
        self.title_label = Label(
            text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50)
        )
        self.title_label.grid(column=1, row=0)

        # Canvas with Tomato Image
        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        try:
            self.tomato_img = PhotoImage(file=IMAGE_PATH)
            self.canvas.create_image(100, 112, image=self.tomato_img)
        except Exception as e:
            print(f"Error loading image: {e}. Ensure {IMAGE_PATH} exists.")

        self.timer_text = self.canvas.create_text(
            100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
        )
        self.canvas.grid(column=1, row=1)

        # Buttons
        self.start_button = Button(
            text="Start", highlightbackground=YELLOW, command=self.start_timer_click
        )
        self.start_button.grid(column=0, row=2)

        self.reset_button = Button(
            text="Reset", highlightbackground=YELLOW, command=self.reset_timer
        )
        self.reset_button.grid(column=2, row=2)

        # Checkmarks
        self.check_marks = Label(fg=GREEN, bg=YELLOW)
        self.check_marks.grid(column=1, row=3)

    def reset_timer(self):
        """Resets the timer, reps, and UI to the initial state."""
        if self.timer:
            self.window.after_cancel(self.timer)
            self.timer = None

        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.title_label.config(text="Timer", fg=GREEN)
        self.check_marks.config(text="")
        self.reps = 0

    def start_timer_click(self):
        """Handler for the Start button click. Prevents multiple timers running simultaneously."""
        if self.timer is None:
            self.start_timer()

    def start_timer(self):
        """Determines the current session type (Work/Break) and starts the countdown."""
        self.reps += 1

        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        # If it's the 8th rep: Long Break
        if self.reps % 8 == 0:
            self.count_down(long_break_sec)
            self.title_label.config(text="Break", fg=RED)
        # If it's an even rep: Short Break
        elif self.reps % 2 == 0:
            self.count_down(short_break_sec)
            self.title_label.config(text="Break", fg=PINK)
        # If it's an odd rep: Work
        else:
            self.count_down(work_sec)
            self.title_label.config(text="Work", fg=GREEN)

    def count_down(self, count):
        """
        Recursive function to handle the countdown mechanism.
        Updates the UI and triggers the next session when finished.
        """
        count_min = math.floor(count / 60)
        count_sec = count % 60

        # Format seconds to always show two digits (e.g., 09 instead of 9)
        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec:02d}")

        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.timer = None
            self.start_timer()
            # Add a checkmark for every two reps (completed work sessions)
            marks = "✔" * math.floor(self.reps / 2)
            self.check_marks.config(text=marks)
