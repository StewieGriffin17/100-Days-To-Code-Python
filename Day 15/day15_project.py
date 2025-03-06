# This is my version of the solution.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def printReport():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
    
    
def givenMoney():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    totalMoney = (quarters * 0.25)+(dimes * 0.10)+(nickles * 0.05)+(pennies * 0.01)
    return totalMoney
    

def isMoneyEnough(money, name):
    if money >= MENU[name]["cost"]:
        return True
    else: 
        return False


def isResources(name):
    if (resources["water"] >= MENU[name]["ingredients"]["water"]) and (resources["milk"] >= MENU[name]["ingredients"]["milk"]) and (resources["coffee"] >= MENU[name]["ingredients"]["coffee"]):
        return True
    else:
        return False
    
    
running = True
  
while running:
    userChoice = input("What would you like? (espresso/latte/cappuccino/report/exit): ")
    match userChoice:
        case "report":
            printReport()
            
        case "espresso":
            money = givenMoney()
            name = "espresso"
            if isMoneyEnough(money, name) and isResources(name):
                remaining = money - MENU[name]["cost"]
                resources["water"] = resources["water"] - MENU[name]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU[name]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU[name]["ingredients"]["coffee"]
                profit = profit + money
                print("espresso")
                print(f"Here is your {name} ☕")
                print(f"Here is the change: {remaining}")
            else:
                print("Sorry, Not enough resources.")
            
        case "latte":
            money = givenMoney()
            name = "latte"
            if isMoneyEnough(money, name) and isResources(name):
                remaining = money - MENU[name]["cost"]
                resources["water"] = resources["water"] - MENU[name]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU[name]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU[name]["ingredients"]["coffee"]
                profit = profit + MENU[name]["cost"]
                print("latte")
                print(f"Here is your {name} ☕")
                print(f"Here is the change: {remaining}")
            else:
                print("Sorry, Not enough resources.")

        case "cappuccino":
            money = givenMoney()
            name = "cappuccino"
            if isMoneyEnough(money, name) and isResources(name):
                remaining = money - MENU[name]["cost"]
                resources["water"] = resources["water"] - MENU[name]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU[name]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU[name]["ingredients"]["coffee"]
                profit = profit + money
                print("cappuccino")
                print(f"Here is your {name} ☕")
                print(f"Here is the change: {remaining}")
            else:
                print("Sorry, Not enough resources.")
        case "exit":
            print("Have a good day!!!")    
        case _:
            print("Invalid Input!")
            running = False
