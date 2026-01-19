from turtle import Turtle
from constants import (
    STARTING_POSITIONS,
    MOVE_DISTANCE,
    UP,
    DOWN,
    LEFT,
    RIGHT,
    SNAKE_COLOR,
    X_LIMIT,
    Y_LIMIT_TOP,
    Y_LIMIT_BOTTOM,
)


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(SNAKE_COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def check_wall_collision(self):
        if (
            self.head.xcor() > X_LIMIT
            or self.head.xcor() < -X_LIMIT
            or self.head.ycor() > Y_LIMIT_TOP
            or self.head.ycor() < Y_LIMIT_BOTTOM
        ):
            return True
        return False

    def check_tail_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
