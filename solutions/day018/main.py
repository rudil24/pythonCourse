"""
rudil24
Python Day 18: Hirst Painting
example painting "lifted" from
https://guyhepner.com/news/206-damien-hirst-master-of-form-spots-dots-and-grids/
"""

import colorgram

# Extract n colors from an image into a list of tuples.
rgb_colors = []
wanted_num_colors = 60
colors = colorgram.extract("hirst-diacetoxyscirpenol.png", wanted_num_colors)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    if (
        60 < (r + g + b) < 660
    ):  # don't take the color if it's almost black (0,0,0) or white (255,255,255)
        new_color = (r, g, b)
        rgb_colors.append(new_color)

# print(rgb_colors) #just checking to make sure we got a list of viable colors

# make a 10 x 10 grid of 20 diameter circles filled in with random colors, 50 pixels apart
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dot_count % 10 == 0:  # if we've reached the end of a row
        tim.setheading(90)  # set heading to 90 degrees aka top of screen
        tim.forward(50)  # go "up" 50 pixels
        tim.setheading(180)  # set heading to 180 degrees aka left of screen
        tim.forward(500)  # go left 500 (10 * 50) pixels
        tim.setheading(0)  # set heading to 0 degrees aka right of screen

screen = t.Screen()
screen.exitonclick()
