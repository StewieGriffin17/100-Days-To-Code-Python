# Dictionaries and nesting

names = {  # Defining dictionaries -> name = {key: value}
    "Luffy": "Warrior of Liberation, Joyboy",
    "Zoro": "King of Hell.",
    "Nami": "Cat Burglar",
}

print(names["Luffy"])  # Getting info from dictionary -> name[key]

# Adding new info after defining dictionary
names["Usopp"] = "A God."

names["Luffy"] = "An idiot."  # Editing value of a key
# names = {}  # Deleting everything in the dictionary

for key in names:
    print(key)
    print(names[key])

# Storing students grade in a dictionary according to their marks.
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for key in student_scores:
    if 90 < student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif 80 < student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 70 < student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)

# Nesting
travel = {  # List and dictionary inside a dictionary
    "France": ["paris", "lille", "dijon"],
    "Germany": {"cities_visited": ["Berlin", "Hamburg"]},
}

travel_list = [  # Dictionaries as list item
    {
        "country": "France",
        "cities_visited": ["paris", "lille", "dijon"],
        "total_visits": 15,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg"],
        "total_visits": 10,
    }
]