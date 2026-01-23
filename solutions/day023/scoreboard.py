from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    Handles the display of the current Level and remaining Lives.
    """

    def __init__(self):
        super().__init__()
        self.level = 1
        self.lives = 3
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)  # Top left corner
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Level: {self.level}  Lives: {self.lives}  High Score: {self.high_score}",
            align="left",
            font=FONT,
        )

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        if self.level > self.high_score:
            self.high_score = self.level
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            self.update_scoreboard()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
