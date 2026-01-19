from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BG_COLOR
import time

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BG_COLOR)
screen.title("rudil24's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_paused = True
is_game_over = False


def toggle_pause():
    global is_paused, is_game_over
    if is_game_over:
        snake.reset()
        scoreboard.reset()
        is_game_over = False
        is_paused = False
    else:
        is_paused = not is_paused


screen.onkey(toggle_pause, "space")


def quit_game(x, y):
    global game_is_on
    game_is_on = False


screen.onscreenclick(quit_game)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if is_paused:
        continue

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.check_wall_collision():
        scoreboard.game_over()
        is_game_over = True
        is_paused = True

    # Detect collision with tail
    if snake.check_tail_collision():
        scoreboard.game_over()
        is_game_over = True
        is_paused = True

screen.exitonclick()
