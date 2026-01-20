from turtle import Turtle
from constants import SCOREBOARD_COLOR, SCORE_FONT, SCORE_POS_L, SCORE_POS_R


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(SCORE_POS_L)
        self.write(self.l_score, align="center", font=SCORE_FONT)
        self.goto(SCORE_POS_R)
        self.write(self.r_score, align="center", font=SCORE_FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=SCORE_FONT)
