# Day 4 -> Randomisation and lists
import random  # Importing random module

random_number = random.randint(0, 2)  # Generates a random number between 0 and 2
print(random_number)

# Lists
names = ["Asif", "Wahid", "asheq"]  # Initializing list
print(names[random_number])
names[2] = "Asheq"  # Updating elements
print(names)
names.append("Moon")  # Adding new item at the end
print(names)

names2 = input("Enter a list of names: ")
given_names = names2.split(", ")  # Splits each item that are separated by a comma and a space
print(given_names)

# Nested list
names_boys = ["Asif", "Naruto", "Luffy"]
names_girls = ["Moon", "Hinata", "Boa"]
names_all = [names_boys, names_girls]
print(names_all, "\n\n")

# Input a spot where you want to hide your treasure. Input can be A1, A2, A3,......, C1, C2, C3
line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
treasure_map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?")
letter = position[0].lower()
number = int(position[1])
letter_list = ["a", "b", "c"]
letter_index = letter_list.index(letter)
treasure_map[number-1][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}")
