from turtle import Turtle
import random
from constants import FOOD_COLOR, X_LIMIT, Y_LIMIT_TOP, Y_LIMIT_BOTTOM


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-X_LIMIT, X_LIMIT)
        random_y = random.randint(Y_LIMIT_BOTTOM, Y_LIMIT_TOP)
        self.goto(random_x, random_y)
