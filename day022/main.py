from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_BG_COLOR,
    SCREEN_TITLE,
    R_PADDLE_START_POS,
    L_PADDLE_START_POS,
    WINNING_SCORE,
    Y_BOUNCE_LIMIT,
    PADDLE_BOUNCE_X_LIMIT,
    PADDLE_HIT_DISTANCE,
    X_MISS_LIMIT,
    DASH_COLOR,
)

screen = Screen()
screen.bgcolor(SCREEN_BG_COLOR)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title(SCREEN_TITLE)
screen.tracer(0)

r_paddle = Paddle(R_PADDLE_START_POS)
l_paddle = Paddle(L_PADDLE_START_POS)
ball = Ball()
scoreboard = Scoreboard()

line = Turtle()
line.hideturtle()
line.color(DASH_COLOR)
line.pensize(5)
line.penup()
line.goto(0, SCREEN_HEIGHT / 2)
line.setheading(270)
for _ in range(30):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > Y_BOUNCE_LIMIT or ball.ycor() < -Y_BOUNCE_LIMIT:
        ball.bounce_y()

    # Detect collision with paddle
    if (
        ball.distance(r_paddle) < PADDLE_HIT_DISTANCE
        and ball.xcor() > PADDLE_BOUNCE_X_LIMIT
    ) or (
        ball.distance(l_paddle) < PADDLE_HIT_DISTANCE
        and ball.xcor() < -PADDLE_BOUNCE_X_LIMIT
    ):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > X_MISS_LIMIT:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -X_MISS_LIMIT:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score >= WINNING_SCORE or scoreboard.r_score >= WINNING_SCORE:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
