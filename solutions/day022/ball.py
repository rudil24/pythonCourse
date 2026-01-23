from turtle import Turtle
from constants import (
    BALL_COLOR,
    BALL_START_X_MOVE,
    BALL_START_Y_MOVE,
    BALL_START_MOVE_SPEED,
    BALL_SPEED_MULTIPLIER,
)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(BALL_COLOR)
        self.shape("circle")
        self.penup()
        self.x_move = BALL_START_X_MOVE
        self.y_move = BALL_START_Y_MOVE
        self.move_speed = BALL_START_MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= BALL_SPEED_MULTIPLIER

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = BALL_START_MOVE_SPEED
        self.bounce_x()
