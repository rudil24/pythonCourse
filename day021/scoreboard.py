from turtle import Turtle
from constants import ALIGNMENT, FONT, SCOREBOARD_COLOR


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(
                data.read()
            )  # read in the high score, convert to integer
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(
                    f"{self.high_score}"
                )  # write the new high score as a string in the data.txt file (overwrite whatever was in that file)
            self.update_scoreboard()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
