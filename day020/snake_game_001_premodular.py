# rudil24
# Snake Game Project
# TODO: 1 Create a snake body
# TODO: 2 Move the snake
# TODO: 3 Create snake food
# TODO: 4 Detect collision with food
# TODO: 5 Create a score board
# TODO: 6 Detect collision with wall
# TODO: 7 Detect collision with tail
# TODO: 8 **SPECIAL** Create a pause feature with spacebar, toggle it on at start, so that i have time to switch to the window before the game starts

from turtle import Screen, Turtle
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("rudil24's Snake Game")
screen.tracer(0)  # screen tracer (updates) is off until we tell it to update

# 1 Create a snake body
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# 3 Create snake food
food = Turtle("circle")
food.color("blue")
food.penup()
food.shapesize(stretch_len=0.5, stretch_wid=0.5)
food.speed("fastest")
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# 5 Create a score board
score = 0
scoreboard = Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 270)
scoreboard.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

screen.listen()

is_paused = True


def toggle_pause():
    global is_paused
    is_paused = not is_paused


def up():
    if segments[0].heading() != 270:
        segments[0].setheading(90)


def down():
    if segments[0].heading() != 90:
        segments[0].setheading(270)


def left():
    if segments[0].heading() != 0:
        segments[0].setheading(180)


def right():
    if segments[0].heading() != 180:
        segments[0].setheading(0)


screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(toggle_pause, "space")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if is_paused:
        continue

    # 2 Move the snake
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)  # this is the head of the snake (segments[0])

    # 4 Detect collision with food
    if segments[0].distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        score += 1
        scoreboard.clear()
        scoreboard.write(
            f"Score: {score}", align="center", font=("Arial", 24, "normal")
        )

        # Extend snake
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(segments[-1].position())
        segments.append(new_segment)

    # 6 Detect collision with wall
    if (
        segments[0].xcor() > 280
        or segments[0].xcor() < -280
        or segments[0].ycor() > 280
        or segments[0].ycor() < -280
    ):
        game_is_on = False
        scoreboard.goto(0, 0)
        scoreboard.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    # 7 Detect collision with tail
    for segment in segments[1:]:
        if segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.goto(0, 0)
            scoreboard.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

screen.exitonclick()
