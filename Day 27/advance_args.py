# Unlimited Positional Arguments

def add(*args):
    sum = 0
    for n in args:
        sum += n
        
    return sum

total = add(1, 2, 3, 4, 5)
print(total)

# Unlimited Keyword Arguments

def calculator(n, **kwargs):
    n += kwargs.get("add")
    n *= kwargs.get("multiply")
    
    print(n)

calculator(5, add=5, multiply=10)


class Car:
    
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
    
my_car = Car(make = "Audi", model = "A8", seats= 5)
print(my_car.make, my_car.model, "with", my_car.seats, "seats")
