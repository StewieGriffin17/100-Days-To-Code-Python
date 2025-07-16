# Reading a file
with open("my_file.txt") as file: 
    contents = file.read()
    print(contents)

# Writing in a file
with open("my_file.txt", mode="w") as file:
    file.write("This is a new line. ")

# Add new text to a file
with open("my_file.txt", mode="a") as file:
    file.write("This line is newly added.")
