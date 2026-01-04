#rudil24 playing with modules and the random module
import random
import my_module
random_number = random.randint(1, 100)
random_number_0_to_1 = random.random()
random_float = random.uniform(1, 10)
coin_flip = random.choice(["heads", "tails"])
print(f"Random Number 1-100: {random_number}")
print(f"Random Number 0-1: {random_number_0_to_1}")
print(f"Random Float 1-10: {random_float}")
print(f"Favorite Number: {my_module.my_favorite_number}")
print(f"Coin Flip: {coin_flip}")
#could also do a coin flip with random.randint(0,1) and an if statement
