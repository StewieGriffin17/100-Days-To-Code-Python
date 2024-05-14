# While loop and functions

name = input("What's your name? ")
number_of_times = int(input("How many times do you want to print? "))

while number_of_times > 0:  # While loop will iterate until the condition is false
    print(name)
    number_of_times -= 1  # Adjusting the condition to avoid infinite loop


def total(number):  # Here number is a parameter
    sum = 0
    for i in range(1, number+1):
        sum += i
    print(f"The sum of 0 to {number} is : {sum}")


total(100)  # Here 100 is passed as an argument, which will replace the parameter in function call

