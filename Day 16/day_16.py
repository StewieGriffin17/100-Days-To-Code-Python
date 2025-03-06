# import day_16_anotherModule
# from turtle import Turtle, Screen

# print(day_16_anotherModule.another_module_variable) 

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()

# print(my_screen.canvheight)
# print(timmy)

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'c'
print(table)



