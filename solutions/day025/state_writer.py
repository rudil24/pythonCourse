from turtle import Turtle


class StateWriter(Turtle):
    """
    A class inheriting from Turtle to handle writing state names on the map.
    """

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, state_name, x, y):
        """
        Moves the turtle to the specified (x, y) coordinates and writes the state name.
        """
        self.goto(x, y)
        self.write(state_name)
