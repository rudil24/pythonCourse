import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # turn off the tracer, using screen.update instead

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        # 20 is a safe distance for a 20x20 turtle hitting a 20x40 car
        # from the top/bottom.
        if car.distance(player) < 20:
            player.go_to_start()
            scoreboard.decrease_lives()

            # Check if lives are exhausted
            if scoreboard.lives == 0:
                game_is_on = False
                scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
