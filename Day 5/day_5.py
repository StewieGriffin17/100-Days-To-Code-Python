# Loops

names = ["Asif", "Naruto", "Luffy"]
for name in names:
    char_num = len(name)
    print(f"{name} has {char_num} character in his name.")
print("----------------------")

for i in range(1, 11):  # 1 is starting point, 11 is ending point. Exclude 11
    print(i)
print("----------------------")

for i  in range(10):  # Without the starting point, it will iterate the number of times inside the range function
    print(i)
print("----------------------")

for i in range(0, 11, 2):  # Skip 2 steps
    print(i)
print("-----------------------")

# Finding max using loop
num_list = input("Enter some numbers separated by a comma and a space: ").split(", ")

for n in range(0, len(num_list)):
    num_list[n] = int(num_list[n])

max_num = num_list[0]
for number in num_list:
    if number > max_num:
        max_num = number
print(f"The max number of given list is : {max_num}")
