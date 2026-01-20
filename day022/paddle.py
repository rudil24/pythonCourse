from turtle import Turtle
from constants import PADDLE_COLOR, PADDLE_WIDTH, PADDLE_LEN, PADDLE_MOVE_DIST


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LEN)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + PADDLE_MOVE_DIST
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - PADDLE_MOVE_DIST
        self.goto(self.xcor(), new_y)
