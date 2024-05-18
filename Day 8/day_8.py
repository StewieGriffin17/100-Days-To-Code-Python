# Function parameter
def greet():
    print("Hello Stewie")
    print("How are you today?")


greet()


def greet_name(name):  # Declaring a parameter in function definition
    print(f"Hello {name}")
    print("How are you today?")


greet_name("Rick")  # passing an argument while calling the function


def greet_multiple(name1, name2):  # declaring multiple parameters
    print(f"Hello {name1}")
    print(f"I am {name2}")


greet_multiple("Rick", "Asif")  # passing arguments
