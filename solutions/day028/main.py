# rudil24's Pomodoro App
# Day 28 of 100 Days of Code - Python Bootcamp

from tkinter import Tk
from pomodoro_timer import PomodoroTimer

if __name__ == "__main__":
    window = Tk()
    # Instantiate the PomodoroTimer class, passing the window
    app = PomodoroTimer(window)
    window.mainloop()
