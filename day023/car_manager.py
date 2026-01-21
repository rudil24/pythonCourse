# car_manager observations and improvements
# To make the cars move at different speeds, we need to move away from using the single global self.car_speed for movement and instead assign a specific speed to each individual car object when it is created.
# Here are the changes for day023/car_manager.py:
# create_car: Assign a move_speed attribute to the new car turtle. We calculate this by taking the current base car_speed and adding a small random variance (e.g., random.randint(0, 4)).
# move_cars: Update the loop to move each car by its own car.move_speed instead of the global self.car_speed.
# level_up: In addition to increasing the base speed for future cars, we iterate through all existing cars and increase their move_speed so the difficulty spike is immediate.

# Level 1 had the most traffic when we want it to have the least
# The Math Behind Your Feeling: The "density" of traffic on the screen is determined by Spawn Rate / Car Speed.
# Since the spawn rate was constant (1 in 6 chance every 0.1s) for all levels...
# And Level 1 has the slowest cars...
# Level 1 mathematically has the highest density of cars on screen at any one time because they take so long to clear the screen.
# Here is the fix. I've adjusted the spawn rate specifically for Level 1 (when car_speed equals STARTING_MOVE_DISTANCE) to be less frequent (1 in 9 chance), while keeping the later levels at the standard rate (1 in 6 chance) since we liked the playability there.

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """
    Manages all the cars in the game.
    Handles spawning cars randomly and moving them across the screen.
    """

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # We don't want a car every single game loop (too many cars).
        # roughly 1 in 6 chance every loop iteration (0.1s)
        # Level 1 (STARTING_MOVE_DISTANCE) feels too crowded because cars are slow.
        if self.car_speed == STARTING_MOVE_DISTANCE:
            random_chance = random.randint(1, 9)
        else:
            random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # 20px high, 40px wide
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # Spawn on the right edge, at a random Y height
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            # Assign a random speed to this specific car to create variety
            new_car.move_speed = self.car_speed + random.randint(0, 4)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(car.move_speed)  # Move left using individual speed

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        # Speed up all existing cars when level increases
        for car in self.all_cars:
            car.move_speed += MOVE_INCREMENT
