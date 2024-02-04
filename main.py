#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
#
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable() #contructing the object
table.add_column("Pokemon Name", ["Pikachu", "Charizard", "Squirtle"],) #add_column is a method (m)
table.align="r"    # align is an attribute ( also known as fields (f))
table.add_column("Type",["Electric","Fire","Water"],"l")
print(table)