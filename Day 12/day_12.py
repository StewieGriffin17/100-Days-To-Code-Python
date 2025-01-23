# Local scope

def number():
    number_inside = 10
    print(f"The number inside the function is {number_inside}")

number()
# print(number_inside) -> gives error cause it can't access 'number_inside' variable

# Global scope
number_global = 17
def number_again():
    print(f"The global number is = {number_global}")

number_again()
print(number_global) # Can access 'number_global' variable
