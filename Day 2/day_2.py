# Data types

# String
print("Hello"[0])
print("123" + "456")

# Integer
print(17)
print(60 + 9)
print(69_420)  # Can use '_' in between integer, python will ignore those underscores.

# Float
print(3.1416)

# Boolean
isRich = False
isUnlucky = True

# Conversion
name = "123"
name_int = int(name)
print(name_int)
print(type(name_int))

age = 22
age_str = str(age)
print(age_str)
print(type(age_str))
# Can also use float() function to convert a string or integer into a float.

# Mathematical Operations
print(3 + 5)
print(5 - 3)
print(5 * 3)
print(10 / 5)  # Always returns a float number
print(2 ** 3)  # 2 to the power 3
print(round(22/7, 4))  # Rounding a floating number
pi = "{:.3f}".format(22/7)  # Another way to round a floating number
print(pi)
print(27 // 7)  # // means floor division, only returns the integer value of a division

# f-string
score = 100
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height} and Winning is {isWinning}")  # Just add a 'f' in front of the string, and it will do the conversion automatically

