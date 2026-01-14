#import turtle #this is one way to import the entire turtle module
# https://docs.python.org/3/library/turtle.html for turtle module documentation
from turtle import Turtle, Screen #this is another way which imports the specified classes from the turtle module
from prettytable import PrettyTable
import another_module
#how to access another module variable
print(another_module.another_variable)

# #Turtle Stuff
# #timmy = turtle.Turtle() #create an object timmy from the Turtle class of the turtle module, if only the turtle module is imported
# timmy = Turtle() #create an object timmy from the Turtle class of the turtle module, if the Turtle class from the turtle module is imported
# print(timmy)
# timmy.shape("turtle") #change timmy's shape
# timmy.color("DarkCyan") #change timmy's color
# timmy.forward(100) #move timmy forward by 100 units

# my_screen = Screen() #create an object my_screen from the Screen class of the turtle module
# print(my_screen.canvheight) #accessing the canvheight attribute of my_screen object
# my_screen.exitonclick() #method to exit the screen on click

#PrettyTable Stuff
table = PrettyTable()
table.add_column("NFL NFC East Teams", ["Dallas Cowboys","New York Giants","Philadelphia Eagles","Washington Commanders"])
table.add_column("City Populations", [1_345_047, 1_841_295, 1_576_596, 632_323])
table.align = "l"
print(table)
print(table.align)  #accessing the align attribute of table object