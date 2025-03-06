# this is the OOP version of the coffee machine project

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_running = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_running:
    choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()
    if choice == "off":
        is_running = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
                
            
                
                
                
            
            
        
        
        