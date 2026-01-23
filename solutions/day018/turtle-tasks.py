# rudil24
# turtle graphics project
# random "dot art" painting
import turtle as t  # helps us make a shorthand name for the turtle module
import random

tim = t.Turtle()
t.colormode(
    255
)  # set colormode to RGB so we can feed r, g, b values instead of named colors
tim.speed("fastest")


def random_color():  # function to generate random RGB colors
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# make a spirograph
for _ in range(360):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(
        tim.heading() + 10
    )  # tim.heading() returns the current heading of the turtle

# #make a random walk with random RGB colors
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# previous exercises
# from turtle import Turtle, Screen
# import random

# tim = Turtle()
# tim.shape("turtle")  # “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.
# tim.color("orange red")  # default method is acceptable list of TK colors.
# # TK colors: https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
# # draw a square 100x100
# # for i in range(4):
# #     tim.forward(100)
# #     tim.right(90)

# # # draw a dashed line for 10 dashes of 10 width
# # for dash in range(20):
# #     if dash % 2:
# #         tim.penup()
# #     else:
# #         tim.pendown()
# #     tim.forward(10)


# # draw shapes from 3 to 10 sides as a python defined function
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# # use random colors from this list of colors to draw the shapes
# colors = [
#     "CornflowerBlue",
#     "DarkOrchid",
#     "IndianRed",
#     "DeepSkyBlue",
#     "LightSeaGreen",
#     "wheat",
#     "SlateGray",
#     "SeaGreen",
# ]
# # for shape_side_n in range(3, 11):
# #     tim.color(random.choice(colors))
# #     draw_shape(shape_side_n)

# # make a random walk in right angle directions of 30 paces, in random colors
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# # keep this screen exit near the bottom so we exit at the end
screen = t.Screen()
screen.exitonclick()
