from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    The Player class inherits from Turtle.
    It manages the turtle's movement and position resets.
    """

    def __init__(self):
        super().__init__()  # Initialize the parent Turtle class
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)  # Face North

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False
