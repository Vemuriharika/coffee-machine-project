# # import turtle
# # timmy = turtle.Turtle()
#
# #-----------or-----------
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red","yellow")
timmy.speed(0)
# timmy.speed()
timmy.forward(100)
timmy.penup()
# timmy.goto(-350,0)
timmy.pendown()
#
# # accessing objects
# my_screen = Screen()
# ## my_screen.setup(width=600, height=600)
# print(my_screen.canvwidth)
# my_screen.exitonclick()
from nltk.translate import ibm_model

# pypi - for package
from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon name", ["pikachu" , "squirtle" , "charmander"])
table.add_column("Type",["Electric" , "Water" , "fire"])
# table.align["Pokemon name"] = "l"
# table.align["Type"] = "l"
table.align = "r"
print(table)

