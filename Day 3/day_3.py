# Control flow and logical operator

# if-else
height = int(input("What's your height? "))
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("Enter your age : "))
    if age >= 18:
        print("Your ticket price is 12$.")
    elif 12 < age < 18:
        print("Your ticket price is 7$.")
    else:
        print("Your ticket price is 5$.")
else:
    print("You can't ride the rollercoaster. ")

# Logical operators
a = 10
print(a > 5 and a > 9)  # True
print(a > 5 or a > 15)  # Ture
print(not a > 5)  # False


# Love calculator
print("The Love Calculator is calculating your score...")
name1 = input()
name2 = input()
new_name1 = name1.lower()
new_name2 = name2.lower()
full_name = new_name1 + new_name2

t = full_name.count("t")
r = full_name.count("r")
u = full_name.count("u")
e = full_name.count("e")
l = full_name.count("l")
o = full_name.count("o")
v = full_name.count("v")

true = str(t + r + u + e)
love = str(l + o + v + e)

score = int(true + love)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
