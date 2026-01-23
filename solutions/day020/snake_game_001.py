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
# TODO: 9 replace the internal code with a Snake class and create a snake object to take advantage of all that class has to offer

from turtle import Screen, Turtle
import time
import random
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("rudil24's Snake Game")
screen.tracer(0)  # screen tracer (updates) is off until we tell it to update

# 1 Create a snake body
snake = Snake()

# 3 Create snake food
food = Turtle("circle")
food.color("blue")
food.penup()
food.shapesize(stretch_len=0.5, stretch_wid=0.5)
food.speed("fastest")
food.goto(
    random.randint(-270, 270), random.randint(-270, 270)
)  # 280 was a little too punitive (you'd get your snake to the edge to eat the middle of the food and you'd hit the wall)

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


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(toggle_pause, "space")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if is_paused:
        continue

    # 2 Move the snake
    snake.move()

    # 4 Detect collision with food
    if snake.head.distance(food) < 15:
        food.goto(random.randint(-270, 270), random.randint(-270, 270))
        score += 1
        scoreboard.clear()
        scoreboard.write(
            f"Score: {score}", align="center", font=("Arial", 24, "normal")
        )

        # Extend snake
        snake.extend()

    # 6 Detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.goto(0, 0)
        scoreboard.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    # 7 Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.goto(0, 0)
            scoreboard.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

screen.exitonclick()
